# BookKeeper EntryLog 855.log (logId 2133) 损坏调查记录

> **文档目的**：完整记录 2026-07-23 前后针对 `pulsar-bookie-1` 上 EntryLog 损坏、Autorecovery EIO 的排查过程与结论，供后续基于 BookKeeper 源码分析，或供他人据此推导、复现、诊断。
>
> **调查时间**：2026-07-23 ~ 2026-07-27  
> **问题节点**：`pulsar-bookie-1`  
> **问题文件**：`data/bookkeeper/ledgers/current/855.log`（EntryLog **logId = 2133**，十六进制文件名 `855` = `0x855`）  
> **典型 Ledger**：**15069**（旧 cursor ledger，Autorecovery 无法修复）

---

## 1. 执行摘要

### 1.1 现象

业务重启/升级后，集群 Autorecovery（`ReplicationWorker`）持续失败：从 `bookie-1` 读取多条 **CLOSED 旧 cursor ledger**（如 L15069）时返回 **`code EIO`**，导致 underreplicated ledger 无法修复，日志刷屏（defer 300s 后重试）。

### 1.2 根因（调查结论）

**不是单一原因**，`855.log` 上存在 **多种并存的损伤**：

| 区域 | 偏移（约） | 损伤类型 | 证据强度 |
|------|------------|----------|----------|
| 文件头 ~86KB | `@86326` | **顺序 EntryLog framing 断裂**：下一条 entry 头非法 | 高 |
| 中段 ~143MB | `@143591610` 等 6 点 | **索引指向处无 BK 头**，读到 payload/杂数据 | 高 |
| 顺序扫误读链 | `@386MB` → `@425MB` | **非独立损坏点**：86326 假超大 size 的连锁误读；425MB 处为 JSON 明文 `PathDetails` | 高 |
| 尾段 ~1.02GB | `@1025196187` 一带 | **盘上为合法 L15021 entry**；**L15069 的 RocksDB index 统一偏 +7**，且全文件 **无 L15069 (0x3add) 头** | 高 |

**对 L15069 的最终结论**：

- 唯一副本在 `bookie-1`（Qw=1），Autorecovery **算法上无法修复**（无第二可读源）。
- `855.log` **不包含** L15069 的可恢复 entry 数据；index 误指到 L15021 孤儿 entry 区域（+7 字节偏置）。
- 该 ledger 为 **已废弃的旧 cursor**（当前 `cursorLedger` 已切换到 30 万+），**业务不依赖修复**。

### 1.3 已排除的假设

| 假设 | 结论 |
|------|------|
| 升级后全集群 EntryLog 改用小端 (LE) | **排除**：同 bookie 上健康 cursor（如 323101）仍为大端 (BE) |
| 当前 DirectEntryLogger / logId 复用覆盖 855 | **排除**：`lastId` 与 max log 一致，855 为 Jul 8 seal 的旧文件 |
| 仅 readlog 顺序扫描假象、磁盘实际完好 | **排除**：按 index 绝对 offset `od` 读 143MB、1.02GB 同样失败 |
| L15069 仅偏几字节即可读出 | **排除**：`-3` 读到 L15021；`-7` 为完整 L15021/E21，非 L15069 |
| L15021 覆写了完好的 L15069 | **弱/基本排除**：全文件 `grep 00 00 3a dd`（L15069）零命中 |

---

## 2. 环境与上下文

### 2.1 集群组件

| 项 | 值 |
|----|-----|
| BookKeeper 版本（本地 Pulsar 仓库） | **4.16.7**（`pom.xml` `bookkeeper.version`） |
| 问题 Bookie | `pulsar-bookie-1.pulsar-bookie.pulsar.svc.cluster.local:3181` |
| EntryLog 路径 | `/pulsar/data/bookkeeper/ledgers/current/855.log` |
| 日志包目录 | 本目录 `bin/20260723/` |
| bookie-1 日志文件 | `pulsar-bookie-1-151842.log`（约 32312 行，UTC `04:54:52` ~ `07:18:41`） |

### 2.2 Bookie 配置要点（调查时已知）

- `journalWriteData/SyncData=true`
- 未使用 DirectEntryLogger
- compaction 开启
- `skipReplayJournalInvalidRecord/LostLog=true`
- `journalMaxBackups=0`（journal 旧文件保留策略需结合运维确认）

### 2.3 存储路径说明（DbLedgerStorage）

写入路径（简化）：

```text
WriteCache → Journal WAL → flush 到 EntryLog + RocksDB location index
           → checkpointComplete 推进 journal mark，可能删除旧 .txn
```

**Journal 职责**：启动时 replay checkpoint 之后的记录；**不能**在 runtime 修复已 seal 的 EntryLog EIO。855.log 已 seal（mtime Jul 8），checkpoint 完成后重启 **无法** 自动修复其 payload。

---

## 3. 业务与 Autorecovery 背景

### 3.1 受影响 Ledger 特征

- 几乎全部为 **CLOSED 的旧 cursor ledger**（metadata 含 `pulsar/cursor=...`）
- 典型配置：`E=2, Qw=1, Qa=1`
- Ledger ID 范围约 14k–15k（如 15069、15011、15103…）
- 当前订阅的 `cursorLedger` 已在 **30 万+**（如 alpha_app 从 307232 到 323101），与 15069 无关

### 3.2 Autorecovery 行为

| 角色 | 说明 |
|------|------|
| Auditor | 发现 underreplicated，写入 ZK `/ledgers/underreplication/...` |
| ReplicationWorker | 任意 bookie 上运行，抢锁后作为 **BK 客户端** 读源、写新副本 |

**日志在 bookie-2 不代表坏数据在 bookie-2**；L15069 的 fragment 明确 `Host: [bookie-1]`，EIO 来自源 bookie。

### 3.3 为何 Qw=1 仍进修复队列

Autorecovery 目标是 **替换故障节点上的唯一副本**，不是把 Qw=1 加成 2 副本。Qw=1 + 源 EIO = **信息论上不可恢复**。

已知社区缺口：不可恢复 ledger **无限重试**（[bookkeeper#3316](https://github.com/apache/bookkeeper/issues/3316)、[pulsar#14573](https://github.com/apache/pulsar/issues/14573)）。PR [#2870](https://github.com/apache/bookkeeper/pull/2870) 提供 `shell recover -sku`，**不**解决 ReplicationWorker 自动 abandon。

### 3.4 EIO 语义（BK 协议）

```text
ENOLEDGER = 402   本机无此 ledger
ENOENTRY  = 403   索引无此 entry
EIO       = 501   读过程中 IOException（索引认为应有，读字节失败）
```

bookie-1 上对应日志：

```text
DefaultEntryLogger - Read invalid entry length ...
DefaultEntryLogger - Sanity check failed for entry size of ... at location ... in 2133
```

---

## 4. 典型案例：Ledger 15069

### 4.1 ZK/BK Metadata（2026-07-24 采集）

```text
ledgerID: 15069
LedgerMetadata{
  formatVersion=3,
  ensembleSize=2, writeQuorumSize=1, ackQuorumSize=1,
  state=CLOSED,
  length=6809,
  lastEntryId=1137,
  digestType=CRC32C,
  ensembles={
    0    -> [bookie-1, bookie-0],      // entry 0..1137
    1138 -> [bookie-2, bookie-0]       // 空尾段切换
  },
  customMetadata={
    pulsar/managed-ledger -> persistent://10001001/default/ssl_tls_log-partition-1
    pulsar/cursor       -> alpha_app
  }
}
```

### 4.2 条带（Qw=1, E=2）

| Entry | 唯一持有者（ensemble 0） |
|-------|--------------------------|
| 0,2,4,…,1136 | **bookie-1** |
| 1,3,5,… | bookie-0 |

Autorecovery 读偶数 entry 只能打 bookie-1 → EIO。

### 4.3 bookie-1 本地 index（`ledger -m 15069`）

全部为 `(log: 2133, pos: …)`，首条：

```text
entry 0  : (log: 2133, pos: 1025196194)
entry 2  : (log: 2133, pos: 1025196239)
...
entry 1136: (log: 2133, pos: 1037338923)
```

**特征**：相邻偶数 entry 间距多为 **45 字节**（4 字节 size + 41 字节 body 的典型 cursor entry）。

### 4.4 Sanity 日志与 size 误读

```text
Sanity check failed for entry size of 687865856 at location 1025196194 in 2133
```

算术：

```text
687865856 = 0x29000000 = 大端解释字节 [29 00 00 00]
41        = 小端解释字节 [29 00 00 00]
```

说明 index pos **落在 BE size 字段 `00 00 00 29` 的第 4 字节 `29` 上**（偏 +3 读 size），或更完整地看，**真实 entry 起点比 index 早 7 字节**（见 §6.4）。

### 4.5 2026-07-27 现场复核：bookie-0 / bookie-1 对照

新增现场验证进一步坐实：**不是 ZK / ensemble metadata 指错**，而是 **bookie-1 本地的 location index 与 entrylog 内容不一致**。

#### 4.5.1 bookie-0：奇数 entry 正常存在于本地 `2482.log`

`bookie-0` 上执行：

```bash
./bin/bookkeeper shell ledger -m 15069 | head -n 10
./bin/bookkeeper shell ledger -m 15069 | tail -n 10
./bin/bookkeeper shell readlog 2482 -sp 1005476495 -ep 1005476541
```

结果显示：

- `entry 1,3,5,...,1137` 全部映射到 **`(log: 2482, pos: ...)`**
- `readlog 2482` 可直接解析出合法 entry：

```text
--------- Lid=15069, Eid=1127, ByteOffset=1005476495, EntrySize=42 ---------
Type:           DATA
LastConfirmed:  1126

--------- Lid=15069, Eid=1129, ByteOffset=1005476541, EntrySize=42 ---------
Type:           DATA
LastConfirmed:  1128
```

**结论**：`bookie-0` 正常持有并可读出 `L15069` 的奇数 entry；其本地 entrylog / index 路径无对应异常迹象。

#### 4.5.2 bookie-1：偶数 entry 被索引到 `855.log`，但文件内找不到对应 ledger/entry

`bookie-1` 上执行：

```bash
./bin/bookkeeper shell ledger -m 15069 | head -n 10
./bin/bookkeeper shell ledger -m 15069 | tail -n 10
./bin/bookkeeper shell readlog 2133 -sp 1037338689 -ep 1037338735
./bin/bookkeeper shell readlog 2133 -ledgerid 15069 -entryid 1126 -msg
```

结果显示：

- `entry 0,2,4,...,1136` 全部映射到 **`(log: 2133, pos: ...)`**
- 例如：

```text
entry 1126      :       (log: 2133, pos: 1037338693)
entry 1128      :       (log: 2133, pos: 1037338739)
entry 1130      :       (log: 2133, pos: 1037338785)
```

但针对同一范围 / 同一 entry 的 `readlog` 结果却是：

```text
WARN  DefaultEntryLogger - Short read for ledger entry from entryLog 2133@425908828 ...
Entry log 2133 (855.log) doesn't has any entry in the range 1037338689 - 1037338735.
LedgerId 15069  EntryId 1126 is not available in the entry log 2133 (855.log)
```

**结论**：

- `bookie-1` 的 RocksDB location index 认为 `L15069/E1126` 位于 `855.log`
- 但 `readlog` 按 `ledgerid=15069, entryid=1126` 在 `855.log` 中**无法找到对应 entry**
- 因而可确认：**bookie-1 本地存在 index/data 不一致**；这与前文“全文件无 `0x3add`（L15069）头、index 误指到 L15021 孤儿区”的结论一致

#### 4.5.3 对问题归属的含义

这组对照将问题边界进一步收紧为：

- **不是** ledger metadata / ensemble 把副本位置指错
- **不是** 两个 bookie 都在同一份 `855.log` 上出现一致性问题
- **而是** `bookie-1` 单侧：`L15069` 偶数 entry 的本地 index 指向 `2133/855.log`，但文件内容并不包含对应的可解析 entry

因此，对 `L15069` 而言，真正不可读的是 **bookie-1 这半边唯一副本**；`bookie-0` 的奇数 entry 正常，不足以恢复偶数 entry。

---

## 5. 文件 855.log 基本信息

| 项 | 值 |
|----|-----|
| logId | 2133 (0x855) |
| 文件名 | `855.log` |
| 节点 | pulsar-bookie-1 |
| 大小 | ~1.1 GB（调查时） |
| mtime | Jul 8 14:30（sealed） |
| 文件头 | `BKLO` v1 合法 |

---

## 6. 分区二进制取证

### 6.1 文件头：正常 BE Entry（1024 ~ 86326）

`readlog 2133 -sp 1024 -ep 90000` 顺序扫描结果：

| Lid | Eid | ByteOffset | EntrySize | 下一偏移 |
|-----|-----|------------|-----------|----------|
| 240725 | 5636 | 1024 | 43 | 1071 |
| 240725 | 5637 | 1071 | 43 | 1118 |
| 240726 | 10755 | 1118 | 63 | 1185 |
| 240727 | 17717 | 1185 | 29790 | 30979 |
| 240727 | 17719 | 30979 | 55343 | **86326** |
| （垃圾） | — | 86326 | 386008842 | → 连锁误读 |

**E17719 @30979 头验证（合法）**：

```bash
od -An -tx1 -N 40 -j 30979 data/bookkeeper/ledgers/current/855.log
```

```text
00 00 d8 2f              size = 55343
00 00 00 00 00 03 ac 57  Lid  = 240727
00 00 00 00 00 00 45 37  Eid  = 17719
00 00 00 00 00 00 45 35  LAC  = 17717
```

30979 + 4 + 55343 = **86326**。算术自洽，但 **86326 处不是下一条合法头**。

**86326 处 od**：

```text
86326: 17 02 07 0a 0f 7e 04 09 ...
       ^^^^^^^^^^^
       BE = 386008842（假超大 entry size）
```

86280~86326 均为 `0f …` 风格 payload，**边界两侧无 BK 头形态**。

> **结论**：顺序 EntryLog 链在 **86326** 断裂；此后 `readlog` 顺序扫描 **不可信**。

---

### 6.2 顺序扫误读链（386MB / 425MB）

由 86326 假 size 推导：

```text
86326 + 4 + 386008842 ≈ 386095172
386095172 + 4 + 39813647 ≈ 425908823
```

425908824 处 od：

```text
73 50 61 74 68 44 65 74 61 69 6c 73 22 3a 5b 22 63 3a 5c 5c
= ...sPathDetails":["c:\\
```

`73 50 61 74` 大端 = **1934647668**，与 `Short read` 警告一致。**425MB 是误读连锁，不是独立损坏带。**

---

### 6.3 中段 ~143MB：索引读失败

bookie-1 日志 Sanity location（2133）在此簇 **6 个唯一点**：

```text
143591610, 143592321, 143593915, 143598674, 143600277, 143600629
```

**od 取证**：

```bash
od -An -tx1 -N 40 -j 143591610 data/bookkeeper/ledgers/current/855.log
# 07 0b 1f 72 46 23 04 0f 74 03 06 0f 5c ...  (0f 流，非 BK 头)

od -An -tx1 -N 40 -j 143598674 data/bookkeeper/ledgers/current/855.log
# 37 4f fa 04 40 99 4e 04 ...  (杂二进制)

od -An -tx1 -N 40 -j 143600629 data/bookkeeper/ledgers/current/855.log
# 2f 04 0f ... 含 ASCII "M9059" 片段
```

**pos±3 也不能对齐到合法 BK 头** → 不是与 L15069 相同的固定 -3/+7 错位。

> **结论**：~143MB 处为 **内容/头损坏或 index 指向 payload**，与 1.02GB 的「L15021 好 entry + 错 index」机制 **不同**。

---

### 6.4 尾段 ~1.02GB：L15021 孤儿数据 + L15069 错 index（核心发现）

#### 6.4.1 L15069 index vs 真实 entry 起点（+7 偏置）

| L15069 Entry | Index pos | 真实 entry 起点 (pos-7) |
|--------------|-----------|-------------------------|
| E0 | 1025196194 | **1025196187** |
| E2 | 1025196239 | 1025196232 |
| E4 | 1025196284 | 1025196277 |

**真实 entry @1025196187（完整合法 BK 头，属于 L15021/E21）**：

```bash
od -An -tx1 -N 48 -j 1025196187 data/bookkeeper/ledgers/current/855.log
```

```text
00 00 00 29                 size = 41
00 00 00 00 00 00 3a ad     Lid  = 15021  (0x3aad)
00 00 00 00 00 00 00 15     Eid  = 21
00 00 00 00 00 00 00 14     LAC  = 20
00 00 00 00 00 00 00 70     length = 112
a8 a3 33 40 08 ac 75 10 22  payload + digest
00 00 00 ...                下一条 size 起始
```

**下一条 @1025196232（E22）**：

```text
00 00 00 29 | Lid=15021 | Eid=22 | LAC=21 | ...
```

连续、LAC 递增、间距 45 → **正常 append 的 L15021 流**。

#### 6.4.2 Index 状态

```bash
./bin/bookkeeper shell ledger -m 15021
# ERROR: Entry -1 not found in 15021   → 本机 RocksDB 无 L15021

./bin/bookkeeper shell ledger -m 15069
# 有完整 (log:2133, pos:...) 映射，但 pos = L15021 真实起点 + 7
```

#### 6.4.3 全文件搜索 L15069

```bash
grep -aob $'\x00\x00\x3a\xdd' data/bookkeeper/ledgers/current/855.log | head
# （无输出）→ 全文件不存在 L15069 的 Lid 形态 (0x3add)
```

#### 6.4.4 机制归纳

```text
855.log @ ~1.02GB:
  磁盘上 = 合法 L15021 entry 流（entrylog 孤儿，index 已删）

RocksDB:
  L15021 = 不存在
  L15069 = 存在，pos 指向 L15021 entry 内部 (+7)

读 L15069:
  从 pos 读 size → 踩进 Lid 字段 → Sanity 687865856 / EIO
```

**不是**「L15069 数据偏几字节可修复」；**是**「文件里根本没有 L15069，index 指错了」。

#### 6.4.5 关于「15021 先写还是覆写 15069」

| 判断 | 依据 |
|------|------|
| 盘上字节作者是 **15021** | 6187/6232 等处完整合法 framing |
| **855.log 内从未出现 L15069 头** | grep `3a dd` 零命中 |
| 正常 BK 只 append | 不支持「先写 15069 再原地被 15021 覆盖」作为主叙事 |
| 15021 < 15069 | 创建顺序上 15021 更早，与 orphan cursor 场景一致 |

---

## 7. bookie-1 日志统计（pulsar-bookie-1-151842.log）

| 指标 | 值 |
|------|-----|
| 时间窗口 | 2026-07-23T04:54:52 ~ 07:18:41 UTC |
| `Read invalid entry length` | 2121 次（93 个不同值） |
| `Sanity check failed ... in 2133` | **4794 次**（220 个唯一 location） |
| 涉及 EntryLog | **仅 2133** |
| Sanity location 分布 | ~143MB：**6** 点；~1.025–1.037GB：**214** 点 |
| L15069 E0 location 1025196194 | Sanity size **687865856**，出现 **66** 次 |

bookie-0 / bookie-2 **无** `Sanity check failed` / `Read invalid entry length`（bookie-2 仅有客户端 `code EIO`）。

---

## 8. 假设演进记录

| 阶段 | 假设 | 验证 | 结果 |
|------|------|------|------|
| 1 | Autorecovery bug / Qw=1 不应修 | 源码 + metadata | 修复流程设计如此；不可恢复无限重试是机制缺口 |
| 2 | 升级后全文件 LE 编码 | 健康 cursor 323101 @4705 | **排除** |
| 3 | 425MB 独立损坏 | od 为 JSON PathDetails | **误读连锁** |
| 4 | 386MB 独立损坏 | 86326 假 size 推导 | **误读连锁** |
| 5 | 中段 truncate 导致 L15069 固定错位 | pos-3 od | 读到 **L15021** 字段，非 L15069 |
| 6 | L15069 偏 -3 可读 | pos-3 | Lid=0x3aad=15021 |
| 7 | L15069 偏 -7 可读 | pos-7 @6187 | **完整 L15021/E21**，非 L15069 |
| 8 | 15021 覆写 15069 | grep 3a dd 全文件 | **零命中**，不支持 |

---

## 9. 综合损伤模型

```text
855.log (2133) on bookie-1
│
├─ [0 ~ 86KB]        正常 BE entry（240725/726/727…）
│
├─ [@86326]          顺序 framing 断裂（下一条头非法）
│                    └─→ 顺序 readlog 从此次起全部误读
│
├─ [@~143.6MB]       6 个 index location Sanity 失败
│                    内容 = 0f 流 / 杂数据（非 BK 头）
│
├─ [@386MB~425MB]    顺序扫误读区（含 PathDetails JSON 明文）
│
└─ [@~1.02GB]        磁盘 = 合法 L15021 entry 流
                     Index: L15021 已删，L15069 pos = 真实起点 + 7
                     全文件无 L15069 (0x3add)
```

**多种机制并存**，不宜用单一「truncate N 字节」解释全文件。

---

## 10. 可复现命令清单

以下命令均在 **pulsar-bookie-1** 上执行，`/pulsar` 为安装根目录。

### 10.1 文件与顺序扫描

```bash
# 文件头
od -An -tx1 -N 32 -j 0 data/bookkeeper/ledgers/current/855.log

# 顺序 readlog（86326 前正常）
./bin/bookkeeper shell readlog 2133 -sp 1024 -ep 90000

# 顺序 readlog（86326 后误读）
./bin/bookkeeper shell readlog 2133 -sp 300000000 -ep 380000000
```

### 10.2 关键 offset od

```bash
od -An -tx1 -N 40 -j 30979 data/bookkeeper/ledgers/current/855.log   # E17719 合法头
od -An -tx1 -N 48 -j 86322 data/bookkeeper/ledgers/current/855.log   # 86326 断裂点
od -An -tx1 -N 40 -j 143591610 data/bookkeeper/ledgers/current/855.log
od -An -tx1 -N 40 -j 425908824 data/bookkeeper/ledgers/current/855.log  # PathDetails

# L15069 / L15021 尾段
od -An -tx1 -N 48 -j 1025196187 data/bookkeeper/ledgers/current/855.log  # L15021/E21 真实起点
od -An -tx1 -N 32 -j 1025196191 data/bookkeeper/ledgers/current/855.log  # index-3（L15021 字段）
od -An -tx1 -N 32 -j 1025196232 data/bookkeeper/ledgers/current/855.log  # L15021/E22

grep -aob $'\x00\x00\x3a\xdd' data/bookkeeper/ledgers/current/855.log | head   # L15069：无
grep -aob $'\x00\x00\x3a\xad' data/bookkeeper/ledgers/current/855.log | head   # L15021：可选
```

### 10.3 本地 index

```bash
./bin/bookkeeper shell ledger -m 15069
./bin/bookkeeper shell ledger -m 15021   # 本机不存在
./bin/bookkeeper shell ledger -m 240727  # 已 GC
```

### 10.4 读 entry（预期失败）

```bash
# bookie-1：按 ledgerid/entryid 在 855.log 中查找，预期失败
./bin/bookkeeper shell readlog 2133 -ledgerid 15069 -entryid 1126 -msg

# bookie-0：在本地 2482.log 中验证奇数 entry 可正常解析
./bin/bookkeeper shell readlog 2482 -sp 1005476495 -ep 1005476541
```

### 10.5 日志关联

```bash
rg 'Sanity check failed.*in 2133' pulsar-bookie-1-151842.log | head
rg '687865856.*1025196194' pulsar-bookie-1-151842.log | head
rg 'ReplicationWorker.*15069' pulsar-bookie-2-151842.log | head
```

---

## 11. 后续 BookKeeper 源码分析指引

建议从以下路径入手（BookKeeper **4.16.7**），验证 **index 写入 offset** 与 **EntryLog append** 是否可能产生 **+7 系统性偏置**，以及 **86326 类 framing 断裂** 的写入/flush 路径。

### 11.1 读路径（EIO / Sanity 来源）

| 类 | 典型位置 | 关注点 |
|----|----------|--------|
| `DefaultEntryLogger` | `bookkeeper-server/.../DefaultEntryLogger.java` | `Sanity check failed for entry size`；`Read invalid entry length` |
| `ReadEntryProcessorV3` | `bookkeeper-server/.../ReadEntryProcessorV3.java` | IOException → EIO |
| `LedgerStorage` / `DbLedgerStorage` | `bookkeeper-server/.../storage/ldb/` | 从 RocksDB 取 location 后读 EntryLog |

**调查问题**：

1. Sanity 检查的 `location` 是 index 的 pos 还是 pos-4？
2. size 上限/合理性检查逻辑是什么？为何 687865856 会失败？

### 11.2 写路径与 index

| 类 | 关注点 |
|----|--------|
| `EntryLogger` / `EntryLogManagerForSingleEntryLog` | append 时如何计算并返回 `logId + offset` |
| `LedgerCacheImpl` / flush | WriteCache → EntryLog 刷盘 |
| `EntryLocationIndex` / RocksDB | `(ledgerId, entryId) → (logId, offset)` 何时写入 |
| `checkpoint` / `Checkpoint` | checkpoint 与 index、EntryLog 的一致性 |

**调查问题（针对 +7）**：

1. offset 是指向 **entry size 字段** 还是 **entry 起始（含 size）**？文档与实现是否一致？
2. 是否存在 **batch flush** 时 location 与 buffer 边界不一致的 bug？
3. L15021 index 被删（GC/compaction）而 L15069 index 仍指向同区域 —— 查 **ledger deletion** 与 **entrylog compaction** 交互。

### 11.3 Journal replay

| 类 | 关注点 |
|----|--------|
| `Journal` / `BookieJournal` | replay 是否可能重复写/错 offset |
| `skipReplayJournalInvalidRecord/LostLog` | 跳过坏 journal 记录后的状态 |

**调查问题**：855 已 seal，journal 能否解释 **sealed 文件内** 的损坏？（一般 **不能**，除非损坏在 seal 前已写入。）

### 11.4 Autorecovery

| 类 | 关注点 |
|----|--------|
| `ReplicationWorker` | `tryReadingFaultyEntries` 失败后的 defer 逻辑 |
| `LedgerChecker` | fragment 判定 |

### 11.5 建议的源码阅读顺序

```text
1. DefaultEntryLogger.readEntry / sanity check  → 理解 EIO 触发条件
2. DbLedgerStorage.readEntry                     → index → file offset
3. EntryLogger.addEntry / flush                    → offset 如何产生
4. EntryLocationIndex.addLocation                  → index 何时持久化
5. GarbageCollector / LedgersStorage.deleteLedger  → 15021 无 index 的原因
6. EntryLogCompactor                               → 是否可能留下 orphan entrylog
```

---

## 12. 运维建议（非源码）

1. **勿尝试手工修 855.log 字节或改 index 来「救」L15069** — 文件内无 L15069 数据。
2. 确认受影响 ledger **非当前 `cursorLedger`** 后，从 underreplication 清理或 skip。
3. 临时降低噪声：禁用 Autorecovery 或使用 `-sku`（视 BK 版本）。
4. 长期：提高 cursor ledger 的 Qw/Qa；关注不可恢复 ledger 的终结态。
5. 对齐 **Jul 7–8** 运维时间线（underreplication Ctime、855 mtime Jul 8 seal）查根因事件（杀进程、磁盘、升级）。

---

## 13. 未解问题 / 后续调查

| # | 问题 | 建议 |
|---|------|------|
| 1 | **+7 偏置如何产生** | 查 BK 4.16.7 index 写 offset 源码；对比 journal 与第一次 flush 记录（若仍有 .txn） |
| 2 | **86326 断裂当时写了什么** | 查同一时段还有哪些 ledger 的 index 指向 2133 且 offset < 1MB |
| 3 | **143MB 6 点属于哪些 ledger** | 从 RocksDB 反查 `(2133, 143591610)` 等（若 index 仍在） |
| 4 | **855 何时开始损坏** | 本日志包仅 07-23；需更早 bookie 日志或监控 |
| 5 | **15069 数据是否曾在别 bookie** | Qw=1 偶数仅在 bookie-1；bookie-0 无偶数 entry，**无副本** |

---

## 14. 相关文件索引

| 路径 | 说明 |
|------|------|
| `bin/20260723/pulsar-bookie-1-151842.log` | 源 bookie 损坏证据（Sanity/invalid length） |
| `bin/20260723/pulsar-bookie-2-151842.log` | ReplicationWorker / EIO 客户端 |
| `bin/20260723/pulsar-bookie-0-151841.log` | 对照（无 Sanity） |
| `data/bookkeeper/ledgers/current/855.log` | 问题 EntryLog（在 bookie-1 上） |
| 本文件 | 调查记录 |

---

## 15. 关键数值速查

| 名称 | 值 |
|------|-----|
| EntryLog logId | 2133 |
| 文件名 | 855.log |
| 顺序链最后好 entry | L240727 E17719 @30979, size=55343 |
| 顺序链断裂点 | 86326 |
| 假超大 size @86326 | 386008842 (0x1702070a) |
| PathDetails 误读点 | 425908824 |
| 143MB Sanity 点（示例） | 143591610 |
| L15021/E21 真实起点 | 1025196187 |
| L15069 E0 index pos | 1025196194 (= 6187 **+ 7**) |
| L15069 Sanity size | 687865856 (= BE `29 00 00 00`) |
| L15069 Lid 期望 | 0x3add (15069) |
| 盘上实际 Lid | 0x3aad (15021) |

---

## 16. 修订历史

| 日期 | 说明 |
|------|------|
| 2026-07-27 | 初始版本：汇总 07-23~07-27 对话、命令输出、结论与源码分析指引 |

---

*本文档由运维排查对话整理，便于与 BookKeeper 4.16.7 源码对照。若集群 BK 版本与仓库不一致，请以实际运行镜像版本为准。*
