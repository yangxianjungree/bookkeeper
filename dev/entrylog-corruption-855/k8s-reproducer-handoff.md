# K8s Standard Deployment Reproducer Handoff

本文档用于把本地已验证的 entrylog partial flush corruption 复现链路交接给 K8s 实现同学。目标是让对方在标准 K8s 部署形态下复现同一类问题，同时不暴露当前内部分析分支和内部上下文文档。

当前本地已完成的验证层：

| layer | status | evidence |
| --- | --- | --- |
| unit test | done | `BufferedChannel` partial flush 后 physical/logical drift 可达 |
| BookKeeper E2E | done | 真实 Bookie/`DbLedgerStorage` 路径可持久化 stale location |
| Pulsar failpoint cluster | done | full broker -> managed ledger -> bookie 路径可复现 target/control drift |
| unmodified local cluster | done | 原版 BookKeeper 4.16.7 bookie + external `LD_PRELOAD` 可复现 |
| K8s standard deployment | todo | 本文档要交接的下一层 |

## 1. Goal

在 K8s 中用原版 BookKeeper/Pulsar 二进制复现：

```text
Pulsar producer
  -> Pulsar broker / ManagedLedger
  -> BookKeeper client
  -> target bookie
  -> DefaultEntryLogger / BufferedChannel
  -> one external entrylog write EIO after bytes reached the file
  -> target entrylog physical/logical position drift
```

关键要求：

1. BookKeeper/Pulsar 源码和镜像不做业务代码改造。
2. 只在目标 bookie 上通过外部层注入一次 fault。
3. 健康 bookie 不注入，用作对照。
4. 故障触发后 workload 继续跑一段时间，让 failed entrylog channel 被复用。
5. 停止服务或冻结 PVC 后采集 entrylog、日志、配置和镜像信息。
6. 用现有离线 parser 解析物理 entrylog，不套生产文档里的固定 offset。

非目标：

1. 不在 K8s 里验证修复方案。
2. 不做已有坏数据修复。
3. 不把当前内部分析分支直接贴到公开 issue 或 PR。

## 2. Existing Local Reference

本地不改源码版本在这里：

```text
dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/
```

可复用工具：

```text
dev/entrylog-corruption-855/tools/ldpreload-entrylog-fault/
dev/entrylog-corruption-855/tools/entrylog_drift_scanner.py
dev/entrylog-corruption-855/tools/pulsar_cluster_entrylog_report.py
```

本地单副本 `2/1/1` 归档结果：

```text
dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runs/single-replica-20260731-184741/summary.md
```

本地三副本 `3/3/2` 归档结果：

```text
dev/entrylog-corruption-855/pulsar-ldpreload-4.16.7-bookie-cluster/runs/stability-20260731-175938/summary.md
```

## 3. Deployment Shape

推荐先做 `2/1/1` 单副本模式，再做 `3/3/2` 对照模式。

### 3.1 Single-copy mode

用于贴近生产调查里的单副本 ledger metadata 形态：

```text
bookieCount=2
managedLedgerDefaultEnsembleSize=2
managedLedgerDefaultWriteQuorum=1
managedLedgerDefaultAckQuorum=1
```

解释：

- `bk1` 是 target bookie，启用 `LD_PRELOAD`。
- `bk2` 是 healthy control，不启用 `LD_PRELOAD`。
- 因为 `writeQuorum < ensemble`，entries 会单副本分布，不应强制做 replica hash equality。
- 验收重点是 target entrylog header/map/physical chain 和 runtime logs。

### 3.2 Replica-control mode

用于严格 target/control entry body 对照：

```text
bookieCount=3
managedLedgerDefaultEnsembleSize=3
managedLedgerDefaultWriteQuorum=3
managedLedgerDefaultAckQuorum=2
```

解释：

- `bk1` 是 target bookie，启用 `LD_PRELOAD`。
- `bk2` 和 `bk3` 是 healthy controls。
- 同一批 entry 会复制到 target/control，报告可以比较 entry hash。

## 4. Target-only LD_PRELOAD Injection

最重要的 K8s 约束：只能让目标 bookie Pod 加载 injector。不能把 env 一次性加到整个 BookKeeper StatefulSet，否则所有 bookie 都会注入 fault，健康对照失效。

推荐实现方式：

| option | recommendation | notes |
| --- | --- | --- |
| split StatefulSet | preferred | target bookie 单独一个 StatefulSet，healthy bookies 另一个 StatefulSet |
| Kustomize/Helm post-renderer | acceptable | 按 pod template/ordinal 只改 target bookie |
| patch existing single StatefulSet env | avoid | 会影响所有 replicas |
| ephemeral container | not suitable | 不能给已启动 JVM 设置 `LD_PRELOAD` |

注入库来源：

1. 用 `dev/entrylog-corruption-855/tools/ldpreload-entrylog-fault/entrylog_fault.c` 构建 `libbk_entrylog_fault.so`。
2. 做一个很小的 injector image，里面只放 `.so` 和 source checksum。
3. 用 initContainer 把 `.so` copy 到 target bookie 的 shared `emptyDir`。
4. target bookie container 设置 `LD_PRELOAD=/opt/bk-fault/libbk_entrylog_fault.so`。

示意 Pod 片段：

```yaml
volumes:
  - name: bk-fault
    emptyDir: {}

initContainers:
  - name: copy-bk-entrylog-fault
    image: <internal-registry>/bk-entrylog-fault:<tag>
    command: ["sh", "-c", "cp /fault/libbk_entrylog_fault.so /opt/bk-fault/"]
    volumeMounts:
      - name: bk-fault
        mountPath: /opt/bk-fault

containers:
  - name: bookie
    env:
      - name: LD_PRELOAD
        value: /opt/bk-fault/libbk_entrylog_fault.so
      - name: BK_ENTRYLOG_FAULT_ENABLED
        value: "1"
      - name: BK_ENTRYLOG_FAULT_DRY_RUN
        value: "0"
      - name: BK_ENTRYLOG_FAULT_MIN_WRITE_BYTES
        value: "65536"
      - name: BK_ENTRYLOG_FAULT_EXACT_WRITE_BYTES
        value: "65536"
      - name: BK_ENTRYLOG_FAULT_AFTER_MATCHES
        value: "1"
      - name: BK_ENTRYLOG_FAULT_MAX_TRIGGERS
        value: "1"
      - name: BK_ENTRYLOG_FAULT_PATH_CONTAINS
        value: "<ledgerDirectories>/current/"
      - name: BK_ENTRYLOG_FAULT_FILE_SUFFIX
        value: ".log"
      - name: BK_ENTRYLOG_FAULT_LOG
        value: "<bookie-log-dir>/ldpreload-entrylog-fault.log"
    volumeMounts:
      - name: bk-fault
        mountPath: /opt/bk-fault
```

`BK_ENTRYLOG_FAULT_AFTER_MATCHES=N` 的含义：

```text
目标 bookie entrylog 文件上第 N 次匹配的 exact 65536 bytes write/pwrite/writev syscall。
不是第 N 条 BookKeeper entry。
```

## 5. Required Recording

每轮必须记录：

```text
cluster name / namespace
Pulsar image digest
BookKeeper image digest
BookKeeper runtime version
BookKeeper server jar sha256
injector source commit / sha256
injector .so sha256
target bookie pod name
healthy bookie pod names
managedLedger quorum config
bookie writeBufferSizeBytes / logSizeLimit / flushInterval
fault env vars
workload command and parameters
```

必须验证目标 bookie 是原版 runtime：

```bash
kubectl exec <target-bookie-pod> -- sh -c "
  jar tf <path-to-bookkeeper-server-jar> |
  grep -F 'DefaultEntryLogger\$BufferedLogChannel\$PartialFlushFault.class' && exit 1 || exit 0
"
```

上面命令应返回 `0`，表示 failpoint class 不存在。

## 6. Workload Procedure

推荐第一批按本地 `2/1/1` 变量跑 5 轮：

| round | messages | size | rate | faultAfter | exactBytes |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 12000 | 512 | 500 | 1 | 65536 |
| 2 | 16000 | 768 | 700 | 2 | 65536 |
| 3 | 20000 | 1024 | 900 | 3 | 65536 |
| 4 | 24000 | 384 | 600 | 4 | 65536 |
| 5 | 28000 | 1536 | 1000 | 5 | 65536 |

示意命令：

```bash
pulsar-perf produce \
  -u pulsar://<broker-service>:6650 \
  -r 500 \
  -s 512 \
  -m 12000 \
  persistent://public/default/entrylog-ldpreload-k8s-round-01
```

每轮流程：

1. 部署 clean cluster。
2. 只让 target bookie 启用 `LD_PRELOAD`。
3. 确认 target/healthy bookies 都 writable。
4. 启动 workload。
5. 等待 target fault log 出现 `bk-entrylog-fault: triggering`。
6. workload 继续跑到 DONE，或记录客户端明确失败。
7. 停 broker 写入入口。
8. 停 bookies 或冻结 PVC。
9. 采集证据。
10. 离线运行 parser。

## 7. Evidence Collection Layout

建议采集后整理成本地统一目录：

```text
runs/k8s-<timestamp>/
├── versions.properties
├── logs/
│   ├── bk1/
│   │   ├── stdout.log
│   │   ├── bookkeeper.log
│   │   └── ldpreload-entrylog-fault.log
│   ├── bk2/
│   │   ├── stdout.log
│   │   └── bookkeeper.log
│   ├── bk3/
│   │   ├── stdout.log
│   │   └── bookkeeper.log
│   ├── broker/
│   │   └── stdout.log
│   └── client/
│       └── pulsar-perftest.log
├── entrylogs/
│   ├── bk1/
│   │   └── *.log
│   ├── bk2/
│   │   └── *.log
│   └── bk3/
│       └── *.log
└── config/
    ├── target-bookie.yaml
    ├── healthy-bookies.yaml
    ├── broker.yaml
    ├── bookkeeper.conf
    └── broker.conf
```

`pulsar_cluster_entrylog_report.py` 已支持从 `entrylogs/<role>/*.log` 读取归档文件。

示意报告命令：

```bash
python3 dev/entrylog-corruption-855/tools/pulsar_cluster_entrylog_report.py \
  --cluster-dir runs/k8s-<timestamp> \
  --write-buffer-bytes 65536 \
  --json-out runs/k8s-<timestamp>/entrylog-cluster-report.json \
  > runs/k8s-<timestamp>/entrylog-cluster-report.md
```

## 8. Acceptance Criteria

一轮 K8s 复现通过需要满足：

| check | expected |
| --- | --- |
| unmodified bookie | target bookie jar 不包含 failpoint class |
| target-only injection | 只有 target bookie 有 `LD_PRELOAD` 和 fault env |
| fault event | target fault log 只有 1 条 `triggering` |
| fault bytes | `count=65536` 且 `real_rc=65536` |
| target bookie log | 出现 `Exception flushing ledgers` 和 `Input/output error` |
| healthy bookie logs | 不出现 entrylog EIO |
| client log | 记录 DONE 或明确失败；不能缺日志 |
| broker log | 记录 bookie connection / disconnect / ManagedLedger 行为 |
| target entrylog | parser 发现 stale header map 或 physical/logical drift |
| healthy entrylog | parser 为 `SEALED_OK` 或无 stale header drift |

`2/1/1` 额外说明：

```text
replicaComparisonApplicable=false
```

这是预期结果。因为 entries 是单副本分布，报告不应把 target/control hash 不相等当成失败。

`3/3/2` 额外说明：

```text
replicaComparisonApplicable=true
```

这时 healthy controls `bk2` / `bk3` 应严格一致，target 与 controls 可做 entry hash 对照。

## 9. Troubleshooting

### Fault does not fire

优先检查：

1. `BK_ENTRYLOG_FAULT_PATH_CONTAINS` 是否匹配真实 `ledgerDirectories/current/`。
2. target bookie 是否真的加载了 `LD_PRELOAD`。
3. `writeBufferSizeBytes` 是否是 `65536`。
4. workload 是否足够大。
5. `BK_ENTRYLOG_FAULT_EXACT_WRITE_BYTES=65536` 是否过严；可先 dry-run 或改成 `MIN_WRITE_BYTES=32768` 观察匹配日志。

### All bookies show EIO

通常说明 `LD_PRELOAD` env 被加到了整个 StatefulSet。必须改成 target-only 注入。

### Client succeeds but entrylog is corrupted

这是可能且重要的现象。Pulsar/BookKeeper 读路径可能从健康副本读取，客户端成功不代表 target 本地 entrylog 没有损坏。

### No entrylogs after pod deletion

不要依赖被删除 Pod 的容器文件系统。entrylog 必须来自 PVC。建议 scale down 后用 collector pod 挂载 PVC，再 `tar` 出 `ledgerDirectories/current/*.log`。

### Broker only logs disconnect during teardown

这是可接受的，但仍要记录。关键是 target bookie 端的 flush EIO 和离线 entrylog drift 证据。

## 10. Suggested K8s Tooling To Add

后续可以补两个薄工具，避免执行同学手工整理证据：

```text
dev/entrylog-corruption-855/tools/k8s_collect_entrylog_evidence.sh
dev/entrylog-corruption-855/tools/k8s_render_entrylog_report.sh
```

`k8s_collect_entrylog_evidence.sh` 建议参数：

```text
--namespace
--broker-pod
--client-pod-or-log
--target-bookie-pod
--healthy-bookie-pod bk2
--healthy-bookie-pod bk3
--target-ledger-pvc
--healthy-ledger-pvc bk2=<pvc>
--healthy-ledger-pvc bk3=<pvc>
--out runs/k8s-<timestamp>
```

采集内容：

1. `kubectl get pod/statefulset/configmap -o yaml`。
2. target/healthy bookie logs。
3. broker/client logs。
4. target/healthy bookie entrylogs。
5. image digest 和 jar checksum。
6. 生成 `versions.properties`。

`k8s_render_entrylog_report.sh` 只需要调用现有 Python report，并输出 `summary.md`。

## 11. Public Hygiene

公开 issue / PR 不应引用当前内部复现分支。对外只暴露：

1. issue 中可公开的简洁证据摘要；
2. sanitized public branch；
3. 无内部文档路径、无生产集群细节、无内部域名/IP 的报告片段；
4. 原版 binary + external fault 的事实；
5. 修复 PR 的代码和测试。

K8s 原始日志、Pod YAML、PVC 路径、topic 名、内部 registry、namespace 等信息需要先审查再外发。
