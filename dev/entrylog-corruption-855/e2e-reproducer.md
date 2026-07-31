# Local E2E Reproducer

This branch contains a local BookKeeper end-to-end reproducer for issue #4855.

The test starts a real in-process ZooKeeper + BookKeeper ensemble, writes real ledger entries through the BookKeeper client, injects one entrylog flush failure on one target bookie, then verifies that the target bookie can persist a stale entry location after reusing the failed entrylog channel.

This is intentionally a reproducer for the current bad state, not the final fix.

## Branch

```text
e2e-entrylog-partial-flush-corruption
```

The branch is based on the reproducer-only PR branch and adds:

1. investigation context under `dev/entrylog-corruption-855/`;
2. an entrylog-specific failpoint in `DefaultEntryLogger.BufferedLogChannel`;
3. a local E2E test:

```text
bookkeeper-server/src/test/java/org/apache/bookkeeper/bookie/EntryLogPartialFlushE2ETest.java
```

## What The Test Covers

The path under test is:

```text
BookKeeper client addEntry
  -> Bookie journal/write cache
  -> LedgerStorage.flush()
  -> DbLedgerStorage / SingleDirectoryDbLedgerStorage.checkpoint()
  -> DefaultEntryLogger.addEntry()
  -> BufferedLogChannel.write()
  -> BufferedChannel.write()
  -> injected flush failure while the write buffer is full
  -> later checkpoint reuses the same entrylog channel
  -> stale entry location is persisted for a later entry
```

The test deliberately invokes `LedgerStorage.flush()` on the target bookie instead of waiting for `SyncThread`. This keeps the reproducer deterministic while still exercising the same storage, entrylog, and RocksDB location-index path.

## Command

From the BookKeeper repository root:

```bash
export JAVA_HOME=/path/to/jdk17
export PATH="$JAVA_HOME/bin:$PATH"

mvn -pl bookkeeper-server \
  -am \
  -Dtest=org.apache.bookkeeper.bookie.EntryLogPartialFlushE2ETest \
  -DfailIfNoTests=false \
  test
```

If the machine is memory constrained, use a bounded Maven/JVM configuration:

```bash
export MAVEN_OPTS="-Xmx2g -XX:MaxMetaspaceSize=512m"

mvn -pl bookkeeper-server \
  -am \
  -Dtest=org.apache.bookkeeper.bookie.EntryLogPartialFlushE2ETest \
  -DfailIfNoTests=false \
  -DforkCount=1 \
  test
```

## Expected Pre-Fix Result

On the current broken behavior, the test should pass because it asserts the reachable bad state:

```text
Tests run: 1, Failures: 0, Errors: 0, Skipped: 0
```

The target bookie should log one injected failure:

```text
Injected entrylog partial flush failure
```

The test then verifies:

1. the injected failure advanced the physical file position beyond the logical `BufferedChannel.position()`;
2. a healthy replica can read a post-failure entry correctly;
3. the target bookie cannot read the same post-failure entry from a correct local location, which demonstrates that a stale location was persisted locally.

## Important Notes

- The failpoint is scoped to `DefaultEntryLogger.BufferedLogChannel`, not global `BufferedChannel`, so it does not intentionally corrupt the journal channel.
- The failpoint is off by default and only enabled by the test through `PartialFlushFault.enableOnceForLogPathContaining(...)`.
- The failure is injected only once.
- The test uses `DbLedgerStorage`, `DefaultEntryLogger`, shared entrylog mode, and `writeBufferBytes=65536`.
- This reproducer is not suitable for an upstream fix PR as-is; it is a diagnostic branch for validating the failure model.

## Moving This To A Pulsar Cluster

After the local E2E test passes, the next reproduction work has two cluster-level goals.

### 1. Failpoint Cluster Validation

This is the deterministic engineering validation. It can use a temporary BookKeeper/Pulsar image with the failpoint enabled only on one target bookie.

The target proof is not merely that a fault was injected. The target proof is that the full Pulsar broker -> managed ledger -> BookKeeper write path can produce the same target/healthy replica evidence:

1. Pulsar writes one persistent topic workload.
2. BookKeeper naturally replicates each ledger entry to the target and healthy bookies.
3. The target bookie hits the controlled entrylog partial-flush fault once.
4. Traffic continues after the fault so the reused target entrylog channel can publish stale locations.
5. The target and healthy bookie entrylogs are copied before teardown.
6. Offline parsing compares target and healthy logs by actual file structure, not fixed production offsets:
   - entrylog header `BKLO`, version, `ledgersMapOffset`, and `ledgersCount`;
   - normal entry frames by length and `ledgerId / entryId`;
   - ledger map frames by `ledgerId=-1, entryId=-2`;
   - target indexed position vs target actual physical entry position;
   - target header map offset vs target actual ledger map frame;
   - healthy indexed/header offsets vs healthy actual frames;
   - target actual entry bodies vs healthy entry bodies for matching `(ledgerId, entryId)`.

Suggested disposable-cluster flow:

1. build a temporary BookKeeper/Pulsar image from this branch;
2. deploy the image to only one target bookie;
3. keep other bookies on a normal build;
4. generate traffic with `pulsar-perf produce` or a fixed-payload producer;
5. wait for the target bookie to log the injected failure;
6. continue traffic for at least one or two checkpoint cycles;
7. inspect the target bookie's entrylog and location index for a stable physical/logical delta.

Do not run this failpoint in production.

A local Docker Compose harness for this layer is stored at:

```text
dev/entrylog-corruption-855/pulsar-failpoint-cluster/
```

### 2. Unmodified-Binary Persuasive Validation

This is the version intended for external review. BookKeeper/Pulsar code should be unchanged. The only fault should come from an auditable external I/O layer.

Candidate approaches:

| Approach | Source changes | Notes |
| --- | --- | --- |
| `LD_PRELOAD` syscall shim | None | Intercept target-bookie `write`/`pwrite` calls for entrylog files, let bytes reach the backing file, then return one controlled `EIO`. |
| FUSE fault-injection filesystem | None | Mount only the target bookie's ledger directory on a filesystem that can accept bytes and return one controlled write error. |
| Block-device fault injection | None | Closest to hardware failure, but the hardest to make deterministic at the exact entrylog window. |
| Byteman/BTrace | None in source tree | Useful fallback, but less persuasive than a syscall/filesystem-level fault. |

Acceptance criteria for the unmodified-binary run:

1. record the exact Pulsar/BookKeeper image digest or binary checksum;
2. run the same single-topic workload with target and healthy bookie data directories mounted;
3. trigger one external I/O fault on the target bookie's entrylog path;
4. copy target and healthy entrylogs before teardown;
5. use the same offline parser to prove the same structural invariants as the failpoint run;
6. optionally force a Pulsar read path through the target replica to show the user-visible failure mode, since normal reads can be masked by healthy replicas.
