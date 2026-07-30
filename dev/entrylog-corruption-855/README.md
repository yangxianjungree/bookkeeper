# EntryLog 855 / logId 2133 Corruption Context

This directory keeps investigation context for the BookKeeper entrylog corruption discussed in:

- GitHub issue: https://github.com/apache/bookkeeper/issues/4855
- Reproducer PR: https://github.com/apache/bookkeeper/pull/4854

The production file was `855.log`, which is entryLogId `2133` decimal / `0x855` hex.

## Primary Reading Order

1. `context/855-entrylog-2133-concise-root-cause-report.md`
   - Short root-cause report.
   - Contains the physical/logical offset model and the main evidence chain.
2. `context/855-entrylog-2133-source-position-analysis.md`
   - Detailed source-position investigation.
   - Useful when checking exact offsets and how the `34553` delta was derived.
3. `context/855-entrylog-2133-fix-plan-optimized.md`
   - Current repair-plan notes.
   - Includes fail-closed, channel poisoning, failure propagation, lifecycle, and compatibility considerations.
4. `context/bookkeeper-bufferedchannel-entrylog-corruption-issue-draft.md`
   - The public issue body draft.

## Supporting Material

- `context/855-entrylog-2133-corruption-investigation.md`
  - Original long investigation notes.
- `context/855-entrylog-2133-source-position-verification-2dws9g.md`
  - Independent verification pass.
- `context/855-entrylog-2133-source-position-verification-78faf567.md`
  - Independent verification pass. Earlier mistakes in this thread were corrected before the final conclusion.
- `context/855-entrylog-2133-b65log-verification-78faf567.md`
  - Separate bookie/log investigation. It is not considered the same root cause as `855.log`, but is kept for context.

## Diagram

The physical/logical position drift diagram is stored at:

```text
assets/pulsar-entrylog-physical-logical-position-drift.drawio.png
```

## Core Failure Model

`BufferedChannel.write()` can call `flush()` before updating its logical `position`.
If the underlying `FileChannel` advances the physical file position and then throws `IOException`, the channel can be left in this state:

```text
FileChannel physical position > BufferedChannel logical position
```

If the same channel is reused, `DefaultEntryLogger` can publish stale logical positions as:

- RocksDB entry locations, and
- the entrylog header `ledgersMapOffset`.

The production evidence showed a stable delta:

```text
delta = 34553

real ledgers map start - header.ledgersMapOffset = 34553
actual L15069 body pos - RocksDB indexed pos     = 34553
65536 write buffer boundary - E17719 bodyStart   = 34553
```

## Local E2E Goal

The E2E reproducer in this branch should prove the same failure mode through the real BookKeeper write path:

```text
BookKeeper client addEntry
  -> Bookie journal/write cache
  -> SyncThread checkpoint
  -> DbLedgerStorage
  -> DefaultEntryLogger
  -> BufferedLogChannel / BufferedChannel
  -> RocksDB entry location index
  -> entrylog file
```

The expected pre-fix bad state is not just an injected `IOException`; the target proof is a stable offset between physical entry bytes and logical/indexed positions after the failed entrylog channel is reused.
