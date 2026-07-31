# Entrylog Cluster Report

- clusterDir: `/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runs/stability-20260731-175938/round-01`
- pulsarVersion: `3.2.4`
- bookieVersion: `4.16.7`
- bookieCount: `3`
- managedLedgerQuorum: `3/3/2`
- failpointEvents: `1`

## Failpoint Events

| kind | logId | logFile | logical | physical | bytes | op | offset | realRc | match | trigger |
|---|---:|---|---:|---:|---:|---|---:|---:|---:|---:|
| ldpreload | 0 | `/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log` |  |  | 65536 | write | -1 | 65536 | 1 | 1 |

## Log Structure

| role | log | status | fileSize | headerMap | trueMap | delta | headerMapValid | entries | strict | prefix | post | parsedSize | mapSize | sizeMatch |
|---|---|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| bk1 | `0.log` | DRIFT_CHECK | 196604 | 130681 | 196564 | 65883 | False | 174 | None | 73 | 101 | 130769 | 129653 | False |
| bk1 | `1.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk1 | `10.log` | SEALED_OK | 130721 | 130681 | 130681 | 0 | True | 218 | 218 | None | None | 129657 | 129657 | True |
| bk1 | `11.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk1 | `12.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk1 | `13.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk1 | `14.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk1 | `15.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk1 | `16.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk1 | `17.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk1 | `18.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk1 | `19.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 212 | 212 | None | None | 129879 | 129879 | True |
| bk1 | `1a.log` | SEALED_OK | 130684 | 130644 | 130644 | 0 | True | 217 | 217 | None | None | 129620 | 129620 | True |
| bk1 | `1b.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk1 | `1c.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk1 | `1d.log` | SEALED_OK | 130684 | 130644 | 130644 | 0 | True | 217 | 217 | None | None | 129620 | 129620 | True |
| bk1 | `1e.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk1 | `1f.log` | SEALED_OK | 130521 | 130481 | 130481 | 0 | True | 214 | 214 | None | None | 129457 | 129457 | True |
| bk1 | `2.log` | SEALED_OK | 130089 | 130049 | 130049 | 0 | True | 199 | 199 | None | None | 129025 | 129025 | True |
| bk1 | `20.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk1 | `21.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk1 | `22.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk1 | `23.log` | SEALED_OK | 130608 | 130568 | 130568 | 0 | True | 216 | 216 | None | None | 129544 | 129544 | True |
| bk1 | `24.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk1 | `25.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk1 | `26.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk1 | `27.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk1 | `28.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk1 | `29.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk1 | `2a.log` | SEALED_OK | 130634 | 130594 | 130594 | 0 | True | 216 | 216 | None | None | 129570 | 129570 | True |
| bk1 | `2b.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk1 | `2c.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk1 | `2d.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk1 | `2e.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk1 | `2f.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk1 | `3.log` | SEALED_OK | 130715 | 130675 | 130675 | 0 | True | 182 | 182 | None | None | 129651 | 129651 | True |
| bk1 | `30.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk1 | `31.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk1 | `32.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk1 | `33.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk1 | `34.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk1 | `35.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk1 | `36.log` | UNSEALED_OK | 70004 | 0 | None | None | False | 117 | 117 | None | None | None | None | None |
| bk1 | `4.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk1 | `5.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk1 | `6.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk1 | `7.log` | SEALED_OK | 131093 | 131053 | 131053 | 0 | True | 215 | 215 | None | None | 130029 | 130029 | True |
| bk1 | `8.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk1 | `9.log` | SEALED_OK | 130671 | 130631 | 130631 | 0 | True | 217 | 217 | None | None | 129607 | 129607 | True |
| bk1 | `a.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk1 | `b.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk1 | `c.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk1 | `d.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk1 | `e.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk1 | `f.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk2 | `0.log` | SEALED_OK | 130927 | 130887 | 130887 | 0 | True | 159 | 159 | None | None | 129863 | 129863 | True |
| bk2 | `1.log` | SEALED_OK | 130584 | 130544 | 130544 | 0 | True | 215 | 215 | None | None | 129520 | 129520 | True |
| bk2 | `10.log` | SEALED_OK | 130721 | 130681 | 130681 | 0 | True | 218 | 218 | None | None | 129657 | 129657 | True |
| bk2 | `11.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk2 | `12.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk2 | `13.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk2 | `14.log` | SEALED_OK | 130684 | 130644 | 130644 | 0 | True | 217 | 217 | None | None | 129620 | 129620 | True |
| bk2 | `15.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk2 | `16.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk2 | `17.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk2 | `18.log` | SEALED_OK | 130621 | 130581 | 130581 | 0 | True | 216 | 216 | None | None | 129557 | 129557 | True |
| bk2 | `19.log` | SEALED_OK | 130571 | 130531 | 130531 | 0 | True | 215 | 215 | None | None | 129507 | 129507 | True |
| bk2 | `1a.log` | SEALED_OK | 130684 | 130644 | 130644 | 0 | True | 217 | 217 | None | None | 129620 | 129620 | True |
| bk2 | `1b.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk2 | `1c.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk2 | `1d.log` | SEALED_OK | 130684 | 130644 | 130644 | 0 | True | 217 | 217 | None | None | 129620 | 129620 | True |
| bk2 | `1e.log` | SEALED_OK | 130571 | 130531 | 130531 | 0 | True | 215 | 215 | None | None | 129507 | 129507 | True |
| bk2 | `1f.log` | SEALED_OK | 130684 | 130644 | 130644 | 0 | True | 217 | 217 | None | None | 129620 | 129620 | True |
| bk2 | `2.log` | SEALED_OK | 130684 | 130644 | 130644 | 0 | True | 217 | 217 | None | None | 129620 | 129620 | True |
| bk2 | `20.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk2 | `21.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk2 | `22.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk2 | `23.log` | SEALED_OK | 130608 | 130568 | 130568 | 0 | True | 216 | 216 | None | None | 129544 | 129544 | True |
| bk2 | `24.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk2 | `25.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk2 | `26.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk2 | `27.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk2 | `28.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk2 | `29.log` | SEALED_OK | 130634 | 130594 | 130594 | 0 | True | 216 | 216 | None | None | 129570 | 129570 | True |
| bk2 | `2a.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk2 | `2b.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk2 | `2c.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk2 | `2d.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk2 | `2e.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk2 | `2f.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk2 | `3.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk2 | `30.log` | SEALED_OK | 130684 | 130644 | 130644 | 0 | True | 217 | 217 | None | None | 129620 | 129620 | True |
| bk2 | `31.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk2 | `32.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk2 | `33.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk2 | `34.log` | SEALED_OK | 130684 | 130644 | 130644 | 0 | True | 217 | 217 | None | None | 129620 | 129620 | True |
| bk2 | `35.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk2 | `36.log` | UNSEALED_OK | 5704 | 0 | None | None | False | 8 | 8 | None | None | None | None | None |
| bk2 | `4.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk2 | `5.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk2 | `6.log` | SEALED_OK | 131093 | 131053 | 131053 | 0 | True | 215 | 215 | None | None | 130029 | 130029 | True |
| bk2 | `7.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk2 | `8.log` | SEALED_OK | 130671 | 130631 | 130631 | 0 | True | 217 | 217 | None | None | 129607 | 129607 | True |
| bk2 | `9.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk2 | `a.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk2 | `b.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk2 | `c.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk2 | `d.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk2 | `e.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk2 | `f.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk3 | `0.log` | SEALED_OK | 130927 | 130887 | 130887 | 0 | True | 159 | 159 | None | None | 129863 | 129863 | True |
| bk3 | `1.log` | SEALED_OK | 130584 | 130544 | 130544 | 0 | True | 215 | 215 | None | None | 129520 | 129520 | True |
| bk3 | `10.log` | SEALED_OK | 130721 | 130681 | 130681 | 0 | True | 218 | 218 | None | None | 129657 | 129657 | True |
| bk3 | `11.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk3 | `12.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk3 | `13.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk3 | `14.log` | SEALED_OK | 130684 | 130644 | 130644 | 0 | True | 217 | 217 | None | None | 129620 | 129620 | True |
| bk3 | `15.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk3 | `16.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk3 | `17.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk3 | `18.log` | SEALED_OK | 130621 | 130581 | 130581 | 0 | True | 216 | 216 | None | None | 129557 | 129557 | True |
| bk3 | `19.log` | SEALED_OK | 130571 | 130531 | 130531 | 0 | True | 215 | 215 | None | None | 129507 | 129507 | True |
| bk3 | `1a.log` | SEALED_OK | 130684 | 130644 | 130644 | 0 | True | 217 | 217 | None | None | 129620 | 129620 | True |
| bk3 | `1b.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk3 | `1c.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk3 | `1d.log` | SEALED_OK | 130684 | 130644 | 130644 | 0 | True | 217 | 217 | None | None | 129620 | 129620 | True |
| bk3 | `1e.log` | SEALED_OK | 130571 | 130531 | 130531 | 0 | True | 215 | 215 | None | None | 129507 | 129507 | True |
| bk3 | `1f.log` | SEALED_OK | 130684 | 130644 | 130644 | 0 | True | 217 | 217 | None | None | 129620 | 129620 | True |
| bk3 | `2.log` | SEALED_OK | 130684 | 130644 | 130644 | 0 | True | 217 | 217 | None | None | 129620 | 129620 | True |
| bk3 | `20.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk3 | `21.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk3 | `22.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk3 | `23.log` | SEALED_OK | 130608 | 130568 | 130568 | 0 | True | 216 | 216 | None | None | 129544 | 129544 | True |
| bk3 | `24.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk3 | `25.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk3 | `26.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk3 | `27.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk3 | `28.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk3 | `29.log` | SEALED_OK | 130634 | 130594 | 130594 | 0 | True | 216 | 216 | None | None | 129570 | 129570 | True |
| bk3 | `2a.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk3 | `2b.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk3 | `2c.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk3 | `2d.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk3 | `2e.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk3 | `2f.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk3 | `3.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk3 | `30.log` | SEALED_OK | 130684 | 130644 | 130644 | 0 | True | 217 | 217 | None | None | 129620 | 129620 | True |
| bk3 | `31.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk3 | `32.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk3 | `33.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk3 | `34.log` | SEALED_OK | 130684 | 130644 | 130644 | 0 | True | 217 | 217 | None | None | 129620 | 129620 | True |
| bk3 | `35.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk3 | `36.log` | UNSEALED_OK | 5704 | 0 | None | None | False | 8 | 8 | None | None | None | None | None |
| bk3 | `4.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk3 | `5.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk3 | `6.log` | SEALED_OK | 131093 | 131053 | 131053 | 0 | True | 215 | 215 | None | None | 130029 | 130029 | True |
| bk3 | `7.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk3 | `8.log` | SEALED_OK | 130671 | 130631 | 130631 | 0 | True | 217 | 217 | None | None | 129607 | 129607 | True |
| bk3 | `9.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk3 | `a.log` | SEALED_OK | 130734 | 130694 | 130694 | 0 | True | 218 | 218 | None | None | 129670 | 129670 | True |
| bk3 | `b.log` | SEALED_OK | 130784 | 130744 | 130744 | 0 | True | 219 | 219 | None | None | 129720 | 129720 | True |
| bk3 | `c.log` | SEALED_OK | 130934 | 130894 | 130894 | 0 | True | 222 | 222 | None | None | 129870 | 129870 | True |
| bk3 | `d.log` | SEALED_OK | 130884 | 130844 | 130844 | 0 | True | 221 | 221 | None | None | 129820 | 129820 | True |
| bk3 | `e.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |
| bk3 | `f.log` | SEALED_OK | 130834 | 130794 | 130794 | 0 | True | 220 | 220 | None | None | 129770 | 129770 | True |

## Replica Entry Comparison

| target | control | targetEntries | controlEntries | common | missingInTarget | missingInControl | hashMismatches |
|---|---|---:|---:|---:|---:|---:|---:|
| bk2 | bk3 | 11780 | 11780 | 11780 | 0 | 0 | 0 |
| bk1 | bk2 | 11780 | 11780 | 11780 | 0 | 0 | 0 |
| bk1 | bk3 | 11780 | 11780 | 11780 | 0 | 0 | 0 |

## Runtime Behavior

- clientExit: `0`

### bk1

| line | tag | log |
|---:|---|---|
| 133 | bookie-fault | `2026-07-31T17:59:53,395 - ERROR - [SyncThread-7-1:SyncThread@181] - Exception flushing ledgers` |
| 134 | bookie-fault | `java.io.IOException: Input/output error` |
| 132 | entrylog-io | `2026-07-31T17:59:53,388 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log for logId 0.` |
| 160 | entrylog-io | `2026-07-31T17:59:54,377 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log for logId 1.` |
| 161 | entrylog-io | `2026-07-31T17:59:54,377 - INFO  - [SyncThread-7-1:EntryLogManagerBase@165] - Flushing entry logger 0 back to filesystem, pending for syncing entry loggers : [BufferedChannel{logId=0, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log, ledgerIdAssigned=-1}].` |
| 163 | entrylog-io | `2026-07-31T17:59:54,378 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/2.log for logId 2.` |
| 164 | entrylog-io | `2026-07-31T17:59:54,379 - INFO  - [SyncThread-7-1:EntryLogManagerBase@165] - Flushing entry logger 1 back to filesystem, pending for syncing entry loggers : [BufferedChannel{logId=0, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log, ledgerIdAssigned=-1}, BufferedChannel{logId=1, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log, ledgerIdAssigned=-1}].` |
| 165 | entrylog-io | `2026-07-31T17:59:54,396 - INFO  - [SyncThread-7-1:EntryLogManagerForSingleEntryLog@210] - Synced entry logger 0 to disk.` |
| 376 | bookie-lifecycle | `2026-07-31T18:00:22,531 - INFO  - [component-shutdown-thread:BookieServer@191] - Shutting down BookieServer` |
| 397 | bookie-lifecycle | `2026-07-31T18:00:22,561 - INFO  - [component-shutdown-thread:BookieImpl@861] - Turning bookie to read only during shut down` |
| 403 | bookie-lifecycle | `2026-07-31T18:00:22,578 - INFO  - [BookieJournal-3181:BookieImpl@828] - Triggering shutdown of Bookie-3181 with exitCode 5` |

### bk2

No matching log lines found.

### bk3

No matching log lines found.

### broker

| line | tag | log |
|---:|---|---|
| 33 | bk-client-init | `2026-07-31T17:59:49,496+0800 [main] INFO  org.apache.bookkeeper.meta.MetadataDrivers - BookKeeper metadata driver manager initialized` |
| 34 | bk-client-init | `2026-07-31T17:59:49,498+0800 [main] INFO  org.apache.pulsar.broker.BookKeeperClientFactoryImpl - Applying BookKeeper client configuration setting tlsHostnameVerificationEnabled=false` |
| 64 | bk-client-init | `2026-07-31T17:59:49,781+0800 [main] INFO  org.apache.pulsar.broker.BookKeeperClientFactoryImpl - Applying BookKeeper client configuration setting tlsHostnameVerificationEnabled=false` |
| 48 | bookie-discovery | `2026-07-31T17:59:49,626+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3181 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3181, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 49 | bookie-discovery | `2026-07-31T17:59:49,626+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3182 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3182, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 50 | bookie-discovery | `2026-07-31T17:59:49,627+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3183 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3183, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 52 | bookie-discovery | `2026-07-31T17:59:49,633+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3181` |
| 54 | bookie-discovery | `2026-07-31T17:59:49,634+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3182` |
| 56 | bookie-discovery | `2026-07-31T17:59:49,634+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3183` |
| 157 | bookie-channel | `2026-07-31T17:59:53,111+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3183 [id: 0xf93f4de1, L:/127.0.0.1:43412 - R:127.0.0.1/127.0.0.1:3183]` |
| 158 | bookie-channel | `2026-07-31T17:59:53,112+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0xf93f4de1, L:/127.0.0.1:43412 - R:127.0.0.1/127.0.0.1:3183] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 159 | bookie-channel | `2026-07-31T17:59:53,113+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3183 [id: 0x720ea714, L:/127.0.0.1:43418 - R:127.0.0.1/127.0.0.1:3183]` |
| 160 | bookie-channel | `2026-07-31T17:59:53,113+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0x720ea714, L:/127.0.0.1:43418 - R:127.0.0.1/127.0.0.1:3183] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 161 | bookie-channel | `2026-07-31T17:59:53,113+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3183 [id: 0x28a8dec0, L:/127.0.0.1:43426 - R:127.0.0.1/127.0.0.1:3183]` |
| 162 | bookie-channel | `2026-07-31T17:59:53,113+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0x28a8dec0, L:/127.0.0.1:43426 - R:127.0.0.1/127.0.0.1:3183] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 388 | managed-ledger | `2026-07-31T18:00:22,992+0800 [metadata-store-9-1] INFO  org.apache.bookkeeper.mledger.impl.ManagedLedgerFactoryImpl - Received MetadataStore session event: ConnectionLost` |
| 259 | broker-error | `2026-07-31T18:00:22,520+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x2cff1596, L:/127.0.0.1:43336 - R:127.0.0.1/127.0.0.1:3183] cause: recvAddress(..) failed: Connection reset by peer` |
| 260 | broker-error | `2026-07-31T18:00:22,522+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0xd231fd26, L:/127.0.0.1:43404 - R:127.0.0.1/127.0.0.1:3183] cause: recvAddress(..) failed: Connection reset by peer` |
| 261 | broker-error | `2026-07-31T18:00:22,522+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x0b1ffc40, L:/127.0.0.1:43326 - R:127.0.0.1/127.0.0.1:3183] cause: recvAddress(..) failed: Connection reset by peer` |
| 262 | broker-error | `2026-07-31T18:00:22,522+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0xc72ad120, L:/127.0.0.1:43388 - R:127.0.0.1/127.0.0.1:3183] cause: recvAddress(..) failed: Connection reset by peer` |
| 263 | broker-error | `2026-07-31T18:00:22,522+0800 [pulsar-io-3-2] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Disconnected from bookie channel [id: 0x2cff1596, L:/127.0.0.1:43336 ! R:127.0.0.1/127.0.0.1:3183]` |
| 264 | broker-error | `2026-07-31T18:00:22,524+0800 [pulsar-io-3-1] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x720ea714, L:/127.0.0.1:43418 - R:127.0.0.1/127.0.0.1:3183] cause: recvAddress(..) failed: Connection reset by peer` |

### client

| line | tag | log |
|---:|---|---|
| 66 | client-progress | `2026-07-31T18:00:02,439+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:    4690 msg ---    469.0 msg/s ---      1.8 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:   6.400 ms - med:   6.064 - 95pct:   9.776 - 99pct:  14.778 - 99.9pct:  43.961 - 99.99pct:  46.752 - Max:  46.752` |
| 67 | client-progress | `2026-07-31T18:00:12,452+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:    9711 msg ---    500.2 msg/s ---      2.0 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:   5.795 ms - med:   5.632 - 95pct:   8.833 - 99pct:  12.736 - 99.9pct:  23.367 - 99.99pct:  28.688 - Max:  29.588` |
| 72 | client-progress | `2026-07-31T18:00:22,458+0800 [Thread-0] INFO  org.apache.pulsar.testclient.PerformanceProducer - Aggregated throughput stats --- 12004 records sent --- 399.448 msg/s --- 1.560 Mbit/s ` |
| 73 | client-progress | `2026-07-31T18:00:22,479+0800 [Thread-0] INFO  org.apache.pulsar.testclient.PerformanceProducer - Aggregated latency stats --- Latency: mean:   5.976 ms - med:   5.762 - 95pct:   9.061 - 99pct:  12.769 - 99.9pct:  29.588 - 99.99pct:  46.120 - 99.999pct:  46.752 - Max:  46.752` |
| 68 | client-completion | `2026-07-31T18:00:17,027+0800 [pulsar-perf-producer-exec-1-1] INFO  org.apache.pulsar.testclient.PerformanceProducer - ------------- DONE (reached the maximum number: 12000 of production) --------------` |
| 74 | client-completion | `workload_rc=0` |
