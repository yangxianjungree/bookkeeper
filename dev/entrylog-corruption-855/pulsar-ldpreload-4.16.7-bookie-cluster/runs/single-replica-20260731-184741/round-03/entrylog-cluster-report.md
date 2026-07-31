# Entrylog Cluster Report

- clusterDir: `/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runs/single-replica-20260731-184741/round-03`
- pulsarVersion: `3.2.4`
- bookieVersion: `4.16.7`
- bookieCount: `2`
- managedLedgerQuorum: `2/1/1`
- failpointEvents: `1`

## Failpoint Events

| kind | logId | logFile | logical | physical | bytes | op | offset | realRc | match | trigger |
|---|---:|---|---:|---:|---:|---|---:|---:|---:|---:|
| ldpreload | 2 | `/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/2.log` |  |  | 65536 | write | -1 | 65536 | 3 | 1 |

## Log Structure

| role | log | status | fileSize | headerMap | trueMap | delta | headerMapValid | entries | strict | prefix | post | parsedSize | mapSize | sizeMatch |
|---|---|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| bk1 | `0.log` | SEALED_OK | 124398 | 124358 | 124358 | 0 | True | 50 | 50 | None | None | 123334 | 123334 | True |
| bk1 | `1.log` | SEALED_OK | 130257 | 130217 | 130217 | 0 | True | 76 | 76 | None | None | 129193 | 129193 | True |
| bk1 | `10.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk1 | `11.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk1 | `12.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk1 | `13.log` | SEALED_OK | 129163 | 129123 | 129123 | 0 | True | 112 | 112 | None | None | 128099 | 128099 | True |
| bk1 | `14.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `15.log` | SEALED_OK | 130147 | 130107 | 130107 | 0 | True | 111 | 111 | None | None | 129083 | 129083 | True |
| bk1 | `16.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk1 | `17.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk1 | `18.log` | SEALED_OK | 131057 | 131017 | 131017 | 0 | True | 108 | 108 | None | None | 129993 | 129993 | True |
| bk1 | `19.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `1a.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk1 | `1b.log` | SEALED_OK | 130918 | 130878 | 130878 | 0 | True | 106 | 106 | None | None | 129854 | 129854 | True |
| bk1 | `1c.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `1d.log` | SEALED_OK | 130047 | 130007 | 130007 | 0 | True | 109 | 109 | None | None | 128983 | 128983 | True |
| bk1 | `1e.log` | SEALED_OK | 131057 | 131017 | 131017 | 0 | True | 108 | 108 | None | None | 129993 | 129993 | True |
| bk1 | `1f.log` | SEALED_OK | 130907 | 130867 | 130867 | 0 | True | 105 | 105 | None | None | 129843 | 129843 | True |
| bk1 | `2.log` | DRIFT_CHECK | 196669 | 130695 | 196629 | 65934 | False | 103 | None | 48 | 55 | 130764 | 129667 | False |
| bk1 | `20.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk1 | `21.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk1 | `22.log` | SEALED_OK | 130410 | 130370 | 130370 | 0 | True | 116 | 116 | None | None | 129346 | 129346 | True |
| bk1 | `23.log` | SEALED_OK | 130097 | 130057 | 130057 | 0 | True | 110 | 110 | None | None | 129033 | 129033 | True |
| bk1 | `24.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk1 | `25.log` | SEALED_OK | 130397 | 130357 | 130357 | 0 | True | 116 | 116 | None | None | 129333 | 129333 | True |
| bk1 | `26.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `27.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk1 | `28.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk1 | `29.log` | SEALED_OK | 127966 | 127926 | 127926 | 0 | True | 109 | 109 | None | None | 126902 | 126902 | True |
| bk1 | `2a.log` | SEALED_OK | 130247 | 130207 | 130207 | 0 | True | 113 | 113 | None | None | 129183 | 129183 | True |
| bk1 | `2b.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `2c.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `2d.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `2e.log` | SEALED_OK | 130768 | 130728 | 130728 | 0 | True | 103 | 103 | None | None | 129704 | 129704 | True |
| bk1 | `2f.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk1 | `3.log` | SEALED_OK | 130781 | 130741 | 130741 | 0 | True | 103 | 103 | None | None | 129717 | 129717 | True |
| bk1 | `30.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `31.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk1 | `32.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk1 | `33.log` | SEALED_OK | 130692 | 130652 | 130652 | 0 | True | 102 | 102 | None | None | 129628 | 129628 | True |
| bk1 | `34.log` | SEALED_OK | 130818 | 130778 | 130778 | 0 | True | 104 | 104 | None | None | 129754 | 129754 | True |
| bk1 | `35.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk1 | `36.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `37.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `38.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk1 | `39.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `3a.log` | SEALED_OK | 130460 | 130420 | 130420 | 0 | True | 117 | 117 | None | None | 129396 | 129396 | True |
| bk1 | `3b.log` | SEALED_OK | 129213 | 129173 | 129173 | 0 | True | 113 | 113 | None | None | 128149 | 128149 | True |
| bk1 | `3c.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk1 | `3d.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk1 | `3e.log` | SEALED_OK | 129013 | 128973 | 128973 | 0 | True | 109 | 109 | None | None | 127949 | 127949 | True |
| bk1 | `3f.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk1 | `4.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk1 | `40.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk1 | `41.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk1 | `42.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `43.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `44.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `45.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk1 | `46.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk1 | `47.log` | SEALED_OK | 130483 | 130443 | 130443 | 0 | True | 115 | 115 | None | None | 129419 | 129419 | True |
| bk1 | `48.log` | SEALED_OK | 130196 | 130156 | 130156 | 0 | True | 109 | 109 | None | None | 129132 | 129132 | True |
| bk1 | `49.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk1 | `4a.log` | SEALED_OK | 130388 | 130348 | 130348 | 0 | True | 113 | 113 | None | None | 129324 | 129324 | True |
| bk1 | `4b.log` | SEALED_OK | 131102 | 131062 | 131062 | 0 | True | 106 | 106 | None | None | 130038 | 130038 | True |
| bk1 | `4c.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk1 | `4d.log` | SEALED_OK | 130484 | 130444 | 130444 | 0 | True | 115 | 115 | None | None | 129420 | 129420 | True |
| bk1 | `4e.log` | SEALED_OK | 130388 | 130348 | 130348 | 0 | True | 113 | 113 | None | None | 129324 | 129324 | True |
| bk1 | `4f.log` | SEALED_OK | 130388 | 130348 | 130348 | 0 | True | 113 | 113 | None | None | 129324 | 129324 | True |
| bk1 | `5.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk1 | `50.log` | SEALED_OK | 130580 | 130540 | 130540 | 0 | True | 117 | 117 | None | None | 129516 | 129516 | True |
| bk1 | `51.log` | SEALED_OK | 130388 | 130348 | 130348 | 0 | True | 113 | 113 | None | None | 129324 | 129324 | True |
| bk1 | `52.log` | SEALED_OK | 130532 | 130492 | 130492 | 0 | True | 116 | 116 | None | None | 129468 | 129468 | True |
| bk1 | `53.log` | SEALED_OK | 130436 | 130396 | 130396 | 0 | True | 114 | 114 | None | None | 129372 | 129372 | True |
| bk1 | `54.log` | SEALED_OK | 130484 | 130444 | 130444 | 0 | True | 115 | 115 | None | None | 129420 | 129420 | True |
| bk1 | `55.log` | SEALED_OK | 130325 | 130285 | 130285 | 0 | True | 112 | 112 | None | None | 129261 | 129261 | True |
| bk1 | `56.log` | UNSEALED_OK | 41602 | 0 | None | None | False | 36 | 36 | None | None | None | None | None |
| bk1 | `6.log` | SEALED_OK | 130407 | 130367 | 130367 | 0 | True | 79 | 79 | None | None | 129343 | 129343 | True |
| bk1 | `7.log` | SEALED_OK | 129347 | 129307 | 129307 | 0 | True | 95 | 95 | None | None | 128283 | 128283 | True |
| bk1 | `8.log` | SEALED_OK | 130768 | 130728 | 130728 | 0 | True | 103 | 103 | None | None | 129704 | 129704 | True |
| bk1 | `9.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk1 | `a.log` | SEALED_OK | 129947 | 129907 | 129907 | 0 | True | 107 | 107 | None | None | 128883 | 128883 | True |
| bk1 | `b.log` | SEALED_OK | 130010 | 129970 | 129970 | 0 | True | 108 | 108 | None | None | 128946 | 128946 | True |
| bk1 | `c.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk1 | `d.log` | SEALED_OK | 129100 | 129060 | 129060 | 0 | True | 111 | 111 | None | None | 128036 | 128036 | True |
| bk1 | `e.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `f.log` | SEALED_OK | 130944 | 130904 | 130904 | 0 | True | 106 | 106 | None | None | 129880 | 129880 | True |
| bk2 | `0.log` | SEALED_OK | 130200 | 130160 | 130160 | 0 | True | 59 | 59 | None | None | 129136 | 129136 | True |
| bk2 | `1.log` | SEALED_OK | 130837 | 130797 | 130797 | 0 | True | 85 | 85 | None | None | 129773 | 129773 | True |
| bk2 | `10.log` | SEALED_OK | 131007 | 130967 | 130967 | 0 | True | 107 | 107 | None | None | 129943 | 129943 | True |
| bk2 | `11.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk2 | `12.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk2 | `13.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk2 | `14.log` | SEALED_OK | 131044 | 131004 | 131004 | 0 | True | 108 | 108 | None | None | 129980 | 129980 | True |
| bk2 | `15.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk2 | `16.log` | SEALED_OK | 130855 | 130815 | 130815 | 0 | True | 105 | 105 | None | None | 129791 | 129791 | True |
| bk2 | `17.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk2 | `18.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk2 | `19.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk2 | `1a.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk2 | `1b.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk2 | `1c.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk2 | `1d.log` | SEALED_OK | 129113 | 129073 | 129073 | 0 | True | 111 | 111 | None | None | 128049 | 128049 | True |
| bk2 | `1e.log` | SEALED_OK | 130047 | 130007 | 130007 | 0 | True | 109 | 109 | None | None | 128983 | 128983 | True |
| bk2 | `1f.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk2 | `2.log` | SEALED_OK | 130544 | 130504 | 130504 | 0 | True | 98 | 98 | None | None | 129480 | 129480 | True |
| bk2 | `20.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk2 | `21.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk2 | `22.log` | SEALED_OK | 130410 | 130370 | 130370 | 0 | True | 116 | 116 | None | None | 129346 | 129346 | True |
| bk2 | `23.log` | SEALED_OK | 131031 | 130991 | 130991 | 0 | True | 108 | 108 | None | None | 129967 | 129967 | True |
| bk2 | `24.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk2 | `25.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk2 | `26.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk2 | `27.log` | SEALED_OK | 130197 | 130157 | 130157 | 0 | True | 112 | 112 | None | None | 129133 | 129133 | True |
| bk2 | `28.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk2 | `29.log` | SEALED_OK | 130460 | 130420 | 130420 | 0 | True | 117 | 117 | None | None | 129396 | 129396 | True |
| bk2 | `2a.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk2 | `2b.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk2 | `2c.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk2 | `2d.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk2 | `2e.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk2 | `2f.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk2 | `3.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk2 | `30.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk2 | `31.log` | SEALED_OK | 130177 | 130137 | 130137 | 0 | True | 93 | 93 | None | None | 129113 | 129113 | True |
| bk2 | `32.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk2 | `33.log` | SEALED_OK | 130247 | 130207 | 130207 | 0 | True | 113 | 113 | None | None | 129183 | 129183 | True |
| bk2 | `34.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk2 | `35.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk2 | `36.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk2 | `37.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk2 | `38.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk2 | `39.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk2 | `3a.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk2 | `3b.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk2 | `3c.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk2 | `3d.log` | SEALED_OK | 130410 | 130370 | 130370 | 0 | True | 116 | 116 | None | None | 129346 | 129346 | True |
| bk2 | `3e.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk2 | `3f.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk2 | `4.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 107 | 107 | None | None | 129930 | 129930 | True |
| bk2 | `40.log` | SEALED_OK | 130197 | 130157 | 130157 | 0 | True | 112 | 112 | None | None | 129133 | 129133 | True |
| bk2 | `41.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk2 | `42.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk2 | `43.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk2 | `44.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk2 | `45.log` | SEALED_OK | 130470 | 130430 | 130430 | 0 | True | 115 | 115 | None | None | 129406 | 129406 | True |
| bk2 | `46.log` | SEALED_OK | 130133 | 130093 | 130093 | 0 | True | 108 | 108 | None | None | 129069 | 129069 | True |
| bk2 | `47.log` | SEALED_OK | 130292 | 130252 | 130252 | 0 | True | 111 | 111 | None | None | 129228 | 129228 | True |
| bk2 | `48.log` | SEALED_OK | 130436 | 130396 | 130396 | 0 | True | 114 | 114 | None | None | 129372 | 129372 | True |
| bk2 | `49.log` | SEALED_OK | 130421 | 130381 | 130381 | 0 | True | 114 | 114 | None | None | 129357 | 129357 | True |
| bk2 | `4a.log` | SEALED_OK | 130436 | 130396 | 130396 | 0 | True | 114 | 114 | None | None | 129372 | 129372 | True |
| bk2 | `4b.log` | SEALED_OK | 130292 | 130252 | 130252 | 0 | True | 111 | 111 | None | None | 129228 | 129228 | True |
| bk2 | `4c.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk2 | `4d.log` | SEALED_OK | 130436 | 130396 | 130396 | 0 | True | 114 | 114 | None | None | 129372 | 129372 | True |
| bk2 | `4e.log` | SEALED_OK | 130436 | 130396 | 130396 | 0 | True | 114 | 114 | None | None | 129372 | 129372 | True |
| bk2 | `4f.log` | SEALED_OK | 130292 | 130252 | 130252 | 0 | True | 111 | 111 | None | None | 129228 | 129228 | True |
| bk2 | `5.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk2 | `50.log` | SEALED_OK | 130277 | 130237 | 130237 | 0 | True | 111 | 111 | None | None | 129213 | 129213 | True |
| bk2 | `51.log` | SEALED_OK | 130292 | 130252 | 130252 | 0 | True | 111 | 111 | None | None | 129228 | 129228 | True |
| bk2 | `52.log` | SEALED_OK | 130388 | 130348 | 130348 | 0 | True | 113 | 113 | None | None | 129324 | 129324 | True |
| bk2 | `53.log` | SEALED_OK | 130388 | 130348 | 130348 | 0 | True | 113 | 113 | None | None | 129324 | 129324 | True |
| bk2 | `54.log` | UNSEALED_OK | 66808 | 0 | None | None | False | 58 | 58 | None | None | None | None | None |
| bk2 | `6.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk2 | `7.log` | SEALED_OK | 130794 | 130754 | 130754 | 0 | True | 103 | 103 | None | None | 129730 | 129730 | True |
| bk2 | `8.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk2 | `9.log` | SEALED_OK | 130655 | 130615 | 130615 | 0 | True | 101 | 101 | None | None | 129591 | 129591 | True |
| bk2 | `a.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk2 | `b.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk2 | `c.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk2 | `d.log` | SEALED_OK | 130034 | 129994 | 129994 | 0 | True | 109 | 109 | None | None | 128970 | 128970 | True |
| bk2 | `e.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk2 | `f.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |

## Replica Entry Comparison

Skipped: write quorum is smaller than ensemble size, so entries are intentionally single-copy distributed across bookies.

## Runtime Behavior

- clientExit: `0`

### bk1

| line | tag | log |
|---:|---|---|
| 141 | bookie-fault | `2026-07-31T18:49:33,164 - ERROR - [SyncThread-7-1:SyncThread@181] - Exception flushing ledgers` |
| 142 | bookie-fault | `java.io.IOException: Input/output error` |
| 134 | entrylog-io | `2026-07-31T18:49:32,165 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log for logId 0.` |
| 136 | entrylog-io | `2026-07-31T18:49:33,159 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log for logId 1.` |
| 137 | entrylog-io | `2026-07-31T18:49:33,159 - INFO  - [SyncThread-7-1:EntryLogManagerBase@165] - Flushing entry logger 0 back to filesystem, pending for syncing entry loggers : [BufferedChannel{logId=0, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log, ledgerIdAssigned=-1}].` |
| 139 | entrylog-io | `2026-07-31T18:49:33,163 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/2.log for logId 2.` |
| 140 | entrylog-io | `2026-07-31T18:49:33,163 - INFO  - [SyncThread-7-1:EntryLogManagerBase@165] - Flushing entry logger 1 back to filesystem, pending for syncing entry loggers : [BufferedChannel{logId=0, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log, ledgerIdAssigned=-1}, BufferedChannel{logId=1, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log, ledgerIdAssigned=-1}].` |
| 168 | entrylog-io | `2026-07-31T18:49:34,158 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/3.log for logId 3.` |
| 506 | bookie-lifecycle | `2026-07-31T18:50:01,417 - INFO  - [component-shutdown-thread:BookieServer@191] - Shutting down BookieServer` |
| 527 | bookie-lifecycle | `2026-07-31T18:50:01,442 - INFO  - [component-shutdown-thread:BookieImpl@861] - Turning bookie to read only during shut down` |
| 533 | bookie-lifecycle | `2026-07-31T18:50:01,458 - INFO  - [BookieJournal-3181:BookieImpl@828] - Triggering shutdown of Bookie-3181 with exitCode 5` |

### bk2

No matching log lines found.

### bk3

No matching log lines found.

### broker

| line | tag | log |
|---:|---|---|
| 33 | bk-client-init | `2026-07-31T18:49:28,413+0800 [main] INFO  org.apache.bookkeeper.meta.MetadataDrivers - BookKeeper metadata driver manager initialized` |
| 34 | bk-client-init | `2026-07-31T18:49:28,416+0800 [main] INFO  org.apache.pulsar.broker.BookKeeperClientFactoryImpl - Applying BookKeeper client configuration setting tlsHostnameVerificationEnabled=false` |
| 61 | bk-client-init | `2026-07-31T18:49:28,702+0800 [main] INFO  org.apache.pulsar.broker.BookKeeperClientFactoryImpl - Applying BookKeeper client configuration setting tlsHostnameVerificationEnabled=false` |
| 48 | bookie-discovery | `2026-07-31T18:49:28,545+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3181 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3181, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 49 | bookie-discovery | `2026-07-31T18:49:28,545+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3182 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3182, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 51 | bookie-discovery | `2026-07-31T18:49:28,554+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3181` |
| 53 | bookie-discovery | `2026-07-31T18:49:28,554+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3182` |
| 75 | bookie-discovery | `2026-07-31T18:49:28,717+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3181 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3181, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 76 | bookie-discovery | `2026-07-31T18:49:28,717+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3182 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3182, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 151 | bookie-channel | `2026-07-31T18:49:32,033+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3182 [id: 0x5824f842, L:/127.0.0.1:44166 - R:127.0.0.1/127.0.0.1:3182]` |
| 152 | bookie-channel | `2026-07-31T18:49:32,034+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0x5824f842, L:/127.0.0.1:44166 - R:127.0.0.1/127.0.0.1:3182] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 153 | bookie-channel | `2026-07-31T18:49:32,035+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3182 [id: 0x6fcaa711, L:/127.0.0.1:44184 - R:127.0.0.1/127.0.0.1:3182]` |
| 154 | bookie-channel | `2026-07-31T18:49:32,035+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0x6fcaa711, L:/127.0.0.1:44184 - R:127.0.0.1/127.0.0.1:3182] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 155 | bookie-channel | `2026-07-31T18:49:32,035+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3182 [id: 0xdcc2d484, L:/127.0.0.1:44192 - R:127.0.0.1/127.0.0.1:3182]` |
| 156 | bookie-channel | `2026-07-31T18:49:32,035+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0xdcc2d484, L:/127.0.0.1:44192 - R:127.0.0.1/127.0.0.1:3182] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 317 | managed-ledger | `2026-07-31T18:50:01,867+0800 [metadata-store-9-1] INFO  org.apache.bookkeeper.mledger.impl.ManagedLedgerFactoryImpl - Received MetadataStore session event: ConnectionLost` |
| 221 | broker-error | `2026-07-31T18:50:01,416+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x0e9c1c0e, L:/127.0.0.1:44280 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 222 | broker-error | `2026-07-31T18:50:01,417+0800 [pulsar-io-3-2] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Disconnected from bookie channel [id: 0x0e9c1c0e, L:/127.0.0.1:44280 ! R:127.0.0.1/127.0.0.1:3182]` |
| 223 | broker-error | `2026-07-31T18:50:01,417+0800 [pulsar-io-3-1] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x77137369, L:/127.0.0.1:44202 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 224 | broker-error | `2026-07-31T18:50:01,417+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Disconnected from bookie channel [id: 0x77137369, L:/127.0.0.1:44202 ! R:127.0.0.1/127.0.0.1:3182]` |
| 226 | broker-error | `2026-07-31T18:50:01,430+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0xadbbf3e3, L:/127.0.0.1:44296 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |
| 227 | broker-error | `2026-07-31T18:50:01,430+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x72b9d912, L:/127.0.0.1:44266 - R:127.0.0.1/127.0.0.1:3182] cause: recvAddress(..) failed: Connection reset by peer` |

### client

| line | tag | log |
|---:|---|---|
| 66 | client-progress | `2026-07-31T18:49:41,341+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:    8448 msg ---    844.8 msg/s ---      6.6 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:   7.551 ms - med:   7.055 - 95pct:  11.600 - 99pct:  15.751 - 99.9pct:  41.869 - 99.99pct:  49.751 - Max:  50.910` |
| 67 | client-progress | `2026-07-31T18:49:51,356+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:   17487 msg ---    900.2 msg/s ---      7.0 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:   7.247 ms - med:   6.829 - 95pct:  10.788 - 99pct:  14.299 - 99.9pct:  51.962 - 99.99pct:  56.689 - Max:  57.676` |
| 72 | client-progress | `2026-07-31T18:50:01,360+0800 [Thread-0] INFO  org.apache.pulsar.testclient.PerformanceProducer - Aggregated throughput stats --- 20007 records sent --- 665.647 msg/s --- 5.200 Mbit/s ` |
| 73 | client-progress | `2026-07-31T18:50:01,378+0800 [Thread-0] INFO  org.apache.pulsar.testclient.PerformanceProducer - Aggregated latency stats --- Latency: mean:   7.325 ms - med:   6.908 - 95pct:  10.982 - 99pct:  14.638 - 99.9pct:  47.322 - 99.99pct:  56.539 - 99.999pct:  57.676 - Max:  57.676` |
| 68 | client-completion | `2026-07-31T18:49:54,144+0800 [pulsar-perf-producer-exec-1-1] INFO  org.apache.pulsar.testclient.PerformanceProducer - ------------- DONE (reached the maximum number: 20000 of production) --------------` |
| 74 | client-completion | `workload_rc=0` |
