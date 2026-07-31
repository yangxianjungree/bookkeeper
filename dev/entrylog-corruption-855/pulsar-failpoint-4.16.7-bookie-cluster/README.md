# Pulsar Cluster Reproducer With BookKeeper 4.16.7 Bookies

This harness runs Pulsar 3.2.4 as the broker/client layer and runs three
external BookKeeper 4.16.7 bookies from a separately built BookKeeper
distribution.

The target evidence is the BookKeeper bookie runtime. Only `bk1` enables the
entrylog partial-flush failpoint. `bk2` and `bk3` are healthy controls.

## Build Input

The default BookKeeper input is:

```bash
/tmp/bookkeeper-4.16.7-failpoint/bookkeeper-dist/server/target/bookkeeper-server-4.16.7-bin.tar.gz
```

The prepare step verifies that the extracted `bookkeeper-server-4.16.7.jar`
contains `DefaultEntryLogger$BufferedLogChannel$PartialFlushFault`.

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
RATE=500 SIZE=512 MESSAGES=20000 TOPIC=persistent://public/default/entrylog-failpoint scripts/run-workload.sh
```

Runtime data and logs are kept under `runtime/` for offline inspection.

## Stability Run

The 2026-07-31 stability archive is:

```text
runs/stability-20260731-151541/
```

It ran five clean clusters with different workload variables. Every round used
Pulsar 3.2.4 for broker/client tooling and external BookKeeper 4.16.7 bookies.
Only `bk1` enabled the entrylog partial-flush failpoint; `bk2` and `bk3` were
healthy controls.

| Round | Messages | Size | Rate | Workload RC | Failpoint Events | bk1 | bk1 Map Delta | bk2 | bk3 | Replica Hash Mismatches |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- | --- | ---: |
| 1 | 20000 | 512 | 500 | 0 | 1 | DRIFT_OK | 135 | SEALED_OK | SEALED_OK | 0 |
| 2 | 25000 | 768 | 700 | 0 | 1 | DRIFT_OK | 295 | SEALED_OK | SEALED_OK | 0 |
| 3 | 30000 | 1024 | 900 | 0 | 1 | DRIFT_OK | 1728 | SEALED_OK | SEALED_OK | 0 |
| 4 | 35000 | 384 | 600 | 0 | 1 | DRIFT_OK | 158 | SEALED_OK | SEALED_OK | 0 |
| 5 | 40000 | 1536 | 1000 | 0 | 1 | DRIFT_OK | 3283 | SEALED_OK | SEALED_OK | 0 |

Tracked results include `summary.csv`, per-round Markdown reports, and
`versions.properties`. The full physical entrylog copies, full JSON reports, and
process logs are retained in the local archive but ignored by git to avoid
committing large artifacts.
