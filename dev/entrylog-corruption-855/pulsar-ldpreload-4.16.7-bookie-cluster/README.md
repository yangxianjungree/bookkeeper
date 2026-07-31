# Pulsar Cluster Reproducer With Unmodified BookKeeper 4.16.7 Bookies

This harness runs Pulsar 3.2.4 as the broker/client layer and runs three
external unmodified BookKeeper 4.16.7 bookies from a clean release-tag
distribution.

The target evidence is the BookKeeper bookie runtime. Only `bk1` enables the
external `LD_PRELOAD` write fault injector. `bk2` and `bk3` are healthy
controls and run without `LD_PRELOAD`.

## Build Input

The default BookKeeper input is:

```bash
/tmp/bookkeeper-4.16.7-clean/bookkeeper-dist/server/target/bookkeeper-server-4.16.7-bin.tar.gz
```

The prepare step verifies that the extracted `bookkeeper-server-4.16.7.jar`
does not contain `DefaultEntryLogger$BufferedLogChannel$PartialFlushFault`.
It also builds and copies the auditable injector from:

```bash
dev/entrylog-corruption-855/tools/ldpreload-entrylog-fault/
```

## Run

```bash
scripts/prepare-local-cluster.sh
scripts/start-local-cluster.sh
scripts/run-workload.sh
scripts/stop-local-cluster.sh
scripts/analyze-entrylogs.sh
```

Useful workload variables:

```bash
RATE=500 SIZE=512 MESSAGES=20000 TOPIC=persistent://public/default/entrylog-ldpreload scripts/run-workload.sh
```

Useful fault variables for `scripts/start-local-cluster.sh`:

```bash
BK_ENTRYLOG_FAULT_ENABLED=1
BK_ENTRYLOG_FAULT_DRY_RUN=0
BK_ENTRYLOG_FAULT_MIN_WRITE_BYTES=32768
BK_ENTRYLOG_FAULT_EXACT_WRITE_BYTES=0
BK_ENTRYLOG_FAULT_AFTER_MATCHES=1
BK_ENTRYLOG_FAULT_MAX_TRIGGERS=1
```

Runtime data and logs are kept under `runtime/` for offline inspection.

## Stability Run

Run fresh local clusters with varied workload and fault variables:

```bash
ROUNDS=5 scripts/run-stability.sh
```

The script archives per-round Markdown reports under `runs/<run-id>/`, plus a
`summary.csv` and `summary.md`. The report includes grouped runtime log
snippets for the client, broker, and bookies. Raw process logs and physical
entrylog copies are kept locally for audit but ignored by git.

## 2/1/1 Single-Copy Run

Run a scenario closer to the production ledger metadata shape from the
investigation notes:

```bash
ROUNDS=5 scripts/run-single-replica-stability.sh
```

This starts two unmodified BookKeeper 4.16.7 bookies and configures Pulsar
managed ledgers as `ensemble=2`, `writeQuorum=1`, `ackQuorum=1`. The injector is
still enabled only on `bk1`, and the default fault filter is tightened to the
N-th exact 64 KiB entrylog write:

```bash
BK_ENTRYLOG_FAULT_MIN_WRITE_BYTES=65536
BK_ENTRYLOG_FAULT_EXACT_WRITE_BYTES=65536
BK_ENTRYLOG_FAULT_AFTER_MATCHES_N=1..5
BK_ENTRYLOG_FAULT_MAX_TRIGGERS=1
```

Because `writeQuorum < ensemble`, entries are intentionally single-copy
distributed across bookies. The report therefore skips replica hash comparison
for this mode and relies on entrylog structure plus client, broker, and bookie
runtime logs.

The bk1 injector log is:

```text
runtime/logs/bk1/ldpreload-entrylog-fault.log
```

The report should be interpreted the same way as the failpoint cluster report:
`bk1` is the target replica and non-injected bookies are healthy controls. In
the default three-bookie run `bk2` and `bk3` are strict replica controls. In
the `2/1/1` single-copy run only `bk2` is present, so the report compares the
entrylog header, discovered ledger map, ledger size accounting, and runtime
chain logs instead of forcing replica hash equality.
