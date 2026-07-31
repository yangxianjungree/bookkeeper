# Stability Run 20260731-151541

This archive records five clean Pulsar cluster failpoint reproductions.

Runtime shape:

- Pulsar 3.2.4 broker/client/ZooKeeper tooling.
- Three external BookKeeper 4.16.7 bookies from a separately built distribution.
- `bk1` enabled `bk.entrylog.partialFlushFault.enabled=true`.
- `bk2` and `bk3` were healthy controls.

Summary:

| Round | Messages | Size | Rate | Workload RC | Failpoint Events | bk1 | bk1 Map Delta | bk1 Header Map Valid | bk2 | bk3 | Replica Hash Mismatches |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- | --- | --- | ---: |
| 1 | 20000 | 512 | 500 | 0 | 1 | DRIFT_OK | 135 | False | SEALED_OK | SEALED_OK | 0 |
| 2 | 25000 | 768 | 700 | 0 | 1 | DRIFT_OK | 295 | False | SEALED_OK | SEALED_OK | 0 |
| 3 | 30000 | 1024 | 900 | 0 | 1 | DRIFT_OK | 1728 | False | SEALED_OK | SEALED_OK | 0 |
| 4 | 35000 | 384 | 600 | 0 | 1 | DRIFT_OK | 158 | False | SEALED_OK | SEALED_OK | 0 |
| 5 | 40000 | 1536 | 1000 | 0 | 1 | DRIFT_OK | 3283 | False | SEALED_OK | SEALED_OK | 0 |

Tracked evidence:

- `summary.csv`: compact machine-readable summary.
- `round-*/entrylog-cluster-report.md`: parsed entrylog/header/ledger-map report.
- `round-*/versions.properties`: Pulsar and BookKeeper distribution versions.

Local-only evidence ignored by git:

- `round-*/entrylogs/`: copied physical entrylog files for `bk1`, `bk2`, and `bk3`.
- `round-*/entrylog-cluster-report.json`: full parsed report with per-entry hashes.
- `round-*/*.log`: process logs, including the bk1 failpoint source log.
