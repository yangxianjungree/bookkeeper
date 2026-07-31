# Entrylog Cluster Report

- clusterDir: `/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runs/stability-20260731-175938/round-02`
- pulsarVersion: `3.2.4`
- bookieVersion: `4.16.7`
- bookieCount: `3`
- managedLedgerQuorum: `3/3/2`
- failpointEvents: `1`

## Failpoint Events

| kind | logId | logFile | logical | physical | bytes | op | offset | realRc | match | trigger |
|---|---:|---|---:|---:|---:|---|---:|---:|---:|---:|
| ldpreload | 0 | `/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log` |  |  | 59029 | write | -1 | 59029 | 2 | 1 |

## Log Structure

| role | log | status | fileSize | headerMap | trueMap | delta | headerMapValid | entries | strict | prefix | post | parsedSize | mapSize | sizeMatch |
|---|---|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| bk1 | `0.log` | STRICT_CHECK | 189471 | 130402 | 189431 | 59029 | False | 80 | 80 | None | None | 123541 | 129378 | False |
| bk1 | `1.log` | SEALED_OK | 130606 | 130566 | 130566 | 0 | True | 139 | 139 | None | None | 129542 | 129542 | True |
| bk1 | `10.log` | SEALED_OK | 130806 | 130766 | 130766 | 0 | True | 143 | 143 | None | None | 129742 | 129742 | True |
| bk1 | `11.log` | SEALED_OK | 130806 | 130766 | 130766 | 0 | True | 143 | 143 | None | None | 129742 | 129742 | True |
| bk1 | `12.log` | SEALED_OK | 130906 | 130866 | 130866 | 0 | True | 145 | 145 | None | None | 129842 | 129842 | True |
| bk1 | `13.log` | SEALED_OK | 130228 | 130188 | 130188 | 0 | True | 147 | 147 | None | None | 129164 | 129164 | True |
| bk1 | `14.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk1 | `15.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk1 | `16.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk1 | `17.log` | SEALED_OK | 130478 | 130438 | 130438 | 0 | True | 152 | 152 | None | None | 129414 | 129414 | True |
| bk1 | `18.log` | SEALED_OK | 130428 | 130388 | 130388 | 0 | True | 151 | 151 | None | None | 129364 | 129364 | True |
| bk1 | `19.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk1 | `1a.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk1 | `1b.log` | SEALED_OK | 131043 | 131003 | 131003 | 0 | True | 148 | 148 | None | None | 129979 | 129979 | True |
| bk1 | `1c.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk1 | `1d.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk1 | `1e.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk1 | `1f.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk1 | `2.log` | SEALED_OK | 130617 | 130577 | 130577 | 0 | True | 140 | 140 | None | None | 129553 | 129553 | True |
| bk1 | `20.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk1 | `21.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk1 | `22.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk1 | `23.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk1 | `24.log` | SEALED_OK | 130856 | 130816 | 130816 | 0 | True | 144 | 144 | None | None | 129792 | 129792 | True |
| bk1 | `25.log` | SEALED_OK | 130743 | 130703 | 130703 | 0 | True | 142 | 142 | None | None | 129679 | 129679 | True |
| bk1 | `26.log` | SEALED_OK | 130643 | 130603 | 130603 | 0 | True | 140 | 140 | None | None | 129579 | 129579 | True |
| bk1 | `27.log` | SEALED_OK | 130793 | 130753 | 130753 | 0 | True | 143 | 143 | None | None | 129729 | 129729 | True |
| bk1 | `28.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 145 | 145 | None | None | 129829 | 129829 | True |
| bk1 | `29.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk1 | `2a.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk1 | `2b.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk1 | `2c.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk1 | `2d.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk1 | `2e.log` | SEALED_OK | 130819 | 130779 | 130779 | 0 | True | 143 | 143 | None | None | 129755 | 129755 | True |
| bk1 | `2f.log` | SEALED_OK | 130391 | 130351 | 130351 | 0 | True | 136 | 136 | None | None | 129327 | 129327 | True |
| bk1 | `3.log` | SEALED_OK | 130656 | 130616 | 130616 | 0 | True | 140 | 140 | None | None | 129592 | 129592 | True |
| bk1 | `30.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk1 | `31.log` | SEALED_OK | 130128 | 130088 | 130088 | 0 | True | 145 | 145 | None | None | 129064 | 129064 | True |
| bk1 | `32.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk1 | `33.log` | SEALED_OK | 130178 | 130138 | 130138 | 0 | True | 146 | 146 | None | None | 129114 | 129114 | True |
| bk1 | `34.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk1 | `35.log` | SEALED_OK | 130756 | 130716 | 130716 | 0 | True | 142 | 142 | None | None | 129692 | 129692 | True |
| bk1 | `36.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk1 | `37.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk1 | `38.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk1 | `39.log` | SEALED_OK | 130619 | 130579 | 130579 | 0 | True | 139 | 139 | None | None | 129555 | 129555 | True |
| bk1 | `3a.log` | SEALED_OK | 130769 | 130729 | 130729 | 0 | True | 142 | 142 | None | None | 129705 | 129705 | True |
| bk1 | `3b.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk1 | `3c.log` | SEALED_OK | 130819 | 130779 | 130779 | 0 | True | 143 | 143 | None | None | 129755 | 129755 | True |
| bk1 | `3d.log` | SEALED_OK | 130530 | 130490 | 130490 | 0 | True | 138 | 138 | None | None | 129466 | 129466 | True |
| bk1 | `3e.log` | SEALED_OK | 130693 | 130653 | 130653 | 0 | True | 141 | 141 | None | None | 129629 | 129629 | True |
| bk1 | `3f.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk1 | `4.log` | SEALED_OK | 130480 | 130440 | 130440 | 0 | True | 137 | 137 | None | None | 129416 | 129416 | True |
| bk1 | `40.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk1 | `41.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk1 | `42.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 145 | 145 | None | None | 129829 | 129829 | True |
| bk1 | `43.log` | SEALED_OK | 130178 | 130138 | 130138 | 0 | True | 146 | 146 | None | None | 129114 | 129114 | True |
| bk1 | `44.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk1 | `45.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk1 | `46.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk1 | `47.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk1 | `48.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk1 | `49.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk1 | `4a.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk1 | `4b.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk1 | `4c.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk1 | `4d.log` | SEALED_OK | 130819 | 130779 | 130779 | 0 | True | 143 | 143 | None | None | 129755 | 129755 | True |
| bk1 | `4e.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk1 | `4f.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk1 | `5.log` | SEALED_OK | 130008 | 129968 | 129968 | 0 | True | 106 | 106 | None | None | 128944 | 128944 | True |
| bk1 | `50.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk1 | `51.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk1 | `52.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk1 | `53.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk1 | `54.log` | SEALED_OK | 130769 | 130729 | 130729 | 0 | True | 142 | 142 | None | None | 129705 | 129705 | True |
| bk1 | `55.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk1 | `56.log` | SEALED_OK | 131006 | 130966 | 130966 | 0 | True | 147 | 147 | None | None | 129942 | 129942 | True |
| bk1 | `57.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk1 | `58.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk1 | `59.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk1 | `5a.log` | SEALED_OK | 130806 | 130766 | 130766 | 0 | True | 143 | 143 | None | None | 129742 | 129742 | True |
| bk1 | `5b.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk1 | `5c.log` | SEALED_OK | 130856 | 130816 | 130816 | 0 | True | 144 | 144 | None | None | 129792 | 129792 | True |
| bk1 | `5d.log` | SEALED_OK | 130769 | 130729 | 130729 | 0 | True | 142 | 142 | None | None | 129705 | 129705 | True |
| bk1 | `5e.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk1 | `5f.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk1 | `6.log` | SEALED_OK | 128780 | 128740 | 128740 | 0 | True | 93 | 93 | None | None | 127716 | 127716 | True |
| bk1 | `60.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk1 | `61.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk1 | `62.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk1 | `63.log` | SEALED_OK | 130706 | 130666 | 130666 | 0 | True | 141 | 141 | None | None | 129642 | 129642 | True |
| bk1 | `64.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk1 | `65.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk1 | `66.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk1 | `67.log` | SEALED_OK | 130719 | 130679 | 130679 | 0 | True | 141 | 141 | None | None | 129655 | 129655 | True |
| bk1 | `68.log` | UNSEALED_OK | 49652 | 0 | None | None | False | 55 | 55 | None | None | None | None | None |
| bk1 | `7.log` | SEALED_OK | 130469 | 130429 | 130429 | 0 | True | 122 | 122 | None | None | 129405 | 129405 | True |
| bk1 | `8.log` | SEALED_OK | 130793 | 130753 | 130753 | 0 | True | 143 | 143 | None | None | 129729 | 129729 | True |
| bk1 | `9.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk1 | `a.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk1 | `b.log` | SEALED_OK | 129878 | 129838 | 129838 | 0 | True | 140 | 140 | None | None | 128814 | 128814 | True |
| bk1 | `c.log` | SEALED_OK | 130819 | 130779 | 130779 | 0 | True | 143 | 143 | None | None | 129755 | 129755 | True |
| bk1 | `d.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk1 | `e.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk1 | `f.log` | SEALED_OK | 130428 | 130388 | 130388 | 0 | True | 151 | 151 | None | None | 129364 | 129364 | True |
| bk2 | `0.log` | SEALED_OK | 124605 | 124565 | 124565 | 0 | True | 80 | 80 | None | None | 123541 | 123541 | True |
| bk2 | `1.log` | SEALED_OK | 130745 | 130705 | 130705 | 0 | True | 99 | 99 | None | None | 129681 | 129681 | True |
| bk2 | `10.log` | SEALED_OK | 129915 | 129875 | 129875 | 0 | True | 141 | 141 | None | None | 128851 | 128851 | True |
| bk2 | `11.log` | SEALED_OK | 130856 | 130816 | 130816 | 0 | True | 144 | 144 | None | None | 129792 | 129792 | True |
| bk2 | `12.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk2 | `13.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk2 | `14.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk2 | `15.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk2 | `16.log` | SEALED_OK | 130528 | 130488 | 130488 | 0 | True | 153 | 153 | None | None | 129464 | 129464 | True |
| bk2 | `17.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk2 | `18.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `19.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk2 | `1a.log` | SEALED_OK | 130993 | 130953 | 130953 | 0 | True | 147 | 147 | None | None | 129929 | 129929 | True |
| bk2 | `1b.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk2 | `1c.log` | SEALED_OK | 129487 | 129447 | 129447 | 0 | True | 148 | 148 | None | None | 128423 | 128423 | True |
| bk2 | `1d.log` | SEALED_OK | 130819 | 130779 | 130779 | 0 | True | 143 | 143 | None | None | 129755 | 129755 | True |
| bk2 | `1e.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk2 | `1f.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `2.log` | SEALED_OK | 130430 | 130390 | 130390 | 0 | True | 136 | 136 | None | None | 129366 | 129366 | True |
| bk2 | `20.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk2 | `21.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk2 | `22.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `23.log` | SEALED_OK | 130856 | 130816 | 130816 | 0 | True | 144 | 144 | None | None | 129792 | 129792 | True |
| bk2 | `24.log` | SEALED_OK | 130743 | 130703 | 130703 | 0 | True | 142 | 142 | None | None | 129679 | 129679 | True |
| bk2 | `25.log` | SEALED_OK | 130643 | 130603 | 130603 | 0 | True | 140 | 140 | None | None | 129579 | 129579 | True |
| bk2 | `26.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 144 | 144 | None | None | 129779 | 129779 | True |
| bk2 | `27.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 144 | 144 | None | None | 129779 | 129779 | True |
| bk2 | `28.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `29.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk2 | `2a.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk2 | `2b.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk2 | `2c.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk2 | `2d.log` | SEALED_OK | 130769 | 130729 | 130729 | 0 | True | 142 | 142 | None | None | 129705 | 129705 | True |
| bk2 | `2e.log` | SEALED_OK | 130391 | 130351 | 130351 | 0 | True | 136 | 136 | None | None | 129327 | 129327 | True |
| bk2 | `2f.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk2 | `3.log` | SEALED_OK | 130606 | 130566 | 130566 | 0 | True | 139 | 139 | None | None | 129542 | 129542 | True |
| bk2 | `30.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `31.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk2 | `32.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk2 | `33.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk2 | `34.log` | SEALED_OK | 130806 | 130766 | 130766 | 0 | True | 143 | 143 | None | None | 129742 | 129742 | True |
| bk2 | `35.log` | SEALED_OK | 130819 | 130779 | 130779 | 0 | True | 143 | 143 | None | None | 129755 | 129755 | True |
| bk2 | `36.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk2 | `37.log` | SEALED_OK | 130078 | 130038 | 130038 | 0 | True | 144 | 144 | None | None | 129014 | 129014 | True |
| bk2 | `38.log` | SEALED_OK | 130519 | 130479 | 130479 | 0 | True | 137 | 137 | None | None | 129455 | 129455 | True |
| bk2 | `39.log` | SEALED_OK | 130819 | 130779 | 130779 | 0 | True | 143 | 143 | None | None | 129755 | 129755 | True |
| bk2 | `3a.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `3b.log` | SEALED_OK | 130769 | 130729 | 130729 | 0 | True | 142 | 142 | None | None | 129705 | 129705 | True |
| bk2 | `3c.log` | SEALED_OK | 130630 | 130590 | 130590 | 0 | True | 140 | 140 | None | None | 129566 | 129566 | True |
| bk2 | `3d.log` | SEALED_OK | 130543 | 130503 | 130503 | 0 | True | 138 | 138 | None | None | 129479 | 129479 | True |
| bk2 | `3e.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk2 | `3f.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk2 | `4.log` | SEALED_OK | 130504 | 130464 | 130464 | 0 | True | 138 | 138 | None | None | 129440 | 129440 | True |
| bk2 | `40.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk2 | `41.log` | SEALED_OK | 130102 | 130062 | 130062 | 0 | True | 145 | 145 | None | None | 129038 | 129038 | True |
| bk2 | `42.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk2 | `43.log` | SEALED_OK | 130819 | 130779 | 130779 | 0 | True | 143 | 143 | None | None | 129755 | 129755 | True |
| bk2 | `44.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk2 | `45.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk2 | `46.log` | SEALED_OK | 130819 | 130779 | 130779 | 0 | True | 143 | 143 | None | None | 129755 | 129755 | True |
| bk2 | `47.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `48.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk2 | `49.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk2 | `4a.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk2 | `4b.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk2 | `4c.log` | SEALED_OK | 130819 | 130779 | 130779 | 0 | True | 143 | 143 | None | None | 129755 | 129755 | True |
| bk2 | `4d.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `4e.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk2 | `4f.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk2 | `5.log` | SEALED_OK | 130756 | 130716 | 130716 | 0 | True | 142 | 142 | None | None | 129692 | 129692 | True |
| bk2 | `50.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk2 | `51.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk2 | `52.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk2 | `53.log` | SEALED_OK | 129928 | 129888 | 129888 | 0 | True | 141 | 141 | None | None | 128864 | 128864 | True |
| bk2 | `54.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk2 | `55.log` | SEALED_OK | 131006 | 130966 | 130966 | 0 | True | 147 | 147 | None | None | 129942 | 129942 | True |
| bk2 | `56.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk2 | `57.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk2 | `58.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk2 | `59.log` | SEALED_OK | 130806 | 130766 | 130766 | 0 | True | 143 | 143 | None | None | 129742 | 129742 | True |
| bk2 | `5a.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `5b.log` | SEALED_OK | 130906 | 130866 | 130866 | 0 | True | 145 | 145 | None | None | 129842 | 129842 | True |
| bk2 | `5c.log` | SEALED_OK | 130719 | 130679 | 130679 | 0 | True | 141 | 141 | None | None | 129655 | 129655 | True |
| bk2 | `5d.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk2 | `5e.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `5f.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk2 | `6.log` | SEALED_OK | 130380 | 130340 | 130340 | 0 | True | 135 | 135 | None | None | 129316 | 129316 | True |
| bk2 | `60.log` | SEALED_OK | 130178 | 130138 | 130138 | 0 | True | 146 | 146 | None | None | 129114 | 129114 | True |
| bk2 | `61.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk2 | `62.log` | SEALED_OK | 130756 | 130716 | 130716 | 0 | True | 142 | 142 | None | None | 129692 | 129692 | True |
| bk2 | `63.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk2 | `64.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk2 | `65.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk2 | `66.log` | SEALED_OK | 130769 | 130729 | 130729 | 0 | True | 142 | 142 | None | None | 129705 | 129705 | True |
| bk2 | `67.log` | UNSEALED_OK | 58853 | 0 | None | None | False | 65 | 65 | None | None | None | None | None |
| bk2 | `7.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `8.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk2 | `9.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk2 | `a.log` | SEALED_OK | 130719 | 130679 | 130679 | 0 | True | 141 | 141 | None | None | 129655 | 129655 | True |
| bk2 | `b.log` | SEALED_OK | 130769 | 130729 | 130729 | 0 | True | 142 | 142 | None | None | 129705 | 129705 | True |
| bk2 | `c.log` | SEALED_OK | 130428 | 130388 | 130388 | 0 | True | 151 | 151 | None | None | 129364 | 129364 | True |
| bk2 | `d.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk2 | `e.log` | SEALED_OK | 130428 | 130388 | 130388 | 0 | True | 151 | 151 | None | None | 129364 | 129364 | True |
| bk2 | `f.log` | SEALED_OK | 130906 | 130866 | 130866 | 0 | True | 145 | 145 | None | None | 129842 | 129842 | True |
| bk3 | `0.log` | SEALED_OK | 124605 | 124565 | 124565 | 0 | True | 80 | 80 | None | None | 123541 | 123541 | True |
| bk3 | `1.log` | SEALED_OK | 130745 | 130705 | 130705 | 0 | True | 99 | 99 | None | None | 129681 | 129681 | True |
| bk3 | `10.log` | SEALED_OK | 129915 | 129875 | 129875 | 0 | True | 141 | 141 | None | None | 128851 | 128851 | True |
| bk3 | `11.log` | SEALED_OK | 130856 | 130816 | 130816 | 0 | True | 144 | 144 | None | None | 129792 | 129792 | True |
| bk3 | `12.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk3 | `13.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk3 | `14.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk3 | `15.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk3 | `16.log` | SEALED_OK | 130528 | 130488 | 130488 | 0 | True | 153 | 153 | None | None | 129464 | 129464 | True |
| bk3 | `17.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk3 | `18.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk3 | `19.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk3 | `1a.log` | SEALED_OK | 130993 | 130953 | 130953 | 0 | True | 147 | 147 | None | None | 129929 | 129929 | True |
| bk3 | `1b.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk3 | `1c.log` | SEALED_OK | 129487 | 129447 | 129447 | 0 | True | 148 | 148 | None | None | 128423 | 128423 | True |
| bk3 | `1d.log` | SEALED_OK | 130819 | 130779 | 130779 | 0 | True | 143 | 143 | None | None | 129755 | 129755 | True |
| bk3 | `1e.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk3 | `1f.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk3 | `2.log` | SEALED_OK | 130430 | 130390 | 130390 | 0 | True | 136 | 136 | None | None | 129366 | 129366 | True |
| bk3 | `20.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk3 | `21.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk3 | `22.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk3 | `23.log` | SEALED_OK | 130856 | 130816 | 130816 | 0 | True | 144 | 144 | None | None | 129792 | 129792 | True |
| bk3 | `24.log` | SEALED_OK | 130743 | 130703 | 130703 | 0 | True | 142 | 142 | None | None | 129679 | 129679 | True |
| bk3 | `25.log` | SEALED_OK | 130643 | 130603 | 130603 | 0 | True | 140 | 140 | None | None | 129579 | 129579 | True |
| bk3 | `26.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 144 | 144 | None | None | 129779 | 129779 | True |
| bk3 | `27.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 144 | 144 | None | None | 129779 | 129779 | True |
| bk3 | `28.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk3 | `29.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk3 | `2a.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk3 | `2b.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk3 | `2c.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk3 | `2d.log` | SEALED_OK | 130769 | 130729 | 130729 | 0 | True | 142 | 142 | None | None | 129705 | 129705 | True |
| bk3 | `2e.log` | SEALED_OK | 130391 | 130351 | 130351 | 0 | True | 136 | 136 | None | None | 129327 | 129327 | True |
| bk3 | `2f.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk3 | `3.log` | SEALED_OK | 130606 | 130566 | 130566 | 0 | True | 139 | 139 | None | None | 129542 | 129542 | True |
| bk3 | `30.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk3 | `31.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk3 | `32.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk3 | `33.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk3 | `34.log` | SEALED_OK | 130806 | 130766 | 130766 | 0 | True | 143 | 143 | None | None | 129742 | 129742 | True |
| bk3 | `35.log` | SEALED_OK | 130819 | 130779 | 130779 | 0 | True | 143 | 143 | None | None | 129755 | 129755 | True |
| bk3 | `36.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk3 | `37.log` | SEALED_OK | 130078 | 130038 | 130038 | 0 | True | 144 | 144 | None | None | 129014 | 129014 | True |
| bk3 | `38.log` | SEALED_OK | 130519 | 130479 | 130479 | 0 | True | 137 | 137 | None | None | 129455 | 129455 | True |
| bk3 | `39.log` | SEALED_OK | 130819 | 130779 | 130779 | 0 | True | 143 | 143 | None | None | 129755 | 129755 | True |
| bk3 | `3a.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk3 | `3b.log` | SEALED_OK | 130769 | 130729 | 130729 | 0 | True | 142 | 142 | None | None | 129705 | 129705 | True |
| bk3 | `3c.log` | SEALED_OK | 130630 | 130590 | 130590 | 0 | True | 140 | 140 | None | None | 129566 | 129566 | True |
| bk3 | `3d.log` | SEALED_OK | 130543 | 130503 | 130503 | 0 | True | 138 | 138 | None | None | 129479 | 129479 | True |
| bk3 | `3e.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk3 | `3f.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk3 | `4.log` | SEALED_OK | 130504 | 130464 | 130464 | 0 | True | 138 | 138 | None | None | 129440 | 129440 | True |
| bk3 | `40.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk3 | `41.log` | SEALED_OK | 130102 | 130062 | 130062 | 0 | True | 145 | 145 | None | None | 129038 | 129038 | True |
| bk3 | `42.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk3 | `43.log` | SEALED_OK | 130819 | 130779 | 130779 | 0 | True | 143 | 143 | None | None | 129755 | 129755 | True |
| bk3 | `44.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk3 | `45.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk3 | `46.log` | SEALED_OK | 130819 | 130779 | 130779 | 0 | True | 143 | 143 | None | None | 129755 | 129755 | True |
| bk3 | `47.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk3 | `48.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk3 | `49.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk3 | `4a.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk3 | `4b.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk3 | `4c.log` | SEALED_OK | 130819 | 130779 | 130779 | 0 | True | 143 | 143 | None | None | 129755 | 129755 | True |
| bk3 | `4d.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk3 | `4e.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk3 | `4f.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk3 | `5.log` | SEALED_OK | 130756 | 130716 | 130716 | 0 | True | 142 | 142 | None | None | 129692 | 129692 | True |
| bk3 | `50.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk3 | `51.log` | SEALED_OK | 130328 | 130288 | 130288 | 0 | True | 149 | 149 | None | None | 129264 | 129264 | True |
| bk3 | `52.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk3 | `53.log` | SEALED_OK | 129928 | 129888 | 129888 | 0 | True | 141 | 141 | None | None | 128864 | 128864 | True |
| bk3 | `54.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk3 | `55.log` | SEALED_OK | 131006 | 130966 | 130966 | 0 | True | 147 | 147 | None | None | 129942 | 129942 | True |
| bk3 | `56.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk3 | `57.log` | SEALED_OK | 130278 | 130238 | 130238 | 0 | True | 148 | 148 | None | None | 129214 | 129214 | True |
| bk3 | `58.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk3 | `59.log` | SEALED_OK | 130806 | 130766 | 130766 | 0 | True | 143 | 143 | None | None | 129742 | 129742 | True |
| bk3 | `5a.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk3 | `5b.log` | SEALED_OK | 130906 | 130866 | 130866 | 0 | True | 145 | 145 | None | None | 129842 | 129842 | True |
| bk3 | `5c.log` | SEALED_OK | 130719 | 130679 | 130679 | 0 | True | 141 | 141 | None | None | 129655 | 129655 | True |
| bk3 | `5d.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk3 | `5e.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk3 | `5f.log` | SEALED_OK | 130969 | 130929 | 130929 | 0 | True | 146 | 146 | None | None | 129905 | 129905 | True |
| bk3 | `6.log` | SEALED_OK | 130380 | 130340 | 130340 | 0 | True | 135 | 135 | None | None | 129316 | 129316 | True |
| bk3 | `60.log` | SEALED_OK | 130178 | 130138 | 130138 | 0 | True | 146 | 146 | None | None | 129114 | 129114 | True |
| bk3 | `61.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk3 | `62.log` | SEALED_OK | 130756 | 130716 | 130716 | 0 | True | 142 | 142 | None | None | 129692 | 129692 | True |
| bk3 | `63.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk3 | `64.log` | SEALED_OK | 130869 | 130829 | 130829 | 0 | True | 144 | 144 | None | None | 129805 | 129805 | True |
| bk3 | `65.log` | SEALED_OK | 131069 | 131029 | 131029 | 0 | True | 148 | 148 | None | None | 130005 | 130005 | True |
| bk3 | `66.log` | SEALED_OK | 130769 | 130729 | 130729 | 0 | True | 142 | 142 | None | None | 129705 | 129705 | True |
| bk3 | `67.log` | UNSEALED_OK | 58853 | 0 | None | None | False | 65 | 65 | None | None | None | None | None |
| bk3 | `7.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk3 | `8.log` | SEALED_OK | 130378 | 130338 | 130338 | 0 | True | 150 | 150 | None | None | 129314 | 129314 | True |
| bk3 | `9.log` | SEALED_OK | 130919 | 130879 | 130879 | 0 | True | 145 | 145 | None | None | 129855 | 129855 | True |
| bk3 | `a.log` | SEALED_OK | 130719 | 130679 | 130679 | 0 | True | 141 | 141 | None | None | 129655 | 129655 | True |
| bk3 | `b.log` | SEALED_OK | 130769 | 130729 | 130729 | 0 | True | 142 | 142 | None | None | 129705 | 129705 | True |
| bk3 | `c.log` | SEALED_OK | 130428 | 130388 | 130388 | 0 | True | 151 | 151 | None | None | 129364 | 129364 | True |
| bk3 | `d.log` | SEALED_OK | 131019 | 130979 | 130979 | 0 | True | 147 | 147 | None | None | 129955 | 129955 | True |
| bk3 | `e.log` | SEALED_OK | 130428 | 130388 | 130388 | 0 | True | 151 | 151 | None | None | 129364 | 129364 | True |
| bk3 | `f.log` | SEALED_OK | 130906 | 130866 | 130866 | 0 | True | 145 | 145 | None | None | 129842 | 129842 | True |

## Replica Entry Comparison

| target | control | targetEntries | controlEntries | common | missingInTarget | missingInControl | hashMismatches |
|---|---|---:|---:|---:|---:|---:|---:|
| bk2 | bk3 | 14929 | 14929 | 14929 | 0 | 0 | 0 |
| bk1 | bk2 | 14923 | 14929 | 14923 | 6 | 0 | 0 |
| bk1 | bk3 | 14923 | 14929 | 14923 | 6 | 0 | 0 |

### Samples: bk1 vs bk2

- missingInTarget: `0:332, 0:333, 0:334, 0:335, 0:336, 0:337`

### Samples: bk1 vs bk3

- missingInTarget: `0:332, 0:333, 0:334, 0:335, 0:336, 0:337`

## Runtime Behavior

- clientExit: `0`

### bk1

| line | tag | log |
|---:|---|---|
| 136 | bookie-fault | `2026-07-31T18:00:43,292 - ERROR - [SyncThread-7-1:SyncThread@181] - Exception flushing ledgers` |
| 137 | bookie-fault | `java.io.IOException: Input/output error` |
| 134 | entrylog-io | `2026-07-31T18:00:43,285 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log for logId 0.` |
| 164 | entrylog-io | `2026-07-31T18:00:44,278 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log for logId 1.` |
| 165 | entrylog-io | `2026-07-31T18:00:44,279 - INFO  - [SyncThread-7-1:EntryLogManagerBase@165] - Flushing entry logger 0 back to filesystem, pending for syncing entry loggers : [BufferedChannel{logId=0, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log, ledgerIdAssigned=-1}].` |
| 167 | entrylog-io | `2026-07-31T18:00:44,281 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/2.log for logId 2.` |
| 168 | entrylog-io | `2026-07-31T18:00:44,281 - INFO  - [SyncThread-7-1:EntryLogManagerBase@165] - Flushing entry logger 1 back to filesystem, pending for syncing entry loggers : [BufferedChannel{logId=0, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log, ledgerIdAssigned=-1}, BufferedChannel{logId=1, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log, ledgerIdAssigned=-1}].` |
| 170 | entrylog-io | `2026-07-31T18:00:44,283 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/3.log for logId 3.` |
| 580 | bookie-lifecycle | `2026-07-31T18:01:12,056 - INFO  - [component-shutdown-thread:BookieServer@191] - Shutting down BookieServer` |
| 601 | bookie-lifecycle | `2026-07-31T18:01:12,098 - INFO  - [component-shutdown-thread:BookieImpl@861] - Turning bookie to read only during shut down` |
| 607 | bookie-lifecycle | `2026-07-31T18:01:12,111 - INFO  - [BookieJournal-3181:BookieImpl@828] - Triggering shutdown of Bookie-3181 with exitCode 5` |
| 614 | bookie-lifecycle | `2026-07-31T18:01:12,337 - INFO  - [BookieDeathWatcher-3181:BookieServer$DeathWatcher@274] - BookieDeathWatcher noticed the bookie is not running any more, exiting the watch loop!` |
| 615 | bookie-lifecycle | `2026-07-31T18:01:12,338 - ERROR - [BookieDeathWatcher-3181:ComponentStarter@75] - Triggered exceptionHandler of Component: bookie-server because of Exception in Thread: Thread[BookieDeathWatcher-3181,5,main]` |

### bk2

No matching log lines found.

### bk3

No matching log lines found.

### broker

| line | tag | log |
|---:|---|---|
| 33 | bk-client-init | `2026-07-31T18:00:39,043+0800 [main] INFO  org.apache.bookkeeper.meta.MetadataDrivers - BookKeeper metadata driver manager initialized` |
| 34 | bk-client-init | `2026-07-31T18:00:39,045+0800 [main] INFO  org.apache.pulsar.broker.BookKeeperClientFactoryImpl - Applying BookKeeper client configuration setting tlsHostnameVerificationEnabled=false` |
| 64 | bk-client-init | `2026-07-31T18:00:39,328+0800 [main] INFO  org.apache.pulsar.broker.BookKeeperClientFactoryImpl - Applying BookKeeper client configuration setting tlsHostnameVerificationEnabled=false` |
| 48 | bookie-discovery | `2026-07-31T18:00:39,170+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3181 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3181, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 49 | bookie-discovery | `2026-07-31T18:00:39,171+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3182 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3182, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 50 | bookie-discovery | `2026-07-31T18:00:39,171+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3183 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3183, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 52 | bookie-discovery | `2026-07-31T18:00:39,179+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3181` |
| 54 | bookie-discovery | `2026-07-31T18:00:39,180+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3182` |
| 56 | bookie-discovery | `2026-07-31T18:00:39,180+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3183` |
| 157 | bookie-channel | `2026-07-31T18:00:42,667+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3182 [id: 0xebd32ab0, L:/127.0.0.1:42384 - R:127.0.0.1/127.0.0.1:3182]` |
| 158 | bookie-channel | `2026-07-31T18:00:42,667+0800 [pulsar-io-3-2] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3182 [id: 0x934e70ee, L:/127.0.0.1:42402 - R:127.0.0.1/127.0.0.1:3182]` |
| 159 | bookie-channel | `2026-07-31T18:00:42,667+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0xebd32ab0, L:/127.0.0.1:42384 - R:127.0.0.1/127.0.0.1:3182] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 160 | bookie-channel | `2026-07-31T18:00:42,668+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3182 [id: 0xd63eec6b, L:/127.0.0.1:42388 - R:127.0.0.1/127.0.0.1:3182]` |
| 161 | bookie-channel | `2026-07-31T18:00:42,668+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0xd63eec6b, L:/127.0.0.1:42388 - R:127.0.0.1/127.0.0.1:3182] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 162 | bookie-channel | `2026-07-31T18:00:42,668+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3182 [id: 0xbcb2db21, L:/127.0.0.1:42422 - R:127.0.0.1/127.0.0.1:3182]` |
| 326 | managed-ledger | `2026-07-31T18:01:12,071+0800 [pulsar-service-shutdown] INFO  org.apache.bookkeeper.mledger.impl.ManagedLedgerImpl - [public/default/persistent/entrylog-ldpreload-round-02] Closing managed ledger` |
| 391 | managed-ledger | `2026-07-31T18:01:12,508+0800 [metadata-store-9-1] INFO  org.apache.bookkeeper.mledger.impl.ManagedLedgerFactoryImpl - Received MetadataStore session event: ConnectionLost` |
| 259 | broker-error | `2026-07-31T18:01:12,038+0800 [pulsar-io-3-1] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x1b51f3ef, L:/127.0.0.1:35508 - R:127.0.0.1/127.0.0.1:3183] cause: recvAddress(..) failed: Connection reset by peer` |
| 260 | broker-error | `2026-07-31T18:01:12,039+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x1eb3a3e8, L:/127.0.0.1:35522 - R:127.0.0.1/127.0.0.1:3183] cause: recvAddress(..) failed: Connection reset by peer` |
| 261 | broker-error | `2026-07-31T18:01:12,039+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Disconnected from bookie channel [id: 0x1b51f3ef, L:/127.0.0.1:35508 ! R:127.0.0.1/127.0.0.1:3183]` |
| 262 | broker-error | `2026-07-31T18:01:12,043+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0xc757c37c, L:/127.0.0.1:35406 - R:127.0.0.1/127.0.0.1:3183] cause: recvAddress(..) failed: Connection reset by peer` |
| 263 | broker-error | `2026-07-31T18:01:12,044+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x91f611d7, L:/127.0.0.1:35466 - R:127.0.0.1/127.0.0.1:3183] cause: recvAddress(..) failed: Connection reset by peer` |
| 264 | broker-error | `2026-07-31T18:01:12,044+0800 [pulsar-io-3-2] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Disconnected from bookie channel [id: 0x1eb3a3e8, L:/127.0.0.1:35522 ! R:127.0.0.1/127.0.0.1:3183]` |

### client

| line | tag | log |
|---:|---|---|
| 66 | client-progress | `2026-07-31T18:00:51,973+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:    6558 msg ---    655.8 msg/s ---      3.8 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:   8.887 ms - med:   8.395 - 95pct:  13.486 - 99pct:  19.382 - 99.9pct:  45.913 - 99.99pct:  52.623 - Max:  53.703` |
| 67 | client-progress | `2026-07-31T18:01:01,983+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:   13580 msg ---    700.4 msg/s ---      4.1 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:   8.080 ms - med:   7.724 - 95pct:  11.945 - 99pct:  15.883 - 99.9pct:  55.175 - 99.99pct:  61.778 - Max:  62.823` |
| 72 | client-progress | `2026-07-31T18:01:11,989+0800 [Thread-0] INFO  org.apache.pulsar.testclient.PerformanceProducer - Aggregated throughput stats --- 16007 records sent --- 532.769 msg/s --- 3.122 Mbit/s ` |
| 73 | client-progress | `2026-07-31T18:01:11,994+0800 [Thread-0] INFO  org.apache.pulsar.testclient.PerformanceProducer - Aggregated latency stats --- Latency: mean:   8.332 ms - med:   7.958 - 95pct:  12.436 - 99pct:  16.942 - 99.9pct:  50.894 - 99.99pct:  60.787 - 99.999pct:  62.823 - Max:  62.823` |
| 68 | client-completion | `2026-07-31T18:01:05,436+0800 [pulsar-perf-producer-exec-1-1] INFO  org.apache.pulsar.testclient.PerformanceProducer - ------------- DONE (reached the maximum number: 16000 of production) --------------` |
| 74 | client-completion | `workload_rc=0` |
