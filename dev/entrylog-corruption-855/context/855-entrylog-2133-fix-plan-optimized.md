# 855.log / EntryLog 2133 修复方案优化版

## 1. 目标

本方案只解决代码层面的再发风险，不处理已有 `855.log` 的数据修复。详细根因分析见：

```text
855-entrylog-2133-concise-root-cause-report.md
855-entrylog-2133-source-position-analysis.md
```

修复目标：

```text
1. BufferedChannel / entrylog writer 发生不可判定 I/O 异常后，不能继续写。
2. failed entrylog 不能正常 seal，不能发布错误 ledgersMapOffset。
3. failed writer 不能继续返回 stale location 写入 RocksDB index。
4. 持续 I/O 异常时不能反复重启创建大量新 .log 文件。
5. 故障文件保留原文件名，只读保守处理，不破坏已有 location index。
6. P0 固定走 fatal / shutdown，不默认降级到 read-only。
```

非目标：

```text
1. 不在 BufferedChannel 层盲目 retry IOException。
2. 不要求在同一个 failed entrylog 上恢复追加写。
3. P0 不依赖 sidecar / suspect 标记写入成功。
```

## 2. 核心故障代码栈

### 2.1 客户端写入进入 write cache 和 journal

客户端写入进入 Bookie 后，DbLedgerStorage 默认不是立即写 entrylog，而是先进入 `LedgerStorage` 的 write cache，然后写 journal：

```text
WriteEntryProcessor / WriteEntryProcessorV3
  -> BookieImpl.addEntry(...)
    -> BookieImpl.addEntryInternal(...)
      -> LedgerDescriptorImpl.addEntry(...)
        -> DbLedgerStorage.addEntry(...)
          -> SingleDirectoryDbLedgerStorage.addEntry(...)
            -> writeCache.put(...)
      -> Journal.logAddEntry(...)
        -> journal queue
        -> Journal thread append/flush/forceWrite
```

源码里 `BookieImpl.addEntryInternal()` 明确先 `handle.addEntry(entry)`，再 `getJournal(ledgerId).logAddEntry(...)`。注释也说明 journal addEntry 要发生在 entry 加入 ledger storage 之后，避免 journal 被 roll 时 ledger storage 里还没有 ledger。

默认 `journalWriteData=true`，所以普通写会进 journal；如果配置为 false，Bookie 会在 write cache 写入后直接回调成功，这种模式有数据丢失风险。`ackBeforeSync` 决定 journal 写入是否可以在 sync 前 ack，但不改变“write cache + journal”这条路径。

这条请求路径上如果抛 `IOException`，请求处理器会返回 `EIO` 给客户端；`NoWritableLedgerDirException` 会触发 read-only。但正常情况下 entrylog 数据文件写入仍发生在后续 flush/checkpoint，而不是客户端 addEntry 线程里。

### 2.2 flush 时写 entrylog 和 location index

这里的主体是 `SyncThread` 的 checkpoint/flush 任务，或者 `SingleDirectoryDbLedgerStorage.triggerFlushAndAddEntry()` 触发的后台 flush 线程。实际写 entrylog 的模块是 `DefaultEntryLogger / EntryLogManagerBase`，它持有 current `BufferedLogChannel`。

DbLedgerStorage flush 的关键顺序：

```text
SyncThread.doCheckpoint()/flush()
  -> SingleDirectoryDbLedgerStorage.checkpoint(...)
  -> swapWriteCache()
  -> writeCacheBeingFlushed.forEach(...)
     -> entryLogger.addEntry(ledgerId, entry)
        -> DefaultEntryLogger.addEntry(...)
          -> EntryLogManagerBase.addEntry(...)
            -> logChannel.write(sizeBuffer)
            -> long pos = logChannel.position()
            -> logChannel.write(entry)
            -> return (logId << 32) | pos
     -> entryLocationIndex.addLocation(batch, ledgerId, entryId, location)
  -> entryLogger.flush()
  -> batch.flush()
  -> ledgerIndex.flush()
```

这个顺序本身是合理的：entrylog flush 在 RocksDB location index batch flush 之前。855.log 的问题不是“先写 index 后写 data”，而是 failed writer 后续继续被使用，导致 `entryLogger.addEntry()` 返回 stale logical location。

write cache 满时，`SingleDirectoryDbLedgerStorage.triggerFlushAndAddEntry()` 会在自己的 `executor` 里异步调用同一条 `flush()` 路径，所以最终还是落到 `SingleDirectoryDbLedgerStorage.checkpoint()` 这段代码，只是发起线程不同。

### 2.3 BufferedChannel 的异常窗口

这一节是对 2.2 的局部放大：只看 `entryLogger.addEntry()` 最终落到 `BufferedChannel.write()` 的那一小段。这里的主体是“当前调用 `BufferedChannel.write()` 的线程”，不是 `BufferedChannel` 自己起的异步线程。对本案来说，通常是 `SyncThread` 的 checkpoint 线程；如果是写缓存满触发的后台 flush，则是 `SingleDirectoryDbLedgerStorage` 的 flush executor 线程。`BufferedChannel` 本身属于 `DefaultEntryLogger` 持有的 current entrylog writer。

当前 `BufferedChannel.write()` 的关键结构：

```java
writeBuffer.writeBytes(...);
if (!writeBuffer.isWritable()) {
    flush();
}
position += copied;
```

如果 `flush()` 已经推进底层 `FileChannel`，随后抛 `IOException`，则：

```text
FileChannel physical position 已前进；
BufferedChannel.position 未执行 position += copied；
channel 未进入 failed 状态；
后续 addEntry / appendLedgersMap 仍可能继续使用该 channel。
```

这正是 `physical = logical + 34553` 的源码入口。

## 3. 现有异常处理薄弱点

### 3.1 被弱处理的 flush IOException

`SingleDirectoryDbLedgerStorage.checkpoint()` 会把 `entryLogger.addEntry()` / `entryLogger.flush()` 的 `IOException` 向上抛。但到 `SyncThread` 后，普通 `IOException` 只是记录日志后返回：

```text
SyncThread.flush()
  try ledgerStorage.flush()
  catch NoWritableLedgerDirException -> allDisksFull(true)
  catch IOException -> log error; return

SyncThread.checkpoint()
  try ledgerStorage.checkpoint(checkpoint)
  catch NoWritableLedgerDirException -> allDisksFull(true)
  catch IOException -> log error; return
```

`SingleDirectoryDbLedgerStorage.triggerFlushAndAddEntry()` 里后台 flush 也有类似弱处理：

```text
executor.execute(() -> {
  try {
    flush();
  } catch (IOException e) {
    log.error("Error during flush", e);
  }
});
```

也就是说，entrylog writer I/O error 当前可能只被 log 掉，没有升级为 diskFailed / fatal / shutdown，current writer 也没有被 poison。

### 3.2 其他模块的对比

Bookie 其他模块已有更强的处理框架：

```text
LedgerDirsMonitor:
  DiskErrorException -> listener.diskFailed(dir)
  DiskOutOfSpaceException -> addToFilledDirs(dir)
  monitor IOException -> listener.fatalError()

BookieImpl listener:
  diskFailed(dir) -> triggerBookieShutdown(BOOKIE_EXCEPTION)
  fatalError() -> triggerBookieShutdown(BOOKIE_EXCEPTION)
  allDisksFull() -> transitionToReadOnlyMode()

Journal:
  ForceWriteThread IOException -> running=false, interrupt parent thread
  Journal main loop IOException -> exit loop, close channel, onJournalExit()

Compaction:
  IOException -> abort compaction, do not delete source entrylog
```

所以不是 Bookie 没有 fail-stop/read-only 框架，而是 `DbLedgerStorage -> EntryLogger -> BufferedChannel` 这条 flush I/O error 路径没有把错误提升到足够强的状态。

## 4. 方案总览

建议按 P0 / P0.5 / P1 / P2 分层落地：

```text
P0：阻断 silent corruption
  - BufferedChannel 增加 failed/poison 状态；
  - failed channel 禁止 write / flush / forceWrite / appendLedgersMap；
  - entrylog writer I/O error 通过 SyncThread / requestFlush / 后台 flush 升级为 fatal/shutdown，而不是只 log；--重启前
  - failed current log 不能正常 seal-and-rotate；---重启后
  - header positioned write 改 writeFully；
  - 新 log header flush 成功后才能发布 lastId / active channel；
  - preallocation 遵守同样的两阶段发布，或在 P0 禁用；---避免重复切换log文件、创建新的log文件
  - entryLogPerLedgerEnabled 路径如果可能启用，必须覆盖；
  - shutdown 路径遇到 poisoned channel 时不能再次写盘，cleanup 要 best-effort 继续；
  - P0 不依赖任何 sidecar 写入成功。

P0.5：覆盖面收敛
  - entry key/body 低成本不变量校验；
  - 关键日志、metrics、诊断信息。

P1：运行时治理
  - 发生 I/O error 的 ledger dir 标记 suspect/failed；
  - selectDirForNextEntryLog 排除 suspect/failed dir；
  - 增加日志、metrics、健康检查和 backoff。

P2：故障文件生命周期和恢复增强
  - suspect/unsealed entrylog sidecar 或元数据；
  - GC / compaction / index rebuild 对 suspect log 保守处理；
  - readlogmetadata 增强 header/map 校验和诊断输出；
  - 可选 salvage 工具，不自动把 ambiguous tail 引入 index。
```

## 5. P0 详细设计

### 5.1 BufferedChannel poison

在 `BufferedChannel` 增加 failed 状态：

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

入口检查：

```text
write()
flush()
flushAndForceWrite()
flushAndForceWriteIfRegularFlush()
forceWrite()
```

`flush()` 中只要 `FileChannel.write()` 抛 `IOException`，立即 mark failure 并继续抛出：

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

`forceWrite()` 也必须同样 poison：

```java
public long forceWrite(boolean forceMetadata) throws IOException {
    checkWritable();
    long positionForceWrite = writeBufferStartPosition.get();
    ...
    try {
        fileChannel.force(forceMetadata);
    } catch (IOException e) {
        markWriteFailure(e);
        throw e;
    }
    return positionForceWrite;
}
```

原因：`fileChannel.force()` 失败时，本地持久化边界不可判定；后续不能继续把该 writer 当作健康 writer 使用。

`write()` 内有两条可能触发 I/O 的路径，都要覆盖：

```text
1. writeBuffer 满时触发 flush()；
2. doRegularFlushes 下 position += copied 后触发 flush()，随后 synchronized 外 forceWrite(false)。
```

因此测试不能只覆盖 64KiB buffer-full flush failure，还要覆盖 regular flush / forceWrite failure。

注意：short write 没有抛异常，可以继续循环补齐；真正 `IOException` 不能在本地 writer 盲目 retry。

### 5.2 让 failed writer 不能继续返回 location

`EntryLogManagerBase.addEntry()` 当前在写 size 后取 logical position：

```java
logChannel.write(sizeBuffer);
long pos = logChannel.position();
logChannel.write(entry);
return (logChannel.getLogId() << 32L) | pos;
```

修复后必须保证：

```text
如果前一次 write/flush 已失败：
  logChannel.write(sizeBuffer) 直接抛异常；
  不会取 position；
  不会 write entry；
  不会 return location；
  不会把 stale location 加入 RocksDB batch。
```

如果本次 `logChannel.write(entry)` 中途触发 flush 并失败，则该 channel 立即进入 failed，后续所有 entry 都不能继续写。

### 5.3 appendLedgersMap 不能发布 stale header

`BufferedLogChannel.appendLedgersMap()` 当前会：

```text
long ledgerMapOffset = this.position();
write(serializedMap);
super.flush();
fileChannel.write(mapInfo, LEDGERS_MAP_OFFSET_POSITION);
```

这里有两类写：

```text
1. write(serializedMap) / super.flush() 走 BufferedChannel；
2. fileChannel.write(mapInfo, LEDGERS_MAP_OFFSET_POSITION) 直接 positioned write header，
   不经过 BufferedChannel.write() / flush() 的入口守卫。
```

修复后：

```text
appendLedgersMap 入口必须 checkWritable；
failed channel 上 appendLedgersMap 必须直接失败；
write(serializedMap) 或 super.flush() 失败后不能写 header；
header positioned write 必须 writeFully，并在 IOException 时 mark failure；
failed current log 不能走正常 seal-and-rotate。
```

这能阻止 `header.ledgersMapOffset` 写入 stale logical offset。

### 5.4 header writeFully

当前 header 更新：

```java
this.fileChannel.write(mapInfo, LEDGERS_MAP_OFFSET_POSITION);
```

`FileChannel.write(ByteBuffer, position)` 不保证一次写完。应改成：

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

header write 失败也应使该 channel/log 进入 failed，不能认为 sealed 成功。

### 5.5 entrylog I/O error 升级

需要把 entrylog writer 的 I/O error 从普通 `IOException` 中区分出来。可选实现：

```text
新增 EntryLogWriteException extends IOException
  fields:
    logId
    logFile
    ledgerDir
    logicalPosition
    writeBufferStartPosition
    writeBufferWriterIndex
    fileChannelPositionAtFailure
    writerRole: MAIN_ENTRYLOG / COMPACTION_ENTRYLOG / JOURNAL
```

在 `EntryLogManagerBase.addEntry()`、`flushLogChannel()`、`createNewLog()`、`appendLedgersMap()` 捕获底层 I/O error 后包装或补充上下文。

P0 的 fatal/shutdown 主要针对 `MAIN_ENTRYLOG`。`COMPACTION_ENTRYLOG` 应让 compaction phase abort 并保留 source log；`JOURNAL` 继续遵循现有 journal fail-stop 语义。区分 writer role 可以避免把后台 compaction 的临时文件写失败误升级成主写路径 corruption。

上层处理：

```text
SyncThread.flush/checkpoint:
  catch EntryLogWriteException -> fatalError() 或 diskFailed(dir)，最终 triggerBookieShutdown
  catch NoWritableLedgerDirException -> allDisksFull(true)
  catch IOException -> 保持现有逻辑或按风险分类处理

SyncThread.requestFlush:
  catch EntryLogWriteException -> fatalError() 或 diskFailed(dir)，最终 triggerBookieShutdown
  catch Throwable -> 不能只 log 后吞掉 poisoned writer

SingleDirectoryDbLedgerStorage 后台 flush:
  catch EntryLogWriteException -> 通知上层 fatalError / diskFailed，最终 triggerBookieShutdown
  catch IOException -> 记录并按现有策略处理
```

不要把所有 `IOException` 都 fatal；重点是将 “entrylog writer 已 poisoned / physical state 不可信” 这一类升级。

P0 必须固定为 shutdown/fatal，而不是默认 read-only：

```text
EntryLogWriteException
  -> LedgerDirsListener.fatalError() 或 diskFailed(ledgerDir)
  -> BookieImpl.triggerBookieShutdown(BOOKIE_EXCEPTION)
```

read-only 可以作为 P1 多目录健康切换方案的一部分，但不应作为 855 类 writer-state-corruption 的默认 P0 结果。原因是 read-only 下仍可能存在 high-priority / recovery / compaction 写路径；如果只切 read-only，正确性将依赖所有写入口都完整识别 failed writer，覆盖面更大。

还需要新增传播通道。当前 `SingleDirectoryDbLedgerStorage.setStateManager()` 是 no-op，后台 flush catch `IOException` 后也只 log。P0 必须提供一种明确机制，例如：

```text
方案 A：让 SingleDirectoryDbLedgerStorage 保存 StateManager / LedgerDirsListener；
方案 B：让 EntryLogger / LedgerStorage 注入 FatalErrorHandler；
方案 C：让 SyncThread 和后台 flush 统一通过可测试的 StorageFailureHandler 上报。
```

否则底层 channel 已 poison，但 Bookie 仍继续接收写入，只是在后续 flush 中反复失败，故障暴露会很慢。

这里可以复用现有的 `LedgerDirsListener.diskFailed()` / `fatalError()` / `BookieImpl.triggerBookieShutdown()`，但从 `DbLedgerStorage` 后台 flush 到这个 listener 的传播通道需要新增或补齐；不能假设现有 `setStateManager()` 已经完成这件事。

### 5.6 正常 rotate 的硬约束

当前 `EntryLogManagerBase.createNewLog()` 的正常 rotate 顺序是：

```text
old log flush();
old log appendLedgersMap();
create new log;
setCurrentLogForLedgerAndAddToRotate(newLog);
onRotateEntryLog();
```

P0 必须明确：

```text
1. old log 的 flush / appendLedgersMap / header update 任一步失败：
   - 不 createNewLog；
   - 不 setCurrent；
   - 不 onRotateEntryLog；
   - old channel poison；
   - 上层 fatal/shutdown。

2. current channel 已 poison：
   - createNewLog 直接失败；
   - 禁止“跳过 seal 硬切新文件”；
   - abortCurrentLogAndCreateNewLog 只能作为 P1 专门设计。

3. 如果 old log 已经 seal，但 new log 创建失败：
   - 不能继续把 old sealed log 当 active writer；
   - 必须 fatal/shutdown，或改成先创建并验证 new log，再 seal old log 的顺序。
```

更稳的长期实现是：

```text
先创建并验证 new log 可用；
再 seal old log；
最后原子替换 current channel。
```

但这会改动 rotate 语义，可作为 P0.5/P1。P0 至少要保证任何中间失败都不会继续复用已 failed 或已 sealed 的旧 writer。

单 entrylog 模式下，如果 `createNewLog()` 在 old log 的 `flush()` / `appendLedgersMap()` 阶段失败，poisoned channel 仍可能留在 active 字段里。P0 不靠“清退后继续运行”解决它，而是靠下一步升级停机收口：

```text
poisoned active channel
  -> 后续 addEntry / flush / appendLedgersMap 立即失败
  -> failure handler 触发 fatal/shutdown
```

实现时不要为了“清掉 active channel”而跳过 seal、硬切新文件；那是 P1 `abortCurrentLogAndCreateNewLog()` 的独立设计。

### 5.7 shutdown 路径收口

触发 `fatalError()` / `diskFailed()` 后，bookie shutdown 自身也会碰到 entrylog flush：

```text
triggerBookieShutdown
  -> DbLedgerStorage.shutdown()
     -> SingleDirectoryDbLedgerStorage.shutdown()
        -> flush()
        -> entryLogger.close()
           -> DefaultEntryLogger.close()
              -> flush()
```

poison 后这些 `flush()` 必须立即失败，不能再次尝试把不可信 buffer 写入文件，也不能正常 seal failed log。

当前 `SingleDirectoryDbLedgerStorage.shutdown()` 是一个大 `try { flush(); ... close resources ... } catch IOException`。如果开头 `flush()` 抛异常，后续 `entryLogger.close()`、cache close、executor shutdown 可能被跳过。P0 应明确：

```text
shutdown 中的 flush 失败不能加剧文件损坏；
资源关闭、executor shutdown、entryLogger.forceClose 应 best-effort 继续；
关闭阶段的 IOException 只作为诊断记录，不再触发新的写入或正常 rotate。
```

对应测试要覆盖 poisoned channel 下 shutdown 不再写盘，并且 close/forceClose 路径可收口。

## 6. 配套治理、恢复与影响面

这一章收拢 P0 核心修复之外必须一起说明的治理问题：持续 I/O 异常如何避免反复建文件、故障文件怎么保留和清理、恢复依赖什么、业务影响是什么，以及其他模块会受到哪些影响。

### 6.1 持续 I/O 异常与新文件创建

用户指出的风险成立：如果底层 I/O 持续异常，单纯依赖重启后切新 log，可能产生：

```text
反复重启；
每次启动 create <next>.log；
写 header 或更新 lastId；
第一次 flush 又失败；
留下大量 header-only / empty / orphan 文件。
```

当前 `EntryLoggerAllocator.allocateNewLog()` 的顺序大致是：

```text
++preallocatedLogId；
创建 <logId>.log；
logChannel.write(logfileHeader)；
setLastLogId(...)；
recentlyCreatedEntryLogsStatus.createdEntryLog(logId)；
return logChannel。
```

其中 header 只是写入 `BufferedChannel` 的 buffer，不代表已经落盘。

P0 硬约束：

```text
create <next>.log；
write header；
flush header 成功；
可选 force header；
再更新 lastId；
再加入 recentlyCreatedEntryLogsStatus；
再暴露为 active current log。
```

如果 header flush 失败：

```text
关闭 channel；
best-effort 删除空文件 / header-only 文件；
删除失败则保留，不作为 active log；
不更新 lastId；
标记该 ledger dir suspect/failed；
触发 fatal/shutdown。
```

运行时 gate：

```text
发生 entrylog write/flush IOException 的 dir 标记 suspect/failed；
selectDirForNextEntryLog 排除 suspect/failed dir；
如果没有健康 writable dir，P0 仍按 entrylog writer failure 触发 fatal/shutdown；
不要通过反复重启持续 createNewLog。
```

P0 选择更保守的策略：entrylog writer I/O error 后 shutdown/fatal，不做进程内切新 log。P1 再实现健康目录切换。

如果启用了 `entryLogFilePreAllocationEnabled`，preallocation 也必须纳入同一规则。当前 preallocation 默认开启，后台会提前 `allocateNewLog()`。P0 有两个选择：

```text
方案 A：P0 临时禁用或绕过 entrylog preallocation；
方案 B：把 preallocated log 改成两阶段状态：
  - header flush / force 成功前只是 private candidate；
  - 不更新 lastId；
  - 不加入 recentlyCreatedEntryLogsStatus；
  - 不可作为 active channel 返回；
  - 失败时关闭并 best-effort 删除。
```

否则在持续 I/O 异常下，即使 writer failure 最终导致 shutdown，后台 preallocation 仍可能提前创建新文件并推进 `lastId`。

### 6.2 故障文件生命周期

#### 6.2.1 基本原则

发生 I/O 异常的 entrylog 文件可能包含：

```text
1. 已成功 flush 且 RocksDB index 已引用的历史 entry；
2. 已写入文件但尚未发布 RocksDB index 的 entry；
3. flush 失败时形成的 partial / ambiguous tail。
```

因此不能简单删除，也不建议 rename 原 `.log` 文件。

原因：

```text
BookKeeper location 的高 32 位是 entryLogId；
读路径按 <hexLogId>.log 找文件；
rename 成 .suspect 会让已有 index 指向 missing log。
```

#### 6.2.2 P0 处置

P0 不依赖任何新写入标记：

```text
保留原 <logId>.log 文件名；
关闭并移除 writable channel；
内存中标记 channel/log failed；
禁止继续 write / flush / seal；
触发 fatal/shutdown；
读路径仍可按原文件名读取并校验 entry。
```

即使 sidecar 写失败，上述行为也必须成立。

#### 6.2.3 P1/P2 处置

可选增加 sidecar 或持久元数据，仅作为诊断和治理增强：

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

注意：sidecar 也涉及 I/O，不能作为 P0 正确性的前提。

读路径：

```text
允许按原 <logId>.log 只读打开；
读取时校验 size、ledgerId、entryId、digest；
失败则返回读失败，让客户端 / 副本恢复机制处理；
不能自动扫描 suspect tail 并补 index。
```

GC / compaction：

```text
suspect log 默认不自动删除；
删除前必须确认没有 active RocksDB location 指向该 log；
需要释放空间时，先 copy 校验通过且仍被引用的 entry 到健康 log；
location index 更新成功后，再删除旧 suspect log；
metadata 异常时宁可保留。
```

index rebuild：

```text
默认只信任 lastKnownSafePosition 之前的范围；
suspect tail 不自动加入 index；
如需抢救，使用显式 salvage 模式并输出报告。
```

### 6.3 恢复策略

#### 6.3.1 最小 P0 恢复

```text
entrylog writer I/O error
  -> poison current channel
  -> reject future writes on that channel
  -> prevent normal seal
  -> Bookie fatal / shutdown
  -> 客户端通过 quorum / ensemble change / retry 写其他 bookie
  -> 重启后只有在存储健康时创建新 log
```

对已经 ack 给客户端、但 checkpoint 尚未完成的 entry，真正的本地恢复依据是 journal replay：

```text
checkpoint 未完成
  -> journal last mark 不应前移到该批次之后
  -> writeCacheBeingFlushed 不应被 clear 为“已持久化”
  -> 重启后 readJournal() 从 last mark 重放
  -> handle.addEntry(...) 重新进入 LedgerStorage
```

前提是 `journalWriteData=true` 且 journal 目录本身未丢失。代码默认 `journalWriteData=true`；如果部署关闭 journal data，fail-stop 只能阻断继续损坏，不能保证已 ack entry 本地无损。

优点：

```text
实现小；
不依赖新磁盘写入；
不会继续 silent corruption；
默认 journalWriteData=true 时，未完成 checkpoint 的已 ack entry 可通过 journal replay 重写；
符合 Journal / WiredTiger 类 fail-stop 思路。
```

代价：

```text
单 bookie 会更早不可写；
如果底层 I/O 间歇性异常，可能触发更多 bookie restart/shutdown；
需要运维告警和自动恢复策略配合。
```

#### 6.3.2 P1 进程内切换健康目录

如果集群希望减少单次 I/O error 对可用性的影响，可以后续实现：

```text
abortCurrentLogAndCreateNewLog()
```

语义必须不同于正常 rotate：

```text
不 flush failed log；
不 appendLedgersMap；
不写 header；
关闭 failed writable channel；
标记原 dir suspect/failed；
只在其他健康 writable dir 上创建新 log。
```

这比 P0 复杂，必须配合 suspect dir、health check、backoff 和故障文件生命周期。

### 6.4 业务影响

正向影响：

```text
避免 silent corruption；
避免 stale location index 继续扩大影响范围；
故障暴露更早，客户端能通过 BK/Pulsar 复制机制重试其他 bookie；
运维可通过日志和 metrics 直接看到 entrylog writer failure。
```

负向影响：

```text
底层 I/O 异常时，P0 会让 bookie 更早 shutdown；P1 若实现健康目录切换，才考虑 read-only 或进程内切换；
forceWrite/fsync 的瞬时 IOException 也会触发 poison + shutdown；
短期写入可用性下降，但比静默损坏更可控；
如果集群副本数或 ack quorum 余量不足，客户端可能感知写失败；
需要避免容器层无限重启，增加 backoff、告警和健康检查。
```

因此 P0 上线的运维前置条件应包括：

```text
bookie restart backoff；
entrylog write failure / poisoned channel metrics；
fatal/shutdown 明确告警；
启动前或启动中存储健康检查，避免持续异常时不断创建新 .log。
```

对外行为：

```text
客户端可能收到 EIO / bookie unavailable；
BK client / Pulsar 应通过 ensemble change、quorum retry、ledger recovery 处理；
P0 shutdown 后本 bookie 不再接受 high-priority / recovery 写；P1 如果选择 read-only 或进程内健康目录切换，必须单独审计 high-priority 写入口是否会绕过 failed writer。
```

### 6.5 前后兼容

P0 兼容性：

```text
不改变 entrylog 文件格式；
不改变 location 编码；
不引入必须读取的新 metadata；
旧文件仍按原 <logId>.log 读取；
header writeFully 只改变写入可靠性，不改变格式。
```

行为变化：

```text
过去某些 IOException 只 log 后继续；
修复后 entrylog writer I/O error 会导致 fatal / shutdown；
这是有意的 fail-closed 行为变化。
```

P1/P2 兼容性：

```text
sidecar 必须可选；
老版本不认识 sidecar 也不能影响读取原 .log；
suspect dir 状态不能破坏现有 filledDirs/writableDirs 语义；
如果新增持久 metadata，需要保证升级/回滚时可忽略。
```

### 6.6 对其他模块影响

#### 6.6.1 Journal

Journal 本身已有较强 fail-stop 语义，P0 不需要改 Journal 的上层策略。但 Journal 也使用 `BufferedChannel`，因此 poison 语义会影响 Journal 底层行为：

```text
Journal 的 bc.write / flush / forceWrite 在首次 IOException 后也会立即 failed；
后续 Journal 写会更早失败；
这与现有 Journal IOException 后退出线程、通知上层 take down bookie 的语义一致。
```

需要补充 Journal 相关单测或回归确认，避免评审时误判为“P0 完全不影响 Journal”。

#### 6.6.2 DbLedgerStorage

需要调整两处：

```text
1. checkpoint / flush 接收到 EntryLogWriteException 后，不应只作为普通 IOException；
2. triggerFlushAndAddEntry 后台 flush 不能只 log error，需要通知上层 fatal/shutdown。
```

建议同时增加 write cache key/body 不变量校验。在 `SingleDirectoryDbLedgerStorage.checkpoint()` 遍历 `writeCacheBeingFlushed` 时，iteration key 是 `(ledgerId, entryId)`，entry body 内也有 ledgerId/entryId：

```text
assert entry.getLong(readerIndex) == ledgerId;
assert entry.getLong(readerIndex + 8) == entryId;
```

如果不一致，直接 fail-fast 并升级为 storage failure。这个校验不能修复 855 的 BufferedChannel position 脱钩，但能防止 WriteCache 竞态、ByteBuf 内容错配或调用方错误继续污染 location index。

#### 6.6.3 EntryLogManager

需要识别 failed current log：

```text
normal rotate:
  flush old log -> appendLedgersMap -> create new log

failed log:
  不 flush；
  不 appendLedgersMap；
  不加入 rotatedLogChannels 等待正常 flush；
  关闭 writable channel；
  上层 fatal/shutdown；P1 可设计 abort 后切健康 dir。
```

`EntryLogManagerForEntryLogPerLedger` 必须纳入 P0，不能只修 single entrylog 模式。当前 per-ledger 的 cache eviction callback 中：

```text
appendLedgersMap() catch Exception -> log error；
仍 replicaOfCurrentLogChannels.remove(logId)；
仍 rotatedLogChannels.add(logChannel)。
```

这会把 appendLedgersMap 失败的 channel 当作正常 rotated log 继续处理。P0 要求：

```text
appendLedgersMap 失败：
  - channel poison；
  - 不加入 rotatedLogChannels；
  - 不认为该 ledger log 已正常 sealed；
  - 必须通过 failure handler 上报并触发 fatal/shutdown。
```

如果生产明确没有启用 `entryLogPerLedgerEnabled`，可以在首版实现中降低优先级，但设计文档必须明确“未覆盖 per-ledger 时该模式仍有风险”。

对 855.log 现场而言，`entryLogPerLedgerEnabled=false` 的可信度很高：同一个 entrylog 的真实 ledgers map 里包含大量 ledger，而 per-ledger 模式语义上一个 entrylog 只服务单个 ledger。该判断只用于本次现场优先级排序，不应把 per-ledger 路径从通用修复方案中移除。

#### 6.6.4 GC / Compaction

已有 compaction 失败后不删除源 log 的策略，应保持。新增：

```text
suspect log 不参与普通自动删除；
compaction/copy 成功且 index 更新后才允许删除；
metadata 解析异常时保守保留。
```

compaction 写路径也会使用 `BufferedLogChannel`，因此底层 poison / writeFully 能自动生效；但它的升级语义要和主写路径区分：

```text
主 entrylog writer 写失败：
  -> EntryLogWriteException
  -> fatal/shutdown

compactionLogChannel 写失败：
  -> abort compaction
  -> 删除或保留未完成 compaction 临时文件
  -> 不删除 source entrylog
  -> 不因为一次 compaction 写失败直接关闭 bookie
```

如果底层是整个 ledger dir 不可信，LedgerDirsMonitor / 后续主写路径仍会触发 fatal/shutdown；这里区分的是 compaction phase 自己的失败处理，不能把失败的 compacted log 发布为可用 log。

#### 6.6.5 readlogmetadata / tools

增强诊断即可，不作为 P0：

```text
header.ledgersMapOffset 指向位置必须校验 lid/eid/count/size；
header map 失败 fallback scan 时输出明确 warning；
如果发现 suspected stale header/map offset，工具报告 suspect，不自动修复。
```

#### 6.6.6 DirectEntryLogger

DirectEntryLogger 是另一套写路径。`DirectWriter` 对 short write / native write error 会抛 `IOException`，async write future 会向等待方重新抛出。P0 修复主要针对 `DefaultEntryLogger + BufferedChannel`，后续可以评估是否抽象统一的 entrylog writer failure 分类。

对 855.log 现场而言，`DefaultEntryLogger + BufferedChannel` 的可信度很高：`34553 = 65536 - 30983` 里的 `65536` 正是 `writeBufferBytes` 默认值，且这种 logical position 落后于 physical FileChannel position 的故障形态是 BufferedChannel 特有的。`dbStorage_directIOEntryLogger` 代码默认值为 false，若使用 DirectEntryLogger，不能用这条 64KiB BufferedChannel 边界解释现场偏移。

## 7. 测试计划

P0 测试：

```text
0. 改写现有坏状态复现测试
   - testPositionCanLagFileChannelAfterPartialFlushFailure；
   - testLedgersMapHeaderUsesStalePositionAfterPartialFlushFailure；
   - 修复后不再断言“坏状态可达”；
   - 改为断言 partial flush IOException 后 channel failed，header 不被写 stale offset。

1. BufferedChannel partial flush failure
   - FileChannel.write 推进 position 后抛 IOException；
   - channel 进入 failed；
   - 后续 write/flush/forceWrite 全部失败。

2. regular flush / forceWrite failure
   - doRegularFlushes 触发 flush 失败；
   - forceWrite(false/true) 抛 IOException；
   - 均 markWriteFailure；
   - 后续 write/appendLedgersMap 全部失败。

3. addEntry after failed channel
   - 第一次写触发 flush failure；
   - 后续 EntryLogManagerBase.addEntry 不能返回 location；
   - RocksDB batch 不新增 stale location。

4. appendLedgersMap after failed channel
   - failed channel 调用 appendLedgersMap；
   - 必须抛异常；
   - header.ledgersMapOffset 不被写入 stale logical position。

5. SyncThread / DbLedgerStorage escalation
   - entryLogger.flush 抛 EntryLogWriteException；
   - SyncThread.flush / checkpoint / requestFlush 都触发 fatal/shutdown；
   - SingleDirectoryDbLedgerStorage.triggerFlushAndAddEntry 后台 flush 也触发 failure handler；
   - 不能仅 log return。

6. header writeFully
   - positioned write 每次只写部分；
   - 12 bytes header 最终完整写入；
   - 写失败时 channel failed。

7. createNewLog / preallocation
   - header flush 失败时不更新 lastId；
   - 不加入 recentlyCreatedEntryLogsStatus；
   - 不暴露 active channel；
   - preallocation 也遵守两阶段发布或在 P0 禁用。

8. entryLogPerLedger eviction
   - appendLedgersMap 失败时不加入 rotatedLogChannels；
   - channel failed；
   - failure handler 被调用。

9. key/body invariant
   - writeCache iteration key 与 entry body ledgerId/entryId 不一致时 fail-fast；
   - 不写入 entrylog，不写 location index。

10. DbLedgerStorage 端到端 checkpoint 回归
   - 写入一批 entry 到 write cache；
   - checkpoint 中注入 entrylog partial flush failure；
   - checkpoint 抛 EntryLogWriteException；
   - RocksDB location index 中不出现该批次 stale location；
   - failure handler 被调用并触发 fatal/shutdown；
   - journalWriteData=true 时，重启 replay 可重新写入未完成 checkpoint 的 entry。

11. poisoned shutdown 收口
   - channel 已 poison 后触发 bookie/storage shutdown；
   - shutdown 内 flush/entryLogger.close 不再写盘、不正常 seal；
   - close/forceClose/cache/executor cleanup best-effort 执行；
   - 关闭阶段 IOException 只记录诊断，不产生新的 stale header/location。
```

P1/P2 测试：

```text
1. 持续 I/O error 不反复创建新 log；
2. suspect/failed dir 不参与 selectDirForNextEntryLog；
3. sidecar 写失败不影响 P0 fail-closed；
4. suspect log 保留原文件名，读路径可读取已校验 entry；
5. GC 不删除 still-referenced suspect log；
6. index rebuild 默认不扫描 suspect tail。
```

## 8. 其他存储系统参考


| 系统         | 相关机制                                                       | 对本方案的启发                            |
| ---------- | ---------------------------------------------------------- | ---------------------------------- |
| WiredTiger | `WT_PANIC` 表示需要 database restart，后续调用会立即失败                 | failed writer 后续调用应失败，不能继续复用       |
| InnoDB     | doublewrite 处理 partial page write；checkpoint 发布可恢复边界       | 数据写入和元数据发布分阶段，header 只能指向完整可验证 map |
| RocksDB    | background error 在 `paranoid_checks=true` 下可使 DB read-only | 本地 writer 不可信时拒绝后续写                |
| TiKV       | RocksDB/Raft Engine I/O/corruption 不可恢复时 panic；可恢复必须有明确机制  | 只有明确可恢复才恢复，否则 fail-stop            |
| OceanBase  | LSM + 多层 checksum + Paxos log stream                       | 数据校验和复制层恢复承担容错，单机本地 writer 不应静默继续  |
| ClickHouse | temp part 校验后 rename/commit；broken part detach             | 未完成/可疑对象不能进入 active metadata       |


## 9. 推荐落地顺序

```text
第一阶段 P0：
  BufferedChannel poison；
  failed channel 阻断 write/flush/seal；
  appendLedgersMap 保护；
  header writeFully；
  EntryLogWriteException 分类；
  SyncThread.flush / checkpoint / requestFlush 对该异常升级为 fatal/shutdown；
  SingleDirectoryDbLedgerStorage.triggerFlushAndAddEntry 后台 flush 对该异常升级为 fatal/shutdown；
  failed current log 不走 normal seal-and-rotate；
  新 log header flush 成功后再发布 lastId / active channel；
  preallocation 两阶段发布，或在 P0 禁用；
  entryLogPerLedger eviction 覆盖；
  持续 I/O error 不反复创建新 log。

第二阶段 P0/P1：
  key/body 不变量校验；
  增加关键日志和 metrics。

第三阶段 P1/P2：
  suspect/failed dir 状态和健康检查；
  suspect entrylog sidecar 或元数据；
  GC / compaction / index rebuild 保守处理；
  readlogmetadata 诊断增强。
```

## 10. 最终建议

最小安全修复应坚持：

```text
entrylog writer I/O error 后 fail-closed；
当前 BufferedChannel poison；
failed current log 不继续写、不正常 seal；
不依赖 sidecar 写入成功；
不在持续异常目录上反复创建新 log；
通过现有 diskFailed/fatalError 路径把故障暴露给上层并关闭 bookie；
把业务重试交给 BK/Pulsar 的复制和恢复机制。
```

这会牺牲部分单 bookie 在异常时的短期可用性，但能阻断 silent corruption。对于 BookKeeper 这种复制存储，明显失败比继续写出错误 index/header 更安全。
