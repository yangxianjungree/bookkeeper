# Entrylog Cluster Report

- clusterDir: `/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runs/stability-20260731-175938/round-04`
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
| bk1 | `0.log` | DRIFT_CHECK | 196520 | 130867 | 196480 | 65613 | False | 224 | None | 88 | 136 | 130296 | 129839 | False |
| bk1 | `1.log` | SEALED_OK | 130727 | 130687 | 130687 | 0 | True | 266 | 266 | None | None | 129663 | 129663 | True |
| bk1 | `10.log` | SEALED_OK | 131059 | 131019 | 131019 | 0 | True | 280 | 280 | None | None | 129995 | 129995 | True |
| bk1 | `11.log` | SEALED_OK | 130909 | 130869 | 130869 | 0 | True | 277 | 277 | None | None | 129845 | 129845 | True |
| bk1 | `12.log` | SEALED_OK | 130759 | 130719 | 130719 | 0 | True | 274 | 274 | None | None | 129695 | 129695 | True |
| bk1 | `13.log` | SEALED_OK | 131009 | 130969 | 130969 | 0 | True | 279 | 279 | None | None | 129945 | 129945 | True |
| bk1 | `14.log` | SEALED_OK | 131078 | 131038 | 131038 | 0 | True | 257 | 257 | None | None | 130014 | 130014 | True |
| bk1 | `15.log` | SEALED_OK | 131077 | 131037 | 131037 | 0 | True | 273 | 273 | None | None | 130013 | 130013 | True |
| bk1 | `16.log` | SEALED_OK | 131009 | 130969 | 130969 | 0 | True | 279 | 279 | None | None | 129945 | 129945 | True |
| bk1 | `17.log` | SEALED_OK | 130916 | 130876 | 130876 | 0 | True | 269 | 269 | None | None | 129852 | 129852 | True |
| bk1 | `18.log` | SEALED_OK | 130859 | 130819 | 130819 | 0 | True | 276 | 276 | None | None | 129795 | 129795 | True |
| bk1 | `19.log` | SEALED_OK | 130459 | 130419 | 130419 | 0 | True | 268 | 268 | None | None | 129395 | 129395 | True |
| bk1 | `1a.log` | SEALED_OK | 130759 | 130719 | 130719 | 0 | True | 274 | 274 | None | None | 129695 | 129695 | True |
| bk1 | `1b.log` | SEALED_OK | 130909 | 130869 | 130869 | 0 | True | 277 | 277 | None | None | 129845 | 129845 | True |
| bk1 | `1c.log` | SEALED_OK | 131009 | 130969 | 130969 | 0 | True | 279 | 279 | None | None | 129945 | 129945 | True |
| bk1 | `1d.log` | SEALED_OK | 130909 | 130869 | 130869 | 0 | True | 277 | 277 | None | None | 129845 | 129845 | True |
| bk1 | `1e.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk1 | `1f.log` | SEALED_OK | 130966 | 130926 | 130926 | 0 | True | 270 | 270 | None | None | 129902 | 129902 | True |
| bk1 | `2.log` | SEALED_OK | 131093 | 131053 | 131053 | 0 | True | 240 | 240 | None | None | 130029 | 130029 | True |
| bk1 | `20.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk1 | `21.log` | SEALED_OK | 130816 | 130776 | 130776 | 0 | True | 267 | 267 | None | None | 129752 | 129752 | True |
| bk1 | `22.log` | SEALED_OK | 131016 | 130976 | 130976 | 0 | True | 271 | 271 | None | None | 129952 | 129952 | True |
| bk1 | `23.log` | SEALED_OK | 130859 | 130819 | 130819 | 0 | True | 276 | 276 | None | None | 129795 | 129795 | True |
| bk1 | `24.log` | SEALED_OK | 130916 | 130876 | 130876 | 0 | True | 269 | 269 | None | None | 129852 | 129852 | True |
| bk1 | `25.log` | SEALED_OK | 130866 | 130826 | 130826 | 0 | True | 268 | 268 | None | None | 129802 | 129802 | True |
| bk1 | `26.log` | SEALED_OK | 131016 | 130976 | 130976 | 0 | True | 271 | 271 | None | None | 129952 | 129952 | True |
| bk1 | `27.log` | SEALED_OK | 130709 | 130669 | 130669 | 0 | True | 273 | 273 | None | None | 129645 | 129645 | True |
| bk1 | `28.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk1 | `29.log` | SEALED_OK | 130916 | 130876 | 130876 | 0 | True | 269 | 269 | None | None | 129852 | 129852 | True |
| bk1 | `2a.log` | SEALED_OK | 130916 | 130876 | 130876 | 0 | True | 269 | 269 | None | None | 129852 | 129852 | True |
| bk1 | `2b.log` | SEALED_OK | 131066 | 131026 | 131026 | 0 | True | 272 | 272 | None | None | 130002 | 130002 | True |
| bk1 | `2c.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk1 | `2d.log` | SEALED_OK | 130709 | 130669 | 130669 | 0 | True | 273 | 273 | None | None | 129645 | 129645 | True |
| bk1 | `2e.log` | SEALED_OK | 131016 | 130976 | 130976 | 0 | True | 271 | 271 | None | None | 129952 | 129952 | True |
| bk1 | `2f.log` | SEALED_OK | 130759 | 130719 | 130719 | 0 | True | 274 | 274 | None | None | 129695 | 129695 | True |
| bk1 | `3.log` | SEALED_OK | 130745 | 130705 | 130705 | 0 | True | 229 | 229 | None | None | 129681 | 129681 | True |
| bk1 | `30.log` | SEALED_OK | 130659 | 130619 | 130619 | 0 | True | 272 | 272 | None | None | 129595 | 129595 | True |
| bk1 | `31.log` | SEALED_OK | 130909 | 130869 | 130869 | 0 | True | 277 | 277 | None | None | 129845 | 129845 | True |
| bk1 | `32.log` | SEALED_OK | 130702 | 130662 | 130662 | 0 | True | 281 | 281 | None | None | 129638 | 129638 | True |
| bk1 | `33.log` | SEALED_OK | 131009 | 130969 | 130969 | 0 | True | 279 | 279 | None | None | 129945 | 129945 | True |
| bk1 | `34.log` | SEALED_OK | 130859 | 130819 | 130819 | 0 | True | 276 | 276 | None | None | 129795 | 129795 | True |
| bk1 | `35.log` | SEALED_OK | 130759 | 130719 | 130719 | 0 | True | 274 | 274 | None | None | 129695 | 129695 | True |
| bk1 | `36.log` | SEALED_OK | 131009 | 130969 | 130969 | 0 | True | 279 | 279 | None | None | 129945 | 129945 | True |
| bk1 | `37.log` | SEALED_OK | 130359 | 130319 | 130319 | 0 | True | 266 | 266 | None | None | 129295 | 129295 | True |
| bk1 | `38.log` | SEALED_OK | 130709 | 130669 | 130669 | 0 | True | 273 | 273 | None | None | 129645 | 129645 | True |
| bk1 | `39.log` | SEALED_OK | 130686 | 130646 | 130646 | 0 | True | 280 | 280 | None | None | 129622 | 129622 | True |
| bk1 | `3a.log` | SEALED_OK | 130970 | 130930 | 130930 | 0 | True | 272 | 272 | None | None | 129906 | 129906 | True |
| bk1 | `3b.log` | SEALED_OK | 130896 | 130856 | 130856 | 0 | True | 279 | 279 | None | None | 129832 | 129832 | True |
| bk1 | `3c.log` | SEALED_OK | 130970 | 130930 | 130930 | 0 | True | 272 | 272 | None | None | 129906 | 129906 | True |
| bk1 | `3d.log` | SEALED_OK | 131018 | 130978 | 130978 | 0 | True | 273 | 273 | None | None | 129954 | 129954 | True |
| bk1 | `3e.log` | SEALED_OK | 130874 | 130834 | 130834 | 0 | True | 270 | 270 | None | None | 129810 | 129810 | True |
| bk1 | `3f.log` | SEALED_OK | 131051 | 131011 | 131011 | 0 | True | 274 | 274 | None | None | 129987 | 129987 | True |
| bk1 | `4.log` | SEALED_OK | 131003 | 130963 | 130963 | 0 | True | 271 | 271 | None | None | 129939 | 129939 | True |
| bk1 | `40.log` | SEALED_OK | 130970 | 130930 | 130930 | 0 | True | 272 | 272 | None | None | 129906 | 129906 | True |
| bk1 | `41.log` | SEALED_OK | 130656 | 130616 | 130616 | 0 | True | 274 | 274 | None | None | 129592 | 129592 | True |
| bk1 | `42.log` | SEALED_OK | 130970 | 130930 | 130930 | 0 | True | 272 | 272 | None | None | 129906 | 129906 | True |
| bk1 | `43.log` | SEALED_OK | 130752 | 130712 | 130712 | 0 | True | 276 | 276 | None | None | 129688 | 129688 | True |
| bk1 | `44.log` | SEALED_OK | 130970 | 130930 | 130930 | 0 | True | 272 | 272 | None | None | 129906 | 129906 | True |
| bk1 | `45.log` | SEALED_OK | 130826 | 130786 | 130786 | 0 | True | 269 | 269 | None | None | 129762 | 129762 | True |
| bk1 | `46.log` | SEALED_OK | 130874 | 130834 | 130834 | 0 | True | 270 | 270 | None | None | 129810 | 129810 | True |
| bk1 | `47.log` | SEALED_OK | 131066 | 131026 | 131026 | 0 | True | 274 | 274 | None | None | 130002 | 130002 | True |
| bk1 | `48.log` | SEALED_OK | 130656 | 130616 | 130616 | 0 | True | 274 | 274 | None | None | 129592 | 129592 | True |
| bk1 | `49.log` | SEALED_OK | 130826 | 130786 | 130786 | 0 | True | 269 | 269 | None | None | 129762 | 129762 | True |
| bk1 | `4a.log` | SEALED_OK | 130656 | 130616 | 130616 | 0 | True | 274 | 274 | None | None | 129592 | 129592 | True |
| bk1 | `4b.log` | SEALED_OK | 130922 | 130882 | 130882 | 0 | True | 271 | 271 | None | None | 129858 | 129858 | True |
| bk1 | `4c.log` | SEALED_OK | 130970 | 130930 | 130930 | 0 | True | 272 | 272 | None | None | 129906 | 129906 | True |
| bk1 | `4d.log` | SEALED_OK | 131018 | 130978 | 130978 | 0 | True | 273 | 273 | None | None | 129954 | 129954 | True |
| bk1 | `4e.log` | SEALED_OK | 130922 | 130882 | 130882 | 0 | True | 271 | 271 | None | None | 129858 | 129858 | True |
| bk1 | `4f.log` | SEALED_OK | 130922 | 130882 | 130882 | 0 | True | 271 | 271 | None | None | 129858 | 129858 | True |
| bk1 | `5.log` | SEALED_OK | 131059 | 131019 | 131019 | 0 | True | 280 | 280 | None | None | 129995 | 129995 | True |
| bk1 | `50.log` | SEALED_OK | 130874 | 130834 | 130834 | 0 | True | 270 | 270 | None | None | 129810 | 129810 | True |
| bk1 | `51.log` | SEALED_OK | 130896 | 130856 | 130856 | 0 | True | 279 | 279 | None | None | 129832 | 129832 | True |
| bk1 | `52.log` | SEALED_OK | 130752 | 130712 | 130712 | 0 | True | 276 | 276 | None | None | 129688 | 129688 | True |
| bk1 | `53.log` | SEALED_OK | 131051 | 131011 | 131011 | 0 | True | 274 | 274 | None | None | 129987 | 129987 | True |
| bk1 | `54.log` | UNSEALED_OK | 84816 | 0 | None | None | False | 174 | 174 | None | None | None | None | None |
| bk1 | `6.log` | SEALED_OK | 130914 | 130874 | 130874 | 0 | True | 270 | 270 | None | None | 129850 | 129850 | True |
| bk1 | `7.log` | SEALED_OK | 130759 | 130719 | 130719 | 0 | True | 274 | 274 | None | None | 129695 | 129695 | True |
| bk1 | `8.log` | SEALED_OK | 131103 | 131063 | 131063 | 0 | True | 273 | 273 | None | None | 130039 | 130039 | True |
| bk1 | `9.log` | SEALED_OK | 130696 | 130656 | 130656 | 0 | True | 273 | 273 | None | None | 129632 | 129632 | True |
| bk1 | `a.log` | SEALED_OK | 130502 | 130462 | 130462 | 0 | True | 277 | 277 | None | None | 129438 | 129438 | True |
| bk1 | `b.log` | SEALED_OK | 130659 | 130619 | 130619 | 0 | True | 272 | 272 | None | None | 129595 | 129595 | True |
| bk1 | `c.log` | SEALED_OK | 131059 | 131019 | 131019 | 0 | True | 280 | 280 | None | None | 129995 | 129995 | True |
| bk1 | `d.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk1 | `e.log` | SEALED_OK | 130703 | 130663 | 130663 | 0 | True | 265 | 265 | None | None | 129639 | 129639 | True |
| bk1 | `f.log` | SEALED_OK | 130659 | 130619 | 130619 | 0 | True | 272 | 272 | None | None | 129595 | 129595 | True |
| bk2 | `0.log` | SEALED_OK | 130715 | 130675 | 130675 | 0 | True | 204 | 204 | None | None | 129651 | 129651 | True |
| bk2 | `1.log` | SEALED_OK | 130860 | 130820 | 130820 | 0 | True | 260 | 260 | None | None | 129796 | 129796 | True |
| bk2 | `10.log` | SEALED_OK | 131059 | 131019 | 131019 | 0 | True | 280 | 280 | None | None | 129995 | 129995 | True |
| bk2 | `11.log` | SEALED_OK | 130659 | 130619 | 130619 | 0 | True | 272 | 272 | None | None | 129595 | 129595 | True |
| bk2 | `12.log` | SEALED_OK | 131059 | 131019 | 131019 | 0 | True | 280 | 280 | None | None | 129995 | 129995 | True |
| bk2 | `13.log` | SEALED_OK | 130777 | 130737 | 130737 | 0 | True | 267 | 267 | None | None | 129713 | 129713 | True |
| bk2 | `14.log` | SEALED_OK | 130120 | 130080 | 130080 | 0 | True | 262 | 262 | None | None | 129056 | 129056 | True |
| bk2 | `15.log` | SEALED_OK | 130846 | 130806 | 130806 | 0 | True | 276 | 276 | None | None | 129782 | 129782 | True |
| bk2 | `16.log` | SEALED_OK | 131016 | 130976 | 130976 | 0 | True | 271 | 271 | None | None | 129952 | 129952 | True |
| bk2 | `17.log` | SEALED_OK | 130859 | 130819 | 130819 | 0 | True | 276 | 276 | None | None | 129795 | 129795 | True |
| bk2 | `18.log` | SEALED_OK | 130709 | 130669 | 130669 | 0 | True | 273 | 273 | None | None | 129645 | 129645 | True |
| bk2 | `19.log` | SEALED_OK | 130866 | 130826 | 130826 | 0 | True | 268 | 268 | None | None | 129802 | 129802 | True |
| bk2 | `1a.log` | SEALED_OK | 130959 | 130919 | 130919 | 0 | True | 278 | 278 | None | None | 129895 | 129895 | True |
| bk2 | `1b.log` | SEALED_OK | 131009 | 130969 | 130969 | 0 | True | 279 | 279 | None | None | 129945 | 129945 | True |
| bk2 | `1c.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk2 | `1d.log` | SEALED_OK | 130859 | 130819 | 130819 | 0 | True | 276 | 276 | None | None | 129795 | 129795 | True |
| bk2 | `1e.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk2 | `1f.log` | SEALED_OK | 130609 | 130569 | 130569 | 0 | True | 271 | 271 | None | None | 129545 | 129545 | True |
| bk2 | `2.log` | SEALED_OK | 130677 | 130637 | 130637 | 0 | True | 265 | 265 | None | None | 129613 | 129613 | True |
| bk2 | `20.log` | SEALED_OK | 130966 | 130926 | 130926 | 0 | True | 270 | 270 | None | None | 129902 | 129902 | True |
| bk2 | `21.log` | SEALED_OK | 131016 | 130976 | 130976 | 0 | True | 271 | 271 | None | None | 129952 | 129952 | True |
| bk2 | `22.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk2 | `23.log` | SEALED_OK | 130459 | 130419 | 130419 | 0 | True | 268 | 268 | None | None | 129395 | 129395 | True |
| bk2 | `24.log` | SEALED_OK | 130866 | 130826 | 130826 | 0 | True | 268 | 268 | None | None | 129802 | 129802 | True |
| bk2 | `25.log` | SEALED_OK | 130966 | 130926 | 130926 | 0 | True | 270 | 270 | None | None | 129902 | 129902 | True |
| bk2 | `26.log` | SEALED_OK | 131016 | 130976 | 130976 | 0 | True | 271 | 271 | None | None | 129952 | 129952 | True |
| bk2 | `27.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk2 | `28.log` | SEALED_OK | 130709 | 130669 | 130669 | 0 | True | 273 | 273 | None | None | 129645 | 129645 | True |
| bk2 | `29.log` | SEALED_OK | 130966 | 130926 | 130926 | 0 | True | 270 | 270 | None | None | 129902 | 129902 | True |
| bk2 | `2a.log` | SEALED_OK | 130866 | 130826 | 130826 | 0 | True | 268 | 268 | None | None | 129802 | 129802 | True |
| bk2 | `2b.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk2 | `2c.log` | SEALED_OK | 130659 | 130619 | 130619 | 0 | True | 272 | 272 | None | None | 129595 | 129595 | True |
| bk2 | `2d.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk2 | `2e.log` | SEALED_OK | 131066 | 131026 | 131026 | 0 | True | 272 | 272 | None | None | 130002 | 130002 | True |
| bk2 | `2f.log` | SEALED_OK | 130659 | 130619 | 130619 | 0 | True | 272 | 272 | None | None | 129595 | 129595 | True |
| bk2 | `3.log` | SEALED_OK | 130352 | 130312 | 130312 | 0 | True | 274 | 274 | None | None | 129288 | 129288 | True |
| bk2 | `30.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk2 | `31.log` | SEALED_OK | 131009 | 130969 | 130969 | 0 | True | 279 | 279 | None | None | 129945 | 129945 | True |
| bk2 | `32.log` | SEALED_OK | 130702 | 130662 | 130662 | 0 | True | 281 | 281 | None | None | 129638 | 129638 | True |
| bk2 | `33.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk2 | `34.log` | SEALED_OK | 130452 | 130412 | 130412 | 0 | True | 276 | 276 | None | None | 129388 | 129388 | True |
| bk2 | `35.log` | SEALED_OK | 130959 | 130919 | 130919 | 0 | True | 278 | 278 | None | None | 129895 | 129895 | True |
| bk2 | `36.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk2 | `37.log` | SEALED_OK | 131023 | 130983 | 130983 | 0 | True | 263 | 263 | None | None | 129959 | 129959 | True |
| bk2 | `38.log` | SEALED_OK | 131059 | 131019 | 131019 | 0 | True | 280 | 280 | None | None | 129995 | 129995 | True |
| bk2 | `39.log` | SEALED_OK | 130780 | 130740 | 130740 | 0 | True | 279 | 279 | None | None | 129716 | 129716 | True |
| bk2 | `3a.log` | SEALED_OK | 130922 | 130882 | 130882 | 0 | True | 271 | 271 | None | None | 129858 | 129858 | True |
| bk2 | `3b.log` | SEALED_OK | 130848 | 130808 | 130808 | 0 | True | 278 | 278 | None | None | 129784 | 129784 | True |
| bk2 | `3c.log` | SEALED_OK | 130922 | 130882 | 130882 | 0 | True | 271 | 271 | None | None | 129858 | 129858 | True |
| bk2 | `3d.log` | SEALED_OK | 130970 | 130930 | 130930 | 0 | True | 272 | 272 | None | None | 129906 | 129906 | True |
| bk2 | `3e.log` | SEALED_OK | 130907 | 130867 | 130867 | 0 | True | 271 | 271 | None | None | 129843 | 129843 | True |
| bk2 | `3f.log` | SEALED_OK | 131066 | 131026 | 131026 | 0 | True | 274 | 274 | None | None | 130002 | 130002 | True |
| bk2 | `4.log` | SEALED_OK | 130909 | 130869 | 130869 | 0 | True | 277 | 277 | None | None | 129845 | 129845 | True |
| bk2 | `40.log` | SEALED_OK | 130656 | 130616 | 130616 | 0 | True | 274 | 274 | None | None | 129592 | 129592 | True |
| bk2 | `41.log` | SEALED_OK | 130922 | 130882 | 130882 | 0 | True | 271 | 271 | None | None | 129858 | 129858 | True |
| bk2 | `42.log` | SEALED_OK | 130704 | 130664 | 130664 | 0 | True | 275 | 275 | None | None | 129640 | 129640 | True |
| bk2 | `43.log` | SEALED_OK | 130656 | 130616 | 130616 | 0 | True | 274 | 274 | None | None | 129592 | 129592 | True |
| bk2 | `44.log` | SEALED_OK | 130874 | 130834 | 130834 | 0 | True | 270 | 270 | None | None | 129810 | 129810 | True |
| bk2 | `45.log` | SEALED_OK | 130778 | 130738 | 130738 | 0 | True | 268 | 268 | None | None | 129714 | 129714 | True |
| bk2 | `46.log` | SEALED_OK | 130826 | 130786 | 130786 | 0 | True | 269 | 269 | None | None | 129762 | 129762 | True |
| bk2 | `47.log` | SEALED_OK | 130848 | 130808 | 130808 | 0 | True | 278 | 278 | None | None | 129784 | 129784 | True |
| bk2 | `48.log` | SEALED_OK | 130970 | 130930 | 130930 | 0 | True | 272 | 272 | None | None | 129906 | 129906 | True |
| bk2 | `49.log` | SEALED_OK | 130922 | 130882 | 130882 | 0 | True | 271 | 271 | None | None | 129858 | 129858 | True |
| bk2 | `4a.log` | SEALED_OK | 131018 | 130978 | 130978 | 0 | True | 273 | 273 | None | None | 129954 | 129954 | True |
| bk2 | `4b.log` | SEALED_OK | 131018 | 130978 | 130978 | 0 | True | 273 | 273 | None | None | 129954 | 129954 | True |
| bk2 | `4c.log` | SEALED_OK | 130922 | 130882 | 130882 | 0 | True | 271 | 271 | None | None | 129858 | 129858 | True |
| bk2 | `4d.log` | SEALED_OK | 130874 | 130834 | 130834 | 0 | True | 270 | 270 | None | None | 129810 | 129810 | True |
| bk2 | `4e.log` | SEALED_OK | 131018 | 130978 | 130978 | 0 | True | 273 | 273 | None | None | 129954 | 129954 | True |
| bk2 | `4f.log` | SEALED_OK | 130874 | 130834 | 130834 | 0 | True | 270 | 270 | None | None | 129810 | 129810 | True |
| bk2 | `5.log` | SEALED_OK | 130877 | 130837 | 130837 | 0 | True | 269 | 269 | None | None | 129813 | 129813 | True |
| bk2 | `50.log` | SEALED_OK | 130704 | 130664 | 130664 | 0 | True | 275 | 275 | None | None | 129640 | 129640 | True |
| bk2 | `51.log` | SEALED_OK | 130848 | 130808 | 130808 | 0 | True | 278 | 278 | None | None | 129784 | 129784 | True |
| bk2 | `52.log` | SEALED_OK | 130656 | 130616 | 130616 | 0 | True | 274 | 274 | None | None | 129592 | 129592 | True |
| bk2 | `53.log` | SEALED_OK | 131051 | 131011 | 131011 | 0 | True | 274 | 274 | None | None | 129987 | 129987 | True |
| bk2 | `54.log` | UNSEALED_OK | 22310 | 0 | None | None | False | 42 | 42 | None | None | None | None | None |
| bk2 | `6.log` | SEALED_OK | 130796 | 130756 | 130756 | 0 | True | 275 | 275 | None | None | 129732 | 129732 | True |
| bk2 | `7.log` | SEALED_OK | 130859 | 130819 | 130819 | 0 | True | 276 | 276 | None | None | 129795 | 129795 | True |
| bk2 | `8.log` | SEALED_OK | 130940 | 130900 | 130900 | 0 | True | 270 | 270 | None | None | 129876 | 129876 | True |
| bk2 | `9.log` | SEALED_OK | 131009 | 130969 | 130969 | 0 | True | 279 | 279 | None | None | 129945 | 129945 | True |
| bk2 | `a.log` | SEALED_OK | 130659 | 130619 | 130619 | 0 | True | 272 | 272 | None | None | 129595 | 129595 | True |
| bk2 | `b.log` | SEALED_OK | 131009 | 130969 | 130969 | 0 | True | 279 | 279 | None | None | 129945 | 129945 | True |
| bk2 | `c.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk2 | `d.log` | SEALED_OK | 131003 | 130963 | 130963 | 0 | True | 271 | 271 | None | None | 129939 | 129939 | True |
| bk2 | `e.log` | SEALED_OK | 130966 | 130926 | 130926 | 0 | True | 270 | 270 | None | None | 129902 | 129902 | True |
| bk2 | `f.log` | SEALED_OK | 130859 | 130819 | 130819 | 0 | True | 276 | 276 | None | None | 129795 | 129795 | True |
| bk3 | `0.log` | SEALED_OK | 130715 | 130675 | 130675 | 0 | True | 204 | 204 | None | None | 129651 | 129651 | True |
| bk3 | `1.log` | SEALED_OK | 130860 | 130820 | 130820 | 0 | True | 260 | 260 | None | None | 129796 | 129796 | True |
| bk3 | `10.log` | SEALED_OK | 131059 | 131019 | 131019 | 0 | True | 280 | 280 | None | None | 129995 | 129995 | True |
| bk3 | `11.log` | SEALED_OK | 130659 | 130619 | 130619 | 0 | True | 272 | 272 | None | None | 129595 | 129595 | True |
| bk3 | `12.log` | SEALED_OK | 131059 | 131019 | 131019 | 0 | True | 280 | 280 | None | None | 129995 | 129995 | True |
| bk3 | `13.log` | SEALED_OK | 130777 | 130737 | 130737 | 0 | True | 267 | 267 | None | None | 129713 | 129713 | True |
| bk3 | `14.log` | SEALED_OK | 130120 | 130080 | 130080 | 0 | True | 262 | 262 | None | None | 129056 | 129056 | True |
| bk3 | `15.log` | SEALED_OK | 130846 | 130806 | 130806 | 0 | True | 276 | 276 | None | None | 129782 | 129782 | True |
| bk3 | `16.log` | SEALED_OK | 131016 | 130976 | 130976 | 0 | True | 271 | 271 | None | None | 129952 | 129952 | True |
| bk3 | `17.log` | SEALED_OK | 130859 | 130819 | 130819 | 0 | True | 276 | 276 | None | None | 129795 | 129795 | True |
| bk3 | `18.log` | SEALED_OK | 130709 | 130669 | 130669 | 0 | True | 273 | 273 | None | None | 129645 | 129645 | True |
| bk3 | `19.log` | SEALED_OK | 130866 | 130826 | 130826 | 0 | True | 268 | 268 | None | None | 129802 | 129802 | True |
| bk3 | `1a.log` | SEALED_OK | 130959 | 130919 | 130919 | 0 | True | 278 | 278 | None | None | 129895 | 129895 | True |
| bk3 | `1b.log` | SEALED_OK | 131009 | 130969 | 130969 | 0 | True | 279 | 279 | None | None | 129945 | 129945 | True |
| bk3 | `1c.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk3 | `1d.log` | SEALED_OK | 130859 | 130819 | 130819 | 0 | True | 276 | 276 | None | None | 129795 | 129795 | True |
| bk3 | `1e.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk3 | `1f.log` | SEALED_OK | 130609 | 130569 | 130569 | 0 | True | 271 | 271 | None | None | 129545 | 129545 | True |
| bk3 | `2.log` | SEALED_OK | 130677 | 130637 | 130637 | 0 | True | 265 | 265 | None | None | 129613 | 129613 | True |
| bk3 | `20.log` | SEALED_OK | 130966 | 130926 | 130926 | 0 | True | 270 | 270 | None | None | 129902 | 129902 | True |
| bk3 | `21.log` | SEALED_OK | 131016 | 130976 | 130976 | 0 | True | 271 | 271 | None | None | 129952 | 129952 | True |
| bk3 | `22.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk3 | `23.log` | SEALED_OK | 130459 | 130419 | 130419 | 0 | True | 268 | 268 | None | None | 129395 | 129395 | True |
| bk3 | `24.log` | SEALED_OK | 130866 | 130826 | 130826 | 0 | True | 268 | 268 | None | None | 129802 | 129802 | True |
| bk3 | `25.log` | SEALED_OK | 130966 | 130926 | 130926 | 0 | True | 270 | 270 | None | None | 129902 | 129902 | True |
| bk3 | `26.log` | SEALED_OK | 131016 | 130976 | 130976 | 0 | True | 271 | 271 | None | None | 129952 | 129952 | True |
| bk3 | `27.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk3 | `28.log` | SEALED_OK | 130709 | 130669 | 130669 | 0 | True | 273 | 273 | None | None | 129645 | 129645 | True |
| bk3 | `29.log` | SEALED_OK | 130966 | 130926 | 130926 | 0 | True | 270 | 270 | None | None | 129902 | 129902 | True |
| bk3 | `2a.log` | SEALED_OK | 130866 | 130826 | 130826 | 0 | True | 268 | 268 | None | None | 129802 | 129802 | True |
| bk3 | `2b.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk3 | `2c.log` | SEALED_OK | 130659 | 130619 | 130619 | 0 | True | 272 | 272 | None | None | 129595 | 129595 | True |
| bk3 | `2d.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk3 | `2e.log` | SEALED_OK | 131066 | 131026 | 131026 | 0 | True | 272 | 272 | None | None | 130002 | 130002 | True |
| bk3 | `2f.log` | SEALED_OK | 130659 | 130619 | 130619 | 0 | True | 272 | 272 | None | None | 129595 | 129595 | True |
| bk3 | `3.log` | SEALED_OK | 130352 | 130312 | 130312 | 0 | True | 274 | 274 | None | None | 129288 | 129288 | True |
| bk3 | `30.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk3 | `31.log` | SEALED_OK | 131009 | 130969 | 130969 | 0 | True | 279 | 279 | None | None | 129945 | 129945 | True |
| bk3 | `32.log` | SEALED_OK | 130702 | 130662 | 130662 | 0 | True | 281 | 281 | None | None | 129638 | 129638 | True |
| bk3 | `33.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk3 | `34.log` | SEALED_OK | 130452 | 130412 | 130412 | 0 | True | 276 | 276 | None | None | 129388 | 129388 | True |
| bk3 | `35.log` | SEALED_OK | 130959 | 130919 | 130919 | 0 | True | 278 | 278 | None | None | 129895 | 129895 | True |
| bk3 | `36.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk3 | `37.log` | SEALED_OK | 131023 | 130983 | 130983 | 0 | True | 263 | 263 | None | None | 129959 | 129959 | True |
| bk3 | `38.log` | SEALED_OK | 131059 | 131019 | 131019 | 0 | True | 280 | 280 | None | None | 129995 | 129995 | True |
| bk3 | `39.log` | SEALED_OK | 130780 | 130740 | 130740 | 0 | True | 279 | 279 | None | None | 129716 | 129716 | True |
| bk3 | `3a.log` | SEALED_OK | 130922 | 130882 | 130882 | 0 | True | 271 | 271 | None | None | 129858 | 129858 | True |
| bk3 | `3b.log` | SEALED_OK | 130848 | 130808 | 130808 | 0 | True | 278 | 278 | None | None | 129784 | 129784 | True |
| bk3 | `3c.log` | SEALED_OK | 130922 | 130882 | 130882 | 0 | True | 271 | 271 | None | None | 129858 | 129858 | True |
| bk3 | `3d.log` | SEALED_OK | 130970 | 130930 | 130930 | 0 | True | 272 | 272 | None | None | 129906 | 129906 | True |
| bk3 | `3e.log` | SEALED_OK | 130907 | 130867 | 130867 | 0 | True | 271 | 271 | None | None | 129843 | 129843 | True |
| bk3 | `3f.log` | SEALED_OK | 131066 | 131026 | 131026 | 0 | True | 274 | 274 | None | None | 130002 | 130002 | True |
| bk3 | `4.log` | SEALED_OK | 130909 | 130869 | 130869 | 0 | True | 277 | 277 | None | None | 129845 | 129845 | True |
| bk3 | `40.log` | SEALED_OK | 130656 | 130616 | 130616 | 0 | True | 274 | 274 | None | None | 129592 | 129592 | True |
| bk3 | `41.log` | SEALED_OK | 130922 | 130882 | 130882 | 0 | True | 271 | 271 | None | None | 129858 | 129858 | True |
| bk3 | `42.log` | SEALED_OK | 130704 | 130664 | 130664 | 0 | True | 275 | 275 | None | None | 129640 | 129640 | True |
| bk3 | `43.log` | SEALED_OK | 130656 | 130616 | 130616 | 0 | True | 274 | 274 | None | None | 129592 | 129592 | True |
| bk3 | `44.log` | SEALED_OK | 130874 | 130834 | 130834 | 0 | True | 270 | 270 | None | None | 129810 | 129810 | True |
| bk3 | `45.log` | SEALED_OK | 130778 | 130738 | 130738 | 0 | True | 268 | 268 | None | None | 129714 | 129714 | True |
| bk3 | `46.log` | SEALED_OK | 130826 | 130786 | 130786 | 0 | True | 269 | 269 | None | None | 129762 | 129762 | True |
| bk3 | `47.log` | SEALED_OK | 130848 | 130808 | 130808 | 0 | True | 278 | 278 | None | None | 129784 | 129784 | True |
| bk3 | `48.log` | SEALED_OK | 130970 | 130930 | 130930 | 0 | True | 272 | 272 | None | None | 129906 | 129906 | True |
| bk3 | `49.log` | SEALED_OK | 130922 | 130882 | 130882 | 0 | True | 271 | 271 | None | None | 129858 | 129858 | True |
| bk3 | `4a.log` | SEALED_OK | 131018 | 130978 | 130978 | 0 | True | 273 | 273 | None | None | 129954 | 129954 | True |
| bk3 | `4b.log` | SEALED_OK | 131018 | 130978 | 130978 | 0 | True | 273 | 273 | None | None | 129954 | 129954 | True |
| bk3 | `4c.log` | SEALED_OK | 130922 | 130882 | 130882 | 0 | True | 271 | 271 | None | None | 129858 | 129858 | True |
| bk3 | `4d.log` | SEALED_OK | 130874 | 130834 | 130834 | 0 | True | 270 | 270 | None | None | 129810 | 129810 | True |
| bk3 | `4e.log` | SEALED_OK | 131018 | 130978 | 130978 | 0 | True | 273 | 273 | None | None | 129954 | 129954 | True |
| bk3 | `4f.log` | SEALED_OK | 130874 | 130834 | 130834 | 0 | True | 270 | 270 | None | None | 129810 | 129810 | True |
| bk3 | `5.log` | SEALED_OK | 130877 | 130837 | 130837 | 0 | True | 269 | 269 | None | None | 129813 | 129813 | True |
| bk3 | `50.log` | SEALED_OK | 130704 | 130664 | 130664 | 0 | True | 275 | 275 | None | None | 129640 | 129640 | True |
| bk3 | `51.log` | SEALED_OK | 130848 | 130808 | 130808 | 0 | True | 278 | 278 | None | None | 129784 | 129784 | True |
| bk3 | `52.log` | SEALED_OK | 130656 | 130616 | 130616 | 0 | True | 274 | 274 | None | None | 129592 | 129592 | True |
| bk3 | `53.log` | SEALED_OK | 131051 | 131011 | 131011 | 0 | True | 274 | 274 | None | None | 129987 | 129987 | True |
| bk3 | `54.log` | UNSEALED_OK | 22310 | 0 | None | None | False | 42 | 42 | None | None | None | None | None |
| bk3 | `6.log` | SEALED_OK | 130796 | 130756 | 130756 | 0 | True | 275 | 275 | None | None | 129732 | 129732 | True |
| bk3 | `7.log` | SEALED_OK | 130859 | 130819 | 130819 | 0 | True | 276 | 276 | None | None | 129795 | 129795 | True |
| bk3 | `8.log` | SEALED_OK | 130940 | 130900 | 130900 | 0 | True | 270 | 270 | None | None | 129876 | 129876 | True |
| bk3 | `9.log` | SEALED_OK | 131009 | 130969 | 130969 | 0 | True | 279 | 279 | None | None | 129945 | 129945 | True |
| bk3 | `a.log` | SEALED_OK | 130659 | 130619 | 130619 | 0 | True | 272 | 272 | None | None | 129595 | 129595 | True |
| bk3 | `b.log` | SEALED_OK | 131009 | 130969 | 130969 | 0 | True | 279 | 279 | None | None | 129945 | 129945 | True |
| bk3 | `c.log` | SEALED_OK | 130809 | 130769 | 130769 | 0 | True | 275 | 275 | None | None | 129745 | 129745 | True |
| bk3 | `d.log` | SEALED_OK | 131003 | 130963 | 130963 | 0 | True | 271 | 271 | None | None | 129939 | 129939 | True |
| bk3 | `e.log` | SEALED_OK | 130966 | 130926 | 130926 | 0 | True | 270 | 270 | None | None | 129902 | 129902 | True |
| bk3 | `f.log` | SEALED_OK | 130859 | 130819 | 130819 | 0 | True | 276 | 276 | None | None | 129795 | 129795 | True |

## Replica Entry Comparison

| target | control | targetEntries | controlEntries | common | missingInTarget | missingInControl | hashMismatches |
|---|---|---:|---:|---:|---:|---:|---:|
| bk2 | bk3 | 22909 | 22909 | 22909 | 0 | 0 | 0 |
| bk1 | bk2 | 22909 | 22909 | 22909 | 0 | 0 | 0 |
| bk1 | bk3 | 22909 | 22909 | 22909 | 0 | 0 | 0 |

## Runtime Behavior

- clientExit: `0`

### bk1

| line | tag | log |
|---:|---|---|
| 135 | bookie-fault | `2026-07-31T18:02:22,972 - ERROR - [SyncThread-7-1:SyncThread@181] - Exception flushing ledgers` |
| 136 | bookie-fault | `java.io.IOException: Input/output error` |
| 134 | entrylog-io | `2026-07-31T18:02:22,968 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log for logId 0.` |
| 162 | entrylog-io | `2026-07-31T18:02:23,959 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log for logId 1.` |
| 163 | entrylog-io | `2026-07-31T18:02:23,959 - INFO  - [SyncThread-7-1:EntryLogManagerBase@165] - Flushing entry logger 0 back to filesystem, pending for syncing entry loggers : [BufferedChannel{logId=0, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log, ledgerIdAssigned=-1}].` |
| 165 | entrylog-io | `2026-07-31T18:02:23,962 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/2.log for logId 2.` |
| 166 | entrylog-io | `2026-07-31T18:02:23,962 - INFO  - [SyncThread-7-1:EntryLogManagerBase@165] - Flushing entry logger 1 back to filesystem, pending for syncing entry loggers : [BufferedChannel{logId=0, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log, ledgerIdAssigned=-1}, BufferedChannel{logId=1, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log, ledgerIdAssigned=-1}].` |
| 167 | entrylog-io | `2026-07-31T18:02:23,980 - INFO  - [SyncThread-7-1:EntryLogManagerForSingleEntryLog@210] - Synced entry logger 0 to disk.` |
| 498 | bookie-lifecycle | `2026-07-31T18:03:11,731 - INFO  - [component-shutdown-thread:BookieServer@191] - Shutting down BookieServer` |
| 519 | bookie-lifecycle | `2026-07-31T18:03:11,763 - INFO  - [component-shutdown-thread:BookieImpl@861] - Turning bookie to read only during shut down` |
| 525 | bookie-lifecycle | `2026-07-31T18:03:11,776 - INFO  - [BookieJournal-3181:BookieImpl@828] - Triggering shutdown of Bookie-3181 with exitCode 5` |
| 532 | bookie-lifecycle | `2026-07-31T18:03:11,997 - INFO  - [BookieDeathWatcher-3181:BookieServer$DeathWatcher@274] - BookieDeathWatcher noticed the bookie is not running any more, exiting the watch loop!` |
| 533 | bookie-lifecycle | `2026-07-31T18:03:11,998 - ERROR - [BookieDeathWatcher-3181:ComponentStarter@75] - Triggered exceptionHandler of Component: bookie-server because of Exception in Thread: Thread[BookieDeathWatcher-3181,5,main]` |

### bk2

No matching log lines found.

### bk3

No matching log lines found.

### broker

| line | tag | log |
|---:|---|---|
| 33 | bk-client-init | `2026-07-31T18:02:18,737+0800 [main] INFO  org.apache.bookkeeper.meta.MetadataDrivers - BookKeeper metadata driver manager initialized` |
| 34 | bk-client-init | `2026-07-31T18:02:18,740+0800 [main] INFO  org.apache.pulsar.broker.BookKeeperClientFactoryImpl - Applying BookKeeper client configuration setting tlsHostnameVerificationEnabled=false` |
| 64 | bk-client-init | `2026-07-31T18:02:19,022+0800 [main] INFO  org.apache.pulsar.broker.BookKeeperClientFactoryImpl - Applying BookKeeper client configuration setting tlsHostnameVerificationEnabled=false` |
| 48 | bookie-discovery | `2026-07-31T18:02:18,870+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3181 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3181, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 49 | bookie-discovery | `2026-07-31T18:02:18,870+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3182 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3182, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 50 | bookie-discovery | `2026-07-31T18:02:18,870+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3183 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3183, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 52 | bookie-discovery | `2026-07-31T18:02:18,878+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3181` |
| 54 | bookie-discovery | `2026-07-31T18:02:18,879+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3182` |
| 56 | bookie-discovery | `2026-07-31T18:02:18,879+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3183` |
| 157 | bookie-channel | `2026-07-31T18:02:22,284+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3181 [id: 0xf1dd36b5, L:/127.0.0.1:35080 - R:127.0.0.1/127.0.0.1:3181]` |
| 158 | bookie-channel | `2026-07-31T18:02:22,285+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0xf1dd36b5, L:/127.0.0.1:35080 - R:127.0.0.1/127.0.0.1:3181] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 159 | bookie-channel | `2026-07-31T18:02:22,286+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3181 [id: 0xb3d98d34, L:/127.0.0.1:35174 - R:127.0.0.1/127.0.0.1:3181]` |
| 160 | bookie-channel | `2026-07-31T18:02:22,286+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0xb3d98d34, L:/127.0.0.1:35174 - R:127.0.0.1/127.0.0.1:3181] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 161 | bookie-channel | `2026-07-31T18:02:22,296+0800 [pulsar-io-3-2] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3181 [id: 0xe3dfb9b2, L:/127.0.0.1:35092 - R:127.0.0.1/127.0.0.1:3181]` |
| 162 | bookie-channel | `2026-07-31T18:02:22,297+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3181 [id: 0xec23ca94, L:/127.0.0.1:35188 - R:127.0.0.1/127.0.0.1:3181]` |
| 395 | managed-ledger | `2026-07-31T18:03:12,195+0800 [metadata-store-9-1] INFO  org.apache.bookkeeper.mledger.impl.ManagedLedgerFactoryImpl - Received MetadataStore session event: ConnectionLost` |
| 259 | broker-error | `2026-07-31T18:03:11,725+0800 [pulsar-io-3-1] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0xa407a50e, L:/127.0.0.1:43054 - R:127.0.0.1/127.0.0.1:3183] cause: recvAddress(..) failed: Connection reset by peer` |
| 260 | broker-error | `2026-07-31T18:03:11,727+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x40bdcbf5, L:/127.0.0.1:45676 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 261 | broker-error | `2026-07-31T18:03:11,726+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Disconnected from bookie channel [id: 0xa407a50e, L:/127.0.0.1:43054 ! R:127.0.0.1/127.0.0.1:3183]` |
| 262 | broker-error | `2026-07-31T18:03:11,732+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x73167dcb, L:/127.0.0.1:43028 - R:127.0.0.1/127.0.0.1:3183] cause: recvAddress(..) failed: Connection reset by peer` |
| 263 | broker-error | `2026-07-31T18:03:11,732+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x2e4a9fb9, L:/127.0.0.1:43014 - R:127.0.0.1/127.0.0.1:3183] cause: recvAddress(..) failed: Connection reset by peer` |
| 264 | broker-error | `2026-07-31T18:03:11,732+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x9929aac1, L:/127.0.0.1:42970 - R:127.0.0.1/127.0.0.1:3183] cause: recvAddress(..) failed: Connection reset by peer` |

### client

| line | tag | log |
|---:|---|---|
| 66 | client-progress | `2026-07-31T18:02:31,626+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:    5634 msg ---    563.4 msg/s ---      1.7 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:   6.360 ms - med:   5.966 - 95pct:   9.493 - 99pct:  15.654 - 99.9pct:  42.119 - 99.99pct:  48.652 - Max:  49.793` |
| 67 | client-progress | `2026-07-31T18:02:41,637+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:   11660 msg ---    600.1 msg/s ---      1.8 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:   6.300 ms - med:   5.678 - 95pct:   9.043 - 99pct:  17.799 - 99.9pct:  85.060 - 99.99pct:  91.948 - Max:  93.062` |
| 68 | client-progress | `2026-07-31T18:02:51,647+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:   17670 msg ---    600.3 msg/s ---      1.8 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:   5.583 ms - med:   5.495 - 95pct:   8.080 - 99pct:   9.993 - 99.9pct:  11.522 - 99.99pct:  12.024 - Max:  12.362` |
| 69 | client-progress | `2026-07-31T18:03:01,660+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:   23679 msg ---    600.3 msg/s ---      1.8 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:  12.321 ms - med:   5.784 - 95pct:  10.189 - 99pct: 266.251 - 99.9pct: 339.187 - 99.99pct: 346.749 - Max: 348.827` |
| 74 | client-progress | `2026-07-31T18:03:11,664+0800 [Thread-0] INFO  org.apache.pulsar.testclient.PerformanceProducer - Aggregated throughput stats --- 24005 records sent --- 479.336 msg/s --- 1.404 Mbit/s ` |
| 75 | client-progress | `2026-07-31T18:03:11,686+0800 [Thread-0] INFO  org.apache.pulsar.testclient.PerformanceProducer - Aggregated latency stats --- Latency: mean:   7.670 ms - med:   5.709 - 95pct:   9.052 - 99pct:  42.283 - 99.9pct: 310.415 - 99.99pct: 345.677 - 99.999pct: 348.827 - Max: 348.827` |
| 70 | client-completion | `2026-07-31T18:03:02,189+0800 [pulsar-perf-producer-exec-1-1] INFO  org.apache.pulsar.testclient.PerformanceProducer - ------------- DONE (reached the maximum number: 24000 of production) --------------` |
| 76 | client-completion | `workload_rc=0` |
