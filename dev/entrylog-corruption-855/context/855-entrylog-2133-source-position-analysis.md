# BookKeeper 855.log 源码侧 position 错位补充分析

> 时间：2026-07-27  
> 对象：`pulsar-bookie-1` 上 `data/bookkeeper/ledgers/current/855.log`  
> EntryLog：`logId=2133` (`0x855`)  
> 目的：单独记录基于 BookKeeper 4.16.7 源码继续推导出的 `BufferedChannel position`、`ledgers map header`、`L15069` 与 `L15021` 的关系。

---

## 1. 新增证据摘要

### 1.1 Header 大端解析

现场命令：

```bash
od -An -tx1 -N 32 -j 0 data/bookkeeper/ledgers/current/855.log
```

输出：

```text
42 4b 4c 4f 00 00 00 01 00 00 00 00 3f ff fe 4c
00 00 00 c9 00 00 00 00 00 00 00 00 00 00 00 00
```

按 BookKeeper `ByteBuf.readLong/readInt` 的大端语义解析：

```text
magic            = BKLO
version          = 1
ledgersMapOffset = 0x3ffffe4c = 1073741388
ledgersCount     = 0x000000c9 = 201
```

注意：`od -tu8/-tu4` 会按宿主小端显示，不能直接当作 Java 读到的 header 值。

### 1.2 Header 记录的是 stale logical offset，物理上不是 ledgers map

现场命令：

```bash
od -An -tx1 -N 96 -j 1073741388 data/bookkeeper/ledgers/current/855.log
```

输出开头：

```text
70 7a 6e 58 66 5a 4c 4a 59 54 52 4f 75 37 36 62
47 58 51 50 75 37 6f 39 ...
```

ASCII 形态：

```text
pznXfZLJYTROu76bGXQPu7o9...
```

严格说，header 字段值 `1073741388` 是 BookKeeper 当时的 logical position。
问题不在于 header 随机写了一个值，而在于 `BufferedChannel.position()` 已经比底层 `FileChannel.position()` 落后 34553 bytes。

因此从物理文件角度看，`1073741388` 处不是 BookKeeper ledgers map metadata，而是普通 entry 字节区域。

正常 ledgers map entry 开头应类似：

```text
00 00 0c a4                 # map entry size
ff ff ff ff ff ff ff ff     # ledgerId = -1
ff ff ff ff ff ff ff fe     # entryId = -2
00 00 00 c9                 # ledger count = 201
```



### 1.3 真正的 ledgers map 在文件末尾

现场命令：

```bash
grep -aob $'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe' 855.log | head
```

输出：

```text
1073775945:...
```

该 pattern 是：

```text
ledgerId = -1
entryId  = -2
```

由于前面 4 字节是 entry size，真实 map 起点为：

```text
1073775945 - 4 = 1073775941
```

与 header 的差值：

```text
1073775941 - 1073741388 = 34553 bytes
```

`readlogmetadata` fallback 的 short read 同时给出了 EOF：

```text
425908828 + 647870353 = 1073779181
```

201 个 ledger 的 ledgers map 总长度按源码计算为：

```text
24 + 16 * 201 = 3240 bytes
```

验证：

```text
1073775941 + 3240 = 1073779181
```

初步结论：

```text
真正的 ledgers map 完整写在文件末尾；
但是 855.log header 里的 ledgersMapOffset 写早了 34553 字节；
更准确地说：header 写入了 stale logical offset；
该 logical offset 在物理文件上落在真实 map 前 34553 字节的位置。
```

---



## 2. 源码对应关系



### 2.1 appendLedgersMap 写 header 的逻辑

源码：

```text
bookkeeper-server/src/main/java/org/apache/bookkeeper/bookie/DefaultEntryLogger.java
```

关键逻辑：

```java
long ledgerMapOffset = this.position();
...
write(serializedMap);
...
super.flush();
...
this.fileChannel.write(mapInfo, LEDGERS_MAP_OFFSET_POSITION);
```

含义：

1. `appendLedgersMap()` 先用 `this.position()` 记录 map 应该开始的位置。
2. 然后写真正的 ledgers map。
3. 最后把 `ledgerMapOffset` 和 `ledgersCount` 写回文件头。

855.log 现在表现为：

```text
header 里的 ledgerMapOffset = 1073741388
真实 ledgers map 起点       = 1073775941
差值                       = 34553
```

这说明 seal 时至少存在一次：

```text
BookKeeper logical position != FileChannel 实际写入位置
```



### 2.2 BufferedChannel position 的风险点

源码：

```text
bookkeeper-server/src/main/java/org/apache/bookkeeper/bookie/BufferedChannel.java
```

关键逻辑：

```java
public void write(ByteBuf src) throws IOException {
    int copied = 0;
    synchronized (this) {
        int len = src.readableBytes();
        while (copied < len) {
            int bytesToCopy = Math.min(src.readableBytes() - copied, writeBuffer.writableBytes());
            writeBuffer.writeBytes(src, src.readerIndex() + copied, bytesToCopy);
            copied += bytesToCopy;

            if (!writeBuffer.isWritable()) {
                flush();
            }
        }
        position += copied;
    }
}
```

重点：

```text
flush() 可能已经把部分 bytes 写进 FileChannel；
但 logical position 是在整个 write() 最后才 position += copied。
```

如果中途发生 IOException、线程中断、FileChannel 异常、进程 crash，或者存在任何绕过 `BufferedChannel.position` 的 FileChannel 写入，都可能出现：

```text
实际文件位置已经前进；
BookKeeper logical position 没有同步前进。
```

855.log 的 header 错位就是这种脱钩的直接证据。

---



## 3. Seal 和 L15069 的时间线关系

源码：

```text
bookkeeper-server/src/main/java/org/apache/bookkeeper/bookie/EntryLogManagerForSingleEntryLog.java
```

关键逻辑：

```java
boolean reachEntryLogLimit = activeLogChannel.position() + entrySize > logSizeLimit;
if (createNewLog || reachEntryLogLimit) {
    createNewLog(...);
}
```

含义：

```text
下一条 entry 再写就会超过 entrylog 大小限制时，
Bookie 先 seal 当前 entrylog，再切到新 entrylog。
```

855.log 的生命周期：

```text
创建 855.log
  -> 写普通 entry
  -> 每条 entry 写入时产生 location，并写入 RocksDB index
  -> 接近 1GiB
  -> 触发 rollover/seal
  -> appendLedgersMap()
  -> 写 header
  -> 855.log 封口
```

因此：

```text
不是 seal 先发生，然后 L15069 跟着拿到错误 position；
如果 L15069 写入 855.log，它一定发生在 855 seal 之前。
```

seal 阶段的错位是最后的验尸证据：它证明到 855 封口时，position 机制已经出现过不一致。

---



## 4. ledgers map 中的 L15069 / L15021

现场解析真实 ledgers map：

```text
map size: 3236 lid: -1 eid: -2 count: 201
hits: [(15069, 26164), (15021, 230424)]
```

含义：

```text
855.log 的真实 ledgers map 同时登记了 L15069 和 L15021。
```

`ledgers map` 不是从 RocksDB index 得来的，而是 EntryLogger 写 entry 时在内存里累计出来的：

```java
logChannel.registerWrittenEntry(ledger, entrySize);
```

因此，Bookie 在写入 / seal 855.log 时，自己认为：

```text
855.log 里写过 L15069，累计 26164 bytes；
855.log 里也写过 L15021，累计 230424 bytes。
```

`L15069 -> 26164 bytes` 与 L15069 偶数 entry 的规模非常接近：

```text
entry 0,2,4,...,1136 共有 569 条
26164 / 569 ~= 46 bytes
```

这与 cursor entry 常见的 45/46 字节大小吻合。

---



## 5. 对 L15069 关系的更新结论

之前可以说：

```text
L15069 RocksDB index 错指到 L15021 区域。
```

现在应更新为更强的结论：

```text
855.log 的真实 ledgers map 证明 L15069 曾经被写路径登记进 855；
但按 index 指向处读到的位置，盘上 body 是 L15021；
因此问题不是单纯的“后期 index 指错文件”，而是写入/flush 阶段已经出现 key/body/location 不一致。
```

在 DbLedgerStorage flush 中，关键代码形态是：

```java
writeCacheBeingFlushed.forEach((ledgerId, entryId, entry) -> {
    long location = entryLogger.addEntry(ledgerId, entry);
    entryLocationIndex.addLocation(batch, ledgerId, entryId, location);
});
```

这里有三份信息必须一致：

```text
ledgerId/entryId  # WriteCache key
entry bytes       # WriteCache 中保存的 ByteBuf 内容
location          # EntryLogger 返回的位置
```

现在的证据说明：

```text
map 和 index 都承认 L15069；
但对应位置的 entry body 不是 L15069。
```

这将可疑范围收窄到：

```text
SingleDirectoryDbLedgerStorage.flush()
WriteCache.forEach()
EntryLogManagerBase.addEntry()
BufferedChannel.write()/flush()
```

尤其要关注：

```text
WriteCache key 是 L15069 时，传给 EntryLogger 的 ByteBuf 内容是否仍是 L15069；
EntryLogger 返回的 logical position 是否与实际写入文件的位置一致。
```

---



## 6. 当前最合理的损伤模型

855.log 至少包含两类强证据：

```text
1. 文件头 ledgersMapOffset 错：
   header 指向 1073741388；
   真实 map 在 1073775941；
   差 34553 bytes。

2. L15069 key/body/location 不一致：
   ledgers map 中有 L15069；
   RocksDB index 中也有 L15069；
   但按 index 指向处读到的是 L15021 或 payload。
```

这两者共同指向：

```text
Bookie 在写 855.log 时，logical position / WriteCache key / 实际 entry bytes 至少有一处发生过脱钩。
```

这不是 Autorecovery 造成的，也不是 `readlog` 工具造成的。Autorecovery 只是后续读到了这个坏状态。

---



## 7. 建议继续验证



### 7.1 找出真实 ledgers map 前最后一条普通 entry

真实 map 起点已经确定为：

```text
1073775941
```

如果能在它前面找到一条满足下面条件的 entry：

```text
entryStart + 4 + entrySize == 1073775941
```

就能知道真实 map 前最后一条普通 entry 属于哪个 ledger，并判断 header 错误 offset 与文件尾部 entry 的相对关系。

建议在 bookie-1 上执行：

```bash
python3 - <<'PY'
import struct

path = 'data/bookkeeper/ledgers/current/855.log'
map_start = 1073775941
header_offset = 1073741388
window = 2 * 1024 * 1024

with open(path, 'rb') as f:
    start = max(1024, map_start - window)
    f.seek(start)
    buf = f.read(map_start - start)

found = False
for rel in range(0, len(buf) - 28):
    pos = start + rel
    size = struct.unpack_from('>i', buf, rel)[0]
    if size <= 0 or size > 16 * 1024 * 1024:
        continue
    if pos + 4 + size == map_start:
        lid = struct.unpack_from('>q', buf, rel + 4)[0]
        eid = struct.unpack_from('>q', buf, rel + 12)[0]
        lac = struct.unpack_from('>q', buf, rel + 20)[0]
        print('entryStart:', pos)
        print('entrySize:', size)
        print('ledgerId:', lid)
        print('entryId:', eid)
        print('lac:', lac)
        print('headerOffsetInsideEntry:', header_offset - pos)
        print('bytesFromHeaderOffsetToMap:', map_start - header_offset)
        found = True

print('found:', found)
PY
```

预期解释：

```text
found=True:
  输出的 ledgerId/entryId 能说明被指中的 payload 属于谁。
  如果 headerOffsetInsideEntry 为负数，说明 header offset 在最后一条 entry 之前，
  错位不是“指进最后一条 entry”，而是一个更早的全局 position 偏移。

found=False:
  map 前最后一段自身也不是标准 BK entry framing；
  文件尾部损坏范围比 header offset 错位更大。
```



### 7.2 精确搜索 L15069/L15021 的 8 字节 ledgerId 出现位置

建议不要只用短 pattern `00 00 3a dd`，而是搜索完整 8 字节 ledgerId，并区分 data entry 与 ledgers map。

```bash
python3 - <<'PY'
import struct

path = 'data/bookkeeper/ledgers/current/855.log'
targets = {
    15021: (15021).to_bytes(8, 'big'),
    15069: (15069).to_bytes(8, 'big'),
}

with open(path, 'rb') as f:
    data = f.read()

for ledger, pat in targets.items():
    print('ledger', ledger)
    start = 0
    count = 0
    while True:
        idx = data.find(pat, start)
        if idx < 0:
            break
        count += 1
        size_pos = idx - 4
        if size_pos >= 0 and idx + 16 <= len(data):
            size = struct.unpack('>i', data[size_pos:idx])[0]
            entry_id = struct.unpack('>q', data[idx + 8:idx + 16])[0]
            print('  offset=%d size_pos=%d size=%s entryId=%s' % (idx, size_pos, size, entry_id))
        else:
            print('  offset=%d' % idx)
        start = idx + 1
    print('  total hits:', count)
PY
```



### 7.3 判断 L15069 是否真的有 data entry body

如果 L15069 只在 ledgers map 中出现，而不在 data entry body 中出现：

```text
说明写路径登记过 L15069，但实际 data body 没落成 L15069。
```

如果 L15069 在 data body 中也出现：

```text
说明 L15069 数据可能仍在 855.log 内，只是 RocksDB index 指错；
需要进一步按真实 offset 尝试读 entry。
```



### 7.4 回查 Jul 8 前后日志

重点搜索：

```text
IOException
ClosedByInterruptException
Error flush entry log
Error during flush
NoWritableLedgerDir
Created new entry log file
Flushing entry logger 2133
Synced entry logger 2133
```

目标是确认 855.log rollover/seal 时是否发生过写异常、线程中断、容器重启或磁盘异常。

同时确认 Bookie 配置：

```text
flushEntrylogBytes
```

源码默认值为 `0`，表示 entrylog 不按字节 regular flush，主要在 rotate/checkpoint 时 flush。该值会影响 `BufferedChannel.write()` 里具体走哪条 flush 分支。

---



## 8. 追加源码验证记录



### 8.1 4.16.7 当前分支未包含两个后续 DbLedgerStorage 竞态修复

本地源码分支：

```text
release-4.16.7
```

检查结果：

```text
3c5123d0a7 Prevent double flush due to race in SingleDirectoryDbLedgerStorage (#4305)
15a5b49c43 SingleDirectoryDbLedgerStorage skip optimistic cache put sometimes (#4306)
```

这两个提交均不是当前 `release-4.16.7` 的 ancestor。

相关当前代码形态：

```java
long stamp = writeCacheRotationLock.tryOptimisticRead();
boolean inserted = false;

inserted = writeCache.put(ledgerId, entryId, entry);
if (!writeCacheRotationLock.validate(stamp)) {
    stamp = writeCacheRotationLock.readLock();
    try {
        inserted = writeCache.put(ledgerId, entryId, entry);
    } finally {
        writeCacheRotationLock.unlockRead(stamp);
    }
}
```

以及：

```java
hasFlushBeenTriggered.set(false);
...
isFlushOngoing.set(true);
```

这些并不直接证明本案由 #4305/#4306 导致，但说明 4.16.7 的 `SingleDirectoryDbLedgerStorage` 在 write-cache swap / flush 并发边界上确实存在后续已修复的竞态问题。

### 8.2 flush IOException 路径不会重置 EntryLogger / BufferedChannel

当前 `SingleDirectoryDbLedgerStorage.checkpoint()` 中：

```java
writeCacheBeingFlushed.forEach((ledgerId, entryId, entry) -> {
    long location = entryLogger.addEntry(ledgerId, entry);
    entryLocationIndex.addLocation(batch, ledgerId, entryId, location);
});

entryLogger.flush();
batch.flush();
...
writeCacheBeingFlushed.clear();
```

如果写 entrylog 阶段抛出 `IOException`：

```java
} catch (IOException e) {
    recordFailedEvent(dbLedgerStorageStats.getFlushStats(), startTime);
    throw e;
} finally {
    ...
    isFlushOngoing.set(false);
    flushMutex.unlock();
}
```

注意：

```text
writeCacheBeingFlushed 不会 clear；
entryLogger / BufferedChannel 不会 reset 或 close；
已经进入 FileChannel 的部分 bytes 也不会回滚。
```

因此，如果 `BufferedChannel.write()` 内部 flush 已经推进了 FileChannel，但 logical `position` 尚未更新就失败，后续 retry 可能在一个 position 已经脱钩的 channel 上继续写。

### 8.3 后续历史中 journal 已减少 length/body 分两次 write 的风险面

本地 git 历史中有后续提交：

```text
591c58df43 Write journal entry length prefix and payload in a single BufferedChannel write (#4833)
```

该提交不是当前 `release-4.16.7` 的 ancestor，并且只修改 journal 写入：

```java
- bc.write(lenBuff);
- bc.write(qe.entry);
+ bc.write(lenBuff, qe.entry);
```

它没有修改 entrylog 的写入路径。当前 entrylog 仍是：

```java
logChannel.write(sizeBuffer);
long pos = logChannel.position();
logChannel.write(entry);
```

该提交不能解释 855.log 的已发生损坏，但它说明 BookKeeper 后续确实在减少 “length prefix 和 payload 分两次写入 BufferedChannel” 的风险面。

### 8.4 L15069 的 +3 错位与 4 字节 size prefix 高度相关

EntryLog 的正常 location 语义是：

```text
sizeStart + 4 = entry body 起点 = RocksDB location pos
```

L15021/E21 在盘上的真实结构：

```text
sizeStart = 1025196187
bodyStart = 1025196191
```

而 L15069/E0 的 RocksDB index pos 是：

```text
1025196194 = 1025196191 + 3
```

也就是说，L15069 index 比 L15021 正常 body 起点多了 3 字节。

`+3` 不是一个随机的大偏移，它刚好落在 BookKeeper 每条 entry 前 4 字节 size prefix 的尺度内。源码中 entrylog 写入正好是三步：

```java
logChannel.write(sizeBuffer);
long pos = logChannel.position();
logChannel.write(entry);
```

因此，L15069 的 `+3` 更像是 size prefix 写入 / position 更新附近发生过不一致，而不是高层 ledger metadata 或 Autorecovery 行为造成的。

需要注意：

```text
855 header 的错位是 -34553；
L15069 index 的局部错位是 +3；
二者不应强行解释为同一个固定偏移。
```

更合理的说法是：

```text
855.log 写入期间至少出现过 position 与实际文件字节流不一致；
这种不一致在 seal header 上表现为 34553 bytes；
在 L15069 index 上表现为 size-prefix 级别的 3 bytes。
```



### 8.5 追加现场验证：L15069 真实 data body 存在，且统一偏移为 34553

后续现场脚本输出：

```text
flushEntrylogBytes=268435456

entryStart: 1073770033
entrySize: 5904
ledgerId: 39095
entryId: 6725
lac: 6724
headerOffsetInsideEntry: -28645
bytesFromHeaderOffsetToMap: 34553
found: True
```

解释：

```text
真实 ledgers map 前最后一条普通 entry 是 L39095/E6725；
header offset = 1073741388 位于这条最后 entry 之前 28645 bytes；
所以 header 不是“指进最后一条 entry”，而是比真实 map 起点整体早 34553 bytes。
```

更关键的是 L15069 搜索结果：

```text
ledger: 15069
total_hits: 585
hits_in_ledgers_map: 1
first_data_like_hits:
  (1025230747, 1025230743, 41, 0)
  (1025230792, 1025230788, 41, 2)
  (1025230837, 1025230833, 41, 4)
  ...
```

这证明：

```text
L15069 的真实 data body 存在于 855.log 中。
```

与 RocksDB index 对照：

```text
L15069/E0 index pos = 1025196194
L15069/E0 real pos  = 1025230747
delta               = 34553

L15069/E2 index pos = 1025196239
L15069/E2 real pos  = 1025230792
delta               = 34553

L15069/E4 index pos = 1025196284
L15069/E4 real pos  = 1025230837
delta               = 34553
```

因此，之前的 `+3` 需要重新解释：

```text
错误 index pos = L15069 真实 pos - 34553
```

它刚好落在 L15021/E21 的 body 起点之后 3 字节：

```text
L15021/E21 bodyStart = 1025196191
L15069/E0 index pos  = 1025196194
```

所以 `+3` 不是根偏移，而是全局 `-34553` 错位落到 L15021 entry 内部后的偶然局部表现。

更新后的更强结论：

```text
855.log 中 L15069 数据并未完全丢失；
RocksDB location index 对 L15069 至少在该区域统一早了 34553 bytes；
该 34553 与 header ledgersMapOffset 错位完全一致。
```



### 8.6 全量验证：L15069 的 569 条本地 index 全部可用 +34553 修正

后续现场脚本对 `ledger -m 15069` 的所有 `(log=2133, pos=...)` 做了验证：

```text
total_index_rows_log2133: 569
ok_after_plus_34553: 569
bad_count: 0
```

样例：

```text
E0:
  index pos = 1025196194
  real pos  = 1025230747
  size=41, lid=15069, eid=0, lac=-1

E2:
  index pos = 1025196239
  real pos  = 1025230792
  size=41, lid=15069, eid=2, lac=1

E4:
  index pos = 1025196284
  real pos  = 1025230837
  size=41, lid=15069, eid=4, lac=3
```

独立佐证报告还补充了 CRC32C 校验：

```text
569 / 569 条 L15069 entry 按 BK V3 + CRC32C 布局校验通过；
569 条的 (4 + size) 累加 = 26164；
该值与真实 ledgers map 中 L15069 的 TotalSize 完全一致。
```

这说明 `+34553` 后读到的不是“看起来像 entry 的随机字节”，而是 digest、entryId、lac、累计字节数都自洽的真实 BookKeeper entry stream。

结论：

```text
L15069 在 bookie-1 上的 569 条偶数 entry 数据都存在于 855.log；
RocksDB location index 对这 569 条 entry 全部统一早了 34553 bytes；
这不是随机损坏，也不是 L15021 覆写 L15069；
这是一个稳定的 logical position 与实际文件位置差值。
```

因此，原调查中“全文件无 L15069 / L15069 数据不存在”的结论应被本补充文档覆盖：

```text
L15069 data body 存在；
不可读的直接原因是本地 location index 记录了错误 offset。
```

---



## 9. 当前结论一句话

```text
855.log 的真实 ledgers map 完整存在，但 header 指早了 34553 bytes；
真实 ledgers map 同时登记 L15069 和 L15021；
L15069 的真实 data body 也存在于 855.log；
RocksDB location index 对 L15069 的 569 条本地 entry 全部统一早了 34553 bytes；
因此该问题高度指向 EntryLogger / BufferedChannel logical position 比实际文件写入位置落后 34553 bytes。
```

---



## 10. 源码侧更精确的落点



### 10.1 直接落点不是 seal，而是写 entry 时返回 location 的 position

`EntryLogManagerBase.addEntry()` 当前 4.16.7 代码形态：

```java
int entrySize = entry.readableBytes() + 4;
BufferedLogChannel logChannel = getCurrentLogForLedgerForAddEntry(ledger, entrySize, rollLog);

sizeBuffer.writeInt(entry.readableBytes());
logChannel.write(sizeBuffer);

long pos = logChannel.position();
logChannel.write(entry);
logChannel.registerWrittenEntry(ledger, entrySize);

return (logChannel.getLogId() << 32L) | pos;
```

这里的 location 语义是：

```text
entry size prefix 起点 + 4 = entry body 起点
```

也就是：

```text
写完 4 字节 size 后，
用 BufferedChannel.logical position 作为 body offset，
随后把 body 写入 entrylog。
```

因此，如果 `logChannel.position()` 已经比真实 `FileChannel.position()` 早 34553：

```text
RocksDB location index 会记录 logical body offset；
真实 entry body 会落在 physical body offset；
二者差值稳定保持 34553。
```

这正好匹配 L15069 全量验证：

```text
total_index_rows_log2133: 569
ok_after_plus_34553: 569
bad_count: 0
```

所以，从读路径角度看，L15069 的直接坏点是：

```text
SingleDirectoryDbLedgerStorage.checkpoint()
  -> EntryLogger.addEntry()
     -> EntryLogManagerBase.addEntry()
        -> long pos = logChannel.position()
  -> EntryLocationIndex.addLocation(batch, ledgerId, entryId, location)
```

`EntryLocationIndex` 没有自己算 offset；它只是保存 `EntryLogger.addEntry()` 返回的值。

### 10.2 为什么 header 也错同一个 34553

`DefaultEntryLogger.BufferedLogChannel.appendLedgersMap()` 当前代码：

```java
long ledgerMapOffset = this.position();
...
write(serializedMap);
...
super.flush();
...
this.fileChannel.write(mapInfo, LEDGERS_MAP_OFFSET_POSITION);
```

这和普通 entry 写入使用的是同一个 `BufferedChannel.position()`。

因此如果 active log channel 在 seal 前已经形成：

```text
logical position = physical position - 34553
```

seal 时就会发生：

```text
header.ledgersMapOffset 写入 logical position；
真实 ledgers map 通过 FileChannel 追加到 physical position；
header 比真实 map 起点早 34553。
```

这解释了两个独立现象为什么 delta 完全相同：

```text
L15069 index offset 早 34553；
855.log header ledgersMapOffset 也早 34553。
```

它们不是两个损坏点，而是同一个 `BufferedChannel.position` 脱钩状态在两个调用点上的表现。

### 10.3 最可疑的脱钩代码窗口

`BufferedChannel.write(ByteBuf src)`：

```java
public void write(ByteBuf src) throws IOException {
    int copied = 0;
    boolean shouldForceWrite = false;
    synchronized (this) {
        int len = src.readableBytes();
        while (copied < len) {
            int bytesToCopy = Math.min(src.readableBytes() - copied, writeBuffer.writableBytes());
            writeBuffer.writeBytes(src, src.readerIndex() + copied, bytesToCopy);
            copied += bytesToCopy;

            if (!writeBuffer.isWritable()) {
                flush();
            }
        }
        position += copied;
        ...
    }
    ...
}
```

`BufferedChannel.flush()`：

```java
public synchronized void flush() throws IOException {
    ByteBuffer toWrite = writeBuffer.internalNioBuffer(0, writeBuffer.writerIndex());
    do {
        fileChannel.write(toWrite);
    } while (toWrite.hasRemaining());
    writeBuffer.clear();
    writeBufferStartPosition.set(fileChannel.position());
}
```

关键点：

```text
write() 过程中，flush() 可以先把 writeBuffer 的部分或全部内容写进 FileChannel；
但是 logical position 要等整个 write() 结束后才 position += copied。
```

如果 `flush()` 在 `fileChannel.write(toWrite)` 已经推进物理文件后抛出 IOException：

```text
FileChannel.position 已经前进；
writeBuffer.clear() 未执行；
writeBufferStartPosition 未更新；
write() 里的 position += copied 未执行；
异常向上抛出。
```

`SingleDirectoryDbLedgerStorage.checkpoint()` 捕获 IOException 后：

```java
} catch (IOException e) {
    recordFailedEvent(...);
    throw e;
} finally {
    isFlushOngoing.set(false);
    flushMutex.unlock();
}
```

它不会做这些事：

```text
不会清空 writeCacheBeingFlushed；
不会关闭当前 BufferedLogChannel；
不会把 FileChannel 截断回 logical position；
不会把 BufferedChannel.position 重置为 FileChannel.position。
```

因此下一轮 flush / checkpoint 可能在同一个已经脱钩的 log channel 上继续：

```text
物理文件从 FileChannel 当前位置继续追加；
EntryLogger 返回的 location 仍来自落后的 logical position；
RocksDB batch 保存这些落后的 location。
```

这就是目前最符合所有证据的源码级损伤序列。

需要强调：

```text
34553 不像是某个固定配置值；
它更像是一次失败/重试窗口中，已经进入 FileChannel 但没有被 logical position 计入的字节数。
```



### 10.4 `flushEntrylogBytes=268435456` 的关系

现场配置：

```text
flushEntrylogBytes=268435456
```

源码传递路径：

```text
ServerConfiguration.getFlushIntervalInBytes()
  -> EntryLoggerAllocator.allocateNewLog()
  -> new BufferedLogChannel(..., conf.getFlushIntervalInBytes())
  -> BufferedChannel.unpersistedBytesBound
```

这会启用 `BufferedChannel.write()` 里的 regular flush 分支：

```java
if (doRegularFlushes) {
    unpersistedBytes.addAndGet(copied);
    if (unpersistedBytes.get() >= unpersistedBytesBound) {
        flush();
        shouldForceWrite = true;
    }
}
```

这不说明 delta 应该等于 256MiB；它只说明：

```text
855.log 写入过程中，除了 rollover/checkpoint，也可能在普通 addEntry 写入路径里触发 flush。
```

因此如果现场日志里能找到 `Error during flush` / `IOException` / 磁盘短暂异常 / 容器中断，就能进一步闭合这条链。

### 10.5 后续修复提交与本案的关系

当前本地分支是：

```text
release-4.16.7
```

后续提交：

```text
3c5123d0a7 Prevent double flush due to race in SingleDirectoryDbLedgerStorage (#4305)
15a5b49c43 SingleDirectoryDbLedgerStorage skip optimistic cache put sometimes (#4306)
591c58df43 Write journal entry length prefix and payload in a single BufferedChannel write (#4833)
```

关系判断：

```text
#4305/#4306 修改 DbLedgerStorage 的 write-cache/flush 并发边界；
它们说明 4.16.7 这块后来确实被修过竞态，但不能单独解释 34553。

#4833 主要修改 Journal，把 len 和 payload 合并成一次 BufferedChannel.write；
它没有修改 EntryLogManagerBase.addEntry() 的 entrylog 写入路径；
所以不能把 855.log 的 entrylog 损坏直接归因到 #4833。
```

当前最稳妥的说法：

```text
本案直接证据指向 entrylog 的 BufferedChannel logical position 脱钩；
DbLedgerStorage 的 flush retry 机制使这个错误 location 被写入 RocksDB；
后续几个提交只能作为“相关区域后来被收紧”的旁证，不是本案的直接证明。
```

---



## 11. 下一步验证：找 34553 从哪里开始

`readlogmetadata` fallback scanning 曾经输出：

```text
Short read for ledger entry from entryLog 2133@425908828 (647870353 != 1934647668)
```

按 `scanEntryLog()` 源码，这里的：

```text
entry body offset = 425908828
entry size offset = 425908824
错误 entrySize   = 1934647668
EOF              = 425908828 + 647870353 = 1073779181
```

这说明顺序扫描在 425MB 左右已经脱帧。

下一条最有价值的现场验证是：

```text
检查 425908824 + 34553 = 425943377 是否是一个合法 entry size 起点。
```

如果那里是合法 entry：

```text
说明 34553 的 logical/physical delta 至少在 425MB 前后已经形成；
L15069 只是后续被这个 delta 影响的一个 ledger。
```

如果那里不是合法 entry：

```text
说明 425MB 处还有另一段 framing 损坏，需要继续向前/向后找第一个 delta 稳定点。
```

建议现场执行：

```bash
python3 - <<'PY'
import os, struct

path = 'data/bookkeeper/ledgers/current/855.log'
delta = 34553
bad_size_start = 425908824
candidates = [
    ('bad_size_start', bad_size_start),
    ('bad_body_start', bad_size_start + 4),
    ('bad_size_start_plus_delta', bad_size_start + delta),
    ('bad_body_start_plus_delta', bad_size_start + 4 + delta),
]

def parse_at(f, pos):
    f.seek(pos)
    b = f.read(4 + 8 + 8 + 8)
    if len(b) < 28:
        return None
    size = struct.unpack_from('>i', b, 0)[0]
    lid = struct.unpack_from('>q', b, 4)[0]
    eid = struct.unpack_from('>q', b, 12)[0]
    lac = struct.unpack_from('>q', b, 20)[0]
    return size, lid, eid, lac

def plausible(size, lid, eid, lac):
    return (
        0 < size < 16 * 1024 * 1024
        and lid >= 0
        and eid >= -2
        and lac >= -1
    )

with open(path, 'rb') as f:
    print('file_size:', os.fstat(f.fileno()).st_size)
    for name, pos in candidates:
        parsed = parse_at(f, pos)
        print(name, 'pos:', pos, 'parsed:', parsed,
              'plausible:', bool(parsed and plausible(*parsed)))

    print('scan +/- 4096 around bad_size_start + delta')
    center = bad_size_start + delta
    hits = []
    start = max(1024, center - 4096)
    end = center + 4096
    f.seek(start)
    buf = f.read(end - start)
    for rel in range(0, len(buf) - 28):
        size = struct.unpack_from('>i', buf, rel)[0]
        if not (0 < size < 16 * 1024 * 1024):
            continue
        lid = struct.unpack_from('>q', buf, rel + 4)[0]
        eid = struct.unpack_from('>q', buf, rel + 12)[0]
        lac = struct.unpack_from('>q', buf, rel + 20)[0]
        if plausible(size, lid, eid, lac):
            hits.append((start + rel, size, lid, eid, lac))
            if len(hits) >= 30:
                break
    print('hits:', hits)
PY
```



### 11.1 不建议直接依赖 rebuild 命令修复

源码里有：

```text
bookkeeper shell rebuild-db-ledger-locations-index
```

它的实现 `LocationsIndexRebuildOp` 是：

```java
entryLogger.scanEntryLog(entryLogId, scanner)
```

而 `scanEntryLog()` 是从 `LOGFILE_HEADER_SIZE` 开始顺序扫：

```java
pos = LOGFILE_HEADER_SIZE;
entrySize = readInt(pos);
pos += 4 + entrySize;
```

当前 855.log 已知在：

```text
425908824 / 425908828
```

发生顺序扫描脱帧，并且工具会在 short read 时 `return`。因此直接跑全量 rebuild 很可能：

```text
只能重建 425MB 之前能顺序扫描到的 location；
不能发现 1.025GB 附近真实存在的 L15069；
反而可能把原 locations index 备份后生成一个不完整的新 index。
```

所以，在没有离线副本和明确恢复方案前，不建议直接在生产数据目录上运行 rebuild。

---



## 12. 本地源码级复现：position 脱钩状态可达

为了确认 `BufferedChannel` 的脱钩不是纯理论推测，在本地 BookKeeper 4.16.7 源码中临时加入一个最小单测：

```text
bookkeeper-server/src/test/java/org/apache/bookkeeper/bookie/BufferedChannelTest.java
```

测试名：

```text
testPositionCanLagFileChannelAfterPartialFlushFailure
```

测试构造：

```text
1. BufferedChannel write buffer capacity = 16 bytes。
2. 写入一个 16 bytes 的 ByteBuf，触发 write() 内部 flush()。
3. 包装 FileChannel：
   第一次 write(ByteBuffer) 只真实写入 8 bytes 并返回；
   第二次 write(ByteBuffer) 抛 IOException。
4. 观察异常后：
   BufferedChannel.logical position = 0；
   FileChannel.physical position    = 8。
5. 再写入 1 byte：
   由于旧 writeBuffer 没有 clear，下一次 write() 会先把旧 16 bytes 再 flush 到 physical position=8；
   然后只把本次 1 byte 计入 logical position。
6. 观察：
   BufferedChannel.logical position = 1；
   FileChannel.physical position    = 24；
   delta                            = 23。
```

这证明当前 4.16.7 实现允许出现：

```text
FileChannel 已经前进；
BufferedChannel.position 没有同步前进；
后续写入继续使用落后的 logical position。
```

这正是 855.log 现场表现需要的底层条件。

执行命令：

```bash
MAVEN_OPTS='-Xmx1g -XX:MaxMetaspaceSize=512m' \
JAVA_HOME=/home/stephen/.local/jdk/jdk-17.0.19+10 \
PATH=/home/stephen/.local/jdk/jdk-17.0.19+10/bin:$PATH \
/home/stephen/github/java/pulsar/mvnw \
  -pl bookkeeper-server \
  -Dtest=BufferedChannelTest#testPositionCanLagFileChannelAfterPartialFlushFailure \
  test \
  -Dmaven.resources.skip=true \
  -DskipSpotbugs \
  -DskipCheckstyle \
  -DskipLicense \
  -Drat.skip=true \
  -Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=warn
```

结果：

```text
Tests run: 1, Failures: 0, Errors: 0, Skipped: 0
BUILD SUCCESS
```

注意：

```text
这个测试当前是“坏状态可达”的复现测试；
它不是最终修复后的回归测试。
```

进入修复阶段后，回归测试应该改为断言下面行为之一：

```text
1. partial flush failure 后 channel 进入不可继续写入状态；
2. 或者后续重试前强制让 logical position 与 FileChannel position 重新一致；
3. 或者 flush/write 的 position 更新具备异常安全语义，不允许返回落后 location。
```

---



## 13. 425MB scan 脱帧点的现场验证

现场执行第 11 节脚本后，结果：

```text
file_size: 1073779181

bad_size_start pos: 425908824
  parsed: (1934647668, 7513241628885740659, 2466383949190552668, 8604529940713927516)
  plausible: False

bad_body_start pos: 425908828
  parsed: (1749312884, 7019260735984917282, 7150128910614228580, 8032015300963231098)
  plausible: False

bad_size_start_plus_delta pos: 425943377
  parsed: (946221926, 3919874823477813554, 7075546664986293303, 7077744585071557981)
  plausible: False

bad_body_start_plus_delta pos: 425943381
  parsed: (912666978, 3559076474553197620, 3906085664289534771, 6639006639827198561)
  plausible: False
```

这说明：

```text
425MB 处不能简单套用后面 L15069/header 的 +34553 delta。
```

但是在 `bad_size_start + 34553` 附近扫描到了一个非常像合法 entry 起点的位置：

```text
offset = 425943701
size   = 22061
lid    = 39044
eid    = 2272
lac    = 2271
```

它与 `bad_size_start` 的差值：

```text
425943701 - 425908824 = 34877
```

与后续稳定 delta 的差异：

```text
34877 - 34553 = 324
```

当前解释：

```text
425MB 处可能已经发生 logical/physical 脱钩；
但当时的有效偏移看起来更接近 34877；
到 L15069/header 阶段稳定为 34553；
中间可能还有一段 324 bytes 级别的局部 framing 变化、重复/缺失片段，或候选 entry 只是 payload 内的巧合。
```

因此不能直接把 425MB 的短读与 L15069 的 34553 视为同一个已闭合事实，还需要验证 `425943701` 能否连续解析出 entry 链。

建议继续现场执行：

```bash
python3 - <<'PY'
import os, struct

path = 'data/bookkeeper/ledgers/current/855.log'
starts = [
    425943701,  # strongest candidate from previous scan
    425943377,  # bad_size_start + 34553
    425908824,  # scanner's bad size offset
]

def parse_at(f, pos):
    f.seek(pos)
    b = f.read(28)
    if len(b) < 28:
        return None
    size = struct.unpack_from('>i', b, 0)[0]
    lid = struct.unpack_from('>q', b, 4)[0]
    eid = struct.unpack_from('>q', b, 12)[0]
    lac = struct.unpack_from('>q', b, 20)[0]
    return size, lid, eid, lac

def plausible(x):
    if not x:
        return False
    size, lid, eid, lac = x
    return 0 < size < 16 * 1024 * 1024 and lid >= 0 and eid >= -2 and lac >= -1

with open(path, 'rb') as f:
    file_size = os.fstat(f.fileno()).st_size
    print('file_size:', file_size)
    for start in starts:
        print('\\nchain_from:', start)
        pos = start
        ok = 0
        for i in range(20):
            x = parse_at(f, pos)
            print(i, 'pos:', pos, 'parsed:', x, 'plausible:', plausible(x))
            if not plausible(x):
                break
            size, lid, eid, lac = x
            ok += 1
            pos += 4 + size
            if pos >= file_size:
                break
        print('ok_chain_len:', ok, 'next_pos:', pos)

    # Find an entry ending exactly at the strongest candidate. This helps locate the
    # previous real frame boundary before the resync point.
    target = 425943701
    window = 2 * 1024 * 1024
    start = max(1024, target - window)
    f.seek(start)
    buf = f.read(target - start)
    endings = []
    for rel in range(0, len(buf) - 28):
        pos = start + rel
        size = struct.unpack_from('>i', buf, rel)[0]
        if not (0 < size < 16 * 1024 * 1024):
            continue
        if pos + 4 + size != target:
            continue
        lid = struct.unpack_from('>q', buf, rel + 4)[0]
        eid = struct.unpack_from('>q', buf, rel + 12)[0]
        lac = struct.unpack_from('>q', buf, rel + 20)[0]
        if lid >= 0 and eid >= -2 and lac >= -1:
            endings.append((pos, size, lid, eid, lac))
    print('\\nentries_ending_at_425943701:', endings[:20])
PY
```

同时建议查 RocksDB location index 中 L39044/E2272 附近的位置：

```bash
./bin/bookkeeper shell ledger -id 39044 2>&1 | egrep 'entry (2268|2269|2270|2271|2272|2273|2274|2275)[[:space:]]'
```

如果命令版本不接受 `-id`，改用旧 shell 参数形式：

```bash
./bin/bookkeeper shell ledger -m 39044 2>&1 | egrep 'entry (2268|2269|2270|2271|2272|2273|2274|2275)[[:space:]]'
```

关键判断：

```text
如果 L39044/E2272 的 index pos = 425908828 左右：
  说明 425MB 处也存在 index 早于真实 body 的问题，但当时 delta 约为 34877。

如果 index pos = 425943705 左右：
  说明 425943701 可能只是文件中的正常 entry，scan 在 425908824 脱帧另有原因。

如果 425943701 不能连续解析：
  说明它可能只是 payload 内的巧合命中。
```



### 13.1 更早的顺序扫描脱帧：86326

后续现场脚本用更严格的 entry 合理性判断重新顺序扫描：

```text
file_size: 1073779181

sequential_fail_pos: 86326
parsed:
  size = 386008842
  lid  = 1116334194590091862
  eid  = 1114927214843331868
  lac  = 461349601976061758

last_sequential_entries_before_fail:
  (1024, 43,    240725,  5636,  5635,  1071)
  (1071, 43,    240725,  5637,  5636,  1118)
  (1118, 63,    240726, 10755, 10754,  1185)
  (1185, 29790, 240727, 17717, 17716, 30979)
  (30979,55343, 240727, 17719, 17717, 86326)
```

这解释了 `readlogmetadata` fallback 输出中的异常 ledger：

```text
Lid=1116334194590091862, TotalSizeOfEntriesOfLedger=386008846
```

因为 BookKeeper `scanEntryLog()` 只判断：

```java
int entrySize = headerBuffer.readInt();
if (entrySize <= 0) {
    pos++;
    continue;
}
```

它不会拒绝 386MB 这种不合理 entry size，因此它会把：

```text
86326 处的 386008842 bytes 假 entry
```

当作真实 entry 处理，并累计：

```text
386008842 + 4 = 386008846
```

这也说明：

```text
855.log 的 fallback scan metadata 从 86326 开始就已经不可信；
425908828 的 short read 只是更晚的结果，不是第一个脱帧点。
```

另一个现场结果：

```text
entries_ending_at_425908824: []
entries_ending_at_425943701: [(425930456, 13241, 39044, 2271, 2270)]
```

含义：

```text
425943701 属于真实连续 entry 链；
425908824 不是某条真实 entry 的自然边界。
```



### 13.2 下一步：检查 86326 附近是否也存在 34553/34877 偏移

现在需要验证：

```text
86326 + 34553 = 120879
86326 + 34877 = 121203
```

附近是否存在真实 entry 链。

如果 `121203` 附近能连续解析：

```text
说明 position 脱钩很可能在 855.log 很早期就已经出现；
425MB 的 34877 只是同一个早期 delta 的延续。
```

如果 `120879` 附近能连续解析：

```text
说明 34553 这个后期稳定 delta 可能从很早就已存在；
425943701 的 34877 需要另行解释。
```

建议现场执行：

```bash
python3 - <<'PY'
import os, struct

path = 'data/bookkeeper/ledgers/current/855.log'
centers = [
    ('fail_86326', 86326),
    ('fail_plus_34553', 86326 + 34553),
    ('fail_plus_34877', 86326 + 34877),
]

def parse_at(f, pos):
    f.seek(pos)
    b = f.read(28)
    if len(b) < 28:
        return None
    return struct.unpack_from('>iqqq', b, 0)

def plausible(x):
    if not x:
        return False
    size, lid, eid, lac = x
    return (
        24 <= size < 16 * 1024 * 1024
        and 0 <= lid < 10_000_000_000
        and 0 <= eid < 100_000_000
        and -1 <= lac <= eid
    )

def chain_len(f, pos, max_steps=12):
    out = []
    for i in range(max_steps):
        x = parse_at(f, pos)
        if not plausible(x):
            break
        size, lid, eid, lac = x
        out.append((pos, size, lid, eid, lac))
        pos += 4 + size
    return out

with open(path, 'rb') as f:
    print('file_size:', os.fstat(f.fileno()).st_size)
    for name, center in centers:
        print('\\ncenter:', name, center)
        exact = chain_len(f, center, 5)
        print('exact_chain:', exact)

        hits = []
        start = max(1024, center - 8192)
        end = center + 8192
        for pos in range(start, end):
            chain = chain_len(f, pos, 6)
            if len(chain) >= 4:
                hits.append(chain)
                if len(hits) >= 10:
                    break
        print('chain_hits:')
        for chain in hits:
            print('  len=%d first=%s last=%s' % (len(chain), chain[0], chain[-1]))
PY
```

另外，旧版 shell 的 `ledger` 命令语法是：

```text
ledger [-m] <ledger_id>
```

所以查 L39044 index 应该用：

```bash
./bin/bookkeeper shell ledger 39044 2>&1 | head -n 80
```

而不是：

```text
ledger -id 39044
```

`ledger -m 39044` 是打印 metadata，会去找 `entry -1`，因此输出：

```text
Entry -1 not found in 39044
```



### 13.3 86326 后第一个强候选物理链：120760

现场继续扫描 `86326 + 34553` 和 `86326 + 34877` 附近，结果：

```text
center: fail_86326 86326
exact_chain: []
chain_hits:

center: fail_plus_34553 120879
exact_chain: []
chain_hits:
  len=6 first=(120760, 32121, 38854, 11625, 11624)
        last=(288397, 54628, 38854, 11630, 11629)

center: fail_plus_34877 121203
exact_chain: []
chain_hits:
  len=6 first=(120760, 32121, 38854, 11625, 11624)
        last=(288397, 54628, 38854, 11630, 11629)
```

含义：

```text
86326 本身不是 entry 起点；
120879 / 121203 精确位置也不是 entry 起点；
但 120760 是一个很强的真实物理 entry 链起点。
```

差值：

```text
120760 - 86326 = 34434
34553 - 34434 = 119
```

当前推断：

```text
855.log 很可能在 86326 附近插入/保留了一段约 34KB 的非 framing 字节；
真实物理 entry stream 在 120760 恢复；
后续 L15069/header 观测到的稳定 logical/physical delta 是 34553；
86326 与 120760 的 34434 不能直接等价于 index delta，因为 86326 是顺序 scanner 的落点，不一定是 EntryLogger 当时返回的 logical location。
```

特别是：

```text
如果 L38854/E11625 的 RocksDB index body pos = 120760 + 4 - 34553 = 86211，
则说明 34553 delta 从这里已经成立；

如果 index body pos = 120760 + 4 - 34434 = 86330，
则说明早期 delta 是 34434，后续又变化成 34553；

如果 L38854 已删除或 index 不存在，则需要用物理链连续性继续间接验证。
```

旧版 shell 对 L39044 的输出：

```text
./bin/bookkeeper shell ledger 39044
ERROR: initializing dbLedgerStorage Entry -1 not found in 39044
```

这表示该 ledger 在当前 DB ledger metadata 中可能已经不存在，不能用它对照 location index。

建议继续验证两点：

1. 物理链是否从 `120760` 一路连续到 L15069 / ledgers map。
2. L38854 是否还能从 location index dump 出来。

现场命令：

```bash
python3 - <<'PY'
import os, struct

path = 'data/bookkeeper/ledgers/current/855.log'
start = 120760
map_start = 1073775941
targets = {
    425930456: 'L39044/E2271 sizeStart',
    425943701: 'L39044/E2272 sizeStart',
    1025230743: 'L15069/E0 sizeStart',
    1073770033: 'last normal entry before map',
    1073775941: 'real ledgers map start',
}

def parse_at(f, pos):
    f.seek(pos)
    b = f.read(28)
    if len(b) < 28:
        return None
    return struct.unpack_from('>iqqq', b, 0)

def plausible(x):
    if not x:
        return False
    size, lid, eid, lac = x
    return (
        24 <= size < 16 * 1024 * 1024
        and 0 <= lid < 10_000_000_000
        and 0 <= eid < 100_000_000
        and -1 <= lac <= eid
    )

with open(path, 'rb') as f:
    file_size = os.fstat(f.fileno()).st_size
    pos = start
    count = 0
    last = None
    hit_targets = []
    ledger_switches = []
    current_lid = None

    while pos < map_start:
        if pos in targets:
            hit_targets.append((pos, targets[pos], parse_at(f, pos)))

        x = parse_at(f, pos)
        if not plausible(x):
            print('FAIL pos:', pos, 'parsed:', x)
            break

        size, lid, eid, lac = x
        if lid != current_lid:
            ledger_switches.append((count, pos, lid, eid, lac))
            current_lid = lid
            if len(ledger_switches) > 30:
                ledger_switches.pop(0)

        last = (pos, size, lid, eid, lac, pos + 4 + size)
        pos += 4 + size
        count += 1
    else:
        print('REACHED map_start')

    print('count:', count)
    print('last:', last)
    print('next_pos:', pos)
    print('hit_targets:')
    for row in hit_targets:
        print(' ', row)
    print('last_ledger_switches:')
    for row in ledger_switches:
        print(' ', row)
PY
```

查 L38854 index：

```bash
./bin/bookkeeper shell ledger 38854 2>&1 | head -n 80
./bin/bookkeeper shell ledger 38854 2>&1 | egrep 'entry (1162[0-9]|1163[0-2])[[:space:]]'
```



### 13.4 120760 到真实 ledgers map 是完整连续主链

现场从 `120760` 开始按 entry framing 连续扫描到真实 ledgers map：

```text
REACHED map_start
count: 411690
last: (1073770033, 5904, 39095, 6725, 6724, 1073775941)
next_pos: 1073775941

hit_targets:
  (425930456, 'L39044/E2271 sizeStart', (13241, 39044, 2271, 2270))
  (425943701, 'L39044/E2272 sizeStart', (22061, 39044, 2272, 2271))
  (1025230743, 'L15069/E0 sizeStart', (41, 15069, 0, -1))
  (1073770033, 'last normal entry before map', (5904, 39095, 6725, 6724))
```

这是目前最强的数据侧结论：

```text
855.log 从 120760 开始直到真实 ledgers map，物理 entry framing 完整连续；
L39044、L15069、文件尾最后一条普通 entry 都在这条连续主链上；
真实 ledgers map 紧跟在最后一条普通 entry 后面。
```

因此 855.log 不是全文件随机损坏，而是：

```text
早期 86326 附近发生一次 framing/position 异常；
之后文件主体继续按物理 FileChannel 位置正常追加；
但 logical position / RocksDB location / header map offset 与 physical position 长期保持固定差值。
```

`120760` 与后期稳定 delta 的关系：

```text
120760 - 34553 = 86207
```

而顺序 scanner 的坏点是：

```text
86326
```

两者差：

```text
86326 - 86207 = 119
```

这个 `119` 很可能不是随机数，而是早期边界错位的一部分：

```text
如果 86207 处能解析出与 120760 相同或相关的 entry stream，
则说明 scanner 因为上一条 L240727/E17719 的 size 多算了 119 bytes，
错过了 86207 这个真实/逻辑边界。
```

当前还需要验证：

```text
86207 处到底是什么；
86207..120760 之间是否包含一段可解析 entry stream、重复 entry stream，还是纯 payload/半条失败写入。
```

建议现场执行：

```bash
python3 - <<'PY'
import os, struct

path = 'data/bookkeeper/ledgers/current/855.log'
starts = [
    86207,    # 120760 - stable delta 34553
    86211,    # possible body offset if 86207 is sizeStart
    86326,    # scanner fail point
    120760,   # physical main-chain start
]

def parse_at(f, pos):
    f.seek(pos)
    b = f.read(28)
    if len(b) < 28:
        return None
    return struct.unpack_from('>iqqq', b, 0)

def plausible(x):
    if not x:
        return False
    size, lid, eid, lac = x
    return (
        24 <= size < 16 * 1024 * 1024
        and 0 <= lid < 10_000_000_000
        and 0 <= eid < 100_000_000
        and -1 <= lac <= eid
    )

def chain(f, pos, limit=20):
    out = []
    for i in range(limit):
        x = parse_at(f, pos)
        out.append((pos, x, plausible(x)))
        if not plausible(x):
            break
        size, lid, eid, lac = x
        pos += 4 + size
    return out

with open(path, 'rb') as f:
    print('file_size:', os.fstat(f.fileno()).st_size)
    for s in starts:
        print('\\nchain_from:', s)
        for row in chain(f, s, 12):
            print(row)

    print('\\nstrong chains in 82000..125000:')
    hits = []
    for pos in range(82000, 125000):
        c = chain(f, pos, 8)
        if sum(1 for _, _, ok in c if ok) >= 5:
            hits.append(c)
            if len(hits) >= 20:
                break
    for c in hits:
        ok_rows = [r for r in c if r[2]]
        print('len=%d first=%s last=%s' % (len(ok_rows), ok_rows[0], ok_rows[-1]))

    print('\\nhex around 86207, 86326, 120760')
    for s in [86207, 86326, 120760]:
        f.seek(s)
        data = f.read(64)
        print(s, data.hex())
PY
```

还可以直接对比 `86207` 和 `120760` 两处的字节是否相似：

```bash
python3 - <<'PY'
path = 'data/bookkeeper/ledgers/current/855.log'
with open(path, 'rb') as f:
    f.seek(86207)
    a = f.read(256)
    f.seek(120760)
    b = f.read(256)

same = sum(x == y for x, y in zip(a, b))
print('same_bytes_256:', same)
print('a_hex:', a[:64].hex())
print('b_hex:', b[:64].hex())
PY
```



### 13.5 101546 是目前找到的更早连续物理主链起点

现场继续验证后，`120760` 不是最早可解析的物理 entry chain 起点。
在 `82000..125000` 范围内找到两条强链：

```text
chain_from: 86207
(86207, (84477735, 4415660474261003, 1131548248660251493, 1084254821866474243), False)

chain_from: 86211
(86211, (1028101, 1298265994190655779, 1124795331700853764, 1106490241214453510), False)

chain_from: 86326
(86326, (386008842, 1116334194590091862, 1114927214843331868, 461349601976061758), False)

chain_from: 120760
(120760, (32121, 38854, 11625, 11624), True)
(152885, (22783, 38854, 11626, 11625), True)
(175672, (12366, 38854, 11627, 11626), True)
(188042, (52113, 38854, 11628, 11627), True)
(240159, (48234, 38854, 11629, 11628), True)
(288397, (54628, 38854, 11630, 11629), True)
(343029, (47443, 38854, 11631, 11630), True)
(390476, (11019, 38854, 11632, 11631), True)
(401499, (2069, 38854, 11633, 11632), True)
(403572, (63780, 38854, 11634, 11633), True)
(467356, (69818, 38854, 11635, 11634), True)
(537178, (58291, 38854, 11636, 11635), True)

strong chains in 82000..125000:
len=8 first=(101546, (19210, 38854, 11624, 11622), True) last=(343029, (47443, 38854, 11631, 11630), True)
len=8 first=(120760, (32121, 38854, 11625, 11624), True) last=(390476, (11019, 38854, 11632, 11631), True)
```

这会修正上一节的一个中间推断：

```text
此前把 120760 当作“主链起点”只是因为从那里开始已经能连续解析；
最新扫描显示 101546 处的 L38854/E11624 才是当前窗口内更早的主链 entry。
```

因此当前的数据侧形态应表述为：

```text
1024 开始的严格顺序扫描在 86326 失败；
86326、86207、86211 都不是有效 entry sizeStart；
从 101546 开始存在一条强连续物理 entry chain，至少覆盖 L38854/E11624..E11631；
此前已验证从 120760 到真实 ledgers map 1073775941 完整连续。
```

两个关键距离：

```text
101546 - 86326 = 15220
120760 - 101546 = 19214 = L38854/E11624 的 4 + size(19210)
```

第二个等式很重要：

```text
101546 处 entry size = 19210；
101546 + 4 + 19210 = 120760；
所以 120760 正好是 L38854/E11625 的 sizeStart。
```

字节对比也排除了 `86207` 是 `120760` 重复流起点的可能：

```text
same_bytes_256: 3
86207: 05090727000fb00512045e0b0fb411230...
120760: 00007d7900000000000097c60000000000...
```

当前更稳妥的结论：

```text
86326 附近不是“真实 entry 边界”，而是严格 scanner 按上一条 size 跳转后的错误位置；
真正恢复到可解析 entry framing 的位置至少在 101546；
86326..101546 之间的 15220 bytes 是损坏/残留/半条写入区域，不能按 entrylog framing 解释。
```

下一步建议现场验证：

```text
1. 从 101546 连续扫描到 map_start，确认与 120760..map_start 是同一条完整主链。
2. 在 30979..101546 之间查找 entry chain 或 entry end，确认 L240727/E17719 之后是否直接进入坏区。
3. 查 L240727/E17717/E17719 的 index location，确认 index 是否还指向早期严格链。
```



## 14. 本地源码复现：partial flush 后 header map offset 会写成 stale position

在本地 `/home/stephen/github/java/bookkeeper` 的 `release-4.16.7` 代码上增加了两个复现测试：

```text
bookkeeper-server/src/test/java/org/apache/bookkeeper/bookie/BufferedChannelTest.java
```



### 14.1 最小 position drift 复现

测试名：

```text
testPositionCanLagFileChannelAfterPartialFlushFailure
```

构造一个 `FileChannel`：

```text
第一次 write 只写出 8 bytes；
第二次 write 抛 IOException；
之后恢复正常。
```

然后让 `BufferedChannel.write()` 写入刚好填满内部 buffer 的 16 bytes。

当前源码路径：

```text
BufferedChannel.write()
  -> copy 16 bytes into writeBuffer
  -> writeBuffer full, call flush()
  -> flush() first FileChannel.write writes 8 bytes
  -> flush() second FileChannel.write throws IOException
  -> write() exits before position += copied
```

结果：

```text
logical position = 0
physical FileChannel position = 8
```

继续对同一个 `BufferedChannel` 写 1 byte 后：

```text
logical position = 1
physical FileChannel position = 24
physical - logical = 23
```

这证明当前 `BufferedChannel` 在 partial flush failure 后可以继续使用，并且 logical position 可以落后 physical FileChannel position。

### 14.2 entrylog header 级复现

测试名：

```text
testLedgersMapHeaderUsesStalePositionAfterPartialFlushFailure
```

测试流程：

```text
1. 构造 DefaultEntryLogger.BufferedLogChannel，初始位置放在 LOGFILE_HEADER_SIZE。
2. 注入同样的 partial flush failure。
3. 继续写同一个 channel，使 physical position > logical position。
4. 调用 flush() 清空当前 write buffer，但不修正 logical position。
5. 调用 appendLedgersMap()。
```

当前源码路径：

```text
DefaultEntryLogger.BufferedLogChannel.appendLedgersMap()
  long ledgerMapOffset = this.position();
  write(serializedMap);
  super.flush();
  this.fileChannel.write(mapInfo, LEDGERS_MAP_OFFSET_POSITION);
```

断言结果：

```text
header 中写入的 ledgersMapOffset == stale logical position；
真实 ledgers map entry 写在更靠后的 physical FileChannel position；
stale offset 处不是 ledgers map entry。
```

这和 855.log 的核心现象一致：

```text
header ledgersMapOffset = 1073741388
true ledgers map offset = 1073775941
true - header = 34553
```



### 14.3 验证命令

```bash
export JAVA_HOME=/home/stephen/.local/jdk/jdk-17.0.19+10
export PATH="$JAVA_HOME/bin:$PATH"
/home/stephen/github/java/pulsar/mvnw -pl bookkeeper-server \
  -Dtest=org.apache.bookkeeper.bookie.BufferedChannelTest \
  -DfailIfNoTests=false \
  -DskipSourceReleaseAssembly=true \
  -DskipShade=true \
  -DskipJavadoc=true \
  -DskipLicense=true \
  -DskipSpotbugs=true \
  -DskipCheckstyle=true \
  -DskipRat=true \
  test
```

结果：

```text
Tests run: 8, Failures: 0, Errors: 0, Skipped: 0
BUILD SUCCESS
```



## 15. 当前源码定位结论

目前最可疑、并且已被本地测试复现的根因点：

```text
bookkeeper-server/src/main/java/org/apache/bookkeeper/bookie/BufferedChannel.java
```

关键路径：

```text
BufferedChannel.write(ByteBuf src)
  copied bytes into writeBuffer
  if writeBuffer is full:
    flush()
  position += copied
```

对应源码行为：

```text
flush() 在 position += copied 之前被调用；
flush() 用 FileChannel.write(toWrite) 循环把 writeBuffer 写到底层文件；
如果 FileChannel.write 已经成功写出一部分 bytes，随后抛 IOException：
  physical FileChannel position 已经前进；
  writeBuffer 没有 clear；
  writeBufferStartPosition 没有更新；
  BufferedChannel.position 没有增加 copied；
  channel 也没有被标记为不可继续使用。
```

之后同一个 channel 如果继续被使用，就会出现：

```text
后续 flush 从 writeBuffer 的 0 开始重写整段 buffered bytes；
物理文件继续从已经前进的 FileChannel position 追加；
logical position 仍然落后；
后续 addEntry 返回的 location 使用 stale logical position；
appendLedgersMap 写 header 时也使用 stale logical position。
```

源码传播路径：

```text
EntryLogManagerBase.addEntry()
  logChannel.write(sizeBuffer)
  long pos = logChannel.position()
  logChannel.write(entry)
  return (logId << 32) | pos

SingleDirectoryDbLedgerStorage.checkpoint()
  writeCacheBeingFlushed.forEach(...)
    location = entryLogger.addEntry(...)
    entryLocationIndex.addLocation(batch, ..., location)
  entryLogger.flush()
  batch.flush()
```

因此：

```text
RocksDB location index 中记录的是 BufferedChannel.position()；
不是底层 FileChannel 的真实物理位置。
```

异常继续运行路径：

```text
SingleDirectoryDbLedgerStorage.checkpoint() 捕获 IOException 后重新抛出；
SyncThread 捕获 IOException 后只记录日志并 return；
当前 active log channel 不会因此自动关闭或失效；
writeCacheBeingFlushed 在失败路径不会 clear，后续 checkpoint 可能重放。
```

`appendLedgersMap()` 不是最初制造偏移的地方，但它会把偏移固化到 entrylog header：

```text
DefaultEntryLogger.BufferedLogChannel.appendLedgersMap()
  long ledgerMapOffset = this.position()
  write(serializedMap)
  super.flush()
  fileChannel.write(mapInfo, LEDGERS_MAP_OFFSET_POSITION)
```

这正好解释 855.log 的两个独立现象：

```text
1. L15069 的 569 条 location index 全部需要 +34553 才能读到真实 entry；
2. header ledgersMapOffset 也需要 +34553 才能读到真实 ledgers map。
```

所以当前判断：

```text
文件损坏最可能出在 BufferedChannel.flush() 的 partial write + IOException 路径；
更准确说，是 BufferedChannel.write() 内部调用 flush() 失败后，
没有让 logical position / write buffer / channel lifecycle 与底层 FileChannel 的 partial progress 保持一致。
```

补充检查：

```text
本地 origin/master 与 origin/branch-4.18 的 BufferedChannel 仍保持同类结构：
copyIntoWriteBuffer() 过程中 buffer full 可触发 flush()；
updatePositionAndFlushIfNeeded(copied) 在 copy/flush 全部成功之后才更新 position。
```

因此当前看不到已有上游分支已经消除该 exception-safety 风险。

## 16. 下一步现场验证命令



### 16.1 收窄 86326..101546 坏区

目标：

```text
确认 101546..1073775941 是否完整连续；
确认 30979..101546 内是否存在能接到 101546 的 entry；
确认 86326..101546 是否只能视作不可 framing 的坏区。
```

现场执行：

```bash
python3 - <<'PY'
import os, struct

path = '855.log'
map_start = 1073775941
starts = [30979, 86207, 86326, 101546, 120760]
targets = {
    30979: 'last strict entry L240727/E17719 sizeStart',
    86326: 'strict scanner fail position',
    101546: 'first strong physical chain candidate L38854/E11624',
    120760: 'L38854/E11625 sizeStart',
    1073770033: 'last normal entry before ledgers map',
}

def parse_at(f, pos):
    f.seek(pos)
    b = f.read(28)
    if len(b) < 28:
        return None
    return struct.unpack_from('>iqqq', b, 0)

def plausible(x):
    if not x:
        return False
    size, lid, eid, lac = x
    return (
        24 <= size < 16 * 1024 * 1024
        and 0 <= lid < 10_000_000_000
        and 0 <= eid < 100_000_000
        and -1 <= lac <= eid
    )

def chain_from(f, start, limit=None, stop=None):
    pos = start
    count = 0
    last = None
    hits = []
    while True:
        if stop is not None and pos >= stop:
            return True, count, last, pos, hits
        if limit is not None and count >= limit:
            return True, count, last, pos, hits
        if pos in targets:
            hits.append((pos, targets[pos], parse_at(f, pos)))
        x = parse_at(f, pos)
        if not plausible(x):
            return False, count, last, pos, hits
        size, lid, eid, lac = x
        last = (pos, size, lid, eid, lac, pos + 4 + size)
        pos += 4 + size
        count += 1

with open(path, 'rb') as f:
    print('file_size:', os.fstat(f.fileno()).st_size)

    print('\\nchains:')
    for start in starts:
        ok, count, last, next_pos, hits = chain_from(f, start, limit=12)
        print('start=%d ok=%s count=%d last=%s next=%d' % (start, ok, count, last, next_pos))
        for h in hits:
            print('  hit:', h)

    print('\\nchain_101546_to_map_start:')
    ok, count, last, next_pos, hits = chain_from(f, 101546, stop=map_start)
    print('ok:', ok)
    print('count:', count)
    print('last:', last)
    print('next_pos:', next_pos)
    for h in hits:
        print('  hit:', h)

    print('\\nentries_ending_at_101546_in_30979_101546:')
    endings = []
    last_plausible_before_101546 = None
    for pos in range(30979, 101546):
        x = parse_at(f, pos)
        if plausible(x):
            size, lid, eid, lac = x
            end = pos + 4 + size
            if end == 101546:
                endings.append((pos, size, lid, eid, lac))
            if end <= 101546:
                last_plausible_before_101546 = (pos, size, lid, eid, lac, end)
    print('count:', len(endings))
    print('samples:', endings[:30])
    print('last_plausible_before_101546:', last_plausible_before_101546)

    print('\\nstrong_chains_30979_101546:')
    strong = []
    for pos in range(30979, 101546):
        ok, count, last, next_pos, _ = chain_from(f, pos, limit=8)
        if count >= 4:
            strong.append((count, pos, last, next_pos))
    strong.sort(key=lambda r: (-r[0], r[1]))
    for row in strong[:30]:
        print(row)
PY
```



### 16.2 查现场 flush/IO 错误日志

目标：

```text
数据文件已经证明出现了 persistent position delta；
日志可以帮助确认触发它的具体 IOException 类型和时间点。
```

现场执行：

```bash
stat data/bookkeeper/ledgers/current/855.log

grep -RniE \
  'Exception flushing ledgers|Error during flush|No space left|Input/output error|Read-only file system|AsynchronousCloseException|ClosedChannelException|855\\.log|2133\\.log|entrylog 2133|entryLog 2133|checkpoint' \
  logs/ conf/ 2>/dev/null | head -n 300
```

如果日志目录不叫 `logs/`，把路径替换成实际 bookie 日志目录即可。

## 17. 现场验证更新：101546 可完整连到真实 ledgers map，且还能前接到 76849

现场执行第 16.1 节脚本后输出：

```text
file_size: 1073779181

chains:
start=30979 ok=False count=1 last=(30979, 55343, 240727, 17719, 17717, 86326) next=86326
  hit: (30979, 'last strict entry L240727/E17719 sizeStart', (55343, 240727, 17719, 17717))
  hit: (86326, 'strict scanner fail position', (386008842, 1116334194590091862, 1114927214843331868, 461349601976061758))
start=86207 ok=False count=0 last=None next=86207
start=86326 ok=False count=0 last=None next=86326
start=101546 ok=True count=12 last=(467356, 69818, 38854, 11635, 11634, 537178) next=537178
start=120760 ok=True count=12 last=(537178, 58291, 38854, 11636, 11635, 595473) next=595473

chain_101546_to_map_start:
ok: True
count: 411691
last: (1073770033, 5904, 39095, 6725, 6724, 1073775941)
next_pos: 1073775941

entries_ending_at_101546_in_30979_101546:
count: 1
samples: [(76849, 24693, 38854, 11623, 11622)]
last_plausible_before_101546: (76849, 24693, 38854, 11623, 11622, 101546)

strong_chains_30979_101546:
(8, 65536, (240159, 48234, 38854, 11629, 11628, 288397), 288397)
(8, 76849, (288397, 54628, 38854, 11630, 11629, 343029), 343029)
```

这个结果把物理主链起点继续前移：

```text
76849 处是 L38854/E11623，size=24693，next=101546；
101546 处是 L38854/E11624，size=19210，next=120760；
120760 处是 L38854/E11625，size=32121。
```

并且：

```text
从 101546 到真实 ledgers map 1073775941 已确认完整连续；
因为 76849 能正好接到 101546，所以从 76849 起至少也接入同一条物理主链。
```

更重要的是，`76849` 落在严格扫描认为的 L240727/E17719 范围内：

```text
L240727/E17719 sizeStart = 30979
declared size = 55343
declared end = 30979 + 4 + 55343 = 86326

L38854/E11623 sizeStart = 76849
```

也就是说：

```text
按 30979 处声明的 size，scanner 会把 76849..86326 当成 L240727/E17719 的 body；
但 76849 开始实际存在一条完整的 L38854 物理 entry chain。
```

这说明 30979 处的 L240727/E17719 本身很可能就是“跨越后续真实 entries 的异常 entry”：

```text
要么它的 size 字段过大；
要么它的 body 在写入途中失败/残缺，随后 retry 或后续 flush 从 76849 开始写入 L38854 chain；
严格 scanner 只相信 30979 的 size，于是跳到 86326 后失败。
```

当前坏区边界从原来的：

```text
86326..101546
```

修正为更细的：

```text
30979 处存在一个可解析但可疑的 L240727/E17719 framing；
76849 开始已经进入后续真实物理主链；
因此 30979..76849 是 L240727/E17719 的实际/残留数据区；
76849..86326 被 30979 的 declared size 错误覆盖，但实际上属于 L38854/E11623 及后续 entry chain。
```

缺口大小：

```text
76849 - 30979 = 45870
86326 - 76849 = 9477
101546 - 76849 = 24697 = 4 + 24693
```

后续更精确验证应集中在：

```text
1. 76849 是否能一直连续到 map_start。
2. 65536 处那条强链的完整 entry 明细。
3. 30979 处 L240727/E17719 的前 64 bytes、尾部附近、以及 76849 前后字节，判断它是真的 entry，还是刚好误解析出的 framing。
```

## 18. 关键闭环：34553 正好等于 64KiB buffer 边界减去 E17719 bodyStart

BookKeeper 当前配置没有显式设置 `writeBufferBytes`，源码默认值：

```text
ServerConfiguration.getWriteBufferBytes() = 65536
```

源码位置：

```text
bookkeeper-server/src/main/java/org/apache/bookkeeper/conf/ServerConfiguration.java
getWriteBufferBytes() -> getInt(WRITE_BUFFER_SIZE, 65536)
```

现场数据：

```text
L240727/E17719 sizeStart = 30979
L240727/E17719 bodyStart = 30979 + 4 = 30983
后续所有正确 physical 位置 - stored/index/header logical 位置 = 34553
```

计算：

```text
65536 - 30983 = 34553
```

这非常关键。它给出了一个能同时解释文件结构和源码行为的时间线：

```text
1. 新 entrylog 创建后，1024 bytes header 和前几条 entries 先留在 64KiB writeBuffer 中。
2. 写 L240727/E17719 时，先写 4-byte size 到 offset 30979。
3. EntryLogManagerBase.addEntry() 此时记录 bodyStart position = 30983。
4. 继续写 E17719 body。
5. E17719 body 的前 34553 bytes 正好把 writeBuffer 填满到 65536。
6. BufferedChannel.write() 在 position += copied 之前调用 flush()。
7. flush() 已经让底层 FileChannel 前进到 65536，但随后抛 IOException。
8. BufferedChannel.position 仍停在 30983。
9. 后续同一个 BufferedLogChannel 继续使用，physical 从 65536 继续追加，但 logical 从 30983 继续计数。
10. 从此产生稳定 delta:
    physical - logical = 65536 - 30983 = 34553。
```

这也解释了为什么严格 scanner 会在 86326 失败：

```text
30979 处的 size 字段仍声明 L240727/E17719 长度为 55343；
严格 scanner 因此认为它应该结束在 86326；
但 65536 起已经变成后续真实物理 entry chain；
所以 86326 落在 L38854/E11623 的 body 内部，不是 entry 边界。
```

目前最精确的数据侧定位：

```text
文件层面：L240727/E17719 的 body 在 offset 65536 处被截断/替换为后续 entry stream。
源码层面：BufferedChannel.write() 内部 flush() 失败后，未同步 logical position 与 physical FileChannel position，也未让 channel 失效。
```

历史日志已经不可用，因此目前无法从日志侧确认当时具体 IOException 类型。
但日志不是当前结论的必要条件：`34553 = 65536 - 30983` 已经把数据偏移和 `BufferedChannel` 的 64KiB write buffer flush 边界直接连起来。

## 19. 最终现场确认：65536 是脱钩后连续物理写入链起点

现场确认命令输出：

```text
delta_buffer: 34553
delta_map: 34553

30979 (55343, 240727, 17719, 17717) True
30983 (0, 1033914592264192, 76102525517824, 76093935583232) False
65536 (11309, 38854, 11622, 11621) True
65540 (0, 166876659318784, 49916109914112, 49911814946816) False
76849 (24693, 38854, 11623, 11622) True
86326 (386008842, 1116334194590091862, 1114927214843331868, 461349601976061758) False
101546 (19210, 38854, 11624, 11622) True

chain_65536_to_map_count: 411693
last: (1073770033, 5904, 39095, 6725, 6724, 1073775941)
next: 1073775941
```

最终数据闭环：

```text
1. 30979 是 L240727/E17719 的 sizeStart。
2. 30983 是 E17719 的 bodyStart。
3. 65536 是 L38854/E11622 的真实 sizeStart，也是脱钩后连续物理写入链起点。
4. 65536..1073775941 是完整连续的真实物理 entry chain。
5. 1073775941 是真实 ledgers map 起点。
6. header ledgersMapOffset = 1073741388。
7. 1073775941 - 1073741388 = 34553。
8. 65536 - 30983 = 34553。
```

这说明同一个 `34553` 同时满足：

```text
writeBuffer boundary offset - failed entry bodyStart；
true ledgersMap physical offset - stale header ledgersMapOffset；
true entry physical body positions - RocksDB stored logical positions。
```

因此根因已经可以较精确地定位为：

```text
写 L240727/E17719 body 时触发 64KiB writeBuffer flush；
flush 使 physical FileChannel 前进到 65536；
随后 flush/write path 抛 IOException；
BufferedChannel.position 没有从 30983 前进；
后续写入继续使用同一个 channel；
从 L38854/E11622 开始，physical 和 logical 永久相差 34553。
```

`readlogmetadata` fallback 在 86326 看到的巨大 ledger：

```text
(386008842, 1116334194590091862, ...)
```

只是因为严格 scanner 信任 30979 处的 declared size，跳到 86326；
但 86326 实际落在 L38854/E11623 body 内部，所以解析出来的是 payload 字节，不是真 entry header。

## 20. 对“98.2% 非合法 entry 字节”的回应

独立佐证报告提到：

```text
按 BK V3 + CRC32C 严格扫描，855.log 合法 entry 累计字节约 19.1MB；
相对于 1024..真实 map 起点约 1.073GB，似乎 98.2% 字节不是合法 entry。
```

这个统计不能直接解释为“855.log 98.2% 随机损坏”，原因是它的“合法”口径很可能是：

```text
能在字节扫描中按 CRC32C digest 直接校验通过的 entry。
```

但 entrylog 的全局结构判断还要看 framing 连续性：

```text
65536..1073775941 已经按 entry framing 连续扫描到真实 ledgers map；
覆盖字节数 = 1073775941 - 65536 = 1073710405 bytes。
```

这说明从 `65536` 开始，文件主体不是随机坏块，而是一条连续的物理 entry stream。
如果某些 entry 不能用 CRC32C 验证，可能原因包括：

```text
1. 不同 ledger 使用了不同 digest 类型；
2. 缺少 ledger metadata/master key，无法按正确 digest 验证；
3. 字节级全文件搜索统计的是“CRC32C-valid hits”，不是“连续 framing 覆盖率”；
4. 30979..65536 确实是失败写留下的 partial entry body 区域，不能代表后续 65536..map_start。
```

因此更准确的全局表述是：

```text
855.log 不是 98.2% 随机损坏；
它在 30979 处留下了一条跨越后续主链的 partial/corrupt E17719 framing；
从 65536 开始存在一条完整连续的真实物理 entry stream；
RocksDB/header 使用的 logical position 则从 30983 开始持续落后 physical position 34553 bytes。
```

## 21. 对 verification-78faf567.md 的评审

第二份佐证/反驳文档：

```text
/home/stephen/github/java/pulsar/bin/20260723/855-entrylog-2133-source-position-verification-78faf567.md
```

总体上，它对核心链路仍然给出 PASS：

```text
34553 = 65536 - 30983；
65536..1073775941 可连续扫到真实 ledgers map；
BufferedChannel.position 脱钩是根因；
appendLedgersMap/header 和 L15069 location 是同源错位表现。
```

这些结论与主分析一致。

### 21.1 可采纳的建议

`verification-78faf567.md` 建议把“65536 是真实物理主链起点”改得更精确。
这个建议是合理的。

更准确的表述是：

```text
30979 是 L240727/E17719 的 sizeStart；
30983..65535 是 E17719 已落盘的 partial body；
65536 是脱钩后连续物理写入链起点，即 L38854/E11622 的 sizeStart。
```

因此本文第 19 节标题已修订为：

```text
65536 是脱钩后连续物理写入链起点
```

### 21.2 明确错误 1：L15069 pattern 搜错

`verification-78faf567.md` 第 4 节声称搜索 L15069 的 8 字节 big-endian pattern：

```text
00 00 00 00 00 00 3a cd
```

这是错误的。

实际换算：

```text
15069 = 0x3add
0x3acd = 15053
```

所以该报告第 4 节“855.log 中无 L15069 合法 entry header”的结论不能成立。
它搜索的是 ledgerId `15053`，不是 `15069`。

这也和已有现场数据矛盾：

```text
L15069 在物理位置 +34553 后可解析出 569 条 entry；
569 / 569 条 CRC32C 校验通过；
这些 entry 的 (4 + size) 累计值 = 26164；
真实 ledgers map 中 L15069 的 TotalSize 也是 26164。
```

因此正确结论仍然是：

```text
L15069 entry body 存在于 855.log；
只是 RocksDB location index 中记录的 pos 统一早了 34553 bytes。
```

### 21.3 明确错误 2：header hex 字节写错

`verification-78faf567.md` 第 1.1 节写的 header offset 字节是：

```text
00 00 00 00 3f fc a7 4c
```

但现场原始 `od` 输出和本文第 1.1 节是：

```text
00 00 00 00 3f ff fe 4c
```

后者才等于：

```text
1073741388 = 0x3ffffe4c
```

而：

```text
0x3ffca74c = 1073522508
```

该报告这里应视为抄写/录入错误。

### 21.4 需纠正的解读：E17719 不应被说成 true size = 70563

`verification-78faf567.md` 有一段说：

```text
物理主链证明 L240727/E17719 的真实 size 应为 70563
```

这个说法不准确。

`101546` 是 L38854/E11624 的 sizeStart，不是 L240727/E17719 的下一条真实 entry 边界。
如果把 `30979..101546` 都解释成 L240727/E17719 body，就会把 `65536..101546` 内已经验证连续的 L38854/E11622/E11623 entry stream 错当成 E17719 payload。

更准确的解释是：

```text
30979 处的 size=55343 是已写入文件的 declared size；
E17719 body 只写到 65536 前；
65536 后已经切换为脱钩后的后续物理写入链；
严格 scanner 信任 declared size 跳到 86326，因该位置落在 L38854/E11623 body 内而失败。
```

因此这不是“E17719 的真实 size 应该是 70563”，而是：

```text
E17719 是 partial/corrupt framing；
它的 declared size 跨越并覆盖了后续真实物理 entry stream 的一部分。
```

### 21.5 综合判断

`verification-78faf567.md` 的主 PASS 结论可以作为旁证使用，但其中两类内容不能采纳：

```text
1. 基于错误 ledgerId pattern 0x3acd 得出的 L15069 不存在结论；
2. 把 30979..101546 解释为 L240727/E17719 true body 的结论。
```

在修正这些问题后，它与主分析没有实质冲突。
