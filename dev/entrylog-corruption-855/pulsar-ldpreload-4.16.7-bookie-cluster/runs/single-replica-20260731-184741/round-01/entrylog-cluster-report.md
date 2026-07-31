# Entrylog Cluster Report

- clusterDir: `/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runs/single-replica-20260731-184741/round-01`
- pulsarVersion: `3.2.4`
- bookieVersion: `4.16.7`
- bookieCount: `2`
- managedLedgerQuorum: `2/1/1`
- failpointEvents: `1`

## Failpoint Events

| kind | logId | logFile | logical | physical | bytes | op | offset | realRc | match | trigger |
|---|---:|---|---:|---:|---:|---|---:|---:|---:|---:|
| ldpreload | 0 | `/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log` |  |  | 65536 | write | -1 | 65536 | 1 | 1 |

## Log Structure

| role | log | status | fileSize | headerMap | trueMap | delta | headerMapValid | entries | strict | prefix | post | parsedSize | mapSize | sizeMatch |
|---|---|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| bk1 | `0.log` | STRICT_CHECK | 196921 | 130778 | 196881 | 66103 | False | 128 | 128 | None | None | 85925 | 129750 | False |
| bk1 | `1.log` | SEALED_OK | 130864 | 130824 | 130824 | 0 | True | 211 | 211 | None | None | 129800 | 129800 | True |
| bk1 | `10.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk1 | `11.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk1 | `12.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk1 | `13.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk1 | `14.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk1 | `15.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk1 | `16.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk1 | `17.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk1 | `18.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk1 | `19.log` | SEALED_OK | 130684 | 130644 | 130644 | 0 | True | 217 | 217 | None | None | 129620 | 129620 | True |
| bk1 | `1a.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk1 | `1b.log` | UNSEALED_OK | 69419 | 0 | None | None | False | 116 | 116 | None | None | None | None | None |
| bk1 | `2.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk1 | `3.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk1 | `4.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk1 | `5.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk1 | `6.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk1 | `7.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk1 | `8.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk1 | `9.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk1 | `a.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk1 | `b.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk1 | `c.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk1 | `d.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk1 | `e.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk1 | `f.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk2 | `0.log` | SEALED_OK | 130671 | 130631 | 130631 | 0 | True | 200 | 200 | None | None | 129607 | 129607 | True |
| bk2 | `1.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk2 | `10.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk2 | `11.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk2 | `12.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk2 | `13.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk2 | `14.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk2 | `15.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk2 | `16.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk2 | `17.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk2 | `18.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk2 | `19.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk2 | `1a.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk2 | `1b.log` | UNSEALED_OK | 3949 | 0 | None | None | False | 5 | 5 | None | None | None | None | None |
| bk2 | `2.log` | SEALED_OK | 130621 | 130581 | 130581 | 0 | True | 216 | 216 | None | None | 129557 | 129557 | True |
| bk2 | `3.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk2 | `4.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk2 | `5.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk2 | `6.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk2 | `7.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk2 | `8.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk2 | `9.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk2 | `a.log` | SEALED_OK | 130621 | 130581 | 130581 | 0 | True | 216 | 216 | None | None | 129557 | 129557 | True |
| bk2 | `b.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk2 | `c.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk2 | `d.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk2 | `e.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk2 | `f.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |

## Replica Entry Comparison

Skipped: write quorum is smaller than ensemble size, so entries are intentionally single-copy distributed across bookies.

## Runtime Behavior

- clientExit: `0`

### bk1

| line | tag | log |
|---:|---|---|
| 135 | bookie-fault | `2026-07-31T18:47:56,651 - ERROR - [SyncThread-7-1:SyncThread@181] - Exception flushing ledgers` |
| 136 | bookie-fault | `java.io.IOException: Input/output error` |
| 134 | entrylog-io | `2026-07-31T18:47:55,657 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log for logId 0.` |
| 162 | entrylog-io | `2026-07-31T18:47:57,651 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log for logId 1.` |
| 163 | entrylog-io | `2026-07-31T18:47:57,651 - INFO  - [SyncThread-7-1:EntryLogManagerBase@165] - Flushing entry logger 0 back to filesystem, pending for syncing entry loggers : [BufferedChannel{logId=0, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log, ledgerIdAssigned=-1}].` |
| 164 | entrylog-io | `2026-07-31T18:47:57,666 - INFO  - [SyncThread-7-1:EntryLogManagerForSingleEntryLog@210] - Synced entry logger 0 to disk.` |
| 166 | entrylog-io | `2026-07-31T18:47:58,650 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/2.log for logId 2.` |
| 167 | entrylog-io | `2026-07-31T18:47:58,650 - INFO  - [SyncThread-7-1:EntryLogManagerBase@165] - Flushing entry logger 1 back to filesystem, pending for syncing entry loggers : [BufferedChannel{logId=1, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log, ledgerIdAssigned=-1}].` |
| 270 | bookie-lifecycle | `2026-07-31T18:48:24,918 - INFO  - [component-shutdown-thread:BookieServer@191] - Shutting down BookieServer` |
| 291 | bookie-lifecycle | `2026-07-31T18:48:24,949 - INFO  - [component-shutdown-thread:BookieImpl@861] - Turning bookie to read only during shut down` |
| 297 | bookie-lifecycle | `2026-07-31T18:48:24,964 - INFO  - [BookieJournal-3181:BookieImpl@828] - Triggering shutdown of Bookie-3181 with exitCode 5` |

### bk2

No matching log lines found.

### bk3

No matching log lines found.

### broker

| line | tag | log |
|---:|---|---|
| 33 | bk-client-init | `2026-07-31T18:47:52,002+0800 [main] INFO  org.apache.bookkeeper.meta.MetadataDrivers - BookKeeper metadata driver manager initialized` |
| 34 | bk-client-init | `2026-07-31T18:47:52,004+0800 [main] INFO  org.apache.pulsar.broker.BookKeeperClientFactoryImpl - Applying BookKeeper client configuration setting tlsHostnameVerificationEnabled=false` |
| 61 | bk-client-init | `2026-07-31T18:47:52,285+0800 [main] INFO  org.apache.pulsar.broker.BookKeeperClientFactoryImpl - Applying BookKeeper client configuration setting tlsHostnameVerificationEnabled=false` |
| 48 | bookie-discovery | `2026-07-31T18:47:52,124+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3181 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3181, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 49 | bookie-discovery | `2026-07-31T18:47:52,124+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3182 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3182, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 51 | bookie-discovery | `2026-07-31T18:47:52,130+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3181` |
| 53 | bookie-discovery | `2026-07-31T18:47:52,131+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3182` |
| 75 | bookie-discovery | `2026-07-31T18:47:52,298+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3181 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3181, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 76 | bookie-discovery | `2026-07-31T18:47:52,298+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3182 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3182, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 151 | bookie-channel | `2026-07-31T18:47:55,571+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3182 [id: 0x19405c76, L:/127.0.0.1:35910 - R:127.0.0.1/127.0.0.1:3182]` |
| 152 | bookie-channel | `2026-07-31T18:47:55,572+0800 [pulsar-io-3-2] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3182 [id: 0x033acfa1, L:/127.0.0.1:35972 - R:127.0.0.1/127.0.0.1:3182]` |
| 153 | bookie-channel | `2026-07-31T18:47:55,577+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0x19405c76, L:/127.0.0.1:35910 - R:127.0.0.1/127.0.0.1:3182] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 154 | bookie-channel | `2026-07-31T18:47:55,578+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3182 [id: 0xefd08297, L:/127.0.0.1:35912 - R:127.0.0.1/127.0.0.1:3182]` |
| 155 | bookie-channel | `2026-07-31T18:47:55,580+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0xefd08297, L:/127.0.0.1:35912 - R:127.0.0.1/127.0.0.1:3182] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 156 | bookie-channel | `2026-07-31T18:47:55,581+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3182 [id: 0x61c9ea69, L:/127.0.0.1:35914 - R:127.0.0.1/127.0.0.1:3182]` |
| 293 | managed-ledger | `2026-07-31T18:48:24,951+0800 [pulsar-service-shutdown] INFO  org.apache.bookkeeper.mledger.impl.ManagedLedgerImpl - [public/default/persistent/entrylog-ldpreload-round-01] Closing managed ledger` |
| 342 | managed-ledger | `2026-07-31T18:48:25,387+0800 [metadata-store-9-1] INFO  org.apache.bookkeeper.mledger.impl.ManagedLedgerFactoryImpl - Received MetadataStore session event: ConnectionLost` |
| 221 | broker-error | `2026-07-31T18:48:24,918+0800 [pulsar-io-3-1] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0xefd08297, L:/127.0.0.1:35912 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 222 | broker-error | `2026-07-31T18:48:24,919+0800 [pulsar-io-3-1] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x61c9ea69, L:/127.0.0.1:35914 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 223 | broker-error | `2026-07-31T18:48:24,918+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x403ee357, L:/127.0.0.1:35992 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 224 | broker-error | `2026-07-31T18:48:24,922+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x73c24398, L:/127.0.0.1:36010 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 225 | broker-error | `2026-07-31T18:48:24,922+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x4394108e, L:/127.0.0.1:36000 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 226 | broker-error | `2026-07-31T18:48:24,924+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x9b809358, L:/127.0.0.1:36034 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |

### client

| line | tag | log |
|---:|---|---|
| 66 | client-progress | `2026-07-31T18:48:04,841+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:    4665 msg ---    466.5 msg/s ---      1.8 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:   5.368 ms - med:   4.985 - 95pct:   7.623 - 99pct:  10.197 - 99.9pct:  38.978 - 99.99pct:  41.241 - Max:  41.241` |
| 67 | client-progress | `2026-07-31T18:48:14,850+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:    9680 msg ---    500.1 msg/s ---      2.0 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:   5.007 ms - med:   4.747 - 95pct:   6.823 - 99pct:   9.352 - 99.9pct:  26.459 - 99.99pct:  29.626 - Max:  31.725` |
| 72 | client-progress | `2026-07-31T18:48:24,855+0800 [Thread-0] INFO  org.apache.pulsar.testclient.PerformanceProducer - Aggregated throughput stats --- 12003 records sent --- 399.559 msg/s --- 1.561 Mbit/s ` |
| 73 | client-progress | `2026-07-31T18:48:24,872+0800 [Thread-0] INFO  org.apache.pulsar.testclient.PerformanceProducer - Aggregated latency stats --- Latency: mean:   5.104 ms - med:   4.808 - 95pct:   7.075 - 99pct:   9.637 - 99.9pct:  28.549 - 99.99pct:  40.779 - 99.999pct:  41.241 - Max:  41.241` |
| 68 | client-completion | `2026-07-31T18:48:19,487+0800 [pulsar-perf-producer-exec-1-1] INFO  org.apache.pulsar.testclient.PerformanceProducer - ------------- DONE (reached the maximum number: 12000 of production) --------------` |
| 74 | client-completion | `workload_rc=0` |
