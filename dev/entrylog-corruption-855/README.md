# EntryLog 855 / logId 2133 Corruption Context

This directory keeps investigation context for the BookKeeper entrylog corruption discussed in:

- GitHub issue: https://github.com/apache/bookkeeper/issues/4855
- Reproducer PR: https://github.com/apache/bookkeeper/pull/4854

The production file was `855.log`, which is entryLogId `2133` decimal / `0x855` hex.

Chinese quick-start context:

```text
CONTEXT.zh.md
```

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
5. `e2e-reproducer.md`
   - Local BookKeeper E2E reproducer instructions.

## Supporting Material

- `context/855-entrylog-2133-corruption-investigation.md`
  - Original long investigation notes.
- `context/855-entrylog-2133-source-position-verification-2dws9g.md`
  - Independent verification pass.
- `context/855-entrylog-2133-source-position-verification-78faf567.md`
  - Independent verification pass. Earlier mistakes in this thread were corrected before the final conclusion.
- `context/855-entrylog-2133-fix-plan.md`
  - Older fix-plan draft, kept only for historical comparison.
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

## Reproduction Evidence Chain

The reproduction work is intentionally split into layers. Each layer answers a different credibility question:

| Layer | Goal | Status |
| --- | --- | --- |
| Unit test | Prove the local `BufferedChannel` physical/logical position window is reachable. | Done |
| BookKeeper E2E | Prove the real Bookie/`DbLedgerStorage` path can persist stale entry locations and a stale entrylog header, with a healthy replica as control. | Done |
| Pulsar cluster with failpoint | Prove the full Pulsar broker -> managed ledger -> BookKeeper path can reproduce the same target/healthy replica drift in a disposable cluster. | Done |
| Unmodified Pulsar/BookKeeper cluster | Prove an unmodified binary can enter the same failure class under an external I/O fault injector, so the result is not dependent on source changes. | Done |
| K8s standard deployment handoff | Package the unmodified-binary approach so it can be reproduced on a standard K8s deployment without exposing this internal branch. | Done |
| Fixed build comparison | Prove the proposed fix fails closed under the same fault and does not publish stale entry locations or stale header offsets. | Later |

The failpoint cluster run is for deterministic engineering validation. The unmodified-binary run is the persuasive version for external review: BookKeeper/Pulsar code should be unchanged, with the fault introduced only by an auditable external layer such as `LD_PRELOAD`, FUSE, or a block-device fault injector.

The Pulsar failpoint cluster evidence uses Pulsar 3.2.4 as broker/client tooling
and external BookKeeper 4.16.7 bookies. Pulsar 3.2.4 embeds BookKeeper 4.16.6
client-side jars, but the bookie runtime and entrylog evidence are from the
separate BookKeeper 4.16.7 distribution. The local five-round stability archive
is under:

```text
dev/entrylog-corruption-855/pulsar-failpoint-4.16.7-bookie-cluster/runs/stability-20260731-151541/
```

All five rounds reproduced the target condition: `bk1` reported `DRIFT_OK`
with an invalid stale header map offset, while healthy controls `bk2` and `bk3`
reported `SEALED_OK` and entry hash comparisons had zero mismatches.

## Unmodified-Source Cluster Result

The local unmodified-source layer uses unmodified BookKeeper/Pulsar source and
introduces the fault only from outside the process:

```text
Pulsar 3.2.4 broker/client/ZooKeeper tooling
  -> external unmodified BookKeeper 4.16.7 bookies
  -> LD_PRELOAD write/pwrite/writev wrapper enabled only for bk1
  -> existing entrylog scanner and target/healthy replica comparison
```

Local evidence archives:

```text
dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runs/stability-20260731-175938/
dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runs/single-replica-20260731-184741/
```

Observed result:

- the bk1 bookie runtime jar must not contain the deterministic failpoint class;
- the fault injector is auditable separately from BookKeeper source;
- both archived 5-round suites triggered exactly one target-bookie entrylog I/O fault per round;
- target `bk1` reproduced stale entrylog header/map drift evidence in all archived rounds;
- healthy controls stayed strict: `bk2`/`bk3` reported `SEALED_OK` where present;
- the client workload completed in all archived rounds, while broker/bookie logs captured the target fault path.

Evidence strength note: the deterministic failpoint suite reached the strongest
`DRIFT_OK` condition in every archived round, including closed ledger size
accounting from parsed physical entries to the discovered ledgers map. The
unmodified `LD_PRELOAD` suites are intentionally closer to a real syscall-level
fault, and the archived target `bk1` rows are `DRIFT_CHECK` or `STRICT_CHECK`,
not `DRIFT_OK`. Those rows prove the external-fault, stale-header/map, and
runtime-chain behavior, but they should not be described as matching the full
`855.log` ledger-size-accounting closure in every round.

The standard K8s handoff for this layer is:

```text
dev/entrylog-corruption-855/k8s-reproducer-handoff.md
```

## Offline Drift Scanner

This directory includes a dependency-free structural scanner:

```bash
dev/entrylog-corruption-855/tools/entrylog_drift_scanner.py
```

It does not hard-code the `855.log` offsets. It derives drift evidence from the input file and optional E2E properties:

- entrylog header `ledgersMapOffset` / `ledgersCount`;
- entry frame lengths and `ledgerId / entryId / lac` fields;
- ledgers map marker `ledgerId=-1, entryId=-2`;
- real file length;
- optional E2E fields such as `injectedPhysicalPosition`, `indexedPosition`, and `writeBufferBytes`.

Batch-scan E2E artifacts:

```bash
dev/entrylog-corruption-855/tools/entrylog_drift_scanner.py \
  --e2e-dir bookkeeper-server/target/entrylog-partial-flush-e2e-runs
```

Scan every non-empty target/healthy entrylog copied by an E2E run:

```bash
dev/entrylog-corruption-855/tools/entrylog_drift_scanner.py \
  --e2e-dir bookkeeper-server/target/entrylog-partial-flush-e2e-healthy-runs \
  --all-logs
```

Verify V3 CRC32 digests for complete entries while scanning E2E artifacts:

```bash
dev/entrylog-corruption-855/tools/entrylog_drift_scanner.py \
  --e2e-dir bookkeeper-server/target/entrylog-partial-flush-e2e-healthy-runs \
  --all-logs \
  --digest-type crc32
```

Scan a single entrylog with a known or suspected write-buffer boundary:

```bash
dev/entrylog-corruption-855/tools/entrylog_drift_scanner.py \
  /path/to/855.log \
  --write-buffer-bytes 65536
```

Scan with an exported properties file:

```bash
dev/entrylog-corruption-855/tools/entrylog_drift_scanner.py \
  /path/to/run01-0.log \
  --properties /path/to/run01.properties
```

The scanner can prove structural consistency:

- strict entry framing up to the suspect point;
- a continuous physical entry chain from the recovered physical start to the real ledgers map;
- the suspect byte interval around the pivot;
- `trueMapStart - header.ledgersMapOffset`;
- parsed complete-entry byte totals equal the ledgers map totals;
- optional candidate `indexedPosition + derivedDelta` points at the expected entry.

With `--digest-type`, the scanner can also verify V3 entry digests for every complete entry outside the suspect interval:

- `crc32`;
- `crc32c` with a dependency-free pure Python implementation;
- `mac` using HMAC-SHA1 and `--password` or `--password-hex`.

It still needs the correct ledger digest type and password/master-key material. An exported location-index dump is still required to prove every indexed location, not only the entrylog bytes and candidate locations.
