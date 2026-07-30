# GitHub Issue Draft: BufferedChannel Partial Flush Failure Can Corrupt EntryLog Locations

## Title

```text
DefaultEntryLogger can publish stale entry locations after BufferedChannel partial flush failure
```

## Labels

```text
type/bug
component/bookie
component/storage
```

## Body

**BUG REPORT**

***Describe the bug***

In a BookKeeper 4.16.7 based deployment using `DbLedgerStorage` and `DefaultEntryLogger`, we observed an entrylog where the entry bytes are still physically present and mostly parseable, but both the RocksDB location index and the entrylog header `ledgersMapOffset` point to positions that are consistently too early by the same offset.

The suspected code-level issue is in `BufferedChannel`. `BufferedChannel.write()` can call `flush()` before updating its logical `position`. If `flush()` advances the underlying `FileChannel` position and then throws `IOException`, the physical file position has moved forward but `BufferedChannel.position` has not. The channel is not marked failed, so later writes can continue using the same stale logical position.

Relevant code shape:

```java
// BufferedChannel.write(...)
writeBuffer.writeBytes(...);
if (!writeBuffer.isWritable()) {
    flush();
}
position += copied;
```

```java
// BufferedChannel.flush(...)
ByteBuffer toWrite = writeBuffer.internalNioBuffer(0, writeBuffer.writerIndex());
do {
    fileChannel.write(toWrite);
} while (toWrite.hasRemaining());
writeBuffer.clear();
writeBufferStartPosition.set(fileChannel.position());
```

If `fileChannel.write(toWrite)` performs a partial local write and then throws, `writeBuffer.clear()` and `writeBufferStartPosition.set(...)` are skipped, and the caller in `write()` also skips `position += copied`.

This can affect the main entrylog writer in two places:

```java
// EntryLogManagerBase.addEntry(...)
logChannel.write(sizeBuffer);
long pos = logChannel.position(); // used as the entry body location
logChannel.write(entry);
return (logChannel.getLogId() << 32L) | pos;
```

```java
// BufferedLogChannel.appendLedgersMap(...)
long ledgerMapOffset = this.position();
write(serializedMap);
super.flush();
fileChannel.write(mapInfo, LEDGERS_MAP_OFFSET_POSITION);
```

So the same stale logical position can be published as:

1. entry locations in RocksDB, and
2. the entrylog header `ledgersMapOffset`.

This makes acknowledged entries unreadable even though their bytes may still exist later in the same entrylog file.

***To Reproduce***

A full production reproduction is hard because it requires a partial local write followed by an `IOException` at a specific point. However, the bad state is reachable with a small fault-injected `FileChannel`.

A reproducer-only PR is available to demonstrate the issue on the BookKeeper test path:

```text
https://github.com/apache/bookkeeper/pull/4854
```

Steps:

1. Check out `branch-4.16`.
2. Apply the reproducer from PR #4854.
3. Run:

```bash
mvn -pl bookkeeper-server -Dtest=org.apache.bookkeeper.bookie.BufferedChannelTest test
```

4. The reproducer injects a `FileChannel` that writes part of the buffer, advances its physical position, then throws `IOException` during `BufferedChannel.flush()`.
5. `testPositionCanLagFileChannelAfterPartialFlushFailure` shows that after the exception, `FileChannel.position()` can be ahead of `BufferedChannel.position()`, and a later write can still succeed on the same channel.
6. `testLedgersMapHeaderUsesStalePositionAfterPartialFlushFailure` shows that `BufferedLogChannel.appendLedgersMap()` can write a stale `ledgersMapOffset` to the entrylog header after that drift.

The tests currently assert the reachable bad state. After a fix, these tests should be rewritten to assert fail-closed behavior instead.

***Expected behavior***

After an `IOException` from a write path where the local writer state is no longer trustworthy, BookKeeper should fail closed instead of continuing to reuse the same entrylog writer.

At minimum:

1. `BufferedChannel` should enter a failed state after `write()`, `flush()`, or `forceWrite()` fails with `IOException`.
2. A failed `BufferedChannel` should reject subsequent `write()`, `flush()`, `forceWrite()`, and `appendLedgersMap()` attempts.
3. `EntryLogger.addEntry()` should not return a location after the underlying log channel has failed.
4. `appendLedgersMap()` should not publish a header pointing to a stale logical position.
5. The direct positioned header write in `appendLedgersMap()` should use full-write semantics and failure handling, because `FileChannel.write(ByteBuffer, position)` is not guaranteed to write all bytes in one call.
6. The main entrylog writer failure should be propagated out of `DbLedgerStorage` / `SyncThread` instead of being only logged and then continuing to accept writes.

For the main entrylog writer, this likely needs fatal/fail-stop handling for the affected bookie process. Continuing to accept writes can persist stale entry locations into RocksDB. Compaction entrylog failures may need a different policy: abort compaction and keep the source entrylog, rather than immediately shutting down the bookie.

***Screenshots***

Not applicable.

***Additional context***

Production evidence from the corrupted entrylog:

```text
BookKeeper version: 4.16.7 based deployment
Ledger storage:     DbLedgerStorage
Entry logger:       DefaultEntryLogger + BufferedChannel
Entrylog file:      855.log
EntryLogId:         2133 decimal / 0x855 hex
writeBufferBytes:   65536
flushEntrylogBytes: 268435456
```

The same delta appears independently in the ledgers map header and in RocksDB entry locations:

```text
delta = 34553

header.ledgersMapOffset = 1073741388
real ledgers map start  = 1073775941
delta                   = 34553

L15069 actual body position - RocksDB indexed position = 34553
```

The delta also matches the 64 KiB write-buffer boundary at the corruption point:

```text
L240727/E17719 sizeStart = 30979
L240727/E17719 bodyStart = 30983
writeBufferBytes         = 65536

65536 - 30983 = 34553
```

Physical entry parsing shows that the file becomes a continuous valid physical entry chain again at the 64 KiB boundary:

```text
65536   L38854/E11622 size=11309 next=76849
76849   L38854/E11623 size=24693 next=101546
101546  L38854/E11624 size=19210 next=120760
120760  L38854/E11625 size=32121 next=152885
...
1073770033 L39095/E6725 size=5904 next=1073775941
1073775941 real ledgers map start
```

Independent scan result:

```text
chain_65536_to_map_count = 411693
chain break count        = 0
last entry next          = 1073775941
```

For ledger `15069`, every RocksDB location in entrylog `2133` becomes valid after adding the same delta:

```text
total_index_rows_log2133 = 569
ok_after_plus_34553      = 569
bad_count                = 0
```

Samples:

| entry | RocksDB index body pos | actual body pos | actual sizeStart | size | lid | eid | lac | delta |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| E0 | 1025196194 | 1025230747 | 1025230743 | 41 | 15069 | 0 | -1 | 34553 |
| E2 | 1025196239 | 1025230792 | 1025230788 | 41 | 15069 | 2 | 1 | 34553 |
| E4 | 1025196284 | 1025230837 | 1025230833 | 41 | 15069 | 4 | 3 | 34553 |

Additional validation:

```text
569 / 569 L15069 entries pass BK V3 + CRC32C validation after +34553.
sum(4 + size) for L15069 = 26164.
The real ledgers map records L15069 TotalSize = 26164.
```

The real ledgers map is also internally consistent with the file size:

```text
real map start = 1073775941
map size       = 3236 = 20 + 16 * 201
map bytes      = 3240 = 4 + 3236
file size      = 1073779181

1073775941 + 3240 = 1073779181
```

Two independent verification passes checked the same evidence:

1. One pass independently confirmed the big-endian header parsing, real ledgers map offset, L15069 CRC32C validation, and `sum(4 + size) = 26164`.
2. Another pass independently mmap-scanned the file and confirmed `65536..1073775941` is a continuous physical entry chain, with `delta_buffer = delta_map = 34553`.

This issue is about the BookKeeper write-path failure mode and fail-closed behavior. It is not a request for corrupted-data repair tooling.
