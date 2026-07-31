# Entrylog Cluster Report

- clusterDir: `/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runs/single-replica-20260731-184741/round-04`
- pulsarVersion: `3.2.4`
- bookieVersion: `4.16.7`
- bookieCount: `2`
- managedLedgerQuorum: `2/1/1`
- failpointEvents: `1`

## Failpoint Events

| kind | logId | logFile | logical | physical | bytes | op | offset | realRc | match | trigger |
|---|---:|---|---:|---:|---:|---|---:|---:|---:|---:|
| ldpreload | 3 | `/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/3.log` |  |  | 65536 | write | -1 | 65536 | 4 | 1 |

## Log Structure

| role | log | status | fileSize | headerMap | trueMap | delta | headerMapValid | entries | strict | prefix | post | parsedSize | mapSize | sizeMatch |
|---|---|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| bk1 | `0.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 235 | 235 | None | None | 129745 | 129745 | True |
| bk1 | `1.log` | SEALED_OK | 130996 | 130956 | 130956 | 0 | True | 279 | 279 | None | None | 129932 | 129932 | True |
| bk1 | `10.log` | SEALED_OK | 130659 | 130619 | 130619 | 0 | True | 272 | 272 | None | None | 129595 | 129595 | True |
| bk1 | `11.log` | SEALED_OK | 130709 | 130669 | 130669 | 0 | True | 273 | 273 | None | None | 129645 | 129645 | True |
| bk1 | `12.log` | SEALED_OK | 130909 | 130869 | 130869 | 0 | True | 277 | 277 | None | None | 129845 | 129845 | True |
| bk1 | `13.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk1 | `14.log` | SEALED_OK | 130859 | 130819 | 130819 | 0 | True | 276 | 276 | None | None | 129795 | 129795 | True |
| bk1 | `15.log` | SEALED_OK | 131016 | 130976 | 130976 | 0 | True | 271 | 271 | None | None | 129952 | 129952 | True |
| bk1 | `16.log` | SEALED_OK | 130302 | 130262 | 130262 | 0 | True | 273 | 273 | None | None | 129238 | 129238 | True |
| bk1 | `17.log` | SEALED_OK | 130859 | 130819 | 130819 | 0 | True | 276 | 276 | None | None | 129795 | 129795 | True |
| bk1 | `18.log` | SEALED_OK | 130909 | 130869 | 130869 | 0 | True | 277 | 277 | None | None | 129845 | 129845 | True |
| bk1 | `19.log` | SEALED_OK | 131016 | 130976 | 130976 | 0 | True | 271 | 271 | None | None | 129952 | 129952 | True |
| bk1 | `1a.log` | SEALED_OK | 130759 | 130719 | 130719 | 0 | True | 274 | 274 | None | None | 129695 | 129695 | True |
| bk1 | `1b.log` | SEALED_OK | 130709 | 130669 | 130669 | 0 | True | 273 | 273 | None | None | 129645 | 129645 | True |
| bk1 | `1c.log` | SEALED_OK | 131009 | 130969 | 130969 | 0 | True | 279 | 279 | None | None | 129945 | 129945 | True |
| bk1 | `1d.log` | SEALED_OK | 131098 | 131058 | 131058 | 0 | True | 276 | 276 | None | None | 130034 | 130034 | True |
| bk1 | `1e.log` | SEALED_OK | 130778 | 130738 | 130738 | 0 | True | 268 | 268 | None | None | 129714 | 129714 | True |
| bk1 | `1f.log` | SEALED_OK | 130752 | 130712 | 130712 | 0 | True | 276 | 276 | None | None | 129688 | 129688 | True |
| bk1 | `2.log` | SEALED_OK | 130909 | 130869 | 130869 | 0 | True | 277 | 277 | None | None | 129845 | 129845 | True |
| bk1 | `20.log` | SEALED_OK | 130826 | 130786 | 130786 | 0 | True | 269 | 269 | None | None | 129762 | 129762 | True |
| bk1 | `21.log` | SEALED_OK | 130826 | 130786 | 130786 | 0 | True | 269 | 269 | None | None | 129762 | 129762 | True |
| bk1 | `22.log` | SEALED_OK | 131066 | 131026 | 131026 | 0 | True | 274 | 274 | None | None | 130002 | 130002 | True |
| bk1 | `23.log` | SEALED_OK | 130704 | 130664 | 130664 | 0 | True | 275 | 275 | None | None | 129640 | 129640 | True |
| bk1 | `24.log` | SEALED_OK | 130656 | 130616 | 130616 | 0 | True | 274 | 274 | None | None | 129592 | 129592 | True |
| bk1 | `25.log` | SEALED_OK | 130704 | 130664 | 130664 | 0 | True | 275 | 275 | None | None | 129640 | 129640 | True |
| bk1 | `26.log` | SEALED_OK | 130970 | 130930 | 130930 | 0 | True | 272 | 272 | None | None | 129906 | 129906 | True |
| bk1 | `27.log` | SEALED_OK | 131018 | 130978 | 130978 | 0 | True | 273 | 273 | None | None | 129954 | 129954 | True |
| bk1 | `28.log` | SEALED_OK | 130800 | 130760 | 130760 | 0 | True | 277 | 277 | None | None | 129736 | 129736 | True |
| bk1 | `29.log` | SEALED_OK | 131018 | 130978 | 130978 | 0 | True | 273 | 273 | None | None | 129954 | 129954 | True |
| bk1 | `2a.log` | UNSEALED_OK | 77728 | 0 | None | None | False | 163 | 163 | None | None | None | None | None |
| bk1 | `3.log` | STRICT_CHECK | 196817 | 130860 | 196777 | 65917 | False | 267 | 267 | None | None | 125262 | 129832 | False |
| bk1 | `4.log` | SEALED_OK | 130759 | 130719 | 130719 | 0 | True | 274 | 274 | None | None | 129695 | 129695 | True |
| bk1 | `5.log` | SEALED_OK | 131009 | 130969 | 130969 | 0 | True | 279 | 279 | None | None | 129945 | 129945 | True |
| bk1 | `6.log` | SEALED_OK | 131053 | 131013 | 131013 | 0 | True | 272 | 272 | None | None | 129989 | 129989 | True |
| bk1 | `7.log` | SEALED_OK | 130896 | 130856 | 130856 | 0 | True | 277 | 277 | None | None | 129832 | 129832 | True |
| bk1 | `8.log` | SEALED_OK | 131059 | 131019 | 131019 | 0 | True | 280 | 280 | None | None | 129995 | 129995 | True |
| bk1 | `9.log` | SEALED_OK | 130659 | 130619 | 130619 | 0 | True | 272 | 272 | None | None | 129595 | 129595 | True |
| bk1 | `a.log` | SEALED_OK | 130352 | 130312 | 130312 | 0 | True | 274 | 274 | None | None | 129288 | 129288 | True |
| bk1 | `b.log` | SEALED_OK | 130709 | 130669 | 130669 | 0 | True | 273 | 273 | None | None | 129645 | 129645 | True |
| bk1 | `c.log` | SEALED_OK | 130759 | 130719 | 130719 | 0 | True | 274 | 274 | None | None | 129695 | 129695 | True |
| bk1 | `d.log` | SEALED_OK | 130859 | 130819 | 130819 | 0 | True | 276 | 276 | None | None | 129795 | 129795 | True |
| bk1 | `e.log` | SEALED_OK | 131009 | 130969 | 130969 | 0 | True | 279 | 279 | None | None | 129945 | 129945 | True |
| bk1 | `f.log` | SEALED_OK | 130759 | 130719 | 130719 | 0 | True | 274 | 274 | None | None | 129695 | 129695 | True |
| bk2 | `0.log` | SEALED_OK | 131093 | 131053 | 131053 | 0 | True | 260 | 260 | None | None | 130029 | 130029 | True |
| bk2 | `1.log` | SEALED_OK | 131066 | 131026 | 131026 | 0 | True | 272 | 272 | None | None | 130002 | 130002 | True |
| bk2 | `10.log` | SEALED_OK | 131016 | 130976 | 130976 | 0 | True | 271 | 271 | None | None | 129952 | 129952 | True |
| bk2 | `11.log` | SEALED_OK | 130859 | 130819 | 130819 | 0 | True | 276 | 276 | None | None | 129795 | 129795 | True |
| bk2 | `12.log` | SEALED_OK | 130859 | 130819 | 130819 | 0 | True | 276 | 276 | None | None | 129795 | 129795 | True |
| bk2 | `13.log` | SEALED_OK | 130916 | 130876 | 130876 | 0 | True | 269 | 269 | None | None | 129852 | 129852 | True |
| bk2 | `14.log` | SEALED_OK | 130509 | 130469 | 130469 | 0 | True | 269 | 269 | None | None | 129445 | 129445 | True |
| bk2 | `15.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk2 | `16.log` | SEALED_OK | 130509 | 130469 | 130469 | 0 | True | 269 | 269 | None | None | 129445 | 129445 | True |
| bk2 | `17.log` | SEALED_OK | 130709 | 130669 | 130669 | 0 | True | 273 | 273 | None | None | 129645 | 129645 | True |
| bk2 | `18.log` | SEALED_OK | 130759 | 130719 | 130719 | 0 | True | 274 | 274 | None | None | 129695 | 129695 | True |
| bk2 | `19.log` | SEALED_OK | 130709 | 130669 | 130669 | 0 | True | 273 | 273 | None | None | 129645 | 129645 | True |
| bk2 | `1a.log` | SEALED_OK | 130909 | 130869 | 130869 | 0 | True | 277 | 277 | None | None | 129845 | 129845 | True |
| bk2 | `1b.log` | SEALED_OK | 130759 | 130719 | 130719 | 0 | True | 274 | 274 | None | None | 129695 | 129695 | True |
| bk2 | `1c.log` | SEALED_OK | 130799 | 130759 | 130759 | 0 | True | 273 | 273 | None | None | 129735 | 129735 | True |
| bk2 | `1d.log` | SEALED_OK | 131018 | 130978 | 130978 | 0 | True | 273 | 273 | None | None | 129954 | 129954 | True |
| bk2 | `1e.log` | SEALED_OK | 130874 | 130834 | 130834 | 0 | True | 270 | 270 | None | None | 129810 | 129810 | True |
| bk2 | `1f.log` | SEALED_OK | 130826 | 130786 | 130786 | 0 | True | 269 | 269 | None | None | 129762 | 129762 | True |
| bk2 | `2.log` | SEALED_OK | 131059 | 131019 | 131019 | 0 | True | 280 | 280 | None | None | 129995 | 129995 | True |
| bk2 | `20.log` | SEALED_OK | 130922 | 130882 | 130882 | 0 | True | 271 | 271 | None | None | 129858 | 129858 | True |
| bk2 | `21.log` | SEALED_OK | 130320 | 130280 | 130280 | 0 | True | 267 | 267 | None | None | 129256 | 129256 | True |
| bk2 | `22.log` | SEALED_OK | 130656 | 130616 | 130616 | 0 | True | 274 | 274 | None | None | 129592 | 129592 | True |
| bk2 | `23.log` | SEALED_OK | 130848 | 130808 | 130808 | 0 | True | 278 | 278 | None | None | 129784 | 129784 | True |
| bk2 | `24.log` | SEALED_OK | 130826 | 130786 | 130786 | 0 | True | 269 | 269 | None | None | 129762 | 129762 | True |
| bk2 | `25.log` | SEALED_OK | 130896 | 130856 | 130856 | 0 | True | 279 | 279 | None | None | 129832 | 129832 | True |
| bk2 | `26.log` | SEALED_OK | 130922 | 130882 | 130882 | 0 | True | 271 | 271 | None | None | 129858 | 129858 | True |
| bk2 | `27.log` | SEALED_OK | 130848 | 130808 | 130808 | 0 | True | 278 | 278 | None | None | 129784 | 129784 | True |
| bk2 | `28.log` | SEALED_OK | 130970 | 130930 | 130930 | 0 | True | 272 | 272 | None | None | 129906 | 129906 | True |
| bk2 | `29.log` | SEALED_OK | 130656 | 130616 | 130616 | 0 | True | 274 | 274 | None | None | 129592 | 129592 | True |
| bk2 | `2a.log` | UNSEALED_OK | 16596 | 0 | None | None | False | 34 | 34 | None | None | None | None | None |
| bk2 | `3.log` | SEALED_OK | 130746 | 130706 | 130706 | 0 | True | 274 | 274 | None | None | 129682 | 129682 | True |
| bk2 | `4.log` | SEALED_OK | 130709 | 130669 | 130669 | 0 | True | 273 | 273 | None | None | 129645 | 129645 | True |
| bk2 | `5.log` | SEALED_OK | 130759 | 130719 | 130719 | 0 | True | 274 | 274 | None | None | 129695 | 129695 | True |
| bk2 | `6.log` | SEALED_OK | 131103 | 131063 | 131063 | 0 | True | 273 | 273 | None | None | 130039 | 130039 | True |
| bk2 | `7.log` | SEALED_OK | 130909 | 130869 | 130869 | 0 | True | 277 | 277 | None | None | 129845 | 129845 | True |
| bk2 | `8.log` | SEALED_OK | 130959 | 130919 | 130919 | 0 | True | 278 | 278 | None | None | 129895 | 129895 | True |
| bk2 | `9.log` | SEALED_OK | 131009 | 130969 | 130969 | 0 | True | 279 | 279 | None | None | 129945 | 129945 | True |
| bk2 | `a.log` | SEALED_OK | 130846 | 130806 | 130806 | 0 | True | 276 | 276 | None | None | 129782 | 129782 | True |
| bk2 | `b.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk2 | `c.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk2 | `d.log` | SEALED_OK | 130966 | 130926 | 130926 | 0 | True | 270 | 270 | None | None | 129902 | 129902 | True |
| bk2 | `e.log` | SEALED_OK | 130959 | 130919 | 130919 | 0 | True | 278 | 278 | None | None | 129895 | 129895 | True |
| bk2 | `f.log` | SEALED_OK | 130709 | 130669 | 130669 | 0 | True | 273 | 273 | None | None | 129645 | 129645 | True |

## Replica Entry Comparison

Skipped: write quorum is smaller than ensemble size, so entries are intentionally single-copy distributed across bookies.

## Runtime Behavior

- clientExit: `0`

### bk1

| line | tag | log |
|---:|---|---|
| 147 | bookie-fault | `2026-07-31T18:50:24,279 - ERROR - [SyncThread-7-1:SyncThread@181] - Exception flushing ledgers` |
| 148 | bookie-fault | `java.io.IOException: Input/output error` |
| 134 | entrylog-io | `2026-07-31T18:50:20,285 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log for logId 0.` |
| 136 | entrylog-io | `2026-07-31T18:50:21,281 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log for logId 1.` |
| 137 | entrylog-io | `2026-07-31T18:50:21,281 - INFO  - [SyncThread-7-1:EntryLogManagerBase@165] - Flushing entry logger 0 back to filesystem, pending for syncing entry loggers : [BufferedChannel{logId=0, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log, ledgerIdAssigned=-1}].` |
| 138 | entrylog-io | `2026-07-31T18:50:21,293 - INFO  - [SyncThread-7-1:EntryLogManagerForSingleEntryLog@210] - Synced entry logger 0 to disk.` |
| 140 | entrylog-io | `2026-07-31T18:50:22,280 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/2.log for logId 2.` |
| 141 | entrylog-io | `2026-07-31T18:50:22,280 - INFO  - [SyncThread-7-1:EntryLogManagerBase@165] - Flushing entry logger 1 back to filesystem, pending for syncing entry loggers : [BufferedChannel{logId=1, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log, ledgerIdAssigned=-1}].` |
| 330 | bookie-lifecycle | `2026-07-31T18:51:09,521 - INFO  - [component-shutdown-thread:BookieServer@191] - Shutting down BookieServer` |
| 351 | bookie-lifecycle | `2026-07-31T18:51:09,545 - INFO  - [component-shutdown-thread:BookieImpl@861] - Turning bookie to read only during shut down` |
| 357 | bookie-lifecycle | `2026-07-31T18:51:09,558 - INFO  - [BookieJournal-3181:BookieImpl@828] - Triggering shutdown of Bookie-3181 with exitCode 5` |

### bk2

No matching log lines found.

### bk3

No matching log lines found.

### broker

| line | tag | log |
|---:|---|---|
| 33 | bk-client-init | `2026-07-31T18:50:16,541+0800 [main] INFO  org.apache.bookkeeper.meta.MetadataDrivers - BookKeeper metadata driver manager initialized` |
| 34 | bk-client-init | `2026-07-31T18:50:16,543+0800 [main] INFO  org.apache.pulsar.broker.BookKeeperClientFactoryImpl - Applying BookKeeper client configuration setting tlsHostnameVerificationEnabled=false` |
| 61 | bk-client-init | `2026-07-31T18:50:16,815+0800 [main] INFO  org.apache.pulsar.broker.BookKeeperClientFactoryImpl - Applying BookKeeper client configuration setting tlsHostnameVerificationEnabled=false` |
| 48 | bookie-discovery | `2026-07-31T18:50:16,668+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3181 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3181, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 49 | bookie-discovery | `2026-07-31T18:50:16,668+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3182 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3182, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 51 | bookie-discovery | `2026-07-31T18:50:16,676+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3181` |
| 53 | bookie-discovery | `2026-07-31T18:50:16,676+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3182` |
| 75 | bookie-discovery | `2026-07-31T18:50:16,830+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3181 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3181, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 76 | bookie-discovery | `2026-07-31T18:50:16,831+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3182 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3182, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 151 | bookie-channel | `2026-07-31T18:50:20,097+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3182 [id: 0x13960280, L:/127.0.0.1:38306 - R:127.0.0.1/127.0.0.1:3182]` |
| 152 | bookie-channel | `2026-07-31T18:50:20,098+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0x13960280, L:/127.0.0.1:38306 - R:127.0.0.1/127.0.0.1:3182] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 153 | bookie-channel | `2026-07-31T18:50:20,099+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3182 [id: 0xc3f9eac9, L:/127.0.0.1:38314 - R:127.0.0.1/127.0.0.1:3182]` |
| 154 | bookie-channel | `2026-07-31T18:50:20,100+0800 [pulsar-io-3-2] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3182 [id: 0xefe4744b, L:/127.0.0.1:38294 - R:127.0.0.1/127.0.0.1:3182]` |
| 155 | bookie-channel | `2026-07-31T18:50:20,103+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0xc3f9eac9, L:/127.0.0.1:38314 - R:127.0.0.1/127.0.0.1:3182] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 156 | bookie-channel | `2026-07-31T18:50:20,103+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3182 [id: 0xdae14168, L:/127.0.0.1:38326 - R:127.0.0.1/127.0.0.1:3182]` |
| 316 | managed-ledger | `2026-07-31T18:51:09,969+0800 [metadata-store-9-1] INFO  org.apache.bookkeeper.mledger.impl.ManagedLedgerFactoryImpl - Received MetadataStore session event: ConnectionLost` |
| 221 | broker-error | `2026-07-31T18:51:09,518+0800 [pulsar-io-3-1] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x13960280, L:/127.0.0.1:38306 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 222 | broker-error | `2026-07-31T18:51:09,519+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x13988760, L:/127.0.0.1:38410 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 224 | broker-error | `2026-07-31T18:51:09,519+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Disconnected from bookie channel [id: 0x13960280, L:/127.0.0.1:38306 ! R:127.0.0.1/127.0.0.1:3182]` |
| 225 | broker-error | `2026-07-31T18:51:09,519+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x23ce60fb, L:/127.0.0.1:38386 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 226 | broker-error | `2026-07-31T18:51:09,522+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x564c3df6, L:/127.0.0.1:38418 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 227 | broker-error | `2026-07-31T18:51:09,522+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x4be71b3a, L:/127.0.0.1:38396 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |

### client

| line | tag | log |
|---:|---|---|
| 66 | client-progress | `2026-07-31T18:50:29,436+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:    5639 msg ---    563.9 msg/s ---      1.7 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:   5.114 ms - med:   4.769 - 95pct:   7.218 - 99pct:  11.182 - 99.9pct:  42.764 - 99.99pct:  50.198 - Max:  51.338` |
| 67 | client-progress | `2026-07-31T18:50:39,447+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:   11661 msg ---    600.1 msg/s ---      1.8 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:   4.680 ms - med:   4.603 - 95pct:   6.399 - 99pct:   7.845 - 99.9pct:  10.957 - 99.99pct:  12.889 - Max:  13.527` |
| 68 | client-progress | `2026-07-31T18:50:49,456+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:   17670 msg ---    600.4 msg/s ---      1.8 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:   4.775 ms - med:   4.548 - 95pct:   6.348 - 99pct:   8.841 - 99.9pct:  53.606 - 99.99pct:  58.789 - Max:  59.878` |
| 69 | client-progress | `2026-07-31T18:50:59,469+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:   23677 msg ---    600.2 msg/s ---      1.8 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:  10.149 ms - med:   4.585 - 95pct:   7.372 - 99pct: 202.874 - 99.9pct: 247.927 - 99.99pct: 256.331 - Max: 257.465` |
| 74 | client-progress | `2026-07-31T18:51:09,473+0800 [Thread-0] INFO  org.apache.pulsar.testclient.PerformanceProducer - Aggregated throughput stats --- 24003 records sent --- 479.373 msg/s --- 1.404 Mbit/s ` |
| 75 | client-progress | `2026-07-31T18:51:09,489+0800 [Thread-0] INFO  org.apache.pulsar.testclient.PerformanceProducer - Aggregated latency stats --- Latency: mean:   6.200 ms - med:   4.615 - 95pct:   6.694 - 99pct:  37.439 - 99.9pct: 233.845 - 99.99pct: 254.239 - 99.999pct: 257.465 - Max: 257.465` |
| 70 | client-completion | `2026-07-31T18:50:59,998+0800 [pulsar-perf-producer-exec-1-1] INFO  org.apache.pulsar.testclient.PerformanceProducer - ------------- DONE (reached the maximum number: 24000 of production) --------------` |
| 76 | client-completion | `workload_rc=0` |
