# Entrylog Cluster Report

- clusterDir: `/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runs/single-replica-20260731-184741/round-02`
- pulsarVersion: `3.2.4`
- bookieVersion: `4.16.7`
- bookieCount: `2`
- managedLedgerQuorum: `2/1/1`
- failpointEvents: `1`

## Failpoint Events

| kind | logId | logFile | logical | physical | bytes | op | offset | realRc | match | trigger |
|---|---:|---|---:|---:|---:|---|---:|---:|---:|---:|
| ldpreload | 1 | `/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log` |  |  | 65536 | write | -1 | 65536 | 2 | 1 |

## Log Structure

| role | log | status | fileSize | headerMap | trueMap | delta | headerMapValid | entries | strict | prefix | post | parsedSize | mapSize | sizeMatch |
|---|---|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| bk1 | `0.log` | SEALED_OK | 130630 | 130590 | 130590 | 0 | True | 101 | 101 | None | None | 129566 | 129566 | True |
| bk1 | `1.log` | DRIFT_CHECK | 196560 | 130407 | 196520 | 66113 | False | 137 | None | 62 | 75 | 130220 | 129379 | False |
| bk1 | `10.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk1 | `11.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk1 | `12.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk1 | `13.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk1 | `14.log` | SEALED_OK | 130680 | 130640 | 130640 | 0 | True | 141 | 141 | None | None | 129616 | 129616 | True |
| bk1 | `15.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk1 | `16.log` | SEALED_OK | 130706 | 130666 | 130666 | 0 | True | 141 | 141 | None | None | 129642 | 129642 | True |
| bk1 | `17.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk1 | `18.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk1 | `19.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk1 | `1a.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk1 | `1b.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk1 | `1c.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk1 | `1d.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk1 | `1e.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk1 | `1f.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk1 | `2.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk1 | `20.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk1 | `21.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk1 | `22.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk1 | `23.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk1 | `24.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk1 | `25.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk1 | `26.log` | SEALED_OK | 130365 | 130325 | 130325 | 0 | True | 150 | 150 | None | None | 129301 | 129301 | True |
| bk1 | `27.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk1 | `28.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk1 | `29.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk1 | `2a.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk1 | `2b.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk1 | `2c.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk1 | `2d.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 144 | 144 | None | None | 129779 | 129779 | True |
| bk1 | `2e.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk1 | `2f.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk1 | `3.log` | SEALED_OK | 130342 | 130302 | 130302 | 0 | True | 137 | 137 | None | None | 129278 | 129278 | True |
| bk1 | `30.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk1 | `31.log` | SEALED_OK | 130819 | 130779 | 130779 | 0 | True | 143 | 143 | None | None | 129755 | 129755 | True |
| bk1 | `32.log` | SEALED_OK | 130819 | 130779 | 130779 | 0 | True | 143 | 143 | None | None | 129755 | 129755 | True |
| bk1 | `33.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk1 | `34.log` | SEALED_OK | 130669 | 130629 | 130629 | 0 | True | 140 | 140 | None | None | 129605 | 129605 | True |
| bk1 | `35.log` | UNSEALED_OK | 27836 | 0 | None | None | False | 30 | 30 | None | None | None | None | None |
| bk1 | `4.log` | SEALED_OK | 129512 | 129472 | 129472 | 0 | True | 107 | 107 | None | None | 128448 | 128448 | True |
| bk1 | `5.log` | SEALED_OK | 130656 | 130616 | 130616 | 0 | True | 140 | 140 | None | None | 129592 | 129592 | True |
| bk1 | `6.log` | SEALED_OK | 131006 | 130966 | 130966 | 0 | True | 147 | 147 | None | None | 129942 | 129942 | True |
| bk1 | `7.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk1 | `8.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk1 | `9.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk1 | `a.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk1 | `b.log` | SEALED_OK | 130478 | 130438 | 130438 | 0 | True | 152 | 152 | None | None | 129414 | 129414 | True |
| bk1 | `c.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk1 | `d.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk1 | `e.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk1 | `f.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk2 | `0.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 103 | 103 | None | None | 129720 | 129720 | True |
| bk2 | `1.log` | SEALED_OK | 130493 | 130453 | 130453 | 0 | True | 137 | 137 | None | None | 129429 | 129429 | True |
| bk2 | `10.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk2 | `11.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk2 | `12.log` | SEALED_OK | 131006 | 130966 | 130966 | 0 | True | 147 | 147 | None | None | 129942 | 129942 | True |
| bk2 | `13.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk2 | `14.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `15.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk2 | `16.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `17.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk2 | `18.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk2 | `19.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `1a.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk2 | `1b.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `1c.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk2 | `1d.log` | SEALED_OK | 130769 | 130729 | 130729 | 0 | True | 142 | 142 | None | None | 129705 | 129705 | True |
| bk2 | `1e.log` | SEALED_OK | 130906 | 130866 | 130866 | 0 | True | 145 | 145 | None | None | 129842 | 129842 | True |
| bk2 | `1f.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `2.log` | SEALED_OK | 131043 | 131003 | 131003 | 0 | True | 148 | 148 | None | None | 129979 | 129979 | True |
| bk2 | `20.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk2 | `21.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk2 | `22.log` | SEALED_OK | 130619 | 130579 | 130579 | 0 | True | 139 | 139 | None | None | 129555 | 129555 | True |
| bk2 | `23.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk2 | `24.log` | SEALED_OK | 130228 | 130188 | 130188 | 0 | True | 147 | 147 | None | None | 129164 | 129164 | True |
| bk2 | `25.log` | SEALED_OK | 131056 | 131016 | 131016 | 0 | True | 148 | 148 | None | None | 129992 | 129992 | True |
| bk2 | `26.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk2 | `27.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk2 | `28.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk2 | `29.log` | SEALED_OK | 130819 | 130779 | 130779 | 0 | True | 143 | 143 | None | None | 129755 | 129755 | True |
| bk2 | `2a.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk2 | `2b.log` | SEALED_OK | 130569 | 130529 | 130529 | 0 | True | 138 | 138 | None | None | 129505 | 129505 | True |
| bk2 | `2c.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk2 | `2d.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `2e.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `2f.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk2 | `3.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk2 | `30.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `31.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk2 | `32.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk2 | `33.log` | UNSEALED_OK | 91702 | 0 | None | None | False | 105 | 105 | None | None | None | None | None |
| bk2 | `4.log` | SEALED_OK | 130719 | 130679 | 130679 | 0 | True | 141 | 141 | None | None | 129655 | 129655 | True |
| bk2 | `5.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk2 | `6.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk2 | `7.log` | SEALED_OK | 130478 | 130438 | 130438 | 0 | True | 152 | 152 | None | None | 129414 | 129414 | True |
| bk2 | `8.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk2 | `9.log` | SEALED_OK | 130856 | 130816 | 130816 | 0 | True | 144 | 144 | None | None | 129792 | 129792 | True |
| bk2 | `a.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk2 | `b.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `c.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk2 | `d.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk2 | `e.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk2 | `f.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |

## Replica Entry Comparison

Skipped: write quorum is smaller than ensemble size, so entries are intentionally single-copy distributed across bookies.

## Runtime Behavior

- clientExit: `0`

### bk1

| line | tag | log |
|---:|---|---|
| 138 | bookie-fault | `2026-07-31T18:48:44,951 - ERROR - [SyncThread-7-1:SyncThread@181] - Exception flushing ledgers` |
| 139 | bookie-fault | `java.io.IOException: Input/output error` |
| 134 | entrylog-io | `2026-07-31T18:48:44,944 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log for logId 0.` |
| 136 | entrylog-io | `2026-07-31T18:48:44,949 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log for logId 1.` |
| 137 | entrylog-io | `2026-07-31T18:48:44,950 - INFO  - [SyncThread-7-1:EntryLogManagerBase@165] - Flushing entry logger 0 back to filesystem, pending for syncing entry loggers : [BufferedChannel{logId=0, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log, ledgerIdAssigned=-1}].` |
| 165 | entrylog-io | `2026-07-31T18:48:45,940 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/2.log for logId 2.` |
| 166 | entrylog-io | `2026-07-31T18:48:45,940 - INFO  - [SyncThread-7-1:EntryLogManagerBase@165] - Flushing entry logger 1 back to filesystem, pending for syncing entry loggers : [BufferedChannel{logId=0, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log, ledgerIdAssigned=-1}, BufferedChannel{logId=1, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log, ledgerIdAssigned=-1}].` |
| 168 | entrylog-io | `2026-07-31T18:48:45,942 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/3.log for logId 3.` |
| 374 | bookie-lifecycle | `2026-07-31T18:49:13,295 - INFO  - [component-shutdown-thread:BookieServer@191] - Shutting down BookieServer` |
| 395 | bookie-lifecycle | `2026-07-31T18:49:13,317 - INFO  - [component-shutdown-thread:BookieImpl@861] - Turning bookie to read only during shut down` |
| 401 | bookie-lifecycle | `2026-07-31T18:49:13,325 - INFO  - [BookieJournal-3181:BookieImpl@828] - Triggering shutdown of Bookie-3181 with exitCode 5` |
| 409 | bookie-lifecycle | `2026-07-31T18:49:13,335 - INFO  - [BookieShutdownTrigger:BookieImpl@861] - Turning bookie to read only during shut down` |

### bk2

No matching log lines found.

### bk3

No matching log lines found.

### broker

| line | tag | log |
|---:|---|---|
| 33 | bk-client-init | `2026-07-31T18:48:40,366+0800 [main] INFO  org.apache.bookkeeper.meta.MetadataDrivers - BookKeeper metadata driver manager initialized` |
| 34 | bk-client-init | `2026-07-31T18:48:40,369+0800 [main] INFO  org.apache.pulsar.broker.BookKeeperClientFactoryImpl - Applying BookKeeper client configuration setting tlsHostnameVerificationEnabled=false` |
| 61 | bk-client-init | `2026-07-31T18:48:40,664+0800 [main] INFO  org.apache.pulsar.broker.BookKeeperClientFactoryImpl - Applying BookKeeper client configuration setting tlsHostnameVerificationEnabled=false` |
| 48 | bookie-discovery | `2026-07-31T18:48:40,501+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3181 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3181, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 49 | bookie-discovery | `2026-07-31T18:48:40,501+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3182 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3182, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 51 | bookie-discovery | `2026-07-31T18:48:40,509+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3181` |
| 53 | bookie-discovery | `2026-07-31T18:48:40,510+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3182` |
| 75 | bookie-discovery | `2026-07-31T18:48:40,680+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3181 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3181, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 76 | bookie-discovery | `2026-07-31T18:48:40,680+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3182 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3182, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 151 | bookie-channel | `2026-07-31T18:48:43,890+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3181 [id: 0x673b4047, L:/127.0.0.1:57584 - R:127.0.0.1/127.0.0.1:3181]` |
| 152 | bookie-channel | `2026-07-31T18:48:43,891+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0x673b4047, L:/127.0.0.1:57584 - R:127.0.0.1/127.0.0.1:3181] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 153 | bookie-channel | `2026-07-31T18:48:43,892+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3181 [id: 0x3a4b3102, L:/127.0.0.1:57608 - R:127.0.0.1/127.0.0.1:3181]` |
| 154 | bookie-channel | `2026-07-31T18:48:43,892+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0x3a4b3102, L:/127.0.0.1:57608 - R:127.0.0.1/127.0.0.1:3181] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 155 | bookie-channel | `2026-07-31T18:48:43,892+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3181 [id: 0xe91579da, L:/127.0.0.1:57618 - R:127.0.0.1/127.0.0.1:3181]` |
| 156 | bookie-channel | `2026-07-31T18:48:43,892+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0xe91579da, L:/127.0.0.1:57618 - R:127.0.0.1/127.0.0.1:3181] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 318 | managed-ledger | `2026-07-31T18:49:13,733+0800 [metadata-store-9-1] INFO  org.apache.bookkeeper.mledger.impl.ManagedLedgerFactoryImpl - Received MetadataStore session event: ConnectionLost` |
| 221 | broker-error | `2026-07-31T18:49:13,287+0800 [pulsar-io-3-1] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x6dedb56d, L:/127.0.0.1:37356 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 222 | broker-error | `2026-07-31T18:49:13,288+0800 [pulsar-io-3-1] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0xae54fd78, L:/127.0.0.1:37366 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 223 | broker-error | `2026-07-31T18:49:13,288+0800 [pulsar-io-3-1] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x13bf5ecc, L:/127.0.0.1:37334 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 224 | broker-error | `2026-07-31T18:49:13,288+0800 [pulsar-io-3-1] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0xb6ce74cb, L:/127.0.0.1:37362 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 225 | broker-error | `2026-07-31T18:49:13,288+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Disconnected from bookie channel [id: 0x6dedb56d, L:/127.0.0.1:37356 ! R:127.0.0.1/127.0.0.1:3182]` |
| 226 | broker-error | `2026-07-31T18:49:13,289+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x49cc868d, L:/127.0.0.1:37266 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |

### client

| line | tag | log |
|---:|---|---|
| 66 | client-progress | `2026-07-31T18:48:53,206+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:    6575 msg ---    657.5 msg/s ---      3.9 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:   5.675 ms - med:   5.311 - 95pct:   8.335 - 99pct:  11.058 - 99.9pct:  31.285 - 99.99pct:  33.530 - Max:  34.674` |
| 67 | client-progress | `2026-07-31T18:49:03,218+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:   13600 msg ---    700.2 msg/s ---      4.1 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:   5.362 ms - med:   4.978 - 95pct:   7.455 - 99pct:  10.095 - 99.9pct:  48.462 - 99.99pct:  52.786 - Max:  53.887` |
| 72 | client-progress | `2026-07-31T18:49:13,223+0800 [Thread-0] INFO  org.apache.pulsar.testclient.PerformanceProducer - Aggregated throughput stats --- 16004 records sent --- 532.630 msg/s --- 3.121 Mbit/s ` |
| 73 | client-progress | `2026-07-31T18:49:13,244+0800 [Thread-0] INFO  org.apache.pulsar.testclient.PerformanceProducer - Aggregated latency stats --- Latency: mean:   5.466 ms - med:   5.108 - 95pct:   7.797 - 99pct:  10.500 - 99.9pct:  36.848 - 99.99pct:  51.999 - 99.999pct:  53.887 - Max:  53.887` |
| 68 | client-completion | `2026-07-31T18:49:06,635+0800 [pulsar-perf-producer-exec-1-1] INFO  org.apache.pulsar.testclient.PerformanceProducer - ------------- DONE (reached the maximum number: 16000 of production) --------------` |
| 74 | client-completion | `workload_rc=0` |
