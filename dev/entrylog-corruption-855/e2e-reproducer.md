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

After the local E2E test passes, the same failpoint can be used in a disposable Pulsar or BookKeeper staging cluster:

1. build a temporary BookKeeper/Pulsar image from this branch;
2. deploy the image to only one target bookie;
3. keep other bookies on a normal build;
4. generate traffic with `pulsar-perf produce` or a fixed-payload producer;
5. wait for the target bookie to log the injected failure;
6. continue traffic for at least one or two checkpoint cycles;
7. inspect the target bookie's entrylog and location index for a stable physical/logical delta.

Do not run this failpoint in production.
