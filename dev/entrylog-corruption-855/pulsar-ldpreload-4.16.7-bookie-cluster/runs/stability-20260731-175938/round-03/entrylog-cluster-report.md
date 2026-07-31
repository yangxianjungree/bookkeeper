# Entrylog Cluster Report

- clusterDir: `/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runs/stability-20260731-175938/round-03`
- pulsarVersion: `3.2.4`
- bookieVersion: `4.16.7`
- bookieCount: `3`
- managedLedgerQuorum: `3/3/2`
- failpointEvents: `1`

## Failpoint Events

| kind | logId | logFile | logical | physical | bytes | op | offset | realRc | match | trigger |
|---|---:|---|---:|---:|---:|---|---:|---:|---:|---:|
| ldpreload | 1 | `/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log` |  |  | 65536 | write | -1 | 65536 | 3 | 1 |

## Log Structure

| role | log | status | fileSize | headerMap | trueMap | delta | headerMapValid | entries | strict | prefix | post | parsedSize | mapSize | sizeMatch |
|---|---|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| bk1 | `0.log` | SEALED_OK | 130159 | 130119 | 130119 | 0 | True | 44 | 44 | None | None | 129095 | 129095 | True |
| bk1 | `1.log` | DRIFT_CHECK | 199773 | 130125 | 199733 | 69608 | False | 76 | None | 22 | 54 | 136411 | 129097 | False |
| bk1 | `10.log` | SEALED_OK | 130134 | 130094 | 130094 | 0 | True | 111 | 111 | None | None | 129070 | 129070 | True |
| bk1 | `11.log` | SEALED_OK | 130021 | 129981 | 129981 | 0 | True | 109 | 109 | None | None | 128957 | 128957 | True |
| bk1 | `12.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 107 | 107 | None | None | 129930 | 129930 | True |
| bk1 | `13.log` | SEALED_OK | 131081 | 131041 | 131041 | 0 | True | 109 | 109 | None | None | 130017 | 130017 | True |
| bk1 | `14.log` | SEALED_OK | 130681 | 130641 | 130641 | 0 | True | 101 | 101 | None | None | 129617 | 129617 | True |
| bk1 | `15.log` | SEALED_OK | 130907 | 130867 | 130867 | 0 | True | 105 | 105 | None | None | 129843 | 129843 | True |
| bk1 | `16.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk1 | `17.log` | SEALED_OK | 130631 | 130591 | 130591 | 0 | True | 100 | 100 | None | None | 129567 | 129567 | True |
| bk1 | `18.log` | SEALED_OK | 129834 | 129794 | 129794 | 0 | True | 105 | 105 | None | None | 128770 | 128770 | True |
| bk1 | `19.log` | SEALED_OK | 131094 | 131054 | 131054 | 0 | True | 109 | 109 | None | None | 130030 | 130030 | True |
| bk1 | `1a.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk1 | `1b.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk1 | `1c.log` | SEALED_OK | 131094 | 131054 | 131054 | 0 | True | 109 | 109 | None | None | 130030 | 130030 | True |
| bk1 | `1d.log` | SEALED_OK | 130981 | 130941 | 130941 | 0 | True | 107 | 107 | None | None | 129917 | 129917 | True |
| bk1 | `1e.log` | SEALED_OK | 130605 | 130565 | 130565 | 0 | True | 100 | 100 | None | None | 129541 | 129541 | True |
| bk1 | `1f.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk1 | `2.log` | SEALED_OK | 130392 | 130352 | 130352 | 0 | True | 96 | 96 | None | None | 129328 | 129328 | True |
| bk1 | `20.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk1 | `21.log` | SEALED_OK | 130460 | 130420 | 130420 | 0 | True | 117 | 117 | None | None | 129396 | 129396 | True |
| bk1 | `22.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk1 | `23.log` | SEALED_OK | 130794 | 130754 | 130754 | 0 | True | 103 | 103 | None | None | 129730 | 129730 | True |
| bk1 | `24.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `25.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk1 | `26.log` | SEALED_OK | 130807 | 130767 | 130767 | 0 | True | 103 | 103 | None | None | 129743 | 129743 | True |
| bk1 | `27.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `28.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk1 | `29.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk1 | `2a.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk1 | `2b.log` | SEALED_OK | 131007 | 130967 | 130967 | 0 | True | 107 | 107 | None | None | 129943 | 129943 | True |
| bk1 | `2c.log` | SEALED_OK | 129013 | 128973 | 128973 | 0 | True | 109 | 109 | None | None | 127949 | 127949 | True |
| bk1 | `2d.log` | SEALED_OK | 130794 | 130754 | 130754 | 0 | True | 103 | 103 | None | None | 129730 | 129730 | True |
| bk1 | `2e.log` | SEALED_OK | 130097 | 130057 | 130057 | 0 | True | 110 | 110 | None | None | 129033 | 129033 | True |
| bk1 | `2f.log` | SEALED_OK | 131044 | 131004 | 131004 | 0 | True | 108 | 108 | None | None | 129980 | 129980 | True |
| bk1 | `3.log` | SEALED_OK | 128252 | 128212 | 128212 | 0 | True | 77 | 77 | None | None | 127188 | 127188 | True |
| bk1 | `30.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk1 | `31.log` | SEALED_OK | 131094 | 131054 | 131054 | 0 | True | 109 | 109 | None | None | 130030 | 130030 | True |
| bk1 | `32.log` | SEALED_OK | 129213 | 129173 | 129173 | 0 | True | 113 | 113 | None | None | 128149 | 128149 | True |
| bk1 | `33.log` | SEALED_OK | 131007 | 130967 | 130967 | 0 | True | 107 | 107 | None | None | 129943 | 129943 | True |
| bk1 | `34.log` | SEALED_OK | 131057 | 131017 | 131017 | 0 | True | 108 | 108 | None | None | 129993 | 129993 | True |
| bk1 | `35.log` | SEALED_OK | 130266 | 130226 | 130226 | 0 | True | 94 | 94 | None | None | 129202 | 129202 | True |
| bk1 | `36.log` | SEALED_OK | 130329 | 130289 | 130289 | 0 | True | 95 | 95 | None | None | 129265 | 129265 | True |
| bk1 | `37.log` | SEALED_OK | 130242 | 130202 | 130202 | 0 | True | 93 | 93 | None | None | 129178 | 129178 | True |
| bk1 | `38.log` | SEALED_OK | 130177 | 130137 | 130137 | 0 | True | 93 | 93 | None | None | 129113 | 129113 | True |
| bk1 | `39.log` | SEALED_OK | 130744 | 130704 | 130704 | 0 | True | 102 | 102 | None | None | 129680 | 129680 | True |
| bk1 | `3a.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk1 | `3b.log` | SEALED_OK | 130957 | 130917 | 130917 | 0 | True | 106 | 106 | None | None | 129893 | 129893 | True |
| bk1 | `3c.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk1 | `3d.log` | SEALED_OK | 130510 | 130470 | 130470 | 0 | True | 118 | 118 | None | None | 129446 | 129446 | True |
| bk1 | `3e.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `3f.log` | SEALED_OK | 129721 | 129681 | 129681 | 0 | True | 103 | 103 | None | None | 128657 | 128657 | True |
| bk1 | `4.log` | SEALED_OK | 130618 | 130578 | 130578 | 0 | True | 100 | 100 | None | None | 129554 | 129554 | True |
| bk1 | `40.log` | SEALED_OK | 130868 | 130828 | 130828 | 0 | True | 105 | 105 | None | None | 129804 | 129804 | True |
| bk1 | `41.log` | SEALED_OK | 130731 | 130691 | 130691 | 0 | True | 102 | 102 | None | None | 129667 | 129667 | True |
| bk1 | `42.log` | SEALED_OK | 130881 | 130841 | 130841 | 0 | True | 105 | 105 | None | None | 129817 | 129817 | True |
| bk1 | `43.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 107 | 107 | None | None | 129930 | 129930 | True |
| bk1 | `44.log` | SEALED_OK | 130047 | 130007 | 130007 | 0 | True | 109 | 109 | None | None | 128983 | 128983 | True |
| bk1 | `45.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk1 | `46.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk1 | `47.log` | SEALED_OK | 129910 | 129870 | 129870 | 0 | True | 106 | 106 | None | None | 128846 | 128846 | True |
| bk1 | `48.log` | SEALED_OK | 130227 | 130187 | 130187 | 0 | True | 94 | 94 | None | None | 129163 | 129163 | True |
| bk1 | `49.log` | SEALED_OK | 130894 | 130854 | 130854 | 0 | True | 105 | 105 | None | None | 129830 | 129830 | True |
| bk1 | `4a.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk1 | `4b.log` | SEALED_OK | 130616 | 130576 | 130576 | 0 | True | 101 | 101 | None | None | 129552 | 129552 | True |
| bk1 | `4c.log` | SEALED_OK | 130944 | 130904 | 130904 | 0 | True | 106 | 106 | None | None | 129880 | 129880 | True |
| bk1 | `4d.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk1 | `4e.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk1 | `4f.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk1 | `5.log` | SEALED_OK | 130705 | 130665 | 130665 | 0 | True | 102 | 102 | None | None | 129641 | 129641 | True |
| bk1 | `50.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk1 | `51.log` | SEALED_OK | 130857 | 130817 | 130817 | 0 | True | 104 | 104 | None | None | 129793 | 129793 | True |
| bk1 | `52.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk1 | `53.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk1 | `54.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk1 | `55.log` | SEALED_OK | 131094 | 131054 | 131054 | 0 | True | 109 | 109 | None | None | 130030 | 130030 | True |
| bk1 | `56.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk1 | `57.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk1 | `58.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk1 | `59.log` | SEALED_OK | 130866 | 130826 | 130826 | 0 | True | 106 | 106 | None | None | 129802 | 129802 | True |
| bk1 | `5a.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk1 | `5b.log` | SEALED_OK | 129063 | 129023 | 129023 | 0 | True | 110 | 110 | None | None | 127999 | 127999 | True |
| bk1 | `5c.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk1 | `5d.log` | SEALED_OK | 130047 | 130007 | 130007 | 0 | True | 109 | 109 | None | None | 128983 | 128983 | True |
| bk1 | `5e.log` | SEALED_OK | 130410 | 130370 | 130370 | 0 | True | 116 | 116 | None | None | 129346 | 129346 | True |
| bk1 | `5f.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk1 | `6.log` | SEALED_OK | 130594 | 130554 | 130554 | 0 | True | 99 | 99 | None | None | 129530 | 129530 | True |
| bk1 | `60.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk1 | `61.log` | SEALED_OK | 131031 | 130991 | 130991 | 0 | True | 108 | 108 | None | None | 129967 | 129967 | True |
| bk1 | `62.log` | SEALED_OK | 131057 | 131017 | 131017 | 0 | True | 108 | 108 | None | None | 129993 | 129993 | True |
| bk1 | `63.log` | SEALED_OK | 131044 | 131004 | 131004 | 0 | True | 108 | 108 | None | None | 129980 | 129980 | True |
| bk1 | `64.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk1 | `65.log` | SEALED_OK | 130510 | 130470 | 130470 | 0 | True | 118 | 118 | None | None | 129446 | 129446 | True |
| bk1 | `66.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk1 | `67.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `68.log` | SEALED_OK | 130410 | 130370 | 130370 | 0 | True | 116 | 116 | None | None | 129346 | 129346 | True |
| bk1 | `69.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk1 | `6a.log` | SEALED_OK | 130347 | 130307 | 130307 | 0 | True | 115 | 115 | None | None | 129283 | 129283 | True |
| bk1 | `6b.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk1 | `6c.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk1 | `6d.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk1 | `6e.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk1 | `6f.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk1 | `7.log` | SEALED_OK | 130718 | 130678 | 130678 | 0 | True | 102 | 102 | None | None | 129654 | 129654 | True |
| bk1 | `70.log` | SEALED_OK | 131057 | 131017 | 131017 | 0 | True | 108 | 108 | None | None | 129993 | 129993 | True |
| bk1 | `71.log` | SEALED_OK | 130831 | 130791 | 130791 | 0 | True | 104 | 104 | None | None | 129767 | 129767 | True |
| bk1 | `72.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk1 | `73.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk1 | `74.log` | SEALED_OK | 130410 | 130370 | 130370 | 0 | True | 116 | 116 | None | None | 129346 | 129346 | True |
| bk1 | `75.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk1 | `76.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk1 | `77.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk1 | `78.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk1 | `79.log` | SEALED_OK | 130147 | 130107 | 130107 | 0 | True | 111 | 111 | None | None | 129083 | 129083 | True |
| bk1 | `7a.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk1 | `7b.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk1 | `7c.log` | SEALED_OK | 131057 | 131017 | 131017 | 0 | True | 108 | 108 | None | None | 129993 | 129993 | True |
| bk1 | `7d.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk1 | `7e.log` | SEALED_OK | 130460 | 130420 | 130420 | 0 | True | 117 | 117 | None | None | 129396 | 129396 | True |
| bk1 | `7f.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk1 | `8.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk1 | `80.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk1 | `81.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk1 | `82.log` | SEALED_OK | 131007 | 130967 | 130967 | 0 | True | 107 | 107 | None | None | 129943 | 129943 | True |
| bk1 | `83.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk1 | `84.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk1 | `85.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk1 | `86.log` | SEALED_OK | 131044 | 131004 | 131004 | 0 | True | 108 | 108 | None | None | 129980 | 129980 | True |
| bk1 | `87.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk1 | `88.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk1 | `89.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk1 | `8a.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk1 | `8b.log` | SEALED_OK | 130386 | 130346 | 130346 | 0 | True | 115 | 115 | None | None | 129322 | 129322 | True |
| bk1 | `8c.log` | SEALED_OK | 130532 | 130492 | 130492 | 0 | True | 116 | 116 | None | None | 129468 | 129468 | True |
| bk1 | `8d.log` | SEALED_OK | 130436 | 130396 | 130396 | 0 | True | 114 | 114 | None | None | 129372 | 129372 | True |
| bk1 | `8e.log` | SEALED_OK | 130181 | 130141 | 130141 | 0 | True | 109 | 109 | None | None | 129117 | 129117 | True |
| bk1 | `8f.log` | SEALED_OK | 130388 | 130348 | 130348 | 0 | True | 113 | 113 | None | None | 129324 | 129324 | True |
| bk1 | `9.log` | SEALED_OK | 127243 | 127203 | 127203 | 0 | True | 47 | 47 | None | None | 126179 | 126179 | True |
| bk1 | `90.log` | SEALED_OK | 130436 | 130396 | 130396 | 0 | True | 114 | 114 | None | None | 129372 | 129372 | True |
| bk1 | `91.log` | SEALED_OK | 129275 | 129235 | 129235 | 0 | True | 112 | 112 | None | None | 128211 | 128211 | True |
| bk1 | `92.log` | SEALED_OK | 130244 | 130204 | 130204 | 0 | True | 110 | 110 | None | None | 129180 | 129180 | True |
| bk1 | `93.log` | SEALED_OK | 130484 | 130444 | 130444 | 0 | True | 115 | 115 | None | None | 129420 | 129420 | True |
| bk1 | `94.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk1 | `95.log` | SEALED_OK | 130325 | 130285 | 130285 | 0 | True | 112 | 112 | None | None | 129261 | 129261 | True |
| bk1 | `96.log` | SEALED_OK | 130196 | 130156 | 130156 | 0 | True | 109 | 109 | None | None | 129132 | 129132 | True |
| bk1 | `97.log` | SEALED_OK | 130292 | 130252 | 130252 | 0 | True | 111 | 111 | None | None | 129228 | 129228 | True |
| bk1 | `98.log` | SEALED_OK | 130196 | 130156 | 130156 | 0 | True | 109 | 109 | None | None | 129132 | 129132 | True |
| bk1 | `99.log` | SEALED_OK | 130292 | 130252 | 130252 | 0 | True | 111 | 111 | None | None | 129228 | 129228 | True |
| bk1 | `9a.log` | SEALED_OK | 130214 | 130174 | 130174 | 0 | True | 110 | 110 | None | None | 129150 | 129150 | True |
| bk1 | `9b.log` | SEALED_OK | 130628 | 130588 | 130588 | 0 | True | 118 | 118 | None | None | 129564 | 129564 | True |
| bk1 | `9c.log` | SEALED_OK | 130292 | 130252 | 130252 | 0 | True | 111 | 111 | None | None | 129228 | 129228 | True |
| bk1 | `9d.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk1 | `9e.log` | SEALED_OK | 130991 | 130951 | 130951 | 0 | True | 104 | 104 | None | None | 129927 | 129927 | True |
| bk1 | `9f.log` | SEALED_OK | 130037 | 129997 | 129997 | 0 | True | 106 | 106 | None | None | 128973 | 128973 | True |
| bk1 | `a.log` | SEALED_OK | 129751 | 129711 | 129711 | 0 | True | 51 | 51 | None | None | 128687 | 128687 | True |
| bk1 | `a0.log` | SEALED_OK | 130100 | 130060 | 130060 | 0 | True | 107 | 107 | None | None | 129036 | 129036 | True |
| bk1 | `a1.log` | SEALED_OK | 130196 | 130156 | 130156 | 0 | True | 109 | 109 | None | None | 129132 | 129132 | True |
| bk1 | `a2.log` | SEALED_OK | 129194 | 129154 | 129154 | 0 | True | 110 | 110 | None | None | 128130 | 128130 | True |
| bk1 | `a3.log` | SEALED_OK | 130196 | 130156 | 130156 | 0 | True | 109 | 109 | None | None | 129132 | 129132 | True |
| bk1 | `a4.log` | SEALED_OK | 130436 | 130396 | 130396 | 0 | True | 114 | 114 | None | None | 129372 | 129372 | True |
| bk1 | `a5.log` | SEALED_OK | 130910 | 130870 | 130870 | 0 | True | 102 | 102 | None | None | 129846 | 129846 | True |
| bk1 | `a6.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk1 | `a7.log` | SEALED_OK | 130484 | 130444 | 130444 | 0 | True | 115 | 115 | None | None | 129420 | 129420 | True |
| bk1 | `a8.log` | SEALED_OK | 130196 | 130156 | 130156 | 0 | True | 109 | 109 | None | None | 129132 | 129132 | True |
| bk1 | `a9.log` | SEALED_OK | 130244 | 130204 | 130204 | 0 | True | 110 | 110 | None | None | 129180 | 129180 | True |
| bk1 | `aa.log` | UNSEALED_OK | 67954 | 0 | None | None | False | 60 | 60 | None | None | None | None | None |
| bk1 | `b.log` | SEALED_OK | 130374 | 130334 | 130334 | 0 | True | 60 | 60 | None | None | 129310 | 129310 | True |
| bk1 | `c.log` | SEALED_OK | 130928 | 130888 | 130888 | 0 | True | 85 | 85 | None | None | 129864 | 129864 | True |
| bk1 | `d.log` | SEALED_OK | 129790 | 129750 | 129750 | 0 | True | 85 | 85 | None | None | 128726 | 128726 | True |
| bk1 | `e.log` | SEALED_OK | 130557 | 130517 | 130517 | 0 | True | 98 | 98 | None | None | 129493 | 129493 | True |
| bk1 | `f.log` | SEALED_OK | 130857 | 130817 | 130817 | 0 | True | 104 | 104 | None | None | 129793 | 129793 | True |
| bk2 | `0.log` | SEALED_OK | 130159 | 130119 | 130119 | 0 | True | 44 | 44 | None | None | 129095 | 129095 | True |
| bk2 | `1.log` | SEALED_OK | 130871 | 130831 | 130831 | 0 | True | 52 | 52 | None | None | 129807 | 129807 | True |
| bk2 | `10.log` | SEALED_OK | 130655 | 130615 | 130615 | 0 | True | 101 | 101 | None | None | 129591 | 129591 | True |
| bk2 | `11.log` | SEALED_OK | 130034 | 129994 | 129994 | 0 | True | 109 | 109 | None | None | 128970 | 128970 | True |
| bk2 | `12.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk2 | `13.log` | SEALED_OK | 130581 | 130541 | 130541 | 0 | True | 99 | 99 | None | None | 129517 | 129517 | True |
| bk2 | `14.log` | SEALED_OK | 131007 | 130967 | 130967 | 0 | True | 107 | 107 | None | None | 129943 | 129943 | True |
| bk2 | `15.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 107 | 107 | None | None | 129930 | 129930 | True |
| bk2 | `16.log` | SEALED_OK | 129671 | 129631 | 129631 | 0 | True | 102 | 102 | None | None | 128607 | 128607 | True |
| bk2 | `17.log` | SEALED_OK | 130894 | 130854 | 130854 | 0 | True | 105 | 105 | None | None | 129830 | 129830 | True |
| bk2 | `18.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk2 | `19.log` | SEALED_OK | 130460 | 130420 | 130420 | 0 | True | 117 | 117 | None | None | 129396 | 129396 | True |
| bk2 | `1a.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk2 | `1b.log` | SEALED_OK | 130981 | 130941 | 130941 | 0 | True | 107 | 107 | None | None | 129917 | 129917 | True |
| bk2 | `1c.log` | SEALED_OK | 129295 | 129255 | 129255 | 0 | True | 95 | 95 | None | None | 128231 | 128231 | True |
| bk2 | `1d.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk2 | `1e.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk2 | `1f.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk2 | `2.log` | SEALED_OK | 130626 | 130586 | 130586 | 0 | True | 64 | 64 | None | None | 129562 | 129562 | True |
| bk2 | `20.log` | SEALED_OK | 130410 | 130370 | 130370 | 0 | True | 116 | 116 | None | None | 129346 | 129346 | True |
| bk2 | `21.log` | SEALED_OK | 130857 | 130817 | 130817 | 0 | True | 104 | 104 | None | None | 129793 | 129793 | True |
| bk2 | `22.log` | SEALED_OK | 130197 | 130157 | 130157 | 0 | True | 112 | 112 | None | None | 129133 | 129133 | True |
| bk2 | `23.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk2 | `24.log` | SEALED_OK | 129810 | 129770 | 129770 | 0 | True | 104 | 104 | None | None | 128746 | 128746 | True |
| bk2 | `25.log` | SEALED_OK | 129960 | 129920 | 129920 | 0 | True | 107 | 107 | None | None | 128896 | 128896 | True |
| bk2 | `26.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk2 | `27.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk2 | `28.log` | SEALED_OK | 131007 | 130967 | 130967 | 0 | True | 107 | 107 | None | None | 129943 | 129943 | True |
| bk2 | `29.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk2 | `2a.log` | SEALED_OK | 130907 | 130867 | 130867 | 0 | True | 105 | 105 | None | None | 129843 | 129843 | True |
| bk2 | `2b.log` | SEALED_OK | 130844 | 130804 | 130804 | 0 | True | 104 | 104 | None | None | 129780 | 129780 | True |
| bk2 | `2c.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk2 | `2d.log` | SEALED_OK | 130084 | 130044 | 130044 | 0 | True | 110 | 110 | None | None | 129020 | 129020 | True |
| bk2 | `2e.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk2 | `2f.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk2 | `3.log` | SEALED_OK | 130978 | 130938 | 130938 | 0 | True | 86 | 86 | None | None | 129914 | 129914 | True |
| bk2 | `30.log` | SEALED_OK | 130147 | 130107 | 130107 | 0 | True | 111 | 111 | None | None | 129083 | 129083 | True |
| bk2 | `31.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk2 | `32.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk2 | `33.log` | SEALED_OK | 130694 | 130654 | 130654 | 0 | True | 101 | 101 | None | None | 129630 | 129630 | True |
| bk2 | `34.log` | SEALED_OK | 130253 | 130213 | 130213 | 0 | True | 94 | 94 | None | None | 129189 | 129189 | True |
| bk2 | `35.log` | SEALED_OK | 130429 | 130389 | 130389 | 0 | True | 97 | 97 | None | None | 129365 | 129365 | True |
| bk2 | `36.log` | SEALED_OK | 130255 | 130215 | 130215 | 0 | True | 93 | 93 | None | None | 129191 | 129191 | True |
| bk2 | `37.log` | SEALED_OK | 130177 | 130137 | 130137 | 0 | True | 93 | 93 | None | None | 129113 | 129113 | True |
| bk2 | `38.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk2 | `39.log` | SEALED_OK | 131007 | 130967 | 130967 | 0 | True | 107 | 107 | None | None | 129943 | 129943 | True |
| bk2 | `3a.log` | SEALED_OK | 131007 | 130967 | 130967 | 0 | True | 107 | 107 | None | None | 129943 | 129943 | True |
| bk2 | `3b.log` | SEALED_OK | 130410 | 130370 | 130370 | 0 | True | 116 | 116 | None | None | 129346 | 129346 | True |
| bk2 | `3c.log` | SEALED_OK | 130410 | 130370 | 130370 | 0 | True | 116 | 116 | None | None | 129346 | 129346 | True |
| bk2 | `3d.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk2 | `3e.log` | SEALED_OK | 129545 | 129505 | 129505 | 0 | True | 100 | 100 | None | None | 128481 | 128481 | True |
| bk2 | `3f.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 107 | 107 | None | None | 129930 | 129930 | True |
| bk2 | `4.log` | SEALED_OK | 130837 | 130797 | 130797 | 0 | True | 85 | 85 | None | None | 129773 | 129773 | True |
| bk2 | `40.log` | SEALED_OK | 129621 | 129581 | 129581 | 0 | True | 101 | 101 | None | None | 128557 | 128557 | True |
| bk2 | `41.log` | SEALED_OK | 130781 | 130741 | 130741 | 0 | True | 103 | 103 | None | None | 129717 | 129717 | True |
| bk2 | `42.log` | SEALED_OK | 130047 | 130007 | 130007 | 0 | True | 109 | 109 | None | None | 128983 | 128983 | True |
| bk2 | `43.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk2 | `44.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk2 | `45.log` | SEALED_OK | 131007 | 130967 | 130967 | 0 | True | 107 | 107 | None | None | 129943 | 129943 | True |
| bk2 | `46.log` | SEALED_OK | 130844 | 130804 | 130804 | 0 | True | 104 | 104 | None | None | 129780 | 129780 | True |
| bk2 | `47.log` | SEALED_OK | 130177 | 130137 | 130137 | 0 | True | 93 | 93 | None | None | 129113 | 129113 | True |
| bk2 | `48.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk2 | `49.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk2 | `4a.log` | SEALED_OK | 129419 | 129379 | 129379 | 0 | True | 98 | 98 | None | None | 128355 | 128355 | True |
| bk2 | `4b.log` | SEALED_OK | 130097 | 130057 | 130057 | 0 | True | 110 | 110 | None | None | 129033 | 129033 | True |
| bk2 | `4c.log` | SEALED_OK | 131007 | 130967 | 130967 | 0 | True | 107 | 107 | None | None | 129943 | 129943 | True |
| bk2 | `4d.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk2 | `4e.log` | SEALED_OK | 130460 | 130420 | 130420 | 0 | True | 117 | 117 | None | None | 129396 | 129396 | True |
| bk2 | `4f.log` | SEALED_OK | 131057 | 131017 | 131017 | 0 | True | 108 | 108 | None | None | 129993 | 129993 | True |
| bk2 | `5.log` | SEALED_OK | 130457 | 130417 | 130417 | 0 | True | 96 | 96 | None | None | 129393 | 129393 | True |
| bk2 | `50.log` | SEALED_OK | 131007 | 130967 | 130967 | 0 | True | 107 | 107 | None | None | 129943 | 129943 | True |
| bk2 | `51.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk2 | `52.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk2 | `53.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk2 | `54.log` | SEALED_OK | 130047 | 130007 | 130007 | 0 | True | 109 | 109 | None | None | 128983 | 128983 | True |
| bk2 | `55.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk2 | `56.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk2 | `57.log` | SEALED_OK | 131016 | 130976 | 130976 | 0 | True | 109 | 109 | None | None | 129952 | 129952 | True |
| bk2 | `58.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk2 | `59.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk2 | `5a.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk2 | `5b.log` | SEALED_OK | 130097 | 130057 | 130057 | 0 | True | 110 | 110 | None | None | 129033 | 129033 | True |
| bk2 | `5c.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk2 | `5d.log` | SEALED_OK | 129313 | 129273 | 129273 | 0 | True | 115 | 115 | None | None | 128249 | 128249 | True |
| bk2 | `5e.log` | SEALED_OK | 129760 | 129720 | 129720 | 0 | True | 103 | 103 | None | None | 128696 | 128696 | True |
| bk2 | `5f.log` | SEALED_OK | 130034 | 129994 | 129994 | 0 | True | 109 | 109 | None | None | 128970 | 128970 | True |
| bk2 | `6.log` | SEALED_OK | 130605 | 130565 | 130565 | 0 | True | 100 | 100 | None | None | 129541 | 129541 | True |
| bk2 | `60.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk2 | `61.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 107 | 107 | None | None | 129930 | 129930 | True |
| bk2 | `62.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk2 | `63.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk2 | `64.log` | SEALED_OK | 130410 | 130370 | 130370 | 0 | True | 116 | 116 | None | None | 129346 | 129346 | True |
| bk2 | `65.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk2 | `66.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk2 | `67.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk2 | `68.log` | SEALED_OK | 130147 | 130107 | 130107 | 0 | True | 111 | 111 | None | None | 129083 | 129083 | True |
| bk2 | `69.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk2 | `6a.log` | SEALED_OK | 130957 | 130917 | 130917 | 0 | True | 106 | 106 | None | None | 129893 | 129893 | True |
| bk2 | `6b.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk2 | `6c.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk2 | `6d.log` | SEALED_OK | 131057 | 131017 | 131017 | 0 | True | 108 | 108 | None | None | 129993 | 129993 | True |
| bk2 | `6e.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk2 | `6f.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 107 | 107 | None | None | 129930 | 129930 | True |
| bk2 | `7.log` | SEALED_OK | 129208 | 129168 | 129168 | 0 | True | 93 | 93 | None | None | 128144 | 128144 | True |
| bk2 | `70.log` | SEALED_OK | 131094 | 131054 | 131054 | 0 | True | 109 | 109 | None | None | 130030 | 130030 | True |
| bk2 | `71.log` | SEALED_OK | 131057 | 131017 | 131017 | 0 | True | 108 | 108 | None | None | 129993 | 129993 | True |
| bk2 | `72.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk2 | `73.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk2 | `74.log` | SEALED_OK | 129163 | 129123 | 129123 | 0 | True | 112 | 112 | None | None | 128099 | 128099 | True |
| bk2 | `75.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk2 | `76.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk2 | `77.log` | SEALED_OK | 130147 | 130107 | 130107 | 0 | True | 111 | 111 | None | None | 129083 | 129083 | True |
| bk2 | `78.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk2 | `79.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk2 | `7a.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk2 | `7b.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk2 | `7c.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk2 | `7d.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk2 | `7e.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk2 | `7f.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk2 | `8.log` | SEALED_OK | 130696 | 130656 | 130656 | 0 | True | 84 | 84 | None | None | 129632 | 129632 | True |
| bk2 | `80.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk2 | `81.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk2 | `82.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk2 | `83.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk2 | `84.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk2 | `85.log` | SEALED_OK | 131044 | 131004 | 131004 | 0 | True | 108 | 108 | None | None | 129980 | 129980 | True |
| bk2 | `86.log` | SEALED_OK | 131057 | 131017 | 131017 | 0 | True | 108 | 108 | None | None | 129993 | 129993 | True |
| bk2 | `87.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk2 | `88.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk2 | `89.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk2 | `8a.log` | SEALED_OK | 130441 | 130401 | 130401 | 0 | True | 115 | 115 | None | None | 129377 | 129377 | True |
| bk2 | `8b.log` | SEALED_OK | 130484 | 130444 | 130444 | 0 | True | 115 | 115 | None | None | 129420 | 129420 | True |
| bk2 | `8c.log` | SEALED_OK | 130388 | 130348 | 130348 | 0 | True | 113 | 113 | None | None | 129324 | 129324 | True |
| bk2 | `8d.log` | SEALED_OK | 130229 | 130189 | 130189 | 0 | True | 110 | 110 | None | None | 129165 | 129165 | True |
| bk2 | `8e.log` | SEALED_OK | 130388 | 130348 | 130348 | 0 | True | 113 | 113 | None | None | 129324 | 129324 | True |
| bk2 | `8f.log` | SEALED_OK | 130436 | 130396 | 130396 | 0 | True | 114 | 114 | None | None | 129372 | 129372 | True |
| bk2 | `9.log` | SEALED_OK | 130805 | 130765 | 130765 | 0 | True | 104 | 104 | None | None | 129741 | 129741 | True |
| bk2 | `90.log` | SEALED_OK | 130373 | 130333 | 130333 | 0 | True | 113 | 113 | None | None | 129309 | 129309 | True |
| bk2 | `91.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk2 | `92.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk2 | `93.log` | SEALED_OK | 130484 | 130444 | 130444 | 0 | True | 115 | 115 | None | None | 129420 | 129420 | True |
| bk2 | `94.log` | SEALED_OK | 130085 | 130045 | 130045 | 0 | True | 107 | 107 | None | None | 129021 | 129021 | True |
| bk2 | `95.log` | SEALED_OK | 130148 | 130108 | 130108 | 0 | True | 108 | 108 | None | None | 129084 | 129084 | True |
| bk2 | `96.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk2 | `97.log` | SEALED_OK | 130148 | 130108 | 130108 | 0 | True | 108 | 108 | None | None | 129084 | 129084 | True |
| bk2 | `98.log` | SEALED_OK | 130214 | 130174 | 130174 | 0 | True | 110 | 110 | None | None | 129150 | 129150 | True |
| bk2 | `99.log` | SEALED_OK | 130580 | 130540 | 130540 | 0 | True | 117 | 117 | None | None | 129516 | 129516 | True |
| bk2 | `9a.log` | SEALED_OK | 130388 | 130348 | 130348 | 0 | True | 113 | 113 | None | None | 129324 | 129324 | True |
| bk2 | `9b.log` | SEALED_OK | 130436 | 130396 | 130396 | 0 | True | 114 | 114 | None | None | 129372 | 129372 | True |
| bk2 | `9c.log` | SEALED_OK | 130052 | 130012 | 130012 | 0 | True | 106 | 106 | None | None | 128988 | 128988 | True |
| bk2 | `9d.log` | SEALED_OK | 130022 | 129982 | 129982 | 0 | True | 106 | 106 | None | None | 128958 | 128958 | True |
| bk2 | `9e.log` | SEALED_OK | 130292 | 130252 | 130252 | 0 | True | 111 | 111 | None | None | 129228 | 129228 | True |
| bk2 | `9f.log` | SEALED_OK | 130100 | 130060 | 130060 | 0 | True | 107 | 107 | None | None | 129036 | 129036 | True |
| bk2 | `a.log` | SEALED_OK | 130444 | 130404 | 130404 | 0 | True | 96 | 96 | None | None | 129380 | 129380 | True |
| bk2 | `a0.log` | SEALED_OK | 130100 | 130060 | 130060 | 0 | True | 107 | 107 | None | None | 129036 | 129036 | True |
| bk2 | `a1.log` | SEALED_OK | 130196 | 130156 | 130156 | 0 | True | 109 | 109 | None | None | 129132 | 129132 | True |
| bk2 | `a2.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk2 | `a3.log` | SEALED_OK | 131006 | 130966 | 130966 | 0 | True | 104 | 104 | None | None | 129942 | 129942 | True |
| bk2 | `a4.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk2 | `a5.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk2 | `a6.log` | SEALED_OK | 130196 | 130156 | 130156 | 0 | True | 109 | 109 | None | None | 129132 | 129132 | True |
| bk2 | `a7.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk2 | `a8.log` | SEALED_OK | 130388 | 130348 | 130348 | 0 | True | 113 | 113 | None | None | 129324 | 129324 | True |
| bk2 | `a9.log` | UNSEALED_OK | 8710 | 0 | None | None | False | 7 | 7 | None | None | None | None | None |
| bk2 | `b.log` | SEALED_OK | 130568 | 130528 | 130528 | 0 | True | 99 | 99 | None | None | 129504 | 129504 | True |
| bk2 | `c.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk2 | `d.log` | SEALED_OK | 130857 | 130817 | 130817 | 0 | True | 104 | 104 | None | None | 129793 | 129793 | True |
| bk2 | `e.log` | SEALED_OK | 130047 | 130007 | 130007 | 0 | True | 109 | 109 | None | None | 128983 | 128983 | True |
| bk2 | `f.log` | SEALED_OK | 130347 | 130307 | 130307 | 0 | True | 115 | 115 | None | None | 129283 | 129283 | True |
| bk3 | `0.log` | SEALED_OK | 130159 | 130119 | 130119 | 0 | True | 44 | 44 | None | None | 129095 | 129095 | True |
| bk3 | `1.log` | SEALED_OK | 130871 | 130831 | 130831 | 0 | True | 52 | 52 | None | None | 129807 | 129807 | True |
| bk3 | `10.log` | SEALED_OK | 130655 | 130615 | 130615 | 0 | True | 101 | 101 | None | None | 129591 | 129591 | True |
| bk3 | `11.log` | SEALED_OK | 130034 | 129994 | 129994 | 0 | True | 109 | 109 | None | None | 128970 | 128970 | True |
| bk3 | `12.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk3 | `13.log` | SEALED_OK | 130581 | 130541 | 130541 | 0 | True | 99 | 99 | None | None | 129517 | 129517 | True |
| bk3 | `14.log` | SEALED_OK | 131007 | 130967 | 130967 | 0 | True | 107 | 107 | None | None | 129943 | 129943 | True |
| bk3 | `15.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 107 | 107 | None | None | 129930 | 129930 | True |
| bk3 | `16.log` | SEALED_OK | 129671 | 129631 | 129631 | 0 | True | 102 | 102 | None | None | 128607 | 128607 | True |
| bk3 | `17.log` | SEALED_OK | 130894 | 130854 | 130854 | 0 | True | 105 | 105 | None | None | 129830 | 129830 | True |
| bk3 | `18.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk3 | `19.log` | SEALED_OK | 130460 | 130420 | 130420 | 0 | True | 117 | 117 | None | None | 129396 | 129396 | True |
| bk3 | `1a.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk3 | `1b.log` | SEALED_OK | 130981 | 130941 | 130941 | 0 | True | 107 | 107 | None | None | 129917 | 129917 | True |
| bk3 | `1c.log` | SEALED_OK | 129295 | 129255 | 129255 | 0 | True | 95 | 95 | None | None | 128231 | 128231 | True |
| bk3 | `1d.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk3 | `1e.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk3 | `1f.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk3 | `2.log` | SEALED_OK | 130626 | 130586 | 130586 | 0 | True | 64 | 64 | None | None | 129562 | 129562 | True |
| bk3 | `20.log` | SEALED_OK | 130410 | 130370 | 130370 | 0 | True | 116 | 116 | None | None | 129346 | 129346 | True |
| bk3 | `21.log` | SEALED_OK | 130857 | 130817 | 130817 | 0 | True | 104 | 104 | None | None | 129793 | 129793 | True |
| bk3 | `22.log` | SEALED_OK | 130197 | 130157 | 130157 | 0 | True | 112 | 112 | None | None | 129133 | 129133 | True |
| bk3 | `23.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk3 | `24.log` | SEALED_OK | 129810 | 129770 | 129770 | 0 | True | 104 | 104 | None | None | 128746 | 128746 | True |
| bk3 | `25.log` | SEALED_OK | 129960 | 129920 | 129920 | 0 | True | 107 | 107 | None | None | 128896 | 128896 | True |
| bk3 | `26.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk3 | `27.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk3 | `28.log` | SEALED_OK | 131007 | 130967 | 130967 | 0 | True | 107 | 107 | None | None | 129943 | 129943 | True |
| bk3 | `29.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk3 | `2a.log` | SEALED_OK | 130907 | 130867 | 130867 | 0 | True | 105 | 105 | None | None | 129843 | 129843 | True |
| bk3 | `2b.log` | SEALED_OK | 130844 | 130804 | 130804 | 0 | True | 104 | 104 | None | None | 129780 | 129780 | True |
| bk3 | `2c.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk3 | `2d.log` | SEALED_OK | 130084 | 130044 | 130044 | 0 | True | 110 | 110 | None | None | 129020 | 129020 | True |
| bk3 | `2e.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk3 | `2f.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk3 | `3.log` | SEALED_OK | 130978 | 130938 | 130938 | 0 | True | 86 | 86 | None | None | 129914 | 129914 | True |
| bk3 | `30.log` | SEALED_OK | 130147 | 130107 | 130107 | 0 | True | 111 | 111 | None | None | 129083 | 129083 | True |
| bk3 | `31.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk3 | `32.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk3 | `33.log` | SEALED_OK | 130694 | 130654 | 130654 | 0 | True | 101 | 101 | None | None | 129630 | 129630 | True |
| bk3 | `34.log` | SEALED_OK | 130253 | 130213 | 130213 | 0 | True | 94 | 94 | None | None | 129189 | 129189 | True |
| bk3 | `35.log` | SEALED_OK | 130429 | 130389 | 130389 | 0 | True | 97 | 97 | None | None | 129365 | 129365 | True |
| bk3 | `36.log` | SEALED_OK | 130255 | 130215 | 130215 | 0 | True | 93 | 93 | None | None | 129191 | 129191 | True |
| bk3 | `37.log` | SEALED_OK | 130177 | 130137 | 130137 | 0 | True | 93 | 93 | None | None | 129113 | 129113 | True |
| bk3 | `38.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk3 | `39.log` | SEALED_OK | 131007 | 130967 | 130967 | 0 | True | 107 | 107 | None | None | 129943 | 129943 | True |
| bk3 | `3a.log` | SEALED_OK | 131007 | 130967 | 130967 | 0 | True | 107 | 107 | None | None | 129943 | 129943 | True |
| bk3 | `3b.log` | SEALED_OK | 130410 | 130370 | 130370 | 0 | True | 116 | 116 | None | None | 129346 | 129346 | True |
| bk3 | `3c.log` | SEALED_OK | 130410 | 130370 | 130370 | 0 | True | 116 | 116 | None | None | 129346 | 129346 | True |
| bk3 | `3d.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk3 | `3e.log` | SEALED_OK | 129545 | 129505 | 129505 | 0 | True | 100 | 100 | None | None | 128481 | 128481 | True |
| bk3 | `3f.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 107 | 107 | None | None | 129930 | 129930 | True |
| bk3 | `4.log` | SEALED_OK | 130837 | 130797 | 130797 | 0 | True | 85 | 85 | None | None | 129773 | 129773 | True |
| bk3 | `40.log` | SEALED_OK | 129621 | 129581 | 129581 | 0 | True | 101 | 101 | None | None | 128557 | 128557 | True |
| bk3 | `41.log` | SEALED_OK | 130781 | 130741 | 130741 | 0 | True | 103 | 103 | None | None | 129717 | 129717 | True |
| bk3 | `42.log` | SEALED_OK | 130047 | 130007 | 130007 | 0 | True | 109 | 109 | None | None | 128983 | 128983 | True |
| bk3 | `43.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk3 | `44.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk3 | `45.log` | SEALED_OK | 131007 | 130967 | 130967 | 0 | True | 107 | 107 | None | None | 129943 | 129943 | True |
| bk3 | `46.log` | SEALED_OK | 130844 | 130804 | 130804 | 0 | True | 104 | 104 | None | None | 129780 | 129780 | True |
| bk3 | `47.log` | SEALED_OK | 130177 | 130137 | 130137 | 0 | True | 93 | 93 | None | None | 129113 | 129113 | True |
| bk3 | `48.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk3 | `49.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk3 | `4a.log` | SEALED_OK | 129419 | 129379 | 129379 | 0 | True | 98 | 98 | None | None | 128355 | 128355 | True |
| bk3 | `4b.log` | SEALED_OK | 130097 | 130057 | 130057 | 0 | True | 110 | 110 | None | None | 129033 | 129033 | True |
| bk3 | `4c.log` | SEALED_OK | 131007 | 130967 | 130967 | 0 | True | 107 | 107 | None | None | 129943 | 129943 | True |
| bk3 | `4d.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk3 | `4e.log` | SEALED_OK | 130460 | 130420 | 130420 | 0 | True | 117 | 117 | None | None | 129396 | 129396 | True |
| bk3 | `4f.log` | SEALED_OK | 131057 | 131017 | 131017 | 0 | True | 108 | 108 | None | None | 129993 | 129993 | True |
| bk3 | `5.log` | SEALED_OK | 130457 | 130417 | 130417 | 0 | True | 96 | 96 | None | None | 129393 | 129393 | True |
| bk3 | `50.log` | SEALED_OK | 131007 | 130967 | 130967 | 0 | True | 107 | 107 | None | None | 129943 | 129943 | True |
| bk3 | `51.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk3 | `52.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk3 | `53.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk3 | `54.log` | SEALED_OK | 130047 | 130007 | 130007 | 0 | True | 109 | 109 | None | None | 128983 | 128983 | True |
| bk3 | `55.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk3 | `56.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk3 | `57.log` | SEALED_OK | 131016 | 130976 | 130976 | 0 | True | 109 | 109 | None | None | 129952 | 129952 | True |
| bk3 | `58.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk3 | `59.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk3 | `5a.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk3 | `5b.log` | SEALED_OK | 130097 | 130057 | 130057 | 0 | True | 110 | 110 | None | None | 129033 | 129033 | True |
| bk3 | `5c.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk3 | `5d.log` | SEALED_OK | 129313 | 129273 | 129273 | 0 | True | 115 | 115 | None | None | 128249 | 128249 | True |
| bk3 | `5e.log` | SEALED_OK | 129760 | 129720 | 129720 | 0 | True | 103 | 103 | None | None | 128696 | 128696 | True |
| bk3 | `5f.log` | SEALED_OK | 130034 | 129994 | 129994 | 0 | True | 109 | 109 | None | None | 128970 | 128970 | True |
| bk3 | `6.log` | SEALED_OK | 130605 | 130565 | 130565 | 0 | True | 100 | 100 | None | None | 129541 | 129541 | True |
| bk3 | `60.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk3 | `61.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 107 | 107 | None | None | 129930 | 129930 | True |
| bk3 | `62.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk3 | `63.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk3 | `64.log` | SEALED_OK | 130410 | 130370 | 130370 | 0 | True | 116 | 116 | None | None | 129346 | 129346 | True |
| bk3 | `65.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk3 | `66.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk3 | `67.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk3 | `68.log` | SEALED_OK | 130147 | 130107 | 130107 | 0 | True | 111 | 111 | None | None | 129083 | 129083 | True |
| bk3 | `69.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk3 | `6a.log` | SEALED_OK | 130957 | 130917 | 130917 | 0 | True | 106 | 106 | None | None | 129893 | 129893 | True |
| bk3 | `6b.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk3 | `6c.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk3 | `6d.log` | SEALED_OK | 131057 | 131017 | 131017 | 0 | True | 108 | 108 | None | None | 129993 | 129993 | True |
| bk3 | `6e.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk3 | `6f.log` | SEALED_OK | 130994 | 130954 | 130954 | 0 | True | 107 | 107 | None | None | 129930 | 129930 | True |
| bk3 | `7.log` | SEALED_OK | 129208 | 129168 | 129168 | 0 | True | 93 | 93 | None | None | 128144 | 128144 | True |
| bk3 | `70.log` | SEALED_OK | 131094 | 131054 | 131054 | 0 | True | 109 | 109 | None | None | 130030 | 130030 | True |
| bk3 | `71.log` | SEALED_OK | 131057 | 131017 | 131017 | 0 | True | 108 | 108 | None | None | 129993 | 129993 | True |
| bk3 | `72.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk3 | `73.log` | SEALED_OK | 130360 | 130320 | 130320 | 0 | True | 115 | 115 | None | None | 129296 | 129296 | True |
| bk3 | `74.log` | SEALED_OK | 129163 | 129123 | 129123 | 0 | True | 112 | 112 | None | None | 128099 | 128099 | True |
| bk3 | `75.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk3 | `76.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk3 | `77.log` | SEALED_OK | 130147 | 130107 | 130107 | 0 | True | 111 | 111 | None | None | 129083 | 129083 | True |
| bk3 | `78.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk3 | `79.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk3 | `7a.log` | SEALED_OK | 130210 | 130170 | 130170 | 0 | True | 112 | 112 | None | None | 129146 | 129146 | True |
| bk3 | `7b.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk3 | `7c.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk3 | `7d.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk3 | `7e.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk3 | `7f.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk3 | `8.log` | SEALED_OK | 130696 | 130656 | 130656 | 0 | True | 84 | 84 | None | None | 129632 | 129632 | True |
| bk3 | `80.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk3 | `81.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk3 | `82.log` | SEALED_OK | 130160 | 130120 | 130120 | 0 | True | 111 | 111 | None | None | 129096 | 129096 | True |
| bk3 | `83.log` | SEALED_OK | 130110 | 130070 | 130070 | 0 | True | 110 | 110 | None | None | 129046 | 129046 | True |
| bk3 | `84.log` | SEALED_OK | 130310 | 130270 | 130270 | 0 | True | 114 | 114 | None | None | 129246 | 129246 | True |
| bk3 | `85.log` | SEALED_OK | 131044 | 131004 | 131004 | 0 | True | 108 | 108 | None | None | 129980 | 129980 | True |
| bk3 | `86.log` | SEALED_OK | 131057 | 131017 | 131017 | 0 | True | 108 | 108 | None | None | 129993 | 129993 | True |
| bk3 | `87.log` | SEALED_OK | 130060 | 130020 | 130020 | 0 | True | 109 | 109 | None | None | 128996 | 128996 | True |
| bk3 | `88.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk3 | `89.log` | SEALED_OK | 130260 | 130220 | 130220 | 0 | True | 113 | 113 | None | None | 129196 | 129196 | True |
| bk3 | `8a.log` | SEALED_OK | 130441 | 130401 | 130401 | 0 | True | 115 | 115 | None | None | 129377 | 129377 | True |
| bk3 | `8b.log` | SEALED_OK | 130484 | 130444 | 130444 | 0 | True | 115 | 115 | None | None | 129420 | 129420 | True |
| bk3 | `8c.log` | SEALED_OK | 130388 | 130348 | 130348 | 0 | True | 113 | 113 | None | None | 129324 | 129324 | True |
| bk3 | `8d.log` | SEALED_OK | 130229 | 130189 | 130189 | 0 | True | 110 | 110 | None | None | 129165 | 129165 | True |
| bk3 | `8e.log` | SEALED_OK | 130388 | 130348 | 130348 | 0 | True | 113 | 113 | None | None | 129324 | 129324 | True |
| bk3 | `8f.log` | SEALED_OK | 130436 | 130396 | 130396 | 0 | True | 114 | 114 | None | None | 129372 | 129372 | True |
| bk3 | `9.log` | SEALED_OK | 130805 | 130765 | 130765 | 0 | True | 104 | 104 | None | None | 129741 | 129741 | True |
| bk3 | `90.log` | SEALED_OK | 130373 | 130333 | 130333 | 0 | True | 113 | 113 | None | None | 129309 | 129309 | True |
| bk3 | `91.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk3 | `92.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk3 | `93.log` | SEALED_OK | 130484 | 130444 | 130444 | 0 | True | 115 | 115 | None | None | 129420 | 129420 | True |
| bk3 | `94.log` | SEALED_OK | 130085 | 130045 | 130045 | 0 | True | 107 | 107 | None | None | 129021 | 129021 | True |
| bk3 | `95.log` | SEALED_OK | 130148 | 130108 | 130108 | 0 | True | 108 | 108 | None | None | 129084 | 129084 | True |
| bk3 | `96.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk3 | `97.log` | SEALED_OK | 130148 | 130108 | 130108 | 0 | True | 108 | 108 | None | None | 129084 | 129084 | True |
| bk3 | `98.log` | SEALED_OK | 130214 | 130174 | 130174 | 0 | True | 110 | 110 | None | None | 129150 | 129150 | True |
| bk3 | `99.log` | SEALED_OK | 130580 | 130540 | 130540 | 0 | True | 117 | 117 | None | None | 129516 | 129516 | True |
| bk3 | `9a.log` | SEALED_OK | 130388 | 130348 | 130348 | 0 | True | 113 | 113 | None | None | 129324 | 129324 | True |
| bk3 | `9b.log` | SEALED_OK | 130436 | 130396 | 130396 | 0 | True | 114 | 114 | None | None | 129372 | 129372 | True |
| bk3 | `9c.log` | SEALED_OK | 130052 | 130012 | 130012 | 0 | True | 106 | 106 | None | None | 128988 | 128988 | True |
| bk3 | `9d.log` | SEALED_OK | 130022 | 129982 | 129982 | 0 | True | 106 | 106 | None | None | 128958 | 128958 | True |
| bk3 | `9e.log` | SEALED_OK | 130292 | 130252 | 130252 | 0 | True | 111 | 111 | None | None | 129228 | 129228 | True |
| bk3 | `9f.log` | SEALED_OK | 130100 | 130060 | 130060 | 0 | True | 107 | 107 | None | None | 129036 | 129036 | True |
| bk3 | `a.log` | SEALED_OK | 130444 | 130404 | 130404 | 0 | True | 96 | 96 | None | None | 129380 | 129380 | True |
| bk3 | `a0.log` | SEALED_OK | 130100 | 130060 | 130060 | 0 | True | 107 | 107 | None | None | 129036 | 129036 | True |
| bk3 | `a1.log` | SEALED_OK | 130196 | 130156 | 130156 | 0 | True | 109 | 109 | None | None | 129132 | 129132 | True |
| bk3 | `a2.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk3 | `a3.log` | SEALED_OK | 131006 | 130966 | 130966 | 0 | True | 104 | 104 | None | None | 129942 | 129942 | True |
| bk3 | `a4.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk3 | `a5.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk3 | `a6.log` | SEALED_OK | 130196 | 130156 | 130156 | 0 | True | 109 | 109 | None | None | 129132 | 129132 | True |
| bk3 | `a7.log` | SEALED_OK | 130340 | 130300 | 130300 | 0 | True | 112 | 112 | None | None | 129276 | 129276 | True |
| bk3 | `a8.log` | SEALED_OK | 130388 | 130348 | 130348 | 0 | True | 113 | 113 | None | None | 129324 | 129324 | True |
| bk3 | `a9.log` | UNSEALED_OK | 8710 | 0 | None | None | False | 7 | 7 | None | None | None | None | None |
| bk3 | `b.log` | SEALED_OK | 130568 | 130528 | 130528 | 0 | True | 99 | 99 | None | None | 129504 | 129504 | True |
| bk3 | `c.log` | SEALED_OK | 131107 | 131067 | 131067 | 0 | True | 109 | 109 | None | None | 130043 | 130043 | True |
| bk3 | `d.log` | SEALED_OK | 130857 | 130817 | 130817 | 0 | True | 104 | 104 | None | None | 129793 | 129793 | True |
| bk3 | `e.log` | SEALED_OK | 130047 | 130007 | 130007 | 0 | True | 109 | 109 | None | None | 128983 | 128983 | True |
| bk3 | `f.log` | SEALED_OK | 130347 | 130307 | 130307 | 0 | True | 115 | 115 | None | None | 129283 | 129283 | True |

## Replica Entry Comparison

| target | control | targetEntries | controlEntries | common | missingInTarget | missingInControl | hashMismatches |
|---|---|---:|---:|---:|---:|---:|---:|
| bk2 | bk3 | 18189 | 18189 | 18189 | 0 | 0 | 0 |
| bk1 | bk2 | 18189 | 18189 | 18189 | 0 | 0 | 0 |
| bk1 | bk3 | 18189 | 18189 | 18189 | 0 | 0 | 0 |

## Runtime Behavior

- clientExit: `0`

### bk1

| line | tag | log |
|---:|---|---|
| 138 | bookie-fault | `2026-07-31T18:01:33,117 - ERROR - [SyncThread-7-1:SyncThread@181] - Exception flushing ledgers` |
| 139 | bookie-fault | `java.io.IOException: Input/output error` |
| 134 | entrylog-io | `2026-07-31T18:01:33,112 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log for logId 0.` |
| 136 | entrylog-io | `2026-07-31T18:01:33,116 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log for logId 1.` |
| 137 | entrylog-io | `2026-07-31T18:01:33,116 - INFO  - [SyncThread-7-1:EntryLogManagerBase@165] - Flushing entry logger 0 back to filesystem, pending for syncing entry loggers : [BufferedChannel{logId=0, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log, ledgerIdAssigned=-1}].` |
| 165 | entrylog-io | `2026-07-31T18:01:34,107 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/2.log for logId 2.` |
| 166 | entrylog-io | `2026-07-31T18:01:34,107 - INFO  - [SyncThread-7-1:EntryLogManagerBase@165] - Flushing entry logger 1 back to filesystem, pending for syncing entry loggers : [BufferedChannel{logId=0, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/0.log, ledgerIdAssigned=-1}, BufferedChannel{logId=1, logFile=/home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/1.log, ledgerIdAssigned=-1}].` |
| 168 | entrylog-io | `2026-07-31T18:01:34,108 - INFO  - [SyncThread-7-1:EntryLoggerAllocator@182] - Created new entry log file /home/stephen/github/java/bookkeeper/dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runtime/data/bk1/ledgers/current/3.log for logId 3.` |
| 842 | bookie-lifecycle | `2026-07-31T18:02:01,806 - INFO  - [component-shutdown-thread:BookieServer@191] - Shutting down BookieServer` |
| 863 | bookie-lifecycle | `2026-07-31T18:02:01,828 - INFO  - [component-shutdown-thread:BookieImpl@861] - Turning bookie to read only during shut down` |
| 869 | bookie-lifecycle | `2026-07-31T18:02:01,840 - INFO  - [BookieJournal-3181:BookieImpl@828] - Triggering shutdown of Bookie-3181 with exitCode 5` |
| 876 | bookie-lifecycle | `2026-07-31T18:02:02,147 - INFO  - [BookieDeathWatcher-3181:BookieServer$DeathWatcher@274] - BookieDeathWatcher noticed the bookie is not running any more, exiting the watch loop!` |
| 877 | bookie-lifecycle | `2026-07-31T18:02:02,147 - ERROR - [BookieDeathWatcher-3181:ComponentStarter@75] - Triggered exceptionHandler of Component: bookie-server because of Exception in Thread: Thread[BookieDeathWatcher-3181,5,main]` |

### bk2

No matching log lines found.

### bk3

No matching log lines found.

### broker

| line | tag | log |
|---:|---|---|
| 33 | bk-client-init | `2026-07-31T18:01:28,821+0800 [main] INFO  org.apache.bookkeeper.meta.MetadataDrivers - BookKeeper metadata driver manager initialized` |
| 34 | bk-client-init | `2026-07-31T18:01:28,824+0800 [main] INFO  org.apache.pulsar.broker.BookKeeperClientFactoryImpl - Applying BookKeeper client configuration setting tlsHostnameVerificationEnabled=false` |
| 64 | bk-client-init | `2026-07-31T18:01:29,098+0800 [main] INFO  org.apache.pulsar.broker.BookKeeperClientFactoryImpl - Applying BookKeeper client configuration setting tlsHostnameVerificationEnabled=false` |
| 48 | bookie-discovery | `2026-07-31T18:01:28,946+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3181 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3181, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 49 | bookie-discovery | `2026-07-31T18:01:28,948+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3182 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3182, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 50 | bookie-discovery | `2026-07-31T18:01:28,948+0800 [ForkJoinPool.commonPool-worker-1-EventThread] INFO  org.apache.bookkeeper.discover.ZKRegistrationClient - Update BookieInfoCache (writable bookie) 127.0.0.1:3183 -> BookieServiceInfo{properties={}, endpoints=[EndpointInfo{id=bookie, port=3183, host=127.0.0.1, protocol=bookie-rpc, auth=[], extensions=[]}]}` |
| 52 | bookie-discovery | `2026-07-31T18:01:28,955+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3181` |
| 54 | bookie-discovery | `2026-07-31T18:01:28,955+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3182` |
| 56 | bookie-discovery | `2026-07-31T18:01:28,955+0800 [BookKeeperClientScheduler-OrderedScheduler-0-0] INFO  org.apache.bookkeeper.net.NetworkTopologyImpl - Adding a new node: /default-rack/127.0.0.1:3183` |
| 157 | bookie-channel | `2026-07-31T18:01:32,407+0800 [pulsar-io-3-2] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3181 [id: 0x2ea99076, L:/127.0.0.1:57288 - R:127.0.0.1/127.0.0.1:3181]` |
| 158 | bookie-channel | `2026-07-31T18:01:32,407+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3181 [id: 0x75b48ba6, L:/127.0.0.1:57282 - R:127.0.0.1/127.0.0.1:3181]` |
| 159 | bookie-channel | `2026-07-31T18:01:32,412+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0x75b48ba6, L:/127.0.0.1:57282 - R:127.0.0.1/127.0.0.1:3181] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 160 | bookie-channel | `2026-07-31T18:01:32,417+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3181 [id: 0xa9dd54d7, L:/127.0.0.1:57342 - R:127.0.0.1/127.0.0.1:3181]` |
| 161 | bookie-channel | `2026-07-31T18:01:32,417+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - connection [id: 0xa9dd54d7, L:/127.0.0.1:57342 - R:127.0.0.1/127.0.0.1:3181] authenticated as BookKeeperPrincipal{ANONYMOUS}` |
| 162 | bookie-channel | `2026-07-31T18:01:32,417+0800 [pulsar-io-3-1] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Successfully connected to bookie: 127.0.0.1:3181 [id: 0xf8ac1763, L:/127.0.0.1:57354 - R:127.0.0.1/127.0.0.1:3181]` |
| 386 | managed-ledger | `2026-07-31T18:02:02,251+0800 [metadata-store-9-1] INFO  org.apache.bookkeeper.mledger.impl.ManagedLedgerFactoryImpl - Received MetadataStore session event: ConnectionLost` |
| 259 | broker-error | `2026-07-31T18:02:01,801+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x9f271a33, L:/127.0.0.1:36764 - R:127.0.0.1/127.0.0.1:3183] cause: recvAddress(..) failed: Connection reset by peer` |
| 260 | broker-error | `2026-07-31T18:02:01,802+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x2680753e, L:/127.0.0.1:36704 - R:127.0.0.1/127.0.0.1:3183] cause: recvAddress(..) failed: Connection reset by peer` |
| 261 | broker-error | `2026-07-31T18:02:01,804+0800 [pulsar-io-3-2] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x88d41cd8, L:/127.0.0.1:36732 - R:127.0.0.1/127.0.0.1:3183] cause: recvAddress(..) failed: Connection reset by peer` |
| 262 | broker-error | `2026-07-31T18:02:01,804+0800 [pulsar-io-3-2] INFO  org.apache.bookkeeper.proto.PerChannelBookieClient - Disconnected from bookie channel [id: 0x9f271a33, L:/127.0.0.1:36764 ! R:127.0.0.1/127.0.0.1:3183]` |
| 263 | broker-error | `2026-07-31T18:02:01,807+0800 [pulsar-io-3-1] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x831687e3, L:/127.0.0.1:36674 - R:127.0.0.1/127.0.0.1:3183] cause: recvAddress(..) failed: Connection reset by peer` |
| 264 | broker-error | `2026-07-31T18:02:01,807+0800 [pulsar-io-3-1] WARN  org.apache.bookkeeper.proto.PerChannelBookieClient - Exception caught on:[id: 0x8fa27656, L:/127.0.0.1:36620 - R:127.0.0.1/127.0.0.1:3183] cause: recvAddress(..) failed: Connection reset by peer` |

### client

| line | tag | log |
|---:|---|---|
| 66 | client-progress | `2026-07-31T18:01:41,725+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:    8440 msg ---    844.0 msg/s ---      6.6 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:  10.931 ms - med:  10.557 - 95pct:  15.565 - 99pct:  19.088 - 99.9pct:  26.463 - 99.99pct:  32.464 - Max:  33.511` |
| 67 | client-progress | `2026-07-31T18:01:51,737+0800 [main] INFO  org.apache.pulsar.testclient.PerformanceProducer - Throughput produced:   17468 msg ---    900.0 msg/s ---      7.0 Mbit/s  --- failure      0.0 msg/s --- Latency: mean:  10.203 ms - med:  10.040 - 95pct:  13.413 - 99pct:  16.458 - 99.9pct:  23.600 - 99.99pct:  28.382 - Max:  29.307` |
| 72 | client-progress | `2026-07-31T18:02:01,741+0800 [Thread-0] INFO  org.apache.pulsar.testclient.PerformanceProducer - Aggregated throughput stats --- 20011 records sent --- 666.021 msg/s --- 5.203 Mbit/s ` |
| 73 | client-progress | `2026-07-31T18:02:01,758+0800 [Thread-0] INFO  org.apache.pulsar.testclient.PerformanceProducer - Aggregated latency stats --- Latency: mean:  10.430 ms - med:  10.172 - 95pct:  14.326 - 99pct:  17.639 - 99.9pct:  25.469 - 99.99pct:  31.378 - 99.999pct:  33.511 - Max:  33.511` |
| 68 | client-completion | `2026-07-31T18:01:54,545+0800 [pulsar-perf-producer-exec-1-1] INFO  org.apache.pulsar.testclient.PerformanceProducer - ------------- DONE (reached the maximum number: 20000 of production) --------------` |
| 74 | client-completion | `workload_rc=0` |
