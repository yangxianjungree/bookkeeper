# Entrylog Cluster Report

- clusterDir: `/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runs/single-replica-20260731-184741/round-05`
- pulsarVersion: `3.2.4`
- bookieVersion: `4.16.7`
- bookieCount: `2`
- managedLedgerQuorum: `2/1/1`
- failpointEvents: `1`

## Failpoint Events

| kind | logId | logFile | logical | physical | bytes | op | offset | realRc | match | trigger |
|---|---:|---|---:|---:|---:|---|---:|---:|---:|---:|
| ldpreload | 4 | `/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/4.log` |  |  | 65536 | write | -1 | 65536 | 5 | 1 |

## Log Structure

| role | log | status | fileSize | headerMap | trueMap | delta | headerMapValid | entries | strict | prefix | post | parsedSize | mapSize | sizeMatch |
|---|---|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| bk1 | `0.log` | SEALED_OK | 130283 | 130243 | 130243 | 0 | True | 36 | 36 | None | None | 129219 | 129219 | True |
| bk1 | `1.log` | SEALED_OK | 129511 | 129471 | 129471 | 0 | True | 47 | 47 | None | None | 128447 | 128447 | True |
| bk1 | `10.log` | SEALED_OK | 130730 | 130690 | 130690 | 0 | True | 68 | 68 | None | None | 129666 | 129666 | True |
| bk1 | `11.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 70 | 70 | None | None | 129779 | 129779 | True |
| bk1 | `12.log` | SEALED_OK | 129334 | 129294 | 129294 | 0 | True | 71 | 71 | None | None | 128270 | 128270 | True |
| bk1 | `13.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 70 | 70 | None | None | 129779 | 129779 | True |
| bk1 | `14.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 71 | 71 | None | None | 129829 | 129829 | True |
| bk1 | `15.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 70 | 70 | None | None | 129779 | 129779 | True |
| bk1 | `16.log` | SEALED_OK | 130993 | 130953 | 130953 | 0 | True | 73 | 73 | None | None | 129929 | 129929 | True |
| bk1 | `17.log` | SEALED_OK | 130880 | 130840 | 130840 | 0 | True | 71 | 71 | None | None | 129816 | 129816 | True |
| bk1 | `18.log` | SEALED_OK | 130930 | 130890 | 130890 | 0 | True | 72 | 72 | None | None | 129866 | 129866 | True |
| bk1 | `19.log` | SEALED_OK | 130291 | 130251 | 130251 | 0 | True | 60 | 60 | None | None | 129227 | 129227 | True |
| bk1 | `1a.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 71 | 71 | None | None | 129829 | 129829 | True |
| bk1 | `1b.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk1 | `1c.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk1 | `1d.log` | SEALED_OK | 130591 | 130551 | 130551 | 0 | True | 66 | 66 | None | None | 129527 | 129527 | True |
| bk1 | `1e.log` | SEALED_OK | 130880 | 130840 | 130840 | 0 | True | 71 | 71 | None | None | 129816 | 129816 | True |
| bk1 | `1f.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 71 | 71 | None | None | 129829 | 129829 | True |
| bk1 | `2.log` | SEALED_OK | 130493 | 130453 | 130453 | 0 | True | 63 | 63 | None | None | 129429 | 129429 | True |
| bk1 | `20.log` | SEALED_OK | 130993 | 130953 | 130953 | 0 | True | 73 | 73 | None | None | 129929 | 129929 | True |
| bk1 | `21.log` | SEALED_OK | 130880 | 130840 | 130840 | 0 | True | 71 | 71 | None | None | 129816 | 129816 | True |
| bk1 | `22.log` | SEALED_OK | 130880 | 130840 | 130840 | 0 | True | 71 | 71 | None | None | 129816 | 129816 | True |
| bk1 | `23.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 71 | 71 | None | None | 129829 | 129829 | True |
| bk1 | `24.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 70 | 70 | None | None | 129779 | 129779 | True |
| bk1 | `25.log` | SEALED_OK | 131043 | 131003 | 131003 | 0 | True | 74 | 74 | None | None | 129979 | 129979 | True |
| bk1 | `26.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk1 | `27.log` | SEALED_OK | 130793 | 130753 | 130753 | 0 | True | 69 | 69 | None | None | 129729 | 129729 | True |
| bk1 | `28.log` | SEALED_OK | 130830 | 130790 | 130790 | 0 | True | 70 | 70 | None | None | 129766 | 129766 | True |
| bk1 | `29.log` | SEALED_OK | 129195 | 129155 | 129155 | 0 | True | 69 | 69 | None | None | 128131 | 128131 | True |
| bk1 | `2a.log` | SEALED_OK | 129045 | 129005 | 129005 | 0 | True | 66 | 66 | None | None | 127981 | 127981 | True |
| bk1 | `2b.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 70 | 70 | None | None | 129779 | 129779 | True |
| bk1 | `2c.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk1 | `2d.log` | SEALED_OK | 130667 | 130627 | 130627 | 0 | True | 67 | 67 | None | None | 129603 | 129603 | True |
| bk1 | `2e.log` | SEALED_OK | 131043 | 131003 | 131003 | 0 | True | 74 | 74 | None | None | 129979 | 129979 | True |
| bk1 | `2f.log` | SEALED_OK | 130880 | 130840 | 130840 | 0 | True | 71 | 71 | None | None | 129816 | 129816 | True |
| bk1 | `3.log` | SEALED_OK | 130667 | 130627 | 130627 | 0 | True | 67 | 67 | None | None | 129603 | 129603 | True |
| bk1 | `30.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk1 | `31.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 71 | 71 | None | None | 129829 | 129829 | True |
| bk1 | `32.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk1 | `33.log` | SEALED_OK | 130930 | 130890 | 130890 | 0 | True | 72 | 72 | None | None | 129866 | 129866 | True |
| bk1 | `34.log` | SEALED_OK | 129034 | 128994 | 128994 | 0 | True | 65 | 65 | None | None | 127970 | 127970 | True |
| bk1 | `35.log` | SEALED_OK | 130743 | 130703 | 130703 | 0 | True | 68 | 68 | None | None | 129679 | 129679 | True |
| bk1 | `36.log` | SEALED_OK | 131043 | 131003 | 131003 | 0 | True | 74 | 74 | None | None | 129979 | 129979 | True |
| bk1 | `37.log` | SEALED_OK | 130993 | 130953 | 130953 | 0 | True | 73 | 73 | None | None | 129929 | 129929 | True |
| bk1 | `38.log` | SEALED_OK | 131093 | 131053 | 131053 | 0 | True | 75 | 75 | None | None | 130029 | 130029 | True |
| bk1 | `39.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk1 | `3a.log` | SEALED_OK | 130793 | 130753 | 130753 | 0 | True | 69 | 69 | None | None | 129729 | 129729 | True |
| bk1 | `3b.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 70 | 70 | None | None | 129779 | 129779 | True |
| bk1 | `3c.log` | SEALED_OK | 130930 | 130890 | 130890 | 0 | True | 72 | 72 | None | None | 129866 | 129866 | True |
| bk1 | `3d.log` | SEALED_OK | 129071 | 129031 | 129031 | 0 | True | 66 | 66 | None | None | 128007 | 128007 | True |
| bk1 | `3e.log` | SEALED_OK | 130793 | 130753 | 130753 | 0 | True | 69 | 69 | None | None | 129729 | 129729 | True |
| bk1 | `3f.log` | SEALED_OK | 130630 | 130590 | 130590 | 0 | True | 66 | 66 | None | None | 129566 | 129566 | True |
| bk1 | `4.log` | DRIFT_CHECK | 196681 | 130757 | 196641 | 65884 | False | 70 | None | 37 | 33 | 131338 | 129729 | False |
| bk1 | `40.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 70 | 70 | None | None | 129779 | 129779 | True |
| bk1 | `41.log` | SEALED_OK | 131043 | 131003 | 131003 | 0 | True | 74 | 74 | None | None | 129979 | 129979 | True |
| bk1 | `42.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 70 | 70 | None | None | 129779 | 129779 | True |
| bk1 | `43.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 71 | 71 | None | None | 129829 | 129829 | True |
| bk1 | `44.log` | SEALED_OK | 130993 | 130953 | 130953 | 0 | True | 73 | 73 | None | None | 129929 | 129929 | True |
| bk1 | `45.log` | SEALED_OK | 129334 | 129294 | 129294 | 0 | True | 71 | 71 | None | None | 128270 | 128270 | True |
| bk1 | `46.log` | SEALED_OK | 130780 | 130740 | 130740 | 0 | True | 69 | 69 | None | None | 129716 | 129716 | True |
| bk1 | `47.log` | SEALED_OK | 130793 | 130753 | 130753 | 0 | True | 69 | 69 | None | None | 129729 | 129729 | True |
| bk1 | `48.log` | SEALED_OK | 130780 | 130740 | 130740 | 0 | True | 69 | 69 | None | None | 129716 | 129716 | True |
| bk1 | `49.log` | SEALED_OK | 129284 | 129244 | 129244 | 0 | True | 70 | 70 | None | None | 128220 | 128220 | True |
| bk1 | `4a.log` | SEALED_OK | 130643 | 130603 | 130603 | 0 | True | 66 | 66 | None | None | 129579 | 129579 | True |
| bk1 | `4b.log` | SEALED_OK | 130980 | 130940 | 130940 | 0 | True | 73 | 73 | None | None | 129916 | 129916 | True |
| bk1 | `4c.log` | SEALED_OK | 131093 | 131053 | 131053 | 0 | True | 75 | 75 | None | None | 130029 | 130029 | True |
| bk1 | `4d.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 70 | 70 | None | None | 129779 | 129779 | True |
| bk1 | `4e.log` | SEALED_OK | 130830 | 130790 | 130790 | 0 | True | 70 | 70 | None | None | 129766 | 129766 | True |
| bk1 | `4f.log` | SEALED_OK | 130880 | 130840 | 130840 | 0 | True | 71 | 71 | None | None | 129816 | 129816 | True |
| bk1 | `5.log` | SEALED_OK | 130680 | 130640 | 130640 | 0 | True | 67 | 67 | None | None | 129616 | 129616 | True |
| bk1 | `50.log` | SEALED_OK | 130793 | 130753 | 130753 | 0 | True | 69 | 69 | None | None | 129729 | 129729 | True |
| bk1 | `51.log` | SEALED_OK | 130767 | 130727 | 130727 | 0 | True | 69 | 69 | None | None | 129703 | 129703 | True |
| bk1 | `52.log` | SEALED_OK | 130039 | 129999 | 129999 | 0 | True | 56 | 56 | None | None | 128975 | 128975 | True |
| bk1 | `53.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 70 | 70 | None | None | 129779 | 129779 | True |
| bk1 | `54.log` | SEALED_OK | 129284 | 129244 | 129244 | 0 | True | 70 | 70 | None | None | 128220 | 128220 | True |
| bk1 | `55.log` | SEALED_OK | 129008 | 128968 | 128968 | 0 | True | 65 | 65 | None | None | 127944 | 127944 | True |
| bk1 | `56.log` | SEALED_OK | 130830 | 130790 | 130790 | 0 | True | 70 | 70 | None | None | 129766 | 129766 | True |
| bk1 | `57.log` | SEALED_OK | 129384 | 129344 | 129344 | 0 | True | 72 | 72 | None | None | 128320 | 128320 | True |
| bk1 | `58.log` | SEALED_OK | 129134 | 129094 | 129094 | 0 | True | 67 | 67 | None | None | 128070 | 128070 | True |
| bk1 | `59.log` | SEALED_OK | 130780 | 130740 | 130740 | 0 | True | 69 | 69 | None | None | 129716 | 129716 | True |
| bk1 | `5a.log` | SEALED_OK | 130880 | 130840 | 130840 | 0 | True | 71 | 71 | None | None | 129816 | 129816 | True |
| bk1 | `5b.log` | SEALED_OK | 129184 | 129144 | 129144 | 0 | True | 68 | 68 | None | None | 128120 | 128120 | True |
| bk1 | `5c.log` | SEALED_OK | 130730 | 130690 | 130690 | 0 | True | 68 | 68 | None | None | 129666 | 129666 | True |
| bk1 | `5d.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 70 | 70 | None | None | 129779 | 129779 | True |
| bk1 | `5e.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk1 | `5f.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk1 | `6.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk1 | `60.log` | SEALED_OK | 130830 | 130790 | 130790 | 0 | True | 70 | 70 | None | None | 129766 | 129766 | True |
| bk1 | `61.log` | SEALED_OK | 130743 | 130703 | 130703 | 0 | True | 68 | 68 | None | None | 129679 | 129679 | True |
| bk1 | `62.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 71 | 71 | None | None | 129829 | 129829 | True |
| bk1 | `63.log` | SEALED_OK | 131093 | 131053 | 131053 | 0 | True | 75 | 75 | None | None | 130029 | 130029 | True |
| bk1 | `64.log` | SEALED_OK | 130717 | 130677 | 130677 | 0 | True | 68 | 68 | None | None | 129653 | 129653 | True |
| bk1 | `65.log` | SEALED_OK | 131043 | 131003 | 131003 | 0 | True | 74 | 74 | None | None | 129979 | 129979 | True |
| bk1 | `66.log` | SEALED_OK | 131093 | 131053 | 131053 | 0 | True | 75 | 75 | None | None | 130029 | 130029 | True |
| bk1 | `67.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 70 | 70 | None | None | 129779 | 129779 | True |
| bk1 | `68.log` | SEALED_OK | 131080 | 131040 | 131040 | 0 | True | 75 | 75 | None | None | 130016 | 130016 | True |
| bk1 | `69.log` | SEALED_OK | 130903 | 130863 | 130863 | 0 | True | 71 | 71 | None | None | 129839 | 129839 | True |
| bk1 | `6a.log` | SEALED_OK | 131042 | 131002 | 131002 | 0 | True | 72 | 72 | None | None | 129978 | 129978 | True |
| bk1 | `6b.log` | SEALED_OK | 130946 | 130906 | 130906 | 0 | True | 70 | 70 | None | None | 129882 | 129882 | True |
| bk1 | `6c.log` | SEALED_OK | 129528 | 129488 | 129488 | 0 | True | 73 | 73 | None | None | 128464 | 128464 | True |
| bk1 | `6d.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 71 | 71 | None | None | 129930 | 129930 | True |
| bk1 | `6e.log` | SEALED_OK | 130916 | 130876 | 130876 | 0 | True | 70 | 70 | None | None | 129852 | 129852 | True |
| bk1 | `6f.log` | SEALED_OK | 130931 | 130891 | 130891 | 0 | True | 70 | 70 | None | None | 129867 | 129867 | True |
| bk1 | `7.log` | SEALED_OK | 130780 | 130740 | 130740 | 0 | True | 69 | 69 | None | None | 129716 | 129716 | True |
| bk1 | `70.log` | SEALED_OK | 130979 | 130939 | 130939 | 0 | True | 71 | 71 | None | None | 129915 | 129915 | True |
| bk1 | `71.log` | SEALED_OK | 130709 | 130669 | 130669 | 0 | True | 66 | 66 | None | None | 129645 | 129645 | True |
| bk1 | `72.log` | SEALED_OK | 130787 | 130747 | 130747 | 0 | True | 67 | 67 | None | None | 129723 | 129723 | True |
| bk1 | `73.log` | SEALED_OK | 129513 | 129473 | 129473 | 0 | True | 73 | 73 | None | None | 128449 | 128449 | True |
| bk1 | `74.log` | SEALED_OK | 130709 | 130669 | 130669 | 0 | True | 66 | 66 | None | None | 129645 | 129645 | True |
| bk1 | `75.log` | SEALED_OK | 131090 | 131050 | 131050 | 0 | True | 73 | 73 | None | None | 130026 | 130026 | True |
| bk1 | `76.log` | SEALED_OK | 129624 | 129584 | 129584 | 0 | True | 75 | 75 | None | None | 128560 | 128560 | True |
| bk1 | `77.log` | SEALED_OK | 130931 | 130891 | 130891 | 0 | True | 70 | 70 | None | None | 129867 | 129867 | True |
| bk1 | `78.log` | SEALED_OK | 129480 | 129440 | 129440 | 0 | True | 72 | 72 | None | None | 128416 | 128416 | True |
| bk1 | `79.log` | SEALED_OK | 130898 | 130858 | 130858 | 0 | True | 69 | 69 | None | None | 129834 | 129834 | True |
| bk1 | `7a.log` | SEALED_OK | 129384 | 129344 | 129344 | 0 | True | 70 | 70 | None | None | 128320 | 128320 | True |
| bk1 | `7b.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 71 | 71 | None | None | 129930 | 129930 | True |
| bk1 | `7c.log` | SEALED_OK | 130772 | 130732 | 130732 | 0 | True | 67 | 67 | None | None | 129708 | 129708 | True |
| bk1 | `7d.log` | SEALED_OK | 129288 | 129248 | 129248 | 0 | True | 68 | 68 | None | None | 128224 | 128224 | True |
| bk1 | `7e.log` | SEALED_OK | 130850 | 130810 | 130810 | 0 | True | 68 | 68 | None | None | 129786 | 129786 | True |
| bk1 | `7f.log` | SEALED_OK | 131042 | 131002 | 131002 | 0 | True | 72 | 72 | None | None | 129978 | 129978 | True |
| bk1 | `8.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 70 | 70 | None | None | 129779 | 129779 | True |
| bk1 | `80.log` | SEALED_OK | 131090 | 131050 | 131050 | 0 | True | 73 | 73 | None | None | 130026 | 130026 | True |
| bk1 | `81.log` | SEALED_OK | 130916 | 130876 | 130876 | 0 | True | 70 | 70 | None | None | 129852 | 129852 | True |
| bk1 | `82.log` | SEALED_OK | 131042 | 131002 | 131002 | 0 | True | 72 | 72 | None | None | 129978 | 129978 | True |
| bk1 | `83.log` | SEALED_OK | 131090 | 131050 | 131050 | 0 | True | 73 | 73 | None | None | 130026 | 130026 | True |
| bk1 | `84.log` | SEALED_OK | 130964 | 130924 | 130924 | 0 | True | 71 | 71 | None | None | 129900 | 129900 | True |
| bk1 | `85.log` | SEALED_OK | 131042 | 131002 | 131002 | 0 | True | 72 | 72 | None | None | 129978 | 129978 | True |
| bk1 | `86.log` | SEALED_OK | 130835 | 130795 | 130795 | 0 | True | 68 | 68 | None | None | 129771 | 129771 | True |
| bk1 | `87.log` | SEALED_OK | 129576 | 129536 | 129536 | 0 | True | 74 | 74 | None | None | 128512 | 128512 | True |
| bk1 | `88.log` | SEALED_OK | 130850 | 130810 | 130810 | 0 | True | 68 | 68 | None | None | 129786 | 129786 | True |
| bk1 | `89.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 71 | 71 | None | None | 129930 | 129930 | True |
| bk1 | `8a.log` | SEALED_OK | 130979 | 130939 | 130939 | 0 | True | 71 | 71 | None | None | 129915 | 129915 | True |
| bk1 | `8b.log` | SEALED_OK | 129528 | 129488 | 129488 | 0 | True | 73 | 73 | None | None | 128464 | 128464 | True |
| bk1 | `8c.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 71 | 71 | None | None | 129930 | 129930 | True |
| bk1 | `8d.log` | SEALED_OK | 129528 | 129488 | 129488 | 0 | True | 73 | 73 | None | None | 128464 | 128464 | True |
| bk1 | `8e.log` | SEALED_OK | 130931 | 130891 | 130891 | 0 | True | 70 | 70 | None | None | 129867 | 129867 | True |
| bk1 | `8f.log` | SEALED_OK | 129465 | 129425 | 129425 | 0 | True | 72 | 72 | None | None | 128401 | 128401 | True |
| bk1 | `9.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk1 | `90.log` | SEALED_OK | 130850 | 130810 | 130810 | 0 | True | 68 | 68 | None | None | 129786 | 129786 | True |
| bk1 | `91.log` | SEALED_OK | 129768 | 129728 | 129728 | 0 | True | 78 | 78 | None | None | 128704 | 128704 | True |
| bk1 | `92.log` | SEALED_OK | 130979 | 130939 | 130939 | 0 | True | 71 | 71 | None | None | 129915 | 129915 | True |
| bk1 | `93.log` | SEALED_OK | 131027 | 130987 | 130987 | 0 | True | 72 | 72 | None | None | 129963 | 129963 | True |
| bk1 | `94.log` | SEALED_OK | 131042 | 131002 | 131002 | 0 | True | 72 | 72 | None | None | 129978 | 129978 | True |
| bk1 | `95.log` | SEALED_OK | 131090 | 131050 | 131050 | 0 | True | 73 | 73 | None | None | 130026 | 130026 | True |
| bk1 | `96.log` | SEALED_OK | 130802 | 130762 | 130762 | 0 | True | 67 | 67 | None | None | 129738 | 129738 | True |
| bk1 | `97.log` | SEALED_OK | 131090 | 131050 | 131050 | 0 | True | 73 | 73 | None | None | 130026 | 130026 | True |
| bk1 | `98.log` | SEALED_OK | 129225 | 129185 | 129185 | 0 | True | 67 | 67 | None | None | 128161 | 128161 | True |
| bk1 | `99.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 71 | 71 | None | None | 129930 | 129930 | True |
| bk1 | `9a.log` | SEALED_OK | 129576 | 129536 | 129536 | 0 | True | 74 | 74 | None | None | 128512 | 128512 | True |
| bk1 | `9b.log` | SEALED_OK | 130883 | 130843 | 130843 | 0 | True | 69 | 69 | None | None | 129819 | 129819 | True |
| bk1 | `9c.log` | SEALED_OK | 130835 | 130795 | 130795 | 0 | True | 68 | 68 | None | None | 129771 | 129771 | True |
| bk1 | `9d.log` | SEALED_OK | 129177 | 129137 | 129137 | 0 | True | 66 | 66 | None | None | 128113 | 128113 | True |
| bk1 | `9e.log` | SEALED_OK | 130946 | 130906 | 130906 | 0 | True | 70 | 70 | None | None | 129882 | 129882 | True |
| bk1 | `9f.log` | SEALED_OK | 130835 | 130795 | 130795 | 0 | True | 68 | 68 | None | None | 129771 | 129771 | True |
| bk1 | `a.log` | SEALED_OK | 130130 | 130090 | 130090 | 0 | True | 59 | 59 | None | None | 129066 | 129066 | True |
| bk1 | `a0.log` | SEALED_OK | 130739 | 130699 | 130699 | 0 | True | 66 | 66 | None | None | 129675 | 129675 | True |
| bk1 | `a1.log` | SEALED_OK | 130868 | 130828 | 130828 | 0 | True | 69 | 69 | None | None | 129804 | 129804 | True |
| bk1 | `a2.log` | SEALED_OK | 131042 | 131002 | 131002 | 0 | True | 72 | 72 | None | None | 129978 | 129978 | True |
| bk1 | `a3.log` | SEALED_OK | 131090 | 131050 | 131050 | 0 | True | 73 | 73 | None | None | 130026 | 130026 | True |
| bk1 | `a4.log` | SEALED_OK | 130787 | 130747 | 130747 | 0 | True | 67 | 67 | None | None | 129723 | 129723 | True |
| bk1 | `a5.log` | SEALED_OK | 129225 | 129185 | 129185 | 0 | True | 67 | 67 | None | None | 128161 | 128161 | True |
| bk1 | `a6.log` | SEALED_OK | 130835 | 130795 | 130795 | 0 | True | 68 | 68 | None | None | 129771 | 129771 | True |
| bk1 | `a7.log` | SEALED_OK | 130850 | 130810 | 130810 | 0 | True | 68 | 68 | None | None | 129786 | 129786 | True |
| bk1 | `a8.log` | SEALED_OK | 131042 | 131002 | 131002 | 0 | True | 72 | 72 | None | None | 129978 | 129978 | True |
| bk1 | `a9.log` | SEALED_OK | 130835 | 130795 | 130795 | 0 | True | 68 | 68 | None | None | 129771 | 129771 | True |
| bk1 | `aa.log` | SEALED_OK | 130946 | 130906 | 130906 | 0 | True | 70 | 70 | None | None | 129882 | 129882 | True |
| bk1 | `ab.log` | SEALED_OK | 130946 | 130906 | 130906 | 0 | True | 70 | 70 | None | None | 129882 | 129882 | True |
| bk1 | `ac.log` | SEALED_OK | 130931 | 130891 | 130891 | 0 | True | 70 | 70 | None | None | 129867 | 129867 | True |
| bk1 | `ad.log` | SEALED_OK | 129273 | 129233 | 129233 | 0 | True | 68 | 68 | None | None | 128209 | 128209 | True |
| bk1 | `ae.log` | SEALED_OK | 131090 | 131050 | 131050 | 0 | True | 73 | 73 | None | None | 130026 | 130026 | True |
| bk1 | `af.log` | SEALED_OK | 131090 | 131050 | 131050 | 0 | True | 73 | 73 | None | None | 130026 | 130026 | True |
| bk1 | `b.log` | SEALED_OK | 130418 | 130378 | 130378 | 0 | True | 37 | 37 | None | None | 129354 | 129354 | True |
| bk1 | `b0.log` | SEALED_OK | 130931 | 130891 | 130891 | 0 | True | 70 | 70 | None | None | 129867 | 129867 | True |
| bk1 | `b1.log` | UNSEALED_OK | 110072 | 0 | None | None | False | 59 | 59 | None | None | None | None | None |
| bk1 | `c.log` | SEALED_OK | 128280 | 128240 | 128240 | 0 | True | 52 | 52 | None | None | 127216 | 127216 | True |
| bk1 | `d.log` | SEALED_OK | 130743 | 130703 | 130703 | 0 | True | 68 | 68 | None | None | 129679 | 129679 | True |
| bk1 | `e.log` | SEALED_OK | 130617 | 130577 | 130577 | 0 | True | 66 | 66 | None | None | 129553 | 129553 | True |
| bk1 | `f.log` | SEALED_OK | 130604 | 130564 | 130564 | 0 | True | 66 | 66 | None | None | 129540 | 129540 | True |
| bk2 | `0.log` | SEALED_OK | 130390 | 130350 | 130350 | 0 | True | 37 | 37 | None | None | 129326 | 129326 | True |
| bk2 | `1.log` | SEALED_OK | 130605 | 130565 | 130565 | 0 | True | 39 | 39 | None | None | 129541 | 129541 | True |
| bk2 | `10.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 71 | 71 | None | None | 129829 | 129829 | True |
| bk2 | `11.log` | SEALED_OK | 130930 | 130890 | 130890 | 0 | True | 72 | 72 | None | None | 129866 | 129866 | True |
| bk2 | `12.log` | SEALED_OK | 130743 | 130703 | 130703 | 0 | True | 68 | 68 | None | None | 129679 | 129679 | True |
| bk2 | `13.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk2 | `14.log` | SEALED_OK | 130693 | 130653 | 130653 | 0 | True | 67 | 67 | None | None | 129629 | 129629 | True |
| bk2 | `15.log` | SEALED_OK | 131093 | 131053 | 131053 | 0 | True | 75 | 75 | None | None | 130029 | 130029 | True |
| bk2 | `16.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 71 | 71 | None | None | 129829 | 129829 | True |
| bk2 | `17.log` | SEALED_OK | 130930 | 130890 | 130890 | 0 | True | 72 | 72 | None | None | 129866 | 129866 | True |
| bk2 | `18.log` | SEALED_OK | 129184 | 129144 | 129144 | 0 | True | 68 | 68 | None | None | 128120 | 128120 | True |
| bk2 | `19.log` | SEALED_OK | 130793 | 130753 | 130753 | 0 | True | 69 | 69 | None | None | 129729 | 129729 | True |
| bk2 | `1a.log` | SEALED_OK | 130743 | 130703 | 130703 | 0 | True | 68 | 68 | None | None | 129679 | 129679 | True |
| bk2 | `1b.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 71 | 71 | None | None | 129829 | 129829 | True |
| bk2 | `1c.log` | SEALED_OK | 130793 | 130753 | 130753 | 0 | True | 69 | 69 | None | None | 129729 | 129729 | True |
| bk2 | `1d.log` | SEALED_OK | 130993 | 130953 | 130953 | 0 | True | 73 | 73 | None | None | 129929 | 129929 | True |
| bk2 | `1e.log` | SEALED_OK | 130993 | 130953 | 130953 | 0 | True | 73 | 73 | None | None | 129929 | 129929 | True |
| bk2 | `1f.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk2 | `2.log` | SEALED_OK | 130254 | 130214 | 130214 | 0 | True | 59 | 59 | None | None | 129190 | 129190 | True |
| bk2 | `20.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk2 | `21.log` | SEALED_OK | 131093 | 131053 | 131053 | 0 | True | 75 | 75 | None | None | 130029 | 130029 | True |
| bk2 | `22.log` | SEALED_OK | 130680 | 130640 | 130640 | 0 | True | 67 | 67 | None | None | 129616 | 129616 | True |
| bk2 | `23.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 71 | 71 | None | None | 129829 | 129829 | True |
| bk2 | `24.log` | SEALED_OK | 130793 | 130753 | 130753 | 0 | True | 69 | 69 | None | None | 129729 | 129729 | True |
| bk2 | `25.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 70 | 70 | None | None | 129779 | 129779 | True |
| bk2 | `26.log` | SEALED_OK | 131043 | 131003 | 131003 | 0 | True | 74 | 74 | None | None | 129979 | 129979 | True |
| bk2 | `27.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk2 | `28.log` | SEALED_OK | 130491 | 130451 | 130451 | 0 | True | 64 | 64 | None | None | 129427 | 129427 | True |
| bk2 | `29.log` | SEALED_OK | 129334 | 129294 | 129294 | 0 | True | 71 | 71 | None | None | 128270 | 128270 | True |
| bk2 | `2a.log` | SEALED_OK | 130830 | 130790 | 130790 | 0 | True | 70 | 70 | None | None | 129766 | 129766 | True |
| bk2 | `2b.log` | SEALED_OK | 130993 | 130953 | 130953 | 0 | True | 73 | 73 | None | None | 129929 | 129929 | True |
| bk2 | `2c.log` | SEALED_OK | 130830 | 130790 | 130790 | 0 | True | 70 | 70 | None | None | 129766 | 129766 | True |
| bk2 | `2d.log` | SEALED_OK | 130993 | 130953 | 130953 | 0 | True | 73 | 73 | None | None | 129929 | 129929 | True |
| bk2 | `2e.log` | SEALED_OK | 130643 | 130603 | 130603 | 0 | True | 66 | 66 | None | None | 129579 | 129579 | True |
| bk2 | `2f.log` | SEALED_OK | 131043 | 131003 | 131003 | 0 | True | 74 | 74 | None | None | 129979 | 129979 | True |
| bk2 | `3.log` | SEALED_OK | 130493 | 130453 | 130453 | 0 | True | 63 | 63 | None | None | 129429 | 129429 | True |
| bk2 | `30.log` | SEALED_OK | 131043 | 131003 | 131003 | 0 | True | 74 | 74 | None | None | 129979 | 129979 | True |
| bk2 | `31.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk2 | `32.log` | SEALED_OK | 130730 | 130690 | 130690 | 0 | True | 68 | 68 | None | None | 129666 | 129666 | True |
| bk2 | `33.log` | SEALED_OK | 131043 | 131003 | 131003 | 0 | True | 74 | 74 | None | None | 129979 | 129979 | True |
| bk2 | `34.log` | SEALED_OK | 130793 | 130753 | 130753 | 0 | True | 69 | 69 | None | None | 129729 | 129729 | True |
| bk2 | `35.log` | SEALED_OK | 130654 | 130614 | 130614 | 0 | True | 67 | 67 | None | None | 129590 | 129590 | True |
| bk2 | `36.log` | SEALED_OK | 130530 | 130490 | 130490 | 0 | True | 64 | 64 | None | None | 129466 | 129466 | True |
| bk2 | `37.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 70 | 70 | None | None | 129779 | 129779 | True |
| bk2 | `38.log` | SEALED_OK | 130793 | 130753 | 130753 | 0 | True | 69 | 69 | None | None | 129729 | 129729 | True |
| bk2 | `39.log` | SEALED_OK | 130930 | 130890 | 130890 | 0 | True | 72 | 72 | None | None | 129866 | 129866 | True |
| bk2 | `3a.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 71 | 71 | None | None | 129829 | 129829 | True |
| bk2 | `3b.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk2 | `3c.log` | SEALED_OK | 130993 | 130953 | 130953 | 0 | True | 73 | 73 | None | None | 129929 | 129929 | True |
| bk2 | `3d.log` | SEALED_OK | 130993 | 130953 | 130953 | 0 | True | 73 | 73 | None | None | 129929 | 129929 | True |
| bk2 | `3e.log` | SEALED_OK | 129271 | 129231 | 129231 | 0 | True | 70 | 70 | None | None | 128207 | 128207 | True |
| bk2 | `3f.log` | SEALED_OK | 130767 | 130727 | 130727 | 0 | True | 69 | 69 | None | None | 129703 | 129703 | True |
| bk2 | `4.log` | SEALED_OK | 122772 | 122732 | 122732 | 0 | True | 65 | 65 | None | None | 121708 | 121708 | True |
| bk2 | `40.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 71 | 71 | None | None | 129829 | 129829 | True |
| bk2 | `41.log` | SEALED_OK | 131043 | 131003 | 131003 | 0 | True | 74 | 74 | None | None | 129979 | 129979 | True |
| bk2 | `42.log` | SEALED_OK | 130917 | 130877 | 130877 | 0 | True | 72 | 72 | None | None | 129853 | 129853 | True |
| bk2 | `43.log` | SEALED_OK | 130817 | 130777 | 130777 | 0 | True | 70 | 70 | None | None | 129753 | 129753 | True |
| bk2 | `44.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 71 | 71 | None | None | 129829 | 129829 | True |
| bk2 | `45.log` | SEALED_OK | 130743 | 130703 | 130703 | 0 | True | 68 | 68 | None | None | 129679 | 129679 | True |
| bk2 | `46.log` | SEALED_OK | 129434 | 129394 | 129394 | 0 | True | 73 | 73 | None | None | 128370 | 128370 | True |
| bk2 | `47.log` | SEALED_OK | 129234 | 129194 | 129194 | 0 | True | 69 | 69 | None | None | 128170 | 128170 | True |
| bk2 | `48.log` | SEALED_OK | 130880 | 130840 | 130840 | 0 | True | 71 | 71 | None | None | 129816 | 129816 | True |
| bk2 | `49.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk2 | `4a.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 70 | 70 | None | None | 129779 | 129779 | True |
| bk2 | `4b.log` | SEALED_OK | 130680 | 130640 | 130640 | 0 | True | 67 | 67 | None | None | 129616 | 129616 | True |
| bk2 | `4c.log` | SEALED_OK | 129384 | 129344 | 129344 | 0 | True | 72 | 72 | None | None | 128320 | 128320 | True |
| bk2 | `4d.log` | SEALED_OK | 130554 | 130514 | 130514 | 0 | True | 65 | 65 | None | None | 129490 | 129490 | True |
| bk2 | `4e.log` | SEALED_OK | 130793 | 130753 | 130753 | 0 | True | 69 | 69 | None | None | 129729 | 129729 | True |
| bk2 | `4f.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk2 | `5.log` | SEALED_OK | 130528 | 130488 | 130488 | 0 | True | 65 | 65 | None | None | 129464 | 129464 | True |
| bk2 | `50.log` | SEALED_OK | 130817 | 130777 | 130777 | 0 | True | 70 | 70 | None | None | 129753 | 129753 | True |
| bk2 | `51.log` | SEALED_OK | 130980 | 130940 | 130940 | 0 | True | 73 | 73 | None | None | 129916 | 129916 | True |
| bk2 | `52.log` | SEALED_OK | 127662 | 127622 | 127622 | 0 | True | 69 | 69 | None | None | 126598 | 126598 | True |
| bk2 | `53.log` | SEALED_OK | 130880 | 130840 | 130840 | 0 | True | 71 | 71 | None | None | 129816 | 129816 | True |
| bk2 | `54.log` | SEALED_OK | 130693 | 130653 | 130653 | 0 | True | 67 | 67 | None | None | 129629 | 129629 | True |
| bk2 | `55.log` | SEALED_OK | 129434 | 129394 | 129394 | 0 | True | 73 | 73 | None | None | 128370 | 128370 | True |
| bk2 | `56.log` | SEALED_OK | 130830 | 130790 | 130790 | 0 | True | 70 | 70 | None | None | 129766 | 129766 | True |
| bk2 | `57.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk2 | `58.log` | SEALED_OK | 131093 | 131053 | 131053 | 0 | True | 75 | 75 | None | None | 130029 | 130029 | True |
| bk2 | `59.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 71 | 71 | None | None | 129829 | 129829 | True |
| bk2 | `5a.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 71 | 71 | None | None | 129829 | 129829 | True |
| bk2 | `5b.log` | SEALED_OK | 130993 | 130953 | 130953 | 0 | True | 73 | 73 | None | None | 129929 | 129929 | True |
| bk2 | `5c.log` | SEALED_OK | 129321 | 129281 | 129281 | 0 | True | 71 | 71 | None | None | 128257 | 128257 | True |
| bk2 | `5d.log` | SEALED_OK | 130867 | 130827 | 130827 | 0 | True | 71 | 71 | None | None | 129803 | 129803 | True |
| bk2 | `5e.log` | SEALED_OK | 130943 | 130903 | 130903 | 0 | True | 72 | 72 | None | None | 129879 | 129879 | True |
| bk2 | `5f.log` | SEALED_OK | 129284 | 129244 | 129244 | 0 | True | 70 | 70 | None | None | 128220 | 128220 | True |
| bk2 | `6.log` | SEALED_OK | 130830 | 130790 | 130790 | 0 | True | 70 | 70 | None | None | 129766 | 129766 | True |
| bk2 | `60.log` | SEALED_OK | 130880 | 130840 | 130840 | 0 | True | 71 | 71 | None | None | 129816 | 129816 | True |
| bk2 | `61.log` | SEALED_OK | 130743 | 130703 | 130703 | 0 | True | 68 | 68 | None | None | 129679 | 129679 | True |
| bk2 | `62.log` | SEALED_OK | 130843 | 130803 | 130803 | 0 | True | 70 | 70 | None | None | 129779 | 129779 | True |
| bk2 | `63.log` | SEALED_OK | 130680 | 130640 | 130640 | 0 | True | 67 | 67 | None | None | 129616 | 129616 | True |
| bk2 | `64.log` | SEALED_OK | 130780 | 130740 | 130740 | 0 | True | 69 | 69 | None | None | 129716 | 129716 | True |
| bk2 | `65.log` | SEALED_OK | 130927 | 130887 | 130887 | 0 | True | 70 | 70 | None | None | 129863 | 129863 | True |
| bk2 | `66.log` | SEALED_OK | 130931 | 130891 | 130891 | 0 | True | 70 | 70 | None | None | 129867 | 129867 | True |
| bk2 | `67.log` | SEALED_OK | 130883 | 130843 | 130843 | 0 | True | 69 | 69 | None | None | 129819 | 129819 | True |
| bk2 | `68.log` | SEALED_OK | 130946 | 130906 | 130906 | 0 | True | 70 | 70 | None | None | 129882 | 129882 | True |
| bk2 | `69.log` | SEALED_OK | 131090 | 131050 | 131050 | 0 | True | 73 | 73 | None | None | 130026 | 130026 | True |
| bk2 | `6a.log` | SEALED_OK | 130787 | 130747 | 130747 | 0 | True | 67 | 67 | None | None | 129723 | 129723 | True |
| bk2 | `6b.log` | SEALED_OK | 129369 | 129329 | 129329 | 0 | True | 70 | 70 | None | None | 128305 | 128305 | True |
| bk2 | `6c.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 71 | 71 | None | None | 129930 | 129930 | True |
| bk2 | `6d.log` | SEALED_OK | 129561 | 129521 | 129521 | 0 | True | 74 | 74 | None | None | 128497 | 128497 | True |
| bk2 | `6e.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 71 | 71 | None | None | 129930 | 129930 | True |
| bk2 | `6f.log` | SEALED_OK | 130964 | 130924 | 130924 | 0 | True | 71 | 71 | None | None | 129900 | 129900 | True |
| bk2 | `7.log` | SEALED_OK | 130880 | 130840 | 130840 | 0 | True | 71 | 71 | None | None | 129816 | 129816 | True |
| bk2 | `70.log` | SEALED_OK | 129480 | 129440 | 129440 | 0 | True | 72 | 72 | None | None | 128416 | 128416 | True |
| bk2 | `71.log` | SEALED_OK | 130835 | 130795 | 130795 | 0 | True | 68 | 68 | None | None | 129771 | 129771 | True |
| bk2 | `72.log` | SEALED_OK | 130835 | 130795 | 130795 | 0 | True | 68 | 68 | None | None | 129771 | 129771 | True |
| bk2 | `73.log` | SEALED_OK | 130835 | 130795 | 130795 | 0 | True | 68 | 68 | None | None | 129771 | 129771 | True |
| bk2 | `74.log` | SEALED_OK | 129576 | 129536 | 129536 | 0 | True | 74 | 74 | None | None | 128512 | 128512 | True |
| bk2 | `75.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 71 | 71 | None | None | 129930 | 129930 | True |
| bk2 | `76.log` | SEALED_OK | 130820 | 130780 | 130780 | 0 | True | 68 | 68 | None | None | 129756 | 129756 | True |
| bk2 | `77.log` | SEALED_OK | 130898 | 130858 | 130858 | 0 | True | 69 | 69 | None | None | 129834 | 129834 | True |
| bk2 | `78.log` | SEALED_OK | 130946 | 130906 | 130906 | 0 | True | 70 | 70 | None | None | 129882 | 129882 | True |
| bk2 | `79.log` | SEALED_OK | 130946 | 130906 | 130906 | 0 | True | 70 | 70 | None | None | 129882 | 129882 | True |
| bk2 | `7a.log` | SEALED_OK | 131090 | 131050 | 131050 | 0 | True | 73 | 73 | None | None | 130026 | 130026 | True |
| bk2 | `7b.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 71 | 71 | None | None | 129930 | 129930 | True |
| bk2 | `7c.log` | SEALED_OK | 131042 | 131002 | 131002 | 0 | True | 72 | 72 | None | None | 129978 | 129978 | True |
| bk2 | `7d.log` | SEALED_OK | 131090 | 131050 | 131050 | 0 | True | 73 | 73 | None | None | 130026 | 130026 | True |
| bk2 | `7e.log` | SEALED_OK | 130850 | 130810 | 130810 | 0 | True | 68 | 68 | None | None | 129786 | 129786 | True |
| bk2 | `7f.log` | SEALED_OK | 130739 | 130699 | 130699 | 0 | True | 66 | 66 | None | None | 129675 | 129675 | True |
| bk2 | `8.log` | SEALED_OK | 130743 | 130703 | 130703 | 0 | True | 68 | 68 | None | None | 129679 | 129679 | True |
| bk2 | `80.log` | SEALED_OK | 131027 | 130987 | 130987 | 0 | True | 72 | 72 | None | None | 129963 | 129963 | True |
| bk2 | `81.log` | SEALED_OK | 130931 | 130891 | 130891 | 0 | True | 70 | 70 | None | None | 129867 | 129867 | True |
| bk2 | `82.log` | SEALED_OK | 130946 | 130906 | 130906 | 0 | True | 70 | 70 | None | None | 129882 | 129882 | True |
| bk2 | `83.log` | SEALED_OK | 130898 | 130858 | 130858 | 0 | True | 69 | 69 | None | None | 129834 | 129834 | True |
| bk2 | `84.log` | SEALED_OK | 130883 | 130843 | 130843 | 0 | True | 69 | 69 | None | None | 129819 | 129819 | True |
| bk2 | `85.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 71 | 71 | None | None | 129930 | 129930 | True |
| bk2 | `86.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 71 | 71 | None | None | 129930 | 129930 | True |
| bk2 | `87.log` | SEALED_OK | 129465 | 129425 | 129425 | 0 | True | 72 | 72 | None | None | 128401 | 128401 | True |
| bk2 | `88.log` | SEALED_OK | 130946 | 130906 | 130906 | 0 | True | 70 | 70 | None | None | 129882 | 129882 | True |
| bk2 | `89.log` | SEALED_OK | 130946 | 130906 | 130906 | 0 | True | 70 | 70 | None | None | 129882 | 129882 | True |
| bk2 | `8a.log` | SEALED_OK | 129624 | 129584 | 129584 | 0 | True | 75 | 75 | None | None | 128560 | 128560 | True |
| bk2 | `8b.log` | SEALED_OK | 130931 | 130891 | 130891 | 0 | True | 70 | 70 | None | None | 129867 | 129867 | True |
| bk2 | `8c.log` | SEALED_OK | 130946 | 130906 | 130906 | 0 | True | 70 | 70 | None | None | 129882 | 129882 | True |
| bk2 | `8d.log` | SEALED_OK | 130898 | 130858 | 130858 | 0 | True | 69 | 69 | None | None | 129834 | 129834 | True |
| bk2 | `8e.log` | SEALED_OK | 130787 | 130747 | 130747 | 0 | True | 67 | 67 | None | None | 129723 | 129723 | True |
| bk2 | `8f.log` | SEALED_OK | 131090 | 131050 | 131050 | 0 | True | 73 | 73 | None | None | 130026 | 130026 | True |
| bk2 | `9.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 71 | 71 | None | None | 129829 | 129829 | True |
| bk2 | `90.log` | SEALED_OK | 130883 | 130843 | 130843 | 0 | True | 69 | 69 | None | None | 129819 | 129819 | True |
| bk2 | `91.log` | SEALED_OK | 130820 | 130780 | 130780 | 0 | True | 68 | 68 | None | None | 129756 | 129756 | True |
| bk2 | `92.log` | SEALED_OK | 129576 | 129536 | 129536 | 0 | True | 74 | 74 | None | None | 128512 | 128512 | True |
| bk2 | `93.log` | SEALED_OK | 130835 | 130795 | 130795 | 0 | True | 68 | 68 | None | None | 129771 | 129771 | True |
| bk2 | `94.log` | SEALED_OK | 131090 | 131050 | 131050 | 0 | True | 73 | 73 | None | None | 130026 | 130026 | True |
| bk2 | `95.log` | SEALED_OK | 130898 | 130858 | 130858 | 0 | True | 69 | 69 | None | None | 129834 | 129834 | True |
| bk2 | `96.log` | SEALED_OK | 130835 | 130795 | 130795 | 0 | True | 68 | 68 | None | None | 129771 | 129771 | True |
| bk2 | `97.log` | SEALED_OK | 129306 | 129266 | 129266 | 0 | True | 69 | 69 | None | None | 128242 | 128242 | True |
| bk2 | `98.log` | SEALED_OK | 131090 | 131050 | 131050 | 0 | True | 73 | 73 | None | None | 130026 | 130026 | True |
| bk2 | `99.log` | SEALED_OK | 131090 | 131050 | 131050 | 0 | True | 73 | 73 | None | None | 130026 | 130026 | True |
| bk2 | `9a.log` | SEALED_OK | 129480 | 129440 | 129440 | 0 | True | 72 | 72 | None | None | 128416 | 128416 | True |
| bk2 | `9b.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 71 | 71 | None | None | 129930 | 129930 | True |
| bk2 | `9c.log` | SEALED_OK | 129576 | 129536 | 129536 | 0 | True | 74 | 74 | None | None | 128512 | 128512 | True |
| bk2 | `9d.log` | SEALED_OK | 131027 | 130987 | 130987 | 0 | True | 72 | 72 | None | None | 129963 | 129963 | True |
| bk2 | `9e.log` | SEALED_OK | 129480 | 129440 | 129440 | 0 | True | 72 | 72 | None | None | 128416 | 128416 | True |
| bk2 | `9f.log` | SEALED_OK | 130946 | 130906 | 130906 | 0 | True | 70 | 70 | None | None | 129882 | 129882 | True |
| bk2 | `a.log` | SEALED_OK | 129284 | 129244 | 129244 | 0 | True | 70 | 70 | None | None | 128220 | 128220 | True |
| bk2 | `a0.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 71 | 71 | None | None | 129930 | 129930 | True |
| bk2 | `a1.log` | SEALED_OK | 130979 | 130939 | 130939 | 0 | True | 71 | 71 | None | None | 129915 | 129915 | True |
| bk2 | `a2.log` | SEALED_OK | 131090 | 131050 | 131050 | 0 | True | 73 | 73 | None | None | 130026 | 130026 | True |
| bk2 | `a3.log` | SEALED_OK | 129288 | 129248 | 129248 | 0 | True | 68 | 68 | None | None | 128224 | 128224 | True |
| bk2 | `a4.log` | SEALED_OK | 130898 | 130858 | 130858 | 0 | True | 69 | 69 | None | None | 129834 | 129834 | True |
| bk2 | `a5.log` | SEALED_OK | 130946 | 130906 | 130906 | 0 | True | 70 | 70 | None | None | 129882 | 129882 | True |
| bk2 | `a6.log` | SEALED_OK | 130898 | 130858 | 130858 | 0 | True | 69 | 69 | None | None | 129834 | 129834 | True |
| bk2 | `a7.log` | SEALED_OK | 130850 | 130810 | 130810 | 0 | True | 68 | 68 | None | None | 129786 | 129786 | True |
| bk2 | `a8.log` | SEALED_OK | 130946 | 130906 | 130906 | 0 | True | 70 | 70 | None | None | 129882 | 129882 | True |
| bk2 | `a9.log` | SEALED_OK | 129369 | 129329 | 129329 | 0 | True | 70 | 70 | None | None | 128305 | 128305 | True |
| bk2 | `aa.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 71 | 71 | None | None | 129930 | 129930 | True |
| bk2 | `ab.log` | SEALED_OK | 130709 | 130669 | 130669 | 0 | True | 66 | 66 | None | None | 129645 | 129645 | True |
| bk2 | `ac.log` | SEALED_OK | 131042 | 131002 | 131002 | 0 | True | 72 | 72 | None | None | 129978 | 129978 | True |
| bk2 | `ad.log` | UNSEALED_OK | 20248 | 0 | None | None | False | 10 | 10 | None | None | None | None | None |
| bk2 | `b.log` | SEALED_OK | 130893 | 130853 | 130853 | 0 | True | 71 | 71 | None | None | 129829 | 129829 | True |
| bk2 | `c.log` | SEALED_OK | 130743 | 130703 | 130703 | 0 | True | 68 | 68 | None | None | 129679 | 129679 | True |
| bk2 | `d.log` | SEALED_OK | 131043 | 131003 | 131003 | 0 | True | 74 | 74 | None | None | 129979 | 129979 | True |
| bk2 | `e.log` | SEALED_OK | 130730 | 130690 | 130690 | 0 | True | 68 | 68 | None | None | 129666 | 129666 | True |
| bk2 | `f.log` | SEALED_OK | 130993 | 130953 | 130953 | 0 | True | 73 | 73 | None | None | 129929 | 129929 | True |

## Replica Entry Comparison

Skipped: write quorum is smaller than ensemble size, so entries are intentionally single-copy distributed across bookies.

## Runtime Behavior

- clientExit: `0`

### bk1

| line | tag | log |
|---:|---|---|
| 147 | bookie-fault | `2026-07-31T18:51:29,363 - ERROR - [SyncThread-7-1:SyncThread@181] - Exception flushing ledgers` |
| 148 | bookie-fault | `java.io.IOException: Input/output error` |
| 134 | entrylog-io | `2026-07-31T18:51:29,354 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log for logId 0.` |
| 136 | entrylog-io | `2026-07-31T18:51:29,357 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log for logId 1.` |
| 137 | entrylog-io | `2026-07-31T18:51:29,357 - INFO  - [SyncThread-7-1:EntryLogManagerBase@165] - Flushing entry logger 0 back to filesystem, pending for syncing entry loggers : [BufferedChannel{logId=0, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log, ledgerIdAssigned=-1}].` |
| 139 | entrylog-io | `2026-07-31T18:51:29,358 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/2.log for logId 2.` |
| 140 | entrylog-io | `2026-07-31T18:51:29,359 - INFO  - [SyncThread-7-1:EntryLogManagerBase@165] - Flushing entry logger 1 back to filesystem, pending for syncing entry loggers : [BufferedChannel{logId=0, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log, ledgerIdAssigned=-1}, BufferedChannel{logId=1, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log, ledgerIdAssigned=-1}].` |
| 142 | entrylog-io | `2026-07-31T18:51:29,360 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/3.log for logId 3.` |
| 870 | bookie-lifecycle | `2026-07-31T18:51:57,748 - INFO  - [component-shutdown-thread:BookieServer@191] - Shutting down BookieServer` |
| 891 | bookie-lifecycle | `2026-07-31T18:51:57,762 - INFO  - [component-shutdown-thread:BookieImpl@861] - Turning bookie to read only during shut down` |
| 897 | bookie-lifecycle | `2026-07-31T18:51:57,935 - INFO  - [BookieJournal-3181:BookieImpl@828] - Triggering shutdown of Bookie-3181 with exitCode 5` |

### bk2

No matching log lines found.

### bk3

No matching log lines found.

### broker

| line | tag | log |
|---:|---|---|
| 33 | bk-client-init | `2026-07-31T18:51:24,808+0800 [main] INFO  org.apache.bookkeeper.meta.MetadataDrivers - BookKeeper metadata driver manager initialized` |
| 34 | bk-client-init | `2026-07-31T18:51:24,811+0800 [main] INFO  org.apache.pulsar.broker.BookKeeperClientFactoryImpl - Applying BookKeeper client configuration setting tlsHostnameVerificationEnabled=false` |
| 61 | bk-client-init | `2026-07-31T18:51:25,112+0800 [main] INFO  org.apache.pulsar.broker.BookKeeperClientFactoryImpl - Applying BookKeeper client configuration setting tlsHostnameVerificationEnabled=false` |
| 48 | bookie-discovery | `2026-07-31T18:51:24,951+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3181 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3181, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 49 | bookie-discovery | `2026-07-31T18:51:24,952+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3182 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3182, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 51 | bookie-discovery | `2026-07-31T18:51:24,958+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3181` |
| 53 | bookie-discovery | `2026-07-31T18:51:24,958+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3182` |
| 75 | bookie-discovery | `2026-07-31T18:51:25,125+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3181 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3181, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 76 | bookie-discovery | `2026-07-31T18:51:25,126+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3182 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3182, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 151 | bookie-channel | `2026-07-31T18:51:28,423+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3182 [id: 0x450017db, L:/127.0.0.1:40872 - R:127.0.0.1/127.0.0.1:3182]` |
| 152 | bookie-channel | `2026-07-31T18:51:28,424+0800 [pulsar-io-3-2] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3182 [id: 0x96a1c4f9, L:/127.0.0.1:40800 - R:127.0.0.1/127.0.0.1:3182]` |
| 153 | bookie-channel | `2026-07-31T18:51:28,427+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0x450017db, L:/127.0.0.1:40872 - R:127.0.0.1/127.0.0.1:3182] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 154 | bookie-channel | `2026-07-31T18:51:28,428+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3182 [id: 0x4418c9e9, L:/127.0.0.1:40886 - R:127.0.0.1/127.0.0.1:3182]` |
| 155 | bookie-channel | `2026-07-31T18:51:28,428+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0x4418c9e9, L:/127.0.0.1:40886 - R:127.0.0.1/127.0.0.1:3182] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 156 | bookie-channel | `2026-07-31T18:51:28,428+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3182 [id: 0xb6e85bda, L:/127.0.0.1:40892 - R:127.0.0.1/127.0.0.1:3182]` |
| 291 | managed-ledger | `2026-07-31T18:51:57,766+0800 [pulsar-service-shutdown] INFO  org.apache.bookkeeper.mledger.impl.ManagedLedgerImpl - [public/default/persistent/entrylog-ldpreload-round-05] Closing managed ledger` |
| 319 | managed-ledger | `2026-07-31T18:51:58,188+0800 [metadata-store-9-1] INFO  org.apache.bookkeeper.mledger.impl.ManagedLedgerFactoryImpl - Received MetadataStore session event: ConnectionLost` |
| 221 | broker-error | `2026-07-31T18:51:57,739+0800 [pulsar-io-3-1] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0xdfa8819b, L:/127.0.0.1:40898 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 222 | broker-error | `2026-07-31T18:51:57,739+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x96a1c4f9, L:/127.0.0.1:40800 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 223 | broker-error | `2026-07-31T18:51:57,739+0800 [pulsar-io-3-2] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Disconnected from bookie channel [id: 0x96a1c4f9, L:/127.0.0.1:40800 ! R:127.0.0.1/127.0.0.1:3182]` |
| 224 | broker-error | `2026-07-31T18:51:57,740+0800 [pulsar-io-3-1] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0xb6e85bda, L:/127.0.0.1:40892 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 225 | broker-error | `2026-07-31T18:51:57,740+0800 [pulsar-io-3-1] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x4418c9e9, L:/127.0.0.1:40886 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 226 | broker-error | `2026-07-31T18:51:57,740+0800 [pulsar-io-3-1] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x35ce6190, L:/127.0.0.1:40914 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |

### client

| line | tag | log |
|---:|---|---|
| 66 | client-progress | `2026-07-31T18:51:37,659+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:    9295 msg ---    929.5 msg/s ---     10.9 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:  10.706 ms - med:  10.704 - 95pct:  13.864 - 99pct:  16.441 - 99.9pct:  18.742 - 99.99pct:  20.408 - Max:  20.609` |
| 67 | client-progress | `2026-07-31T18:51:47,669+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:   19324 msg ---   1000.2 msg/s ---     11.7 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:  10.433 ms - med:  10.502 - 95pct:  13.033 - 99pct:  15.419 - 99.9pct:  20.262 - 99.99pct:  23.765 - Max:  24.591` |
| 89 | client-progress | `2026-07-31T18:51:57,683+0800 [Thread-0] INFO  org.apache.pulsar.testclient.PerformanceProducer - Aggregated throughput stats --- 28010 records sent --- 932.130 msg/s --- 10.923 Mbit/s ` |
| 90 | client-progress | `2026-07-31T18:51:57,697+0800 [Thread-0] INFO  org.apache.pulsar.testclient.PerformanceProducer - Aggregated latency stats --- Latency: mean:  10.519 ms - med:  10.560 - 95pct:  13.158 - 99pct:  15.577 - 99.9pct:  18.742 - 99.99pct:  22.721 - 99.999pct:  24.591 - Max:  24.591` |
| 68 | client-completion | `2026-07-31T18:51:56,341+0800 [pulsar-perf-producer-exec-1-1] INFO  org.apache.pulsar.testclient.PerformanceProducer - ------------- DONE (reached the maximum number: 28000 of production) --------------` |
| 91 | client-completion | `workload_rc=0` |
| 72 | client-error | `2026-07-31T18:51:57,674+0800 [pulsar-perf-producer-exec-1-1] ERROR org.apache.pulsar.testclient.PerformanceProducer - Failed to close test client` |
| 73 | client-error | `org.apache.pulsar.client.api.PulsarClientException: java.lang.InterruptedException` |
| 74 | client-error | `	at org.apache.pulsar.client.api.PulsarClientException.unwrap(PulsarClientException.java:1051) ~[org.apache.pulsar-pulsar-client-api-3.2.4.jar:3.2.4]` |
| 84 | client-error | `Caused by: java.lang.InterruptedException` |
