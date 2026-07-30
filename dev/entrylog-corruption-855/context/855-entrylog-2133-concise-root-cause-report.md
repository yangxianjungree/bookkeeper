# 855.log / EntryLog 2133 损坏根因报告

## 1. 结论摘要

`pulsar-bookie-1` 上的 `855.log`（entryLogId=2133）损坏不是随机坏块，也不是 L15069 数据被 L15021 覆写。核心问题是 BookKeeper `BufferedChannel` 的 logical position 与底层 `FileChannel` physical position 在一次 flush 异常后脱钩，后续写入继续使用同一个 channel，形成稳定偏移：

```text
physical position = logical position + 34553
```

这个 `34553` 同时出现在三类互相独立的证据里：

```text
真实 ledgers map offset - header.ledgersMapOffset = 34553
L15069 真实 entry body pos - RocksDB index pos      = 34553
64KiB writeBuffer 边界 - L240727/E17719 bodyStart   = 34553
```

最精确的文件层损坏点是：

```text
L240727/E17719 body 写到 64KiB write buffer 边界时发生 flush 异常；
offset 65536 之后已经变成脱钩后的连续物理写入链。
```

## 2. 855.log 整体分布图

以下 offset 均为十进制字节偏移，区间按左闭右开理解；图不是按比例绘制。

```text
0
|-- entrylog header ------------------------------------------------------|
| magic=BKLO, version=1                                                   |
| header.ledgersMapOffset = 1073741388   <-- stale logical map offset     |
| header.ledgersCount     = 201                                           |
1024
|-- 正常可顺序解析 entry -------------------------------------------------|
| L240725/E5636 -> L240725/E5637 -> L240726/E10755 -> L240727/E17717      |
30979
|-- L240727/E17719 sizeStart ---------------------------------------------|
| size field = 55343                                                      |
30983
|-- L240727/E17719 partial body ------------------------------------------|
| 真实只写入 34553 bytes body，刚好填满 64KiB writeBuffer                  |
65536
|-- 脱钩后的连续物理写入链起点 -------------------------------------------|
| L38854/E11622 -> L38854/E11623 -> L38854/E11624 -> ...                  |
| 后续 entry 在物理文件上连续，但 RocksDB/location 记录使用 stale logical |
1025196194
|-- RocksDB 记录的 L15069/E0 body pos，实际落在旧位置/其他 entry 内部 -----|
1025230747
|-- L15069/E0 真实 body pos = index pos + 34553 --------------------------|
1073741388
|-- header 指向的 stale ledgers map offset，物理上仍在普通 entry stream 内 |
1073770033
|-- 最后一条普通 entry：L39095/E6725, size=5904 --------------------------|
1073775941
|-- 真实 ledgers map start -----------------------------------------------|
| size field = 3236；map entry 总长度 = 3240 = 4 + 20 + 16 * 201          |
1073779181
|-- EOF ------------------------------------------------------------------|
```

真实 ledgers map 的文件尾证据：

```text
真实 map 起点 = 1073775941
size field   = 3236 = 20 + 16 * 201
entry bytes  = 3240 = 4 + 3236
file size    = 1073779181
1073775941 + 3240 = 1073779181
```

header 里的 `1073741388` 不是随机写坏值，而是 BookKeeper 当时从 `BufferedChannel.position()` 取到的 stale logical position。错的是 logical position 已经比 `FileChannel` 实际物理位置落后 `34553`。

## 3. Entry 错误图、拐点 entry 与 64KiB 异常

### 3.1 严格 scanner 视角

严格 scanner 从文件头顺序信任每条 entry 的 declared size，因此会这样走：

```text
1024    L240725/E5636 size=43     next=1071
1071    L240725/E5637 size=43     next=1118
1118    L240726/E10755 size=63    next=1185
1185    L240727/E17717 size=29790 next=30979
30979   L240727/E17719 size=55343 next=86326
86326   解析出伪 header:
        (386008842, 1116334194590091862, 1114927214843331868, ...)
        => 非法，scanner fail
```

`86326` 不是一个真实 entry 边界。它落在后续 `L38854/E11623` 的 body 内部，所以 payload 被误当成 `size/lid/eid/lac` 解析，得到巨大伪值。

### 3.2 物理真实写入视角

物理文件上的实际连续链是：

```text
30979   L240727/E17719 sizeStart，size field 已写入 55343
30983   L240727/E17719 bodyStart
30983..65536  partial body，共 34553 bytes

65536   L38854/E11622 size=11309 next=76849
76849   L38854/E11623 size=24693 next=101546
101546  L38854/E11624 size=19210 next=120760
120760  L38854/E11625 size=32121 next=152885
...
1073770033 L39095/E6725 size=5904 next=1073775941
1073775941 true ledgers map start
```

独立复算确认：

```text
chain_65536_to_map_count = 411693
chain break count        = 0
last entry next          = 1073775941
```

因此 `65536` 应精确称为“脱钩后的连续物理写入链起点”。`30979..65536` 仍属于 `L240727/E17719` 的 size field + partial body，不应把 `65536` 简化为“整个物理主链的起点”。

### 3.3 64KiB 异常闭环

现场配置和默认值都指向 64KiB write buffer：

```text
writeBufferBytes = 65536
L240727/E17719 sizeStart = 30979
L240727/E17719 bodyStart = 30983
65536 - 30983 = 34553
```

这说明异常发生在 `L240727/E17719` body 写入过程中：body 的前 `34553` bytes 正好把 `BufferedChannel` 的 64KiB write buffer 填满。`BufferedChannel.write()` 在更新 logical `position` 前触发 `flush()`；如果 `flush()` 已经把 64KiB 写进 `FileChannel`，随后抛出 `IOException`，就会出现：

```text
FileChannel physical position = 65536
BufferedChannel logical position = 30983
physical - logical = 34553
```

后续同一个 channel 继续追加，物理写入从 `65536` 往后走，但所有由 `BufferedChannel.position()` 产生的位置，包括 RocksDB location index 和最终 header 的 ledgersMapOffset，都持续早 `34553`。

### 3.4 Physical / Logical 偏移图

BookKeeper 这里同时存在两个位置概念：

```text
physical position：底层 FileChannel 真实文件写入位置
logical position ：BufferedChannel.position() 维护的逻辑位置
```

flush 前，entry 字节先进入 `BufferedChannel` 的 writeBuffer，尚未全部反映到 `FileChannel.position()`；正常情况下 flush 成功返回后，logical position 与文件真实 offset 会重新对齐。本次异常点在于：flush 已经把 64KiB 写进文件并推进 `FileChannel`，但 `BufferedChannel.write()` 没走到 `position += copied`。

```text
时间点 / 事件                         logical position      FileChannel 落点
--------------------------------------------------------------------------------
E17719 size 写完                       30983                 仍由 buffer 持有
E17719 body 写入 34553 bytes            待更新到 65536         仍由 buffer 持有
64KiB buffer 满，触发 flush()
flush 已写到文件后抛 IOException        30983                 65536
--------------------------------------------------------------------------------
脱钩成立                               physical - logical = 65536 - 30983 = 34553
```

之后每次 `addEntry()` 返回给 RocksDB 的位置都来自 logical position，而真实数据落在 physical position：

```text
logical 视角，也就是 index/header 记录      physical 视角，也就是文件真实位置
--------------------------------------------------------------------------------
30983                                      65536
76849 - 34553 = 42296                     76849
101546 - 34553 = 66993                    101546
...
1025230747 - 34553 = 1025196194           1025230747  L15069/E0 real body pos
1073775941 - 34553 = 1073741388           1073775941  true ledgers map start
```

所以两个看似不同的现象其实是同一个偏移在不同调用点的表现：

```text
RocksDB index 早 34553：addEntry() 记录 stale logical body pos
header map offset 早 34553：appendLedgersMap() 记录 stale logical map pos
```

## 4. L15069 证据

真实 ledgers map 中存在：

```text
L15069 TotalSize = 26164
```

现场 RocksDB index 对 `log=2133` 的 L15069 entries：

```text
total_index_rows_log2133 = 569
ok_after_plus_34553 = 569
bad_count = 0
```

样例：

```text
L15069/E0 index pos = 1025196194
L15069/E0 real pos  = 1025230747
delta = 34553
```

独立 CRC32C 校验显示：

```text
569 / 569 条 L15069 entry 按 BK V3 + CRC32C 校验通过
sum(4 + size) = 26164
```

所以 L15069 数据存在于 855.log；不可读的直接原因是 RocksDB location index 统一早了 `34553` bytes。最初看起来“L15069 读到了 L15021 附近”，是因为 stale index 落在更早的物理 entry stream 内部，不是 L15069 被 L15021 覆写。

## 5. 源码根因

`EntryLogManagerBase.addEntry()` 的 location 语义：

```java
logChannel.write(sizeBuffer);
long pos = logChannel.position();  // bodyStart
logChannel.write(entry);
return (logId << 32L) | pos;
```

RocksDB 保存的是 `BufferedChannel.position()`，即 logical position。

`BufferedChannel.write()` 的风险窗口：

```java
writeBuffer.writeBytes(...);
if (!writeBuffer.isWritable()) {
    flush();
}
position += copied;
```

如果 `flush()` 已经把数据写入 `FileChannel`，但随后抛 `IOException`，则：

```text
FileChannel physical position 已前进；
BufferedChannel.position 未前进；
writeBuffer/channel 未被标记为不可继续使用。
```

后续 `appendLedgersMap()` 又使用同一个 stale position：

```java
long ledgerMapOffset = this.position();
write(serializedMap);
super.flush();
fileChannel.write(mapInfo, LEDGERS_MAP_OFFSET_POSITION);
```

因此 header 中写入的也是 stale logical offset，最终形成：

```text
true map offset       = 1073775941
header logical offset = 1073741388
delta                 = 34553
```

## 6. 本地复现

已在 BookKeeper 本地测试中增加两个复现用例：

```text
BufferedChannelTest.testPositionCanLagFileChannelAfterPartialFlushFailure
BufferedChannelTest.testLedgersMapHeaderUsesStalePositionAfterPartialFlushFailure
```

验证命令：

```text
mvn -pl bookkeeper-server -Dtest=org.apache.bookkeeper.bookie.BufferedChannelTest test
```

结果：

```text
Tests run: 8, Failures: 0, Errors: 0, Skipped: 0
BUILD SUCCESS
```

测试证明当前源码可进入“physical position 已前进、logical position 落后、appendLedgersMap 写 stale header”的状态。

## 7. 两份独立佐证

### 7.1 verification-2dws9g

该报告独立复核了 header 大端解析、真实 ledgers map、L15069/L15021 ledgersMap size、L15069 CRC32C、源码语义等，最终结论为 PASS。关键补强点包括：

```text
真实 map 起点 - header offset = 1073775941 - 1073741388 = 34553
L15069 569/569 CRC32C 通过
569 条 (4+size) 累加 = 26164，与 ledgers map 一致
```

它提出的主要修订是措辞层面：header 不是随机写错，而是写入 stale logical position；这已纳入本文表述。

### 7.2 verification-78faf567

该报告独立 mmap 复算关键位置，确认：

```text
65536 = L38854/E11622 sizeStart
65536..1073775941 连续 411693 条 entry
last entry next = 1073775941
delta_buffer = delta_map = 34553
```

其早期版本曾把 L15069 pattern 写错、把 E17719 误解释为 true size=70563；这些错误已撤回。修正后，它与主分析无实质冲突，并建议将 `65536` 精确表述为“脱钩后的连续物理写入链起点”，本文已采用该表述。

## 8. 非同根因边界案例：bookie-2 L15002

另一个 bookie-2/L15002/b65.log 调查显示：

```text
L15002 部分 RocksDB index 指向 b65.log，部分指向 85.log；
b65.log 当前存在且自洽；
85.log 不存在；
该问题表现为 stale index / missing entrylog。
```

它不是 855.log 的同根因，不能作为 `BufferedChannel 34553 脱钩` 的直接佐证。它应作为另一类 BookKeeper 本地 index 与 entrylog 文件不一致问题单独调查。

## 9. 最终判断

855.log 的根因证据链已经闭合：

```text
文件证据：34553 = true map offset - stale header offset
边界证据：34553 = 65536 - L240727/E17719 bodyStart
entry 证据：65536..1073775941 连续 411693 条 physical entry
数据证据：L15069 569/569 entries +34553 后 CRC32C 通过
源码证据：BufferedChannel.write() 在 position 更新前 flush，异常后不失效 channel
复现证据：本地测试可复现 position/header 脱钩
```

因此，855.log 损坏应归因于 BookKeeper `BufferedChannel.write()/flush()` 异常路径缺乏一致性保护，而不是业务 payload 随机损坏、L15069 数据缺失或 ledgers map 本体丢失。
