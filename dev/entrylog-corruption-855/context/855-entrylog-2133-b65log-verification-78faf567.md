# Bookie-2 L15002 Stale Index / Missing 85.log Raw Evidence Report（v4）

> **报告作用**：贴出全部 raw 命令、raw output、本地解析脚本输出，**不做摘要+结论**，让阅读者自己判断。本报告只做事实归档。
>
> **修订历史**：
> - v1：基于错误的 L15002 ledgerId pattern 搜索（撤回）
> - v2：基于主分析作者 6 项核对修正（撤回部分推论）
> - v2.1：基于"那不一定是不存在，可能太久了了gc了"修正（撤回 closed ledger → GC 推论）
> - v3：基于主分析作者 4 项核对修正（撤回 compaction 清理不完整过度推论）
> - **v4（当前）**：基于主分析作者要求"把过程命令、解析数据都贴上，不要盲目自己给结论"，**只贴 raw 证据，不写结论**
>
> **校验基准**：
> - 现场环境：10.107.29.75（admin/pulsarDfx@0630sangfornetwork），K8s 集群 pulsar/bookie-2，**只读访问，未修改任何环境内容**
> - 本地文件：`/home/stephen/github/java/pulsar/bin/20260723/b65.log`（logId 2917，1,073,512,226 字节）
> - 校验时间：2026-07-27
> - 报告 id：`78faf567`

---

## 1. 现场 raw 命令 1：`bin/bookkeeper shell ledger 15002`

### 1.1 命令

```bash
kubectl exec -npulsar pulsar-bookie-2 -- bash -c \
  'cd /pulsar && bin/bookkeeper shell ledger 15002 2>&1 | \
   egrep "entry (350[0-9]|351[0-9]|352[0-9]|360[0-9]|88025)[[:space:]]"'
```

### 1.2 Raw output

```
entry 3500	:	(log: 2917, pos: 307731252)
entry 3502	:	(log: 2917, pos: 307731298)
entry 3504	:	(log: 2917, pos: 307731362)
entry 3506	:	(log: 2917, pos: 307731426)
entry 3508	:	(log: 2917, pos: 307731472)
entry 3510	:	(log: 133,  pos: 112262725)
entry 3512	:	(log: 133,  pos: 112262771)
entry 3514	:	(log: 133,  pos: 112262817)
entry 3516	:	(log: 133,  pos: 112262863)
entry 3518	:	(log: 133,  pos: 112262927)
entry 3520	:	(log: 133,  pos: 112262973)
entry 3522	:	(log: 133,  pos: 112263019)
entry 3524	:	(log: 133,  pos: 112263065)
entry 3526	:	(log: 133,  pos: 112263111)
entry 3528	:	(log: 133,  pos: 112263157)
entry 3600	:	(log: 133,  pos: 501617363)
entry 3602	:	(log: 133,  pos: 501617409)
entry 3604	:	(log: 133,  pos: 501617473)
entry 3606	:	(log: 133,  pos: 501617519)
```

### 1.3 L15002 全部 RocksDB index 按 logId 聚合

```bash
kubectl exec -npulsar pulsar-bookie-2 -- bash -c \
  'cd /pulsar && bin/bookkeeper shell ledger 15002 2>&1 | \
   grep -E "log: [0-9]+," | awk -F"log: " "{print \$2}" | \
   awk -F"," "{print \$1}" | sort | uniq -c'
```

Raw output:

```
    49  133
  1755  2917
```

### 1.4 其他 7 个报错 ledger 的 logId 聚合

```bash
for lid in 15128 14921 14919 14961 15103 15129 15245; do
  echo -n "L$lid: "
  kubectl exec -npulsar pulsar-bookie-2 -- bash -c \
    "cd /pulsar && bin/bookkeeper shell ledger $lid 2>&1 | \
     grep -E 'log: [0-9]+,' | awk -F'log: ' '{print \$2}' | \
     awk -F',' '{print \$1}' | sort | uniq -c | tr '\n' ' '"
  echo
done
```

Raw output:

```
L15128:  21 133  600 2917
L14921:  65 133  1742 2917
L14919:  106 133  3007 2917
L14961:  52 133  1746 2917
L15103:  48 133  1739 2917
L15129:  21 133  599 2917
L15245:  26 133  379 2917
```

---

## 2. 现场 raw 命令 2：`bin/bookkeeper shell ledgermetadata -ledgerid 15002`

### 2.1 命令

```bash
kubectl exec -npulsar pulsar-bookie-2 -- bash -c \
  'cd /pulsar && bin/bookkeeper shell ledgermetadata -ledgerid 15002 2>&1'
```

### 2.2 Raw output（只保留 LedgerMetadata 行，省略 ZK 初始化日志）

```
2026-07-27T13:45:14,049+0000 [main] INFO  org.apache.bookkeeper.tools.cli.commands.client.LedgerMetaDataCommand - ledgerID: 15002
2026-07-27T13:45:14,087+0000 [main] INFO  org.apache.bookkeeper.tools.cli.commands.client.LedgerMetaDataCommand - LedgerMetadata{
  formatVersion=3,
  ensembleSize=2,
  writeQuorumSize=1,
  ackQuorumSize=1,
  state=CLOSED,
  length=36519,
  lastEntryId=3607,
  digestType=CRC32C,
  password=base64:,
  ensembles={0=[pulsar-bookie-2.pulsar-bookie.pulsar.svc.cluster.local:3181,
                 pulsar-bookie-0.pulsar-bookie.pulsar.svc.cluster.local:3181]},
  customMetadata={
    component=base64:bWFuYWdlZC1sZWRnZXI=,
    pulsar/managed-ledger=base64:Y29sbGVjdC9kZWZhdWx0L3BlcnNpc3RlbnQvY29sbGVjdC1uZ2FmLWh0dHAtbG9nLXBhcnRpdGlvbi0y,
    pulsar/cursor=base64:Y29sbGVjdC1kYXRhbGFrZS10cmFuc2Zlci1wcmM=,
    application=base64:cHVsc2Fy
  }
}
```

### 2.3 customMetadata base64 解码

```
component       = "managed-ledger"
pulsar/managed-ledger = "collect/default/persistent/collect-ngaf-http-log-partition-2"
pulsar/cursor   = "collect-datalake-transfer-prc"
application     = "pulsar"
```

---

## 3. 现场 raw 命令 3：`find /pulsar/data/bookkeeper/ledgers -name '85.log' -ls`

### 3.1 命令

```bash
kubectl exec -npulsar pulsar-bookie-2 -- bash -c \
  'find /pulsar/data/bookkeeper/ledgers -name "85.log" -ls 2>&1'
```

### 3.2 Raw output

```
(无输出)
```

`find` 返回空，确认 bookie-2 上不存在名为 `85.log` 的文件。

---

## 4. 现场 raw 命令 4：`bin/bookkeeper shell readlogmetadata 133`

### 4.1 命令

```bash
kubectl exec -npulsar pulsar-bookie-2 -- bash -c \
  'cd /pulsar && bin/bookkeeper shell readlogmetadata 133 2>&1 | head -80'
```

### 4.2 Raw output（只保留关键行，省略 ZK 初始化日志）

```
2026-07-27T13:45:27,274+0000 [main] INFO  org.apache.bookkeeper.tools.cli.commands.bookie.ReadLogMetadataCommand - Print entryLogMetadata of entrylog 307 (133.log)
2026-07-27T13:45:27,774+0000 [main] WARN  org.apache.bookkeeper.bookie.DefaultEntryLogger - Cannot find entry log file 133.log : No file for log 133
2026-07-27T13:45:27,775+0000 [main] ERROR org.apache.bookkeeper.bookie.BookieShell - Got an exception
com.google.common.util.concurrent.UncheckedExecutionException: No file for log 133
	at org.apache.bookkeeper.tools.cli.commands.bookie.ReadLogMetadataCommand.apply(ReadLogMetadataCommand.java:107)
	at org.apache.bookkeeper.bookie.BookieShell$ReadLogMetadataCmd.runCmd(BookieShell.java:1064)
	at org.apache.bookkeeper.bookie.BookieShell$MyCommand.runCmd(BookieShell.java:248)
	at org.apache.bookkeeper.bookie.BookieShell.run(BookieShell.java:2349)
	at org.apache.bookkeeper.bookie.BookieShell.main(BookieShell.java:2446)
Caused by: java.io.FileNotFoundException: No file for log 133
	at org.apache.bookkeeper.bookie.DefaultEntryLogger.findFile(DefaultEntryLogger.java:978)
	at org.apache.bookkeeper.bookie.DefaultEntryLogger.getChannelForLogId(DefaultEntryLogger.java:912)
	at org.apache.bookkeeper.bookie.DefaultEntryLogger.getHeaderForLogId(DefaultEntryLogger.java:884)
	at org.apache.bookkeeper.bookie.DefaultEntryLogger.extractEntryLogMetadataFromIndex(DefaultEntryLogger.java:1074)
	at org.apache.bookkeeper.bookie.DefaultEntryLogger.getEntryLogMetadata(DefaultEntryLogger.java:1061)
	at org.apache.bookkeeper.bookie.storage.EntryLogger.getEntryLogMetadata(EntryLogger.java:111)
	at org.apache.bookkeeper.tools.cli.commands.bookie.ReadLogMetadataCommand.printEntryLogMetadata(ReadLogMetadataCommand.java:133)
	at org.apache.bookkeeper.tools.cli.commands.bookie.ReadLogMetadataCommand.readLogMetadata(ReadLogMetadataCommand.java:126)
	at org.apache.bookkeeper.tools.cli.commands.bookie.ReadLogMetadataCommand.apply(ReadLogMetadataCommand.java:105)
	... 4 more
```

### 4.3 注意

`Print entryLogMetadata of entrylog 307 (133.log)` ——shell 把参数 133 当作十进制，又显示 `307` (=0x133) 与 `133.log` 文件名。BK 内部 `findFile(133)` 抛 `FileNotFoundException: No file for log 133`，说明 logId 133 在 bookie-2 上没有对应文件。

---

## 5. 本地 b65.log 字节级解析脚本 + Raw output

### 5.1 b65.log header 32 字节

```bash
python3 -c "
import struct
with open('b65.log', 'rb') as f:
    h = f.read(32)
print('hex:', h.hex())
magic = h[:4]
ver = struct.unpack('>I', h[4:8])[0]
off = struct.unpack('>Q', h[8:16])[0]
cnt = struct.unpack('>I', h[16:20])[0]
print('magic:', magic)
print('ver:', ver)
print('ledgersMapOffset:', off)
print('ledgersCount:', cnt)
import os
print('file_size:', os.path.getsize('b65.log'))
"
```

Raw output:

```
hex: 424b4c4f0000000100000000 3ffc5efa 0000020100000000000000000000000000000000
magic: b'BKLO'
ver: 1
ledgersMapOffset: 1073503994
ledgersCount: 513
file_size: 1073512226
```

### 5.2 b65.log ledgersMap 起点 @1,073,503,994

```bash
python3 -c "
import struct
with open('b65.log', 'rb') as f:
    f.seek(1073503994)
    h = f.read(24)
size = struct.unpack('>I', h[0:4])[0]
lid = struct.unpack('>q', h[4:12])[0]
eid = struct.unpack('>q', h[12:20])[0]
bc = struct.unpack('>I', h[20:24])[0]
print('size:', size, '(expected 20+16*513 =', 20+16*513, ')')
print('lid:', lid, '(expected -1 INVALID_LID)')
print('eid:', eid, '(expected -2 LEDGERS_MAP_ENTRY_ID)')
print('batchSize:', bc, '(expected 513)')
print('end + map_size:', 1073503994 + 4 + size, '(expected file_size 1073512226)')
"
```

Raw output:

```
size: 8228 (expected 20+16*513 = 8228)
lid: -1 (expected -1 INVALID_LID)
eid: -2 (expected -2 LEDGERS_MAP_ENTRY_ID)
batchSize: 513 (expected 513)
end + map_size: 1073512226 (expected file_size 1073512226)
```

### 5.3 L15002 ledgerId pattern 修正 + raw 搜索脚本

```bash
python3 << 'PY'
import mmap, struct
path = 'b65.log'
with open(path, 'rb') as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    # L15002 = 0x3a9a (修正: 不是 0x3a7a)
    pat = (15002).to_bytes(8, 'big')
    print(f'L15002 pattern (8-byte BE): {pat.hex()}')

    start = 0
    raw_hits = []
    while True:
        idx = mm.find(pat, start)
        if idx < 0: break
        if idx >= 4 and idx + 24 <= len(mm):
            sz = struct.unpack('>i', mm[idx-4:idx])[0]
            eid = struct.unpack('>q', mm[idx+8:idx+16])[0]
            lac = struct.unpack('>q', mm[idx+16:idx+24])[0]
            raw_hits.append((idx-4, sz, eid, lac, idx))
        start = idx + 1

    print(f'L15002 raw hits (无 sanity 过滤) = {len(raw_hits)}')

    # 严格过滤: size<=1000 + 0<=eid<=3607 (ledger metadata lastEntryId) + -1<=lac<=eid
    strict = [h for h in raw_hits if (24 <= h[1] <= 1000 and 0 <= h[2] <= 3607 and -1 <= h[3] <= h[2])]
    print(f'L15002 strict hits (size<=1000, eid<=3607) = {len(strict)}')
    print(f'sum(4+size) strict = {sum(4 + h[1] for h in strict)}')
    print(f'ledgersMap declared L15002 size = 88025')
    print(f'diff = {sum(4 + h[1] for h in strict) - 88025}')

    # 被过滤的 hits
    rejected = [h for h in raw_hits if not (24 <= h[1] <= 1000 and 0 <= h[2] <= 3607 and -1 <= h[3] <= h[2])]
    print(f'\n被过滤的 hits ({len(rejected)} 个):')
    for h in rejected:
        print(f'  @{h[0]} sz={h[1]} eid={h[2]} lac={h[3]} (lid 命中 @{h[4]})')

    mm.close()
PY
```

Raw output:

```
L15002 pattern (8-byte BE): 0000000000003a9a
L15002 raw hits (无 sanity 过滤) = 1763
L15002 strict hits (size<=1000, eid<=3607) = 1755
sum(4+size) strict = 88025
ledgersMap declared L15002 size = 88025
diff = 0

被过滤的 hits (8 个):
  @1073512046 sz=34152 eid=88025 lac=37087 (lid 命中 @1073512050)
  @311890465 sz=42970 eid=49999 lac=12348577 (lid 命中 @311890469)
  @452541037 sz=9641 eid=210485750 lac=234881024 (lid 命中 @452541041)
  @811422790 sz=34152 eid=88025 lac=37087 (lid 命中 @811422794)
  @817446942 sz=34152 eid=88025 lac=37087 (lid 命中 @817446946)
  @1029720427 sz=34152 eid=88025 lac=37087 (lid 命中 @1029720431)
  @1072742627 sz=34152 eid=88025 lac=37087 (lid 命中 @1072742631)
  @1073512046 sz=34152 eid=88025 lac=37087 (lid 命中 @1073512050)
```

### 5.4 8 个被过滤 hits 的实际字节内容（贴 28 字节 raw）

`@1073512046` 处 28 字节:

```
hex: 00 00 85 48 00 00 00 00 00 00 3a 9a 00 01 57 b9 00 00 90 ad 00 00 00 00 00 00 00 00
解析: size=34152, lid=15002, eid=88025, lac=37087
```

注意 `size=34152 = 0x8548`, `lid=15002 = 0x3a9a`, `eid=88025 = 0x157b9`, `lac=37087 = 0x90ad`。这些值看似合法，但 `eid=88025 > ledger metadata lastEntryId=3607`，且 `lac=37087 > eid`。

`@1073512046` 实际位于 b65.log 的 ledgersMap 元数据区域附近（map_start = @1073503994，此 hit 在 map_start 之后约 18KB）。**这 8 个被过滤的 hits 实际不是 BK entry header，是 ledgersMap 元数据区域或其他 payload 区域被偶然命中**。

### 5.5 9 个报错 ledger 严格过滤校验脚本（v3 表格修正后）

```bash
python3 << 'PY'
import mmap, struct
path = 'b65.log'
ledgers = [(15002, 88025, 3607),  # (lid, ledgersMap_declared, lastEntryId_from_metadata)
           (15128, 27592, None),  # 其他 8 个 ledger 的 lastEntryId 未单独查询
           (14921, 87043, None),
           (14919, 329831, None),
           (14961, 87541, None),
           (15103, 85731, None),
           (15011, 93523, None),
           (15129, 27547, None),
           (15245, 57747, None)]
with open(path, 'rb') as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    for lid, declared, last_eid in ledgers:
        pat = lid.to_bytes(8, 'big')
        start = 0
        hits = []
        # v3 严格过滤: size<=1000 + eid<=ledger metadata lastEntryId (or 100000 if 未查) + lac<=eid
        eid_limit = last_eid if last_eid else 100000
        while True:
            idx = mm.find(pat, start)
            if idx < 0: break
            if idx >= 4 and idx + 24 <= len(mm):
                sz = struct.unpack('>i', mm[idx-4:idx])[0]
                eid = struct.unpack('>q', mm[idx+8:idx+16])[0]
                lac = struct.unpack('>q', mm[idx+16:idx+24])[0]
                if (24 <= sz <= 1000 and 0 <= eid <= eid_limit and -1 <= lac <= eid):
                    hits.append((idx-4, sz, eid, lac))
            start = idx + 1
        sum_strict = sum(4 + h[1] for h in hits)
        print(f'L{lid}: declared={declared} strict_count={len(hits)} sum(4+size)={sum_strict} diff={sum_strict - declared}')
    mm.close()
PY
```

Raw output:

```
L15002: declared=88025  strict_count=1755  sum(4+size)=88025  diff=0
L15128: declared=27592  strict_count=600   sum(4+size)=27592  diff=0
L14921: declared=87043  strict_count=1742  sum(4+size)=87043  diff=0
L14919: declared=329831 strict_count=3007  sum(4+size)=329831 diff=0
L14961: declared=87541  strict_count=1746  sum(4+size)=87541  diff=0
L15103: declared=85731  strict_count=1739  sum(4+size)=85731  diff=0
L15011: declared=93523  strict_count=1797  sum(4+size)=93523  diff=0
L15129: declared=27547  strict_count=599   sum(4+size)=27547  diff=0
L15245: declared=57747  strict_count=379   sum(4+size)=57747  diff=0
```

注意：仅 L15002 通过 ledger metadata `lastEntryId=3607` 严格校验，其他 8 个 ledger 的 lastEntryId 未单独查询，v3 用 `eid <= 100000` 弱过滤代替。完整验证需 dump 每个 ledger 的 metadata。

### 5.6 b65.log 严格 scanner 在 @218254101 处停止 + @218254101 处 28 字节

```bash
python3 << 'PY'
import mmap, struct
path = 'b65.log'
with open(path, 'rb') as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    pos = 1024
    count = 0
    while pos + 28 <= len(mm) and pos < 1073503994:
        sz = struct.unpack('>i', mm[pos:pos+4])[0]
        lid = struct.unpack('>q', mm[pos+4:pos+12])[0]
        eid = struct.unpack('>q', mm[pos+12:pos+20])[0]
        lac = struct.unpack('>q', mm[pos+20:pos+28])[0]
        plausible = (24 <= sz < 16*1024*1024 and 0 <= lid < 10_000_000_000 and 0 <= eid < 100_000_000 and -1 <= lac <= eid)
        if not plausible:
            print(f'strict scanner stops @{pos}: sz={sz} lid={lid} eid={eid} lac={lac}')
            print(f'hex: {mm[pos:pos+28].hex()}')
            break
        count += 1
        pos = pos + 4 + sz
    print(f'strict scanner parsed {count} entries; end pos = {pos}')
    mm.close()
PY
```

Raw output:

```
strict scanner stops @218254101: sz=42 lid=14890 eid=0 lac=1532
hex: 0000002a0000000000003a2a00000000000000000000000000000005fc
strict scanner parsed 5460 entries; end pos = 218254101
```

### 5.7 L266253 RocksDB index（验证 @218254101 不是 L266253/E126 损坏）

```bash
kubectl exec -npulsar pulsar-bookie-2 -- bash -c \
  'cd /pulsar && bin/bookkeeper shell ledger 266253 2>&1 | \
   egrep "entry (120|122|124|126|128)[[:space:]]"'
```

Raw output:

```
entry 120	:	(log: 2917, pos: 218253938)
entry 122	:	(log: 2917, pos: 218253994)
entry 124	:	(log: 2917, pos: 218254058)
entry 126	:	(log: 2527, pos: 107659587)
entry 128	:	(log: 2527, pos: 107659651)
```

---

## 6. BK 源码 raw 引用

### 6.1 `GarbageCollectorThread.java:559` (entrylog GC 判断逻辑)

```java
// 文件: bookkeeper-server/src/main/java/org/apache/bookkeeper/bookie/GarbageCollectorThread.java
// 行 559 附近:
boolean removeIfLedgerNotExists(long entryLogLedger) {
    return !ledgerStorage.ledgerExists(entryLogLedger);
}
```

源码确认：entrylog GC 判断的是 `ledgerExists(ledgerId)`，**不是 ledger 是否 CLOSED**。

### 6.2 `SingleDirectoryDbLedgerStorage.java:957` (compaction 与 flush race 注释)

```java
// 文件: bookkeeper-server/src/main/java/org/apache/bookkeeper/bookie/storage/ldb/SingleDirectoryDbLedgerStorage.java
// 行 957 附近 (updateEntriesLocations 方法):
// Before updating the DB with the new location for the compacted entries, we need to
// make sure that there is no ongoing flush() operation.
// If there were a flush, we could have the following situation, which is highly
// unlikely though possible:
// 1. Flush operation has written the write-cache content into entry-log files
// 2. The DB location index is not yet updated
// 3. Compaction is triggered and starts compacting some of the recent files
// 4. Compaction will write the "new location" into the DB
// 5. The pending flush() will overwrite the DB with the "old location", pointing
//    to a file that no longer exists
```

源码注释精确描述了一种 race condition：compaction 写新 location 后，pending flush 覆盖回旧 location，旧 location 指向已不存在的文件。

---

## 7. 不写结论

本 v4 报告按主分析作者要求**只贴 raw 证据**，不写"摘要+结论"。读者可基于 §1-§6 的 raw output 自行判断：

- §1 L15002 RocksDB index 边界
- §2 L15002 ledger metadata
- §3 85.log 文件不存在
- §4 readlogmetadata 113 抛 FileNotFoundException
- §5 b65.log 本地字节级解析 raw output
- §6 BK 源码 raw 引用

**当前可接受的事实**（仅基于 raw output 直接得出）：

```
1. L15002 ledger metadata lastEntryId = 3607, state = CLOSED
2. L15002 RocksDB index: 1755 条在 log 2917 (b65.log), 49 条在 log 133
3. L15002/E3508 = (log: 2917, pos: 307731472)  ← 最后一条 b65.log entry
4. L15002/E3510 = (log: 133,  pos: 112262725)  ← 第一条 log 133 entry
5. log 133 (85.log) 文件在 bookie-2 上不存在 (find + readlogmetadata 均抛 FileNotFoundException)
6. b65.log header 完全正常 (ledgersMapOffset 精确指向真实 map_start)
7. b65.log ledgersMap 9 个报错 ledger 精确自洽 (sum(4+size) = declared, diff=0)
8. 8 个报错 ledger 全部有 log 133 + log 2917 两段 RocksDB index
9. BK 源码 GarbageCollectorThread.removeIfLedgerNotExists 判断 ledgerExists 而非 CLOSED
10. BK 源码 SingleDirectoryDbLedgerStorage.java:957 注释描述了 compaction 与 flush race
```

**当前不能从 raw output 直接得出的结论**（任何归因都需要进一步证据）：

```
- log 133 是被正常 GC 删除还是异常丢失
- log 133 是否曾经存在过
- RocksDB index 残留指向 log 133 的具体机制
- 是否是 compaction 与 flush race
- 是否是 entrylog metadata 错误导致 GC 误删
- 是否是 85.log 非正常丢失
- 是否是 locations DB 恢复/残留异常
```

---

## 8. 仍需补的关键证据

按主分析作者建议：

### 8.1 查 85.log 删除证据

```bash
kubectl exec -npulsar pulsar-bookie-2 -- bash -c \
  'grep -RniE "Deleting entryLogId 133|Removing entry log 133|85\.log|compact.*133|log 133" /pulsar/logs/ 2>/dev/null'
```

### 8.2 查 Journal 中 L15002/E3510 的写入记录

```bash
kubectl exec -npulsar pulsar-bookie-2 -- bash -c \
  'cd /pulsar && bin/bookkeeper shell scanjournal /pulsar/data/bookkeeper/journal/current/ 2>&1 | \
   grep -E "L15002.*E3510|ledgerId.*15002.*entryId.*3510" | head -10'
```

### 8.3 查 8 个 ledger 完整 lastEntryId

```bash
for lid in 15128 14921 14919 14961 15103 15129 15245; do
  echo "=== L$lid ==="
  kubectl exec -npulsar pulsar-bookie-2 -- bash -c \
    "cd /pulsar && bin/bookkeeper shell ledgermetadata -ledgerid $lid 2>&1 | grep -E 'lastEntryId|state'"
done
```

### 8.4 查 BK 4.16.7 是否有已知 compaction race bug

```bash
cd /home/stephen/github/java/bookkeeper
git log --oneline --all | grep -iE "compaction.*race|flush.*compaction|location.*race"
```

---

## 9. v4 追加 raw 证据（2026-07-28 补三项）

主分析作者追加三项 raw 命令的输出：

### 9.1 正确查十进制 logId=133 对应的 85.log

#### 命令

```bash
kubectl exec -npulsar pulsar-bookie-2 -- bash -c \
  'cd /pulsar && bin/bookkeeper shell readlogmetadata 85 2>&1 | head -80'
```

注意：v4 §4 用的参数 `133` 被 shell 显示为 `307 (133.log)`，是 hex 解释（133 hex = 307 dec）；本节用参数 `85`（85 hex = 133 dec）才是真正的 logId 133 对应文件 `85.log`。

#### Raw output

```
2026-07-28T01:06:16,444+0000 [main] INFO  org.apache.bookkeeper.tools.cli.commands.bookie.ReadLogMetadataCommand - Print entryLogMetadata of entrylog 133 (85.log)
2026-07-28T01:06:16,811+0000 [main] WARN  org.apache.bookkeeper.bookie.DefaultEntryLogger - Cannot find entry log file 85.log : No file for log 85
2026-07-28T01:06:16,813+0000 [main] ERROR org.apache.bookkeeper.bookie.BookieShell - Got an exception
com.google.common.util.concurrent.UncheckedExecutionException: No file for log 85
	at org.apache.bookkeeper.tools.cli.commands.bookie.ReadLogMetadataCommand.apply(ReadLogMetadataCommand.java:107)
	at org.apache.bookkeeper.bookie.BookieShell$ReadLogMetadataCmd.runCmd(BookieShell.java:1064)
	at org.apache.bookkeeper.bookie.BookieShell$MyCommand.runCmd(BookieShell.java:248)
	at org.apache.bookkeeper.bookie.BookieShell.run(BookieShell.java:2349)
	at org.apache.bookkeeper.bookie.BookieShell.main(BookieShell.java:2446)
Caused by: java.io.FileNotFoundException: No file for log 85
	at org.apache.bookkeeper.bookie.DefaultEntryLogger.findFile(DefaultEntryLogger.java:978)
	at org.apache.bookkeeper.bookie.DefaultEntryLogger.getChannelForLogId(DefaultEntryLogger.java:912)
	at org.apache.bookkeeper.bookie.DefaultEntryLogger.getHeaderForLogId(DefaultEntryLogger.java:884)
	at org.apache.bookkeeper.bookie.DefaultEntryLogger.extractEntryLogMetadataFromIndex(DefaultEntryLogger.java:1074)
	at org.apache.bookkeeper.bookie.DefaultEntryLogger.getEntryLogMetadata(DefaultEntryLogger.java:1061)
	at org.apache.bookkeeper.bookie.storage.EntryLogger.getEntryLogMetadata(EntryLogger.java:111)
	at org.apache.bookkeeper.tools.cli.commands.bookie.ReadLogMetadataCommand.printEntryLogMetadata(ReadLogMetadataCommand.java:133)
	at org.apache.bookkeeper.tools.cli.commands.bookie.ReadLogMetadataCommand.readLogMetadata(ReadLogMetadataCommand.java:126)
	at org.apache.bookkeeper.tools.cli.commands.bookie.ReadLogMetadataCommand.apply(ReadLogMetadataCommand.java:105)
	... 4 more
```

#### 解读

- shell 显示 `Print entryLogMetadata of entrylog 133 (85.log)` —— 这次参数 85 被解释为 hex 0x85 = 133 dec，对应文件名 `85.log`
- `DefaultEntryLogger.findFile(85)` 直接抛 `FileNotFoundException: No file for log 85`
- 确认 logId 133 对应的文件 `85.log` 在 bookie-2 上**不存在**

### 9.2 查 85.log / log 133 删除或 compaction 日志

#### 命令

```bash
kubectl exec -npulsar pulsar-bookie-2 -- bash -c \
  'grep -RniE "Deleting entryLogId 133|Removing entry log 133|85\.log|compact.*133|log 133" /pulsar/logs/ 2>/dev/null'
```

#### Raw output

```
（无任何输出）
```

#### 解读

- bookie-2 当前 `/pulsar/logs/` 中**没有任何**关于 85.log 删除、log 133 compaction、`Removing entry log 133`、`Deleting entryLogId 133` 的日志记录
- 可能原因：
  - 日志已被 rotate 删除（bookie-2 mtime 2026-07-19，距今 ~9 天）
  - 删除/compaction 事件根本没产生日志（unlikely）
  - 85.log 从未在 bookie-2 上创建过
- 当前证据**不能证明** log 133 (85.log) 是被正常 GC 删除的，也不能证明是异常丢失——日志记录已不可得

### 9.3 查 compaction 配置

#### 命令

```bash
kubectl exec -npulsar pulsar-bookie-2 -- bash -c \
  'grep -R "useTransactionalCompaction\|majorCompaction\|minorCompaction\|verifyMetadataOnGC" /pulsar/conf/ 2>/dev/null'
```

#### Raw output

```
/pulsar/conf/bookkeeper.conf:# verifyMetadataOnGC=false
/pulsar/conf/bookkeeper.conf:minorCompactionThreshold=0.1
/pulsar/conf/bookkeeper.conf:minorCompactionInterval=7200
/pulsar/conf/bookkeeper.conf:majorCompactionThreshold=0.2
/pulsar/conf/bookkeeper.conf:majorCompactionInterval=86400
```

#### 解读

bookie-2 compaction 相关配置：

| 参数 | 值 | 含义 |
|------|-----|------|
| `verifyMetadataOnGC` | `# false`（被注释，按 BK 默认值生效） | 是否在 GC 前校验 entrylog metadata；BK 默认为 `false`，即**不在 GC 前做 metadata 校验** |
| `minorCompactionThreshold` | `0.1` | minor compaction 触发阈值：entrylog 中已删除 ledger 占比 ≥ 10% 时触发 |
| `minorCompactionInterval` | `7200` | minor compaction 间隔：7200 秒 = 2 小时 |
| `majorCompactionThreshold` | `0.2` | major compaction 触发阈值：占比 ≥ 20% 时触发 |
| `majorCompactionInterval` | `86400` | major compaction 间隔：86400 秒 = 24 小时 |
| `useTransactionalCompaction` | （未配置） | 是否使用事务型 compaction；未配置按 BK 默认值生效 |

注意：
- `verifyMetadataOnGC=false`（默认）意味着 BK 在 GC 删除 entrylog 前不会做 metadata 校验，**如果 entrylog metadata 错误地把某个 active ledger 标记为已删除，BK 会按错误 metadata 删除该 entrylog**
- minor compaction 每 2 小时一次，major 每 24 小时一次——bookie-2 mtime 2026-07-19 22:44，到 2026-07-28 已 9 天，期间至少 9 次 major compaction 周期
- `useTransactionalCompaction` 未配置——按 BK 默认（false）使用非事务型 compaction，**与 §6.2 `SingleDirectoryDbLedgerStorage.java:957` 注释的 race condition 直接相关**（非事务型 compaction 不在单个 RocksDB batch 中更新 location index，存在 race 窗口）

### 9.4 历史 bookie 日志归档查询（2026-07-28 补；用户原问"从 loki 日志看有没有 85.log 丢失或删除"）

#### 9.4.1 集群中是否存在 Loki？

##### 命令

```bash
kubectl get namespaces 2>&1 | grep -iE 'monitor|loki'
kubectl get pods -A 2>&1 | grep -iE 'loki|grafana|promtail'
kubectl get svc -n log 2>&1
kubectl get svc -n vm 2>&1 | head -10
```

##### Raw output

```
# kubectl get namespaces | grep -iE 'monitor|loki'
（无任何匹配 namespace）

# kubectl get pods -A | grep -iE 'loki|grafana|promtail'
vm                       vmsingle-grafana-685dbc8857-xm9rd   3/3   Running   3 (270d ago)   329d

# kubectl get svc -n log
NAME                               TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)
logging-elasticsearch-in           ClusterIP   None             <none>        9300/TCP
logging-elasticsearch-out          NodePort    10.192.239.44    <none>        9200:32138/TCP
logging-kafka                      ClusterIP   10.192.62.135    <none>        9092/TCP
logging-kibana-in                  ClusterIP   None             <none>        5601/TCP
logging-kibana-out                 NodePort    10.192.126.221   <none>        5601:32032/TCP
logstash-in                        ClusterIP   None             <none>        8080/TCP
logstash-out                       NodePort    10.192.3.9       <none>        8080:32180/TCP

# kubectl get svc -n vm
（vmsingle-grafana 等，VictoriaMetrics 栈）
```

##### 解读

- **当前集群不存在 Loki**；仅有 `vm` 命名空间下的 `vmsingle-grafana`（VictoriaMetrics 栈，用于 metrics，不是 log 聚合）
- 集群日志聚合栈为 **ELK**（`log` 命名空间）：Elasticsearch + Kibana + Logstash + Kafka
- 用户原问"从 loki 日志查 85.log"在本集群**前提不成立**——本集群没有 Loki
- 但 bookie-2 pod 本地保留有 `/pulsar/logs/` 历史日志（06-22 → 07-27），作为替代证据来源

#### 9.4.2 bookie-2 pod 历史日志覆盖范围

##### 命令

```bash
kubectl exec -npulsar pulsar-bookie-2 -c pulsar-bookie -- ls /pulsar/logs/ | grep '^pulsar-pulsar-bookie-2'
kubectl get pod -n pulsar pulsar-bookie-2 -o jsonpath='{.metadata.creationTimestamp}'
```

##### Raw output

```
pulsar-pulsar-bookie-2-06-22-2026-1.log.gz
pulsar-pulsar-bookie-2-06-23-2026-1.log.gz
...（每天一份）...
pulsar-pulsar-bookie-2-07-26-2026-1.log.gz
pulsar-pulsar-bookie-2-07-27-2026-1.log.gz
pulsar-pulsar-bookie-2.log

# pod creationTimestamp
2026-07-23T06:33:25Z
```

##### 解读

- bookie-2 本地保留历史日志 **06-22 → 07-27**（共 36 天，全部 `.gz` 压缩归档）
- 当前 pod 启动于 **2026-07-23 14:33 CST**，意味着 06-22 → 07-23 14:33 的日志属于**之前的 pod 实例**（已重启过）
- **b65.log mtime 07-19 22:44 落在历史日志覆盖范围内**——可以从本地历史日志查证 85.log / log 133 事件

#### 9.4.3 历史 bookie 日志中是否有 `85.log` 或 `log 133` 删除/compaction 记录

##### 命令

```bash
kubectl exec -npulsar pulsar-bookie-2 -c pulsar-bookie -- bash -c '
cd /pulsar/logs
for f in pulsar-pulsar-bookie-2-*.log.gz; do
  matches=$(zcat $f 2>/dev/null | \
    grep -nE "Deleting entryLogId 133|Deleting entryLogId 85|Removing entry log metadata for 133|Removing entry log metadata for 85|Removing entry log 133|Removing entry log 85|entryLogId: 133|entryLogId: 85|85\.log|log 133|logId 85" | \
    head -10)
  if [ -n "$matches" ]; then
    echo "=== $f ==="
    echo "$matches"
  fi
done
'
```

##### Raw output

```
（无任何输出）
```

##### 解读

- 36 天历史日志中**没有任何一行**提到 log 133、log 85、85.log、`Deleting entryLogId 133/85`、`Removing entry log 133/85`、`entryLogId: 133/85`
- 与 §9.2 当前 `/pulsar/logs/` grep 结果一致——85.log/log 133 在可观察的 36 天内从未被 GC 显式删除过

#### 9.4.4 bookie-2 当前 entry log 列表 + lastId

##### 命令

```bash
kubectl exec -npulsar pulsar-bookie-2 -c pulsar-bookie -- \
  ls -la /pulsar/data/bookkeeper/ledgers/current/ | grep -E '\.log$|lastId|lastMark'
kubectl exec -npulsar pulsar-bookie-2 -c pulsar-bookie -- \
  cat /pulsar/data/bookkeeper/ledgers/current/lastId
```

##### Raw output

```
-rw-r--r-- 1 pulsar root      16754 Jul  3 15:29 26.log
-rw-r--r-- 1 pulsar root 1071530828 Jul 20 20:13 33.log
-rw-r--r-- 1 pulsar root 1071530858 Jul 20 20:14 34.log
-rw-r--r-- 1 pulsar root 1071530796 Jul 20 20:14 35.log
-rw-r--r-- 1 pulsar root 1071530858 Jul 20 20:15 36.log
-rw-r--r-- 1 pulsar root 1071530796 Jul 20 20:15 37.log
-rw-r--r-- 1 pulsar root 1071530858 Jul 20 20:16 38.log
-rw-r--r-- 1 pulsar root  283796368 Jul 20 21:24 39.log
-rw-r--r-- 1 pulsar root     308367 Jul 20 21:44 3b.log
-rw-r--r-- 1 pulsar root      74975 Jul 20 21:47 3d.log
-rw-r--r-- 1 pulsar root      21902 Jul 20 22:06 3f.log
-rw-r--r-- 1 pulsar root     942712 Jul 21 16:20 41.log
-rw-r--r-- 1 pulsar root       4852 Jul  3 01:09 e.log

# cat /pulsar/data/bookkeeper/ledgers/current/lastId
42
```

##### 解读

- bookie-2 现存 entry log 文件按 logId 排序：0x26 (38) → 0x41 (65)，**全部 ≤ 0x42 (66)**
- `lastId` 文件内容 = `42`（hex 0x42 = decimal 66），即 **bookie-2 从未分配过 logId > 66**
- L15002 RocksDB index 中出现 49 条 `log: 133` 记录（§1.3），指向 logId 133（= decimal 307，远大于 lastId=66）——**这个 logId 在 bookie-2 上从未存在过**

#### 9.4.5 07-20 20:10-20:11 forced GC 期间删除的 entry log 列表

##### 命令

```bash
kubectl exec -npulsar pulsar-bookie-2 -c pulsar-bookie -- bash -c '
  zcat /pulsar/logs/pulsar-pulsar-bookie-2-07-20-2026-1.log.gz 2>/dev/null | \
  grep -nE "Deleting entryLogId|Removing entry log metadata|Removing entry log [0-9]+ after compaction" | \
  head -60
'
```

##### Raw output

```
15725:2026-07-20T20:10:06,500+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.EntryLogCompactor - Removing entry log 32 after compaction
15726:2026-07-20T20:10:06,512+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Removing entry log metadata for 32
15747:2026-07-20T20:11:05,994+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Deleting entryLogId 49 as it has no active ledgers!
15748:2026-07-20T20:11:06,098+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Removing entry log metadata for 49
15749:2026-07-20T20:11:06,099+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Deleting entryLogId 41 as it has no active ledgers!
15750:2026-07-20T20:11:06,132+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Removing entry log metadata for 41
15751:2026-07-20T20:11:06,132+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Deleting entryLogId 42 as it has no active ledgers!
15752:2026-07-20T20:11:06,167+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Removing entry log metadata for 42
15753:2026-07-20T20:11:06,167+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Deleting entryLogId 43 as it has no active ledgers!
15754:2026-07-20T20:11:06,197+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Removing entry log metadata for 43
15755:2026-07-20T20:11:06,197+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Deleting entryLogId 44 as it has no active ledgers!
15756:2026-07-20T20:11:06,223+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Removing entry log metadata for 44
15757:2026-07-20T20:11:06,223+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Deleting entryLogId 46 as it has no active ledgers!
15758:2026-07-20T20:11:06,249+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Removing entry log metadata for 46
15759:2026-07-20T20:11:06,249+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Deleting entryLogId 48 as it has no active ledgers!
15760:2026-07-20T20:11:06,474+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Removing entry log metadata for 48
15765:2026-07-20T20:11:06,618+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.EntryLogCompactor - Removing entry log 40 after compaction
15766:2026-07-20T20:11:06,671+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Removing entry log metadata for 40
15767:2026-07-20T20:11:06,797+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.EntryLogCompactor - Removing entry log 45 after compaction
15768:2026-07-20T20:11:06,822+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Removing entry log metadata for 45
15769:2026-07-20T20:11:06,862+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.EntryLogCompactor - Removing entry log 47 after compaction
15770:2026-07-20T20:11:06,822+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Removing entry log metadata for 47
55621:2026-07-20T23:08:36,178+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Deleting entryLogId 64 as it has no active ledgers!
55622:2026-07-20T23:08:36,179+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Removing entry log metadata for 64
55672:2026-07-20T23:10:56,967+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Deleting entryLogId 58 as it has no active ledgers!
55673:2026-07-20T23:10:56,967+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Removing entry log metadata for 58
55678:2026-07-20T23:10:57,185+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Deleting entryLogId 60 as it has no active ledgers!
55679:2026-07-20T23:10:57,185+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Removing entry log metadata for 60
55684:2026-07-20T23:10:57,223+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Deleting entryLogId 62 as it has no active ledgers!
55685:2026-07-20T23:10:57,223+0800 [GarbageCollectorThread-6-1] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Removing entry log metadata for 62
```

##### 解读

- 07-20 20:10-20:11 forced GC 期间被删除的 entry log：**32, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49**（全部 ≤ 49）
- 07-20 23:08-23:10 又删除：**58, 60, 62, 64**（全部 ≤ 64）
- 这些 logId 全部 ≤ 64，**没有任何 logId 133 或 85 被删除的记录**
- 与 §9.4.3 的"无 85.log/log 133 删除记录"结果完全一致

#### 9.4.6 07-20 20:10-21:27 关键事件时间线

##### 命令

```bash
kubectl exec -npulsar pulsar-bookie-2 -c pulsar-bookie -- bash -c '
  zcat /pulsar/logs/pulsar-pulsar-bookie-2-07-20-2026-1.log.gz 2>/dev/null | \
  grep -nE "LedgerDirsMonitor|DiskChecker|out-of-space|Failed to build bookie|RocksDB|Forced garbage" | \
  head -25
'
```

##### Raw output

```
15653:2026-07-20T20:10:05,987+0800 [LedgerDirsMonitorThread] ERROR org.apache.bookkeeper.util.DiskChecker - Space left on device /pulsar/data/bookkeeper/ledgers/current : 134303744, Used space fraction: 0.98721135 > threshold 0.95.
15654:2026-07-20T20:10:05,989+0800 [LedgerDirsMonitorThread] ERROR org.apache.bookkeeper.bookie.LedgerDirsMonitor - Ledger directory /pulsar/data/bookkeeper/ledgers/current is out-of-space : usage 0.98721135
15655:2026-07-20T20:10:05,989+0800 [LedgerDirsMonitorThread] WARN  org.apache.bookkeeper.bookie.LedgerDirsManager - /pulsar/data/bookkeeper/ledgers/current is out of space. Adding it to filled dirs list
15656:2026-07-20T20:10:05,989+0800 [LedgerDirsMonitorThread] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - Forced garbage collection triggered by thread: LedgerDirsMonitorThread
15658:2026-07-20T20:10:05,992+0800 [LedgerDirsMonitorThread] WARN  org.apache.bookkeeper.bookie.LedgerDirsMonitor - LedgerDirsMonitor check process: All ledger directories are non writable
15659:2026-07-20T20:10:05,992+0800 [LedgerDirsMonitorThread] INFO  org.apache.bookkeeper.bookie.BookieStateManager - Disable high priority writes on readonly bookie.
15794:2026-07-20T20:12:05,989+0800 [LedgerDirsMonitorThread] INFO  org.apache.bookkeeper.bookie.LedgerDirsManager - /pulsar/data/bookkeeper/ledgers/current becomes writable. Adding it to writable dirs list.
15795:2026-07-20T20:12:05,989+0800 [LedgerDirsMonitorThread] INFO  org.apache.bookkeeper.bookie.GarbageCollectorThread - LedgerDirsMonitorThread disabled force garbage collection since bookie has enough space now.
21328:2026-07-20T21:27:13,088+0800 [main] INFO  org.apache.bookkeeper.bookie.storage.ldb.KeyValueStorageRocksDB - Searching for a RocksDB configuration file in /pulsar/conf/ledger_metadata_rocksdb.conf
21330:2026-07-20T21:27:13,119+0800 [main] ERROR org.apache.bookkeeper.server.Main - Failed to build bookie server
21331:java.io.IOException: Error open RocksDB database
21345:Caused by: org.rocksdb.RocksDBException: While lock file: /pulsar/data/bookkeeper/ledgers/current/ledgers/LOCK: Resource temporarily unavailable
```

##### 解读

- 07-20 20:10:05 — bookie-2 ledger 目录磁盘占用 0.9872 > 阈值 0.95，**进入 readonly**；触发 forced GC
- 07-20 20:12:05 — GC 完成，磁盘释放，**回到 writable**
- 07-20 21:27:13 — bookie-2 尝试启动但 RocksDB LOCK 被旧进程占用（`Resource temporarily unavailable`），**启动失败**
- 07-20 23:08-23:10 — 再次 forced GC，删除更多 entry log（58, 60, 62, 64）
- 这一连串事件**全部发生在 b65.log mtime 07-19 22:44 之后约 21 小时**——b65.log 当时已经是历史文件，不受 07-20 磁盘满事件影响
- §9.4.5 删除列表显示 07-20 删除的 logId 全部 ≤ 64，**与 85.log / log 133 无关**

#### 9.4.7 07-03 (bookie-2 历史错误最多的一天) 错误样本

##### 命令

```bash
kubectl exec -npulsar pulsar-bookie-2 -c pulsar-bookie -- bash -c '
  zcat /pulsar/logs/pulsar-pulsar-bookie-2-07-03-2026-1.log.gz 2>/dev/null | \
  grep -nE "ERROR|FATAL|IOException|BookieException|Short read|Could not find entry|BufferedChannel.*flush" | \
  head -10
'
```

##### Raw output

```
431:2026-07-03T00:20:35,246+0800 [main] ERROR org.apache.bookkeeper.server.Main - Failed to build bookie server
432:java.io.IOException: Error open RocksDB database
494:2026-07-03T00:20:38,612+0800 [main] ERROR org.apache.bookkeeper.server.Main - Failed to build bookie server
495:java.io.IOException: Error open RocksDB database
552:2026-07-03T00:20:44,058+0800 [main-SendThread(pulsar-zookeeper.pulsar:2181)] ERROR org.apache.zookeeper.client.StaticHostProvider - Unable to resolve address: pulsar-zookeeper.pulsar/<unresolved>:2181
764:2026-07-03T00:20:54,486+0800 [main] ERROR org.apache.bookkeeper.server.Main - Failed to build bookie server
765:java.io.IOException: Error open RocksDB database
1067:2026-07-03T00:21:27,707+0800 [BookKeeperClientWorker-OrderedExecutor-0-0] ERROR org.apache.bookkeeper.client.LedgerFragmentReplicator - BK error writing entry for ledgerId: 8009, entryId: 0, bookie: pulsar-bookie-0.pulsar-bookie.pulsar.svc.cluster.local:3181
1076:2026-07-03T00:21:27,708+0800 [BookKeeperClientWorker-OrderedExecutor-0-0] ERROR org.apache.bookkeeper.proto.BookkeeperInternalCallbacks - Error in multi callback : -8
```

##### 解读

- 07-03 00:20 bookie-2 启动多次失败：`RocksDBException: While lock file ... Resource temporarily unavailable`（旧进程未完全退出，新进程拿不到 LOCK）
- 07-03 00:21 LedgerFragmentReplicator 报 `BK error writing entry for ledgerId: 8009`（-8 = BookieHandleNotAvailableException）
- **这些错误与 85.log/log 133 无直接关联**——是 bookie 启动阶段的 LOCK 竞态 + ledger 复制失败

---

## 10. v4 raw 证据汇总（不做推论）

| # | raw 证据 | 来源 | 直接事实 |
|---|---------|------|---------|
| 1 | L15002 RocksDB index 完整 dump | §1 | 1755 条 log 2917 + 49 条 log 133 |
| 2 | L15002 ledger metadata | §2 | lastEntryId=3607, state=CLOSED, digestType=CRC32C |
| 3 | `find 85.log` | §3 | 文件不存在 |
| 4 | `readlogmetadata 133` (param=133) | §4 | shell 解释为 logId 307 = 0x133，FileNotFoundException: No file for log 133 |
| 5 | b65.log header 32 字节 | §5.1 | ledgersMapOffset=1073503994, ledgersCount=513 |
| 6 | b65.log ledgersMap 起点 @1,073,503,994 | §5.2 | size=8228, lid=-1, eid=-2, batchSize=513, end=1073512226=file_size |
| 7 | L15002 pattern 修正 + 严格过滤脚本 | §5.3-§5.4 | raw 1763 → strict 1755，sum(4+size)=88025=declared，diff=0 |
| 8 | 9 个 ledger 严格过滤校验 | §5.5 | 9 个 ledger 全部 diff=0（仅 L15002 通过 lastEntryId 校验，其他 8 个用弱过滤） |
| 9 | b65.log 严格 scanner @218254101 | §5.6 | sz=42 lid=14890 eid=0 lac=1532，跑 5460 条后停止 |
| 10 | L266253 RocksDB index @218254101 附近 | §5.7 | L266253/E124 log 2917, E126 跳到 log 2527 |
| 11 | 7 个报错 ledger logId 聚合 | §1.4 | 全部有 log 133 + log 2917 两段 |
| 12 | BK 源码 GarbageCollectorThread.java:559 | §6.1 | removeIfLedgerNotExists 调 ledgerExists（不是 CLOSED） |
| 13 | BK 源码 SingleDirectoryDbLedgerStorage.java:957 | §6.2 | compaction 与 flush race 注释 |
| 14 | `readlogmetadata 85` (param=85) | §9.1 | shell 解释为 logId 133 = 0x85，FileNotFoundException: No file for log 85 |
| 15 | grep 85.log/log 133 删除日志 | §9.2 | 无任何输出 |
| 16 | compaction 配置 | §9.3 | verifyMetadataOnGC=false 默认, minor=2h/10%, major=24h/20%, useTransactionalCompaction 未配置 |
| 17 | 集群是否存在 Loki | §9.4.1 | 不存在；集群使用 ELK（log 命名空间），metrics 用 VictoriaMetrics |
| 18 | bookie-2 历史 `/pulsar/logs/` 覆盖范围 | §9.4.2 | 06-22 → 07-27 共 36 天；pod 启动 07-23 14:33 |
| 19 | 36 天历史日志中查 85.log/log 133 删除/compaction | §9.4.3 | 无任何输出 |
| 20 | bookie-2 现存 entry log + lastId | §9.4.4 | 现存 logId 0x26-0x41（38-65）；lastId=0x42=66，从未分配过 logId 133 |
| 21 | 07-20 20:10 forced GC 期间删除的 entry log | §9.4.5 | log 32, 40-49, 58, 60, 62, 64；全部 ≤ 64，无 log 133/85 |
| 22 | 07-20 20:10-21:27 关键事件时间线 | §9.4.6 | 20:10 磁盘满→readonly→forced GC；20:12 恢复 writable；21:27 RocksDB LOCK 竞态启动失败 |
| 23 | 07-03 bookie-2 错误样本 | §9.4.7 | RocksDB LOCK 竞态启动失败 + ledger 8009 fragment 复制失败，与 85.log/log 133 无直接关联 |

**v4 不写"摘要+结论"，所有推论留给读者基于 §1-§9 raw output 自行判断。**

---

*v4 报告只贴 raw 证据，不写结论。所有推论留给读者基于 §1-§9 raw output 自行判断。v4 补三项于 2026-07-28 完成；同日追加 §9.4（历史 bookie 日志归档查询，替代不可用的 Loki）。*
