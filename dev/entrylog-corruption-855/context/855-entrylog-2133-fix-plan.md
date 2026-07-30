# 855.log / EntryLog 2133 损坏修复方案

## 1. 背景与问题边界

`pulsar-bookie-1` 上 `855.log`（entryLogId=2133）的根因已经定位为：`BufferedChannel.flush()` 在 64KiB write buffer 边界发生 `IOException` 后，底层 `FileChannel` 的 physical position 已经前进，但 `BufferedChannel.position` 仍停留在旧 logical position；同一个 `BufferedLogChannel` 后续继续写 entry 和 ledgers map，最终造成：

```text
physical position = logical position + 34553
```

后果包括：

```text
RocksDB location index 记录 stale logical body position；
entrylog header.ledgersMapOffset 记录 stale logical map position；
物理文件中 entry stream 大部分连续，但 index/header 指向早 34553 bytes。
```

因此修复目标不是“修复已有 855.log 数据”，也不是“尽量在同一个 writer 上恢复写入”，而是阻断这类 silent corruption 再次发生。

## 2. 修复目标

核心目标：

```text
底层 I/O 状态不确定时，必须 fail-closed；
不能继续写出 stale RocksDB index；
不能继续 seal 出 stale ledgersMapOffset header；
不能把 partial flush failure 变成 silent corruption。
```

非目标：

```text
不在本方案内修复已有损坏 entrylog；
不在 BufferedChannel 层盲目 retry IOException；
不要求在同一个损坏 entrylog 上恢复追加写。
```

## 3. Bookie 重启行为

BookKeeper 正常重启后不会 reopen 最后一个 entrylog 继续 append。源码路径是：

```text
DefaultEntryLogger 构造：
  扫描 ledgerDirs 中现有 .log 和 lastId；
  取最大 logId；
  EntryLoggerAllocator 初始化为该最大 logId；
  activeLogChannel 初始为 null。

第一次 addEntry：
  EntryLogManagerForSingleEntryLog.getCurrentLogForLedgerForAddEntry()
    -> activeLogChannel == null
    -> createNewLog()
    -> EntryLoggerAllocator.allocateNewLog()
    -> ++preallocatedLogId
    -> 创建新的 <next>.log。
```

所以如果 Bookie 在 I/O 异常后直接失败并重启，一般会切到下一个 log 文件写，不会继续在旧 `855.log` 上 append。

这对修复设计很重要：最安全的恢复路径是让当前 writer 失败，让 Bookie 进入 read-only、fatal storage error 或进程退出，依赖重启创建新 log，而不是在旧 log 上尝试继续写。

## 4. I/O 失败是否应该重试

`BufferedChannel.flush()` 当前已经处理了 short write：

```java
do {
    fileChannel.write(toWrite);
} while (toWrite.hasRemaining());
```

这是安全的，因为 `fileChannel.write()` 没有抛异常，只是一次写入不完整，可以继续循环把剩余 bytes 写完。

但真正的 `IOException` 不应在 `BufferedChannel` 层盲目 retry。原因是异常发生后底层状态不确定：

```text
可能一点没写；
可能已经写入一部分；
可能 FileChannel position 已经前进；
可能 ByteBuffer position 已经变化；
可能文件系统、磁盘或容器存储层处于持续异常。
```

在这个层级原地 retry 可能造成重复写、空洞、错位或 partial frame。正确分层应是：

```text
FileChannel / BufferedChannel 层：
  只 retry short write；
  IOException 后 poison 当前 channel。

Bookie 存储层：
  返回写失败，或者进入 read-only / fatal storage error。

BK client / Pulsar 层：
  通过 ack quorum、ensemble change、ledger recovery 等机制重试到其他 bookie。
```

## 5. 推荐方案总览

推荐分三层落地：

```text
P0：阻断 silent corruption
  - BufferedChannel 遇到 IOException 后 poison channel；
  - failed channel 禁止继续 write / flush / forceWrite / appendLedgersMap；
  - 上层收到 failed writer 后进入 read-only / fatal storage error / 重启；
  - header positioned write 改为 writeFully。

P1：强化 position 一致性
  - 增加 logical / physical invariant 校验；
  - 调整 position accounting，降低异常窗口；
  - 增加关键状态日志和 metrics。

P2：恢复与诊断增强
  - 读取 entrylog metadata 时校验 ledgers map offset；
  - header offset 不合法时支持 fallback 扫描文件尾；
  - GC 删除前增强 metadata 校验。
```

## 6. P0：BufferedChannel 失败后 poison

涉及文件：

```text
bookkeeper-server/src/main/java/org/apache/bookkeeper/bookie/BufferedChannel.java
```

建议新增 failed 状态：

```java
private volatile IOException writeFailure;

private void checkWritable() throws IOException {
    IOException failure = writeFailure;
    if (failure != null) {
        throw new IOException("BufferedChannel is in failed state", failure);
    }
}

private void markWriteFailure(IOException e) {
    if (writeFailure == null) {
        writeFailure = e;
    }
}
```

在以下入口开头调用 `checkWritable()`：

```text
write()
flush()
flushAndForceWrite()
flushAndForceWriteIfRegularFlush()
forceWrite()
```

`flush()` 中捕获 `IOException` 并 poison：

```java
public synchronized void flush() throws IOException {
    checkWritable();

    ByteBuffer toWrite = writeBuffer.internalNioBuffer(0, writeBuffer.writerIndex());
    try {
        do {
            fileChannel.write(toWrite);
        } while (toWrite.hasRemaining());
    } catch (IOException e) {
        markWriteFailure(e);
        throw e;
    }

    writeBuffer.clear();
    writeBufferStartPosition.set(fileChannel.position());
}
```

这样第一次 flush failure 后，后续任何写路径都会明确失败，不会继续使用 stale logical position。

## 7. P0：appendLedgersMap 不能发布 stale header

涉及文件：

```text
bookkeeper-server/src/main/java/org/apache/bookkeeper/bookie/DefaultEntryLogger.java
```

当前 `BufferedLogChannel.appendLedgersMap()` 会先取：

```java
long ledgerMapOffset = this.position();
```

然后写 ledgers map、flush、再更新 header。如果 channel 已经 failed，必须保证：

```text
不能写 ledgers map；
不能 super.flush()；
不能 fileChannel.write(header)；
不能认为 entrylog 已经正常 sealed。
```

只要 `BufferedChannel.write()` / `flush()` 在 failed 状态下必然抛异常，`appendLedgersMap()` 就不会继续发布 header。为了代码可读性，可以在 `appendLedgersMap()` 开头显式检查 channel 状态。

同时需要注意 `EntryLogManagerBase.createNewLog()` 的正常 rotation 逻辑：

```text
logChannel.flush();
logChannel.appendLedgersMap();
create next log;
```

对于 failed channel，不能走“正常 seal 后再 rotate”的路径。如果后续要支持进程内恢复，应设计独立方法：

```text
abortCurrentLogAndCreateNewLog()
  - 当前 failed log 标记不可写；
  - 不 appendLedgersMap；
  - 不写 header；
  - 从 current channel 移除；
  - 直接 allocate next log。
```

短期更稳的 P0 做法是：让 Bookie 进入 read-only / fatal storage error / 退出，由重启后新建 log。

## 8. P0：header positioned write 改 writeFully

当前 header 更新代码：

```java
this.fileChannel.write(mapInfo, LEDGERS_MAP_OFFSET_POSITION);
```

`FileChannel.write(ByteBuffer, position)` 不保证一次写完 12 bytes。建议改为循环写满：

```java
private static void writeFully(FileChannel channel, ByteBuffer buffer, long position) throws IOException {
    while (buffer.hasRemaining()) {
        int written = channel.write(buffer, position);
        if (written < 0) {
            throw new EOFException("Unexpected EOF while writing entrylog header");
        }
        position += written;
    }
}
```

然后：

```java
writeFully(this.fileChannel, mapInfo, LEDGERS_MAP_OFFSET_POSITION);
```

如果写 header 过程中抛 `IOException`，也应 poison channel，不能把该 log 当作已正常 sealed。

## 9. P1：position accounting 强化

当前异常窗口来自：

```java
writeBuffer.writeBytes(...);
if (!writeBuffer.isWritable()) {
    flush();
}
position += copied;
```

即 flush 在 `position += copied` 前执行。P0 poison 可以阻断事故复现，但长期可以考虑把 position 维护改得更难错。

可选方向：

```text
方向 A：copy 到 writeBuffer 后立即推进 logical position；
方向 B：不单独维护 position，而由 writeBufferStartPosition + writeBuffer.writerIndex() 派生；
方向 C：保留 position，但每次写/flush 后校验 invariant。
```

推荐先做 C，风险较低：

```text
position == writeBufferStartPosition + writeBuffer.writerIndex()
```

该 invariant 的含义：

```text
writeBufferStartPosition：当前 buffer 对应的文件起点；
writeBuffer.writerIndex：buffer 中尚未 flush 的字节数；
position：下一次 logical write offset。
```

如果 invariant 被破坏，应 error 日志并抛异常。

## 10. P1：日志与 metrics

flush failure 时至少记录：

```text
entryLogId
logFile
logical position
writeBufferStartPosition
writeBuffer.writerIndex
fileChannel.position()
toWrite.position()
toWrite.remaining()
exception class/message
```

建议新增 metrics：

```text
bookie_buffered_channel_write_failures
bookie_buffered_channel_failed_channels
bookie_entrylog_seal_failures
bookie_entrylog_header_write_failures
```

这样以后可以直接从日志和指标判断是否发生了 logical/physical 脱钩，而不必完全依赖事后字节分析。

## 11. P2：读路径和 GC 防护

读取 entrylog metadata 时，应校验 header 指向的位置是否真的是 ledgers map：

```text
offset 合理；
size 合理；
lid = INVALID_LID；
eid = LEDGERS_MAP_ENTRY_ID；
count 与 size 匹配；
map entry 数量与 header.ledgersCount 一致。
```

如果 header offset 不合法：

```text
不要静默信任；
fallback 到 scan entrylog；
可选：从文件尾反向寻找合法 ledgers map。
```

GC 删除 entrylog 前，如果 metadata 来自异常 header 或 scan 失败，应保守处理：

```text
不删除该 entrylog；
或者要求 verifyMetadataOnGC；
或者标记为 suspect entrylog，等待人工/后台修复任务。
```

P2 不是根因修复，但能减少坏 header 造成的二次伤害。

## 12. 回归测试建议

建议新增或调整以下测试：

```text
1. BufferedChannel partial flush failure
   - 构造 writeBufferBytes=65536；
   - 写到 buffer 满时让 FileChannel.write() 推进 position 后抛 IOException；
   - 断言 channel 进入 failed 状态。

2. failed channel blocks future writes
   - 第一次 flush 抛 IOException；
   - 再次 write() 必须继续抛 IOException；
   - 不能继续推进 logical position。

3. failed channel blocks appendLedgersMap
   - 模拟 addEntry 过程中 flush 失败；
   - 调用 appendLedgersMap()；
   - 断言抛 IOException；
   - header.ledgersMapOffset 未被写成 stale logical position。

4. header writeFully handles short positioned write
   - 模拟 FileChannel.write(ByteBuffer, position) 每次只写部分字节；
   - 断言 12 bytes header 最终完整写入。

5. normal path regression
   - 普通 addEntry / flush / appendLedgersMap 行为不变；
   - 正常 entrylog metadata 仍可从 header ledgers map 解析。
```

已有的复现测试：

```text
BufferedChannelTest.testPositionCanLagFileChannelAfterPartialFlushFailure
BufferedChannelTest.testLedgersMapHeaderUsesStalePositionAfterPartialFlushFailure
```

在修复后应改为断言：

```text
partial flush failure 后不能继续写；
appendLedgersMap 不能写 stale header。
```

## 13. 上线与兼容性风险

P0 的行为变化是：过去某些底层 I/O 异常后，Bookie 可能继续工作；修复后会更早失败或进入 read-only。

这是预期变化。因为继续工作可能导致 silent corruption，明显失败更安全。

需要关注：

```text
是否有上层代码吞掉 IOException 后继续复用同一个 writer；
Bookie 在 write failure 后当前配置会 read-only 还是退出；
Kubernetes / supervisor 是否能及时重启；
客户端是否能通过 quorum / ensemble change 吸收单个 bookie 写失败；
告警是否覆盖新增 failure metrics。
```

## 14. 推荐落地顺序

```text
第一步：
  实现 BufferedChannel poison；
  failed 后所有写路径直接抛异常；
  调整现有复现测试。

第二步：
  保护 appendLedgersMap；
  header positioned write 改 writeFully；
  增加 header short write 测试。

第三步：
  增加日志和 metrics；
  明确 Bookie 上层遇到 failed writer 后的 read-only / fatal 行为。

第四步：
  增加 position invariant 校验；
  评估是否重构 position accounting。

第五步：
  增强 readlogmetadata / GC 的坏 header 防护。
```

## 15. 其他存储引擎对照

### 15.1 WiredTiger

WiredTiger 的错误处理文档明确区分可重试错误和 fatal 错误：

```text
WT_CACHE_FULL：
  操作可以回滚后重试。

WT_PANIC：
  表示底层问题要求 database restart；
  应用可以立即退出；
  后续 WiredTiger 调用不再需要，且后续调用自身也会立即失败。
```

对 BookKeeper 的启发：

```text
BufferedChannel.flush() IOException 如果已导致 writer 状态不可判定，
就应进入类似 panic 的 failed state；
后续 write / flush / seal 调用必须立即失败；
不能让调用方继续在同一个 writer 上“试试看”。
```

### 15.2 InnoDB

InnoDB 的 doublewrite buffer 处理的是另一类问题：page flushed from buffer pool 先写到 doublewrite buffer，再写到目标位置。如果 page write 中途进程退出，恢复时可以从 doublewrite buffer 找到好副本。

InnoDB checkpoint 则是发布可恢复边界：恢复时从 checkpoint label 开始扫描 redo log，应用 checkpoint 之后的修改。

对 BookKeeper 的启发不是“照搬 doublewrite 到每个 entry”，而是两个原则：

```text
1. 数据写入和元数据发布要分阶段；
2. 元数据只能指向已经完整写入、可验证的数据边界。
```

映射到 entrylog：

```text
ledgers map 本体写入成功；
flush 成功；
map 结构可校验；
再写 header.ledgersMapOffset。
```

如果 ledgers map 写入或 flush 失败，header 不应发布 stale offset。对 append-only entrylog 来说，doublewrite 每条 entry 的成本和复杂度都过高，P0 更应该是 fail-closed。

### 15.3 RocksDB

RocksDB 的处理原则和本方案非常接近：

```text
foreground Get/Write I/O error：
  返回 rocksdb::IOError 给调用方。

background flush/compaction I/O error 且 paranoid_checks=true：
  DB 切到 read-only；
  后续所有 writes 被拒绝；
  fatal error 通常需要 close DB、修复底层问题、reopen。
```

RocksDB 官方 Background Error Handling 文档也明确说，`OnBackgroundError` 可以覆盖错误继续写，但这是有风险的，因为 RocksDB 可能无法保证 DB 一致性。

对 BookKeeper 的启发：

```text
BufferedChannel.flush() IOException 后不能继续当作正常 writer 使用；
应该 poison channel / read-only / fatal，而不是静默继续写。
```

### 15.4 TiDB / TiKV

TiDB 的本地存储层主要是 TiKV；TiKV 使用 RocksDB/Raft Engine。TiKV 的 RocksDB event listener 对 background error 的策略也偏 fail-stop：

```text
部分 NoSpace flush/compaction error：
  可交给 RocksDB 自动恢复。

Corruption / IO error：
  如果能调度 SST recovery，则 reset status；
  否则 panic；
  panic 后由 TiKV 进程退出 / abort-on-panic 配置决定退出方式。
```

也就是说，TiKV 不是在同一个不可信 RocksDB writer 上盲目继续写，而是：

```text
能明确证明可恢复的错误才恢复；
不能证明可恢复的 I/O / corruption 走 panic/fail-stop。
```

对 BookKeeper 的启发：

```text
short write 可以在 flush 内部循环处理；
IOException 后如果不能证明 writer 状态一致，就必须 fail-closed；
重试应交给 BK/Pulsar 复制层，而不是本地 FileChannel writer。
```

### 15.5 OceanBase

OceanBase 的存储层是 LSM 思路：写入先进入 MemTable，再 flush/merge 成不可变 SSTable。官方资料描述其 SSTable 由固定 2 MB macroblock 组成，macroblock 是基本写 I/O 单元；microblock 是约 16 KB 的读 I/O 单元。OceanBase 还在多个层级维护 checksum：

```text
macroblock header checksum；
microblock header checksum；
SSTable / partition 更高层 checksum。
```

OceanBase 的复制层基于 log stream / Paxos，DML 会生成 redo log 并持久化到 log stream，多副本通过共识保证可用性和一致性。

对 BookKeeper 的启发：

```text
要把“数据写入”和“元数据发布”拆开；
entrylog header.ledgersMapOffset 应视为发布元数据；
只有 ledgers map 本体写入、flush、校验成功后，才能发布 header；
读路径和 GC 路径也应校验 header 指向的 map 是否结构自洽。
```

### 15.6 ClickHouse

ClickHouse MergeTree 严格说不是传统 LSM。官方架构文档明确说：MergeTree 没有 MemTable 和 WAL，INSERT 数据直接写到文件系统形成 data part；data part 是不可变的，只创建和删除，不原地修改。

ClickHouse 的关键做法是：

```text
写入生成临时 part；
校验通过后 renameTempPartAndAdd；
part 进入 PreActive，事务 commit 后才进入 active set；
part 有 checksums；
CHECK TABLE 会校验 checksums 和文件大小；
broken / unexpected part 可以被 server detach，不再参与查询；
复制表 ATTACH 时要求 part checksums 正确，否则从其他 replica 下载。
```

对 BookKeeper 的启发：

```text
未完成或可疑的文件对象不应进入 active metadata；
failed entrylog 不应正常 appendLedgersMap / header publish；
如果以后支持进程内恢复，应设计 abort failed log -> create next log，
而不是在 failed log 上继续 append。
```

### 15.7 横向结论

这些系统虽然实现不同，但原则一致：

```text
1. 本地 short write 可以循环补齐；
2. 真正 IOException / corruption 后，不能默认继续复用同一个 writer；
3. fatal / panic 类错误后，后续调用应立即失败，而不是继续复用原 writer；
4. 可恢复必须有明确边界，例如 RocksDB Resume、TiKV SST recovery、InnoDB doublewrite、ClickHouse temp part rename；
5. 元数据发布必须晚于数据写入与校验；
6. 可疑对象应 read-only / detach / abort / panic，而不是继续参与正常写路径。
```

因此，BookKeeper 这次修复仍应坚持：

```text
P0：BufferedChannel IOException 后 poison；
P0：failed entrylog 禁止正常 seal；
P0：上层失败 / read-only；仅在存在健康 writable dir 时才切新 log；
P1：校验 ledgers map/header 结构；
P2：再考虑更复杂的进程内 abort failed log + create next log。
```

参考资料：

```text
WiredTiger Error handling:
https://source.wiredtiger.com/10.0.0/error_handling.html

MySQL InnoDB Doublewrite Buffer:
https://dev.mysql.com/doc/refman/8.4/en/innodb-doublewrite-buffer.html

MySQL InnoDB Checkpoints:
https://dev.mysql.com/doc/refman/8.4/en/innodb-checkpoints.html

RocksDB Background Error Handling:
https://github.com/facebook/rocksdb/wiki/Background-Error-Handling

RocksDB FAQ: read/write I/O errors:
https://github.com/facebook/rocksdb/wiki/RocksDB-FAQ

TiKV RocksEventListener:
https://raw.githubusercontent.com/tikv/tikv/master/components/engine_rocks/src/event_listener.rs

TiKV abort-on-panic:
https://docs.pingcap.com/tidb/stable/tikv-configuration-file/

OceanBase storage checksums:
https://en.oceanbase.com/blog/28468829696

OceanBase architecture:
https://en.oceanbase.com/docs/common-oceanbase-database-10000000001971022

ClickHouse CHECK TABLE:
https://clickhouse.com/docs/reference/statements/check-table

ClickHouse MergeTree architecture:
https://clickhouse.com/docs/resources/develop-contribute/introduction/architecture

ClickHouse renameTempPartAndAdd source:
https://github.com/ClickHouse/ClickHouse/blob/master/src/Storages/MergeTree/MergeTreeData.h
```

## 16. 方案再审视

基于源码再审视后，当前方案需要强调三个边界。

### 16.1 仅 poison BufferedChannel 是必要但不完全充分

`BufferedChannel` poison 能阻断“同一个 writer 后续继续返回 stale position”，这是 P0 核心。但上层还必须配合：

```text
收到 poisoned channel 抛出的 IOException 后，
不能吞掉异常后继续复用同一个 entryLogger / current log；
应让 Bookie 当前存储路径进入 read-only / fatal / 重启。
```

否则即使底层 channel 后续都会抛异常，上层如果反复走正常 rotate：

```text
logChannel.flush();
logChannel.appendLedgersMap();
create next log;
```

也会持续失败，无法切到新 log。因此 P0 修复应包含一条明确语义：

```text
failed current log 不能走正常 seal-and-rotate；
短期选择 fail bookie / read-only；
长期如需不中断，新增 abortCurrentLogAndCreateNewLog。
```

### 16.2 DbLedgerStorage 的 flush 顺序本身是合理的

`SingleDirectoryDbLedgerStorage.flush()` 的顺序是：

```text
entryLogger.addEntry() 写 entrylog 并收集 location；
entryLogger.flush()；
batch.flush() 写 RocksDB location index；
ledgerIndex.flush()。
```

这个顺序比“先写 index 再 flush entrylog”安全。855.log 的问题不是该顺序错误，而是 failed writer 被继续使用后，`entryLogger.addEntry()` 后续返回了 stale logical location。

因此修复重点仍是：

```text
第一次 I/O 异常后，entryLogger.addEntry() 不得再返回 location；
failed channel 上 appendLedgersMap 不得发布 header。
```

### 16.3 重启切新 log 需要 storage health gate

用户指出一个重要风险：如果底层 I/O 持续异常，Bookie 每次重启都会创建新 entrylog，可能形成重启风暴和大量空/半空 `.log` 文件。

这个风险真实存在。`EntryLoggerAllocator.allocateNewLog()` 的行为是：

```text
++preallocatedLogId；
创建新的 <logId>.log；
写 entrylog header；
更新各 ledger dir 的 lastId；
后续第一次真正 flush 才可能暴露底层 I/O 异常。
```

所以“失败后重启切新 log”不能单独作为完整恢复策略，必须增加 gate：

```text
1. 发生 write/flush IOException 的 ledger dir 标记为 suspect / failed；
2. failed dir 不再参与 selectDirForNextEntryLog；
3. 如果没有健康 writable dir，则 Bookie 进入 read-only 或 fatal，拒绝写入；
4. 不要通过反复重启持续 createNewLog；
5. 只有通过健康检查后，dir 才能回到 writable 集合。
```

实现上可以复用 `LedgerDirsManager` 已有语义：

```text
LedgerDirsManager.addToFilledDirs(dir) 会把目录从 writableLedgerDirectories 移除；
LedgerDirsListener.diskFailed(dir) / fatalError() 已经会触发 Bookie read-only / fatal 路径；
selectDirForNextEntryLog() 只应从健康 writable dir 里选。
```

但要注意：`addToFilledDirs()` 表达的是 disk full，不完全等价于 I/O error。更准确的长期方案是新增 failed/suspect dir 状态，而不是把所有 I/O error 都伪装成 full。

推荐策略：

```text
短期 P0：
  flush/write IOException 后 poison channel；
  通知 LedgerDirsListener.diskFailed(dir) 或 fatalError()；
  Bookie 进入 read-only / fatal，避免立即在同一目录反复创建新 log。

中期 P1：
  LedgerDirsManager 增加 suspect/failed dirs；
  selectDirForNextEntryLog 排除 suspect/failed dirs；
  health checker 周期性验证创建临时文件、写入、fsync、删除成功后才恢复 writable。

长期 P2：
  对 failed entrylog 建立明确状态，例如 ABORTED / UNSEALED / SUSPECT；
  启动时清理或隔离明显空文件 / header-only 文件；
  对连续失败增加 backoff，避免容器层重启风暴。
```

因此，修复后的状态机应是：

```text
I/O error
  -> poison current BufferedChannel
  -> mark current ledger dir suspect/failed
  -> reject normal seal-and-rotate on current log
  -> if other healthy dirs exist: optionally create next log on healthy dir
  -> if no healthy dirs: read-only / fatal / wait for external repair
```

关键点：重启切新 log 是在“存在健康目录”时的结果，不应成为持续异常下的无限创建新文件机制。

### 16.4 failed channel 对应文件的处置

发生 I/O 异常的 entrylog 文件不能按正常 sealed log 处理，也不能立即删除。原因是它可能同时包含三类内容：

```text
1. 已经成功 flush 且 RocksDB index 已引用的历史 entry；
2. 已写入文件但尚未发布 RocksDB index 的 entry；
3. flush 失败时形成的 partial / ambiguous tail。
```

因此处置策略应是“隔离、只读、保守 GC”，而不是 rename 或 delete。

#### 16.4.1 不建议 rename 原 `.log` 文件

不要把 `855.log` 这类文件直接 rename 成 `.suspect` 或其他后缀。BookKeeper location 的高 32 位是 entryLogId，读路径会按 `<hexLogId>.log` 找文件。如果已有 RocksDB location index 指向这个 logId，rename 会让这些历史 entry 直接变成 missing log。

更安全的做法是：

```text
保留原 <logId>.log 文件名；
关闭并移除 writable channel；
内存中标记该 channel/log 为 failed，阻止继续写和正常 seal；
best-effort 用 sidecar 或元数据标记该 log 为 SUSPECT / ABORTED / UNSEALED；
后续只能按 read-only entrylog 打开。
```

注意：sidecar / metadata 标记本身也涉及 I/O。在已经出现 I/O error 的目录上，不能假设该标记一定能写成功。因此 sidecar 只能是诊断增强，不能作为 P0 正确性的前提。P0 必须满足：

```text
即使 sidecar 写失败，
进程内也不能继续使用 failed channel；
不能正常 appendLedgersMap；
不能在同一 failed dir 上继续 createNewLog；
上层必须 read-only / fatal / shutdown。
```

sidecar 可以类似：

```text
855.log.suspect
{
  "logId": 2133,
  "state": "SUSPECT",
  "reason": "flush IOException",
  "lastKnownSafePosition": <writeBufferStartPosition before failing flush>,
  "fileChannelPositionAtFailure": <best effort>,
  "writeBufferWriterIndex": <writerIndex>,
  "headerPublished": false
}
```

`lastKnownSafePosition` 很重要：失败时正在 flush 的 writeBuffer 覆盖区间是 ambiguous tail；该位置之前的内容来自更早成功 flush，可信度更高。

#### 16.4.2 读路径

failed log 可以保留给读路径使用，但必须只读打开，并强制校验：

```text
location index 指向该 log 时，允许读取；
读取时校验 size、ledgerId、entryId、digest；
校验失败则返回读失败，让客户端 / 副本恢复机制处理；
不能因为文件是 suspect 就自动扫描并补 location index。
```

这样可以保护已提交且仍可读的历史 entry，同时不会把 ambiguous tail 当成正常数据发布。

#### 16.4.3 GC / compaction

suspect entrylog 不能仅凭 header ledgers map 或普通 scan metadata 自动删除。推荐策略：

```text
默认不自动删除 suspect log；
GC 删除前必须确认没有 active RocksDB location index 指向该 log；
如果要释放空间，先 compaction/copy 仍被引用且校验通过的 entry 到新健康 log；
location index 更新成功后，再删除旧 suspect log；
metadata 异常时宁可保留，不要删除。
```

这与 P2 的 `verifyMetadataOnGC` / metadata 校验增强是一致的。

#### 16.4.4 index rebuild / recovery

如果需要重建 location index，suspect log 不能被静默当成普通 log 全量扫描。原因是 failed buffer 中可能有“写入了但没有发布 index”的 entry，自动扫描可能把这些 ambiguous entry 重新引入 index。

推荐：

```text
普通 rebuild 默认跳过 suspect tail；
只信任 lastKnownSafePosition 之前的范围；
如需最大化抢救，使用显式 salvage 模式，严格校验 size/lid/eid/digest，并输出人工确认报告。
```

#### 16.4.5 新 log 的发布顺序

持续 I/O 异常下还有一个细节：`EntryLoggerAllocator.allocateNewLog()` 当前创建新文件后，把 entrylog header 写入 `BufferedChannel` 的 buffer，然后更新 `lastId`。header 此时未必已经落到文件。

更稳的顺序应是：

```text
create <next>.log；
write header；
flush header 成功；
可选 force header；
再更新 lastId；
再把 channel 暴露为 active current log。
```

如果 header flush 失败：

```text
关闭 channel；
删除 0-byte/header-only 临时文件，删除失败则标记 orphan/suspect；
不更新 lastId；
不把该 logId 加入 recentlyCreatedEntryLogsStatus；
将目录标记 suspect/failed。
```

这可以减少持续异常下的 logId 空洞和小文件堆积。

#### 16.4.6 现有机制与新增机制边界

现有 BookKeeper 已有的可复用机制：

```text
BufferedChannel / BufferedLogChannel：已有写 buffer 和 flush，但没有 failed/poison 状态；
LedgerDirsManager：已有 writable dirs / filled dirs 管理；
LedgerDirsListener.diskFailed(dir)：BookieImpl 当前会 shutdown；
LedgerDirsListener.fatalError()：BookieImpl 当前会 shutdown；
LedgerDirsListener.allDisksFull(...)：可触发 read-only；
BookieStateManager：已有 read-only 转换；
读路径：已有 size/lid/eid/digest 校验；
GC/readlogmetadata：已有 header map 失败后 fallback scan 的部分逻辑。
```

本修复需要新增或改造的机制：

```text
1. BufferedChannel failed/poison 状态；
2. failed channel 禁止 write/flush/forceWrite/appendLedgersMap；
3. flush/write IOException 后通知上层 diskFailed/fatalError/read-only；
4. failed current log 不能走正常 seal-and-rotate；
5. header positioned writeFully；
6. 新 log header flush 成功后再更新 lastId；
7. failed/suspect dir 状态和健康检查恢复机制；
8. suspect/aborted/unsealed entrylog 的持久化 sidecar 或元数据；
9. GC / index rebuild 对 suspect log 的保守策略。
```

因此，最小 P0 不依赖 sidecar：

```text
内存 poison + 上层 fatal/read-only + 不继续写；
```

sidecar、suspect log 生命周期、健康检查恢复属于 P1/P2，主要用于诊断、运维和长期空间回收。

### 16.5 现有 IOException 处理方式对照

Bookie 里已经有不少 `IOException` 捕获，但不同模块处理强度不一样。

#### 16.5.1 目录监控 / Bookie 状态

`LedgerDirsMonitor` 对目录健康检查的处理比较强：

```text
DiskErrorException：
  通知 LedgerDirsListener.diskFailed(dir)。

DiskOutOfSpaceException：
  LedgerDirsManager.addToFilledDirs(dir)，从 writable dirs 移除。

监控过程 IOException：
  通知 LedgerDirsListener.fatalError()。
```

`BookieImpl` 的 listener 当前行为：

```text
diskFailed(dir) -> triggerBookieShutdown(BOOKIE_EXCEPTION)
fatalError()    -> triggerBookieShutdown(BOOKIE_EXCEPTION)
allDisksFull()  -> transitionToReadOnlyMode()
```

这说明 Bookie 已经有 “disk failure -> shutdown” 和 “all disks full -> read-only” 的现有框架，可以复用。

#### 16.5.2 Journal

Journal 写路径比 entrylog 更接近 fail-stop：

```text
ForceWriteThread.syncJournal() 发生 IOException：
  记录失败 stats；
  向外抛；
  ForceWriteThread catch 后 running=false；
  interrupt parent thread。

Journal 主线程写入发生 IOException：
  log error；
  finally close buffered channel；
  onJournalExit() 通知上层。
```

源码注释也说明：journal 异常会导致 bookie 被 take down，否则写请求可能 hang。

对比结论：journal 对 I/O failure 的语义更强，接近我们建议的 fail-closed。

#### 16.5.3 DbLedgerStorage / EntryLogger flush

`SingleDirectoryDbLedgerStorage.checkpoint()` 的顺序是：

```text
entryLogger.addEntry() 写 entrylog 并收集 location；
entryLogger.flush()；
batch.flush() 写 RocksDB location index；
ledgerIndex.flush()。
```

如果 `entryLogger.flush()` 抛 `IOException`，`SingleDirectoryDbLedgerStorage` 会继续向上抛。

但 `SyncThread.flush()` / `SyncThread.checkpoint()` 对普通 `IOException` 的处理是：

```text
log "Exception flushing ledgers";
return;
```

只有 `NoWritableLedgerDirException` 会触发 `allDisksFull(true)`，`checkpointSource.checkpointComplete()` 失败才会触发 `allDisksFull(true)`。

这就是当前设计上的薄弱点：entrylog flush I/O error 没有被提升为 diskFailed/fatal/read-only；如果底层 channel 状态已经不可信，后续仍可能复用同一个 current log。

#### 16.5.4 Sorted / InterleavedLedgerStorage

`InterleavedLedgerStorage.flushOrCheckpoint()` 会分别捕获 ledger cache 和 entryLogger flush 的 IOException，设置 `flushFailed=true`，最后抛新的 `IOException`。也就是说它本身没有吞掉错误。

`SortedLedgerStorage` 的异步 memtable flush 捕获 `Exception` 后会：

```text
stateManager.transitionToReadOnlyMode();
log error;
```

对比结论：SortedLedgerStorage 对 flush 异常的上层处置比 DbLedgerStorage 更保守。

#### 16.5.5 GC / compaction

普通 compaction 遇到 `IOException` 的策略是：

```text
log error；
abort compaction；
不删除原 entrylog。
```

transactional compaction 分阶段执行，phase 里 `IOException` 会：

```text
log error；
abort current compaction；
return false。
```

这类后台任务的保守策略是合理的：失败时不删除原数据，不发布不完整 compaction 结果。

#### 16.5.6 metadata 读取

`DefaultEntryLogger.getEntryLogMetadata()` 读取 header ledgers map 失败时会 fallback 到 scan：

```text
extractEntryLogMetadataFromIndex() 失败；
log "Failed to get ledgers map index";
extractEntryLogMetadataByScanning()。
```

这能处理“没有 ledgers map / header map 不可解析”的场景，但不能修复 writer 已经返回 stale location 的问题。855.log 的 header map offset 错误只是症状之一，另一个症状是 RocksDB location index 也已经错位。

#### 16.5.7 DirectEntryLogger

DirectEntryLogger 是另一套实现。`DirectWriter` 的 direct I/O 写入如果 short write 或 native write error，会抛 `IOException`；async write future 在 `waitForFuture()` 中会把 `IOException` 重新抛回等待方。

这与当前出问题的 `DefaultEntryLogger + BufferedChannel` 路径不同，但可以作为参考：底层写失败不应静默转成成功。

#### 16.5.8 小结

现有代码里已经有三种风格：

```text
强处理：
  LedgerDirsMonitor / BookieImpl listener / Journal -> shutdown 或 read-only。

保守后台处理：
  compaction -> abort，不删除原 log。

弱处理：
  SyncThread 对 ledgerStorage.flush/checkpoint 的普通 IOException 只 log 后 return。
```

855.log 这类问题落在弱处理区域。修复应把 “entrylog writer I/O error / poisoned channel” 从普通 flush IOException 中区分出来，提升为：

```text
diskFailed / fatalError / read-only；
并禁止 failed current log 继续 write 或正常 seal。
```

### 16.6 不建议把 position 提前更新作为主修复

把 `position += copied` 移到 `flush()` 前，看似可以消除 logical 落后的表象，但不能解决：

```text
flush IOException 后，哪些 bytes 已经落盘不确定；
writeBuffer / ByteBuffer 状态可能已经被推进；
retry 可能造成重复、空洞或 partial frame；
当前 entry 是否完整不可判定。
```

所以 position accounting 重构只能作为 P1 防御增强；P0 必须仍然是 fail-closed。

## 17. 最终建议

最小且安全的修复是：

```text
BufferedChannel IOException 后 fail-closed；
禁止同一个 entrylog writer 继续写；
禁止 failed log 正常 seal；
failed log 保留原文件名、关闭 writable channel，sidecar/metadata 只作为 best-effort 标记；
读路径只读打开并校验 entry，GC 默认保守保留；
将发生 I/O error 的 ledger dir 标记为 suspect/failed；
只有存在健康 writable dir 时才允许切新 log；
否则让 Bookie 上层 read-only / fatal，而不是反复重启创建新文件；
把重试交给 BK/Pulsar 复制协议，而不是在本地 FileChannel writer 上盲目 retry。
```

这与 WiredTiger 这类存储引擎的 fail-stop 思路一致，也更符合 BookKeeper append-only entrylog 的数据安全需求。
