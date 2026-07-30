# 855.log / EntryLog 2133 损坏问题上下文

这个目录用于给新的分析者快速接上上下文。它来自 Pulsar 项目目录里的调查文档，已拷贝到本 BookKeeper 分支，方便在另一台机器上直接查看和运行复现。

## 对应的公开信息

- GitHub issue: https://github.com/apache/bookkeeper/issues/4855
- Reproducer PR: https://github.com/apache/bookkeeper/pull/4854
- 本分支: `e2e-entrylog-partial-flush-corruption`

本分支不是正式修复分支，而是为了复现和验证根因。

## 问题一句话

`pulsar-bookie-1` 上的 `855.log`，也就是 entryLogId `2133`，出现了稳定的位置偏移：

```text
physical position = logical/indexed position + 34553
```

同一个 `34553` 同时出现在三类证据里：

```text
真实 ledgers map start - header.ledgersMapOffset = 34553
L15069 真实 entry body pos - RocksDB index pos    = 34553
64KiB writeBuffer 边界 - L240727/E17719 bodyStart = 34553
```

这说明问题不是随机坏块，也不是 L15069 数据被 L15021 覆写，而是 BookKeeper entrylog writer 在一次 flush 异常后继续复用，导致 `BufferedChannel.position()` 落后于底层 `FileChannel` 真实写入位置。

## 最短阅读路径

新同学建议按这个顺序看：

1. `context/855-entrylog-2133-concise-root-cause-report.md`
   - 主报告，包含整体分布图、entry 错误图、物理/逻辑偏移图、源码根因。
2. `context/855-entrylog-2133-source-position-analysis.md`
   - 更详细的 offset 和源码推导。
3. `context/855-entrylog-2133-source-position-verification-2dws9g.md`
   - 独立佐证之一。
4. `context/855-entrylog-2133-source-position-verification-78faf567.md`
   - 独立佐证之二，最终版本与主结论一致。
5. `context/855-entrylog-2133-fix-plan-optimized.md`
   - 当前推荐修复方案。
6. `e2e-reproducer.md`
   - 本分支 E2E 复现运行说明。

## 文档目录说明

```text
dev/entrylog-corruption-855/
├── CONTEXT.zh.md
├── README.md
├── e2e-reproducer.md
├── assets/
│   └── pulsar-entrylog-physical-logical-position-drift.drawio.png
└── context/
    ├── 855-entrylog-2133-corruption-investigation.md
    ├── 855-entrylog-2133-source-position-analysis.md
    ├── 855-entrylog-2133-concise-root-cause-report.md
    ├── 855-entrylog-2133-fix-plan.md
    ├── 855-entrylog-2133-fix-plan-optimized.md
    ├── 855-entrylog-2133-source-position-verification-2dws9g.md
    ├── 855-entrylog-2133-source-position-verification-78faf567.md
    ├── 855-entrylog-2133-b65log-verification-78faf567.md
    └── bookkeeper-bufferedchannel-entrylog-corruption-issue-draft.md
```

注意：

- `855-entrylog-2133-fix-plan.md` 是旧版方案，保留用于历史对比。
- `855-entrylog-2133-fix-plan-optimized.md` 是当前建议看的修复方案。
- `855-entrylog-2133-b65log-verification-78faf567.md` 是另一台 bookie 的问题分析，不认为和 855.log 是同一个根因，只作为边界案例保留。

## 本分支额外代码

本分支在现有 reproducer 单测基础上新增了 E2E 复现能力：

```text
bookkeeper-server/src/main/java/org/apache/bookkeeper/bookie/DefaultEntryLogger.java
bookkeeper-server/src/test/java/org/apache/bookkeeper/bookie/EntryLogPartialFlushE2ETest.java
dev/entrylog-corruption-855/e2e-reproducer.md
```

`DefaultEntryLogger` 里的 failpoint 默认关闭，只由 E2E 测试显式打开。它只作用于 entrylog `BufferedLogChannel`，不故意污染 journal channel。

## 如何运行 E2E

在资源足够的机器上：

```bash
git clone -b e2e-entrylog-partial-flush-corruption \
  https://github.com/yangxianjungree/bookkeeper.git

cd bookkeeper

export JAVA_HOME=/path/to/jdk17
export PATH="$JAVA_HOME/bin:$PATH"
export MAVEN_OPTS="-Xmx2g -XX:MaxMetaspaceSize=512m"

mvn -pl bookkeeper-server \
  -am \
  -Dtest=org.apache.bookkeeper.bookie.EntryLogPartialFlushE2ETest \
  -DfailIfNoTests=false \
  -DforkCount=1 \
  test
```

预期在当前未修复代码上测试通过。这个测试通过不代表系统正确，而是表示它成功复现了当前坏状态。

## 复现成功的含义

复现目标不是简单看到一次 `IOException`，而是证明：

```text
FileChannel physical position 已前进
BufferedChannel logical position 未同步前进
同一个 entrylog channel 被继续复用
后续 entry location 被 stale logical position 污染
目标 bookie 本地读同一条 post-failure entry 失败或读到错误位置
健康副本仍可读同一条 entry
```

Pulsar consumer 能正常读不代表没有复现，因为客户端可能从其他健康副本读到数据。

## 本机验证状态

当前机器没有系统 `mvn` 命令。使用 `/home/stephen/github/java/pulsar/mvnw` 尝试跑 Maven reactor 时，仍卡在本地资源问题：

```text
Cannot allocate memory copying buildtools/src/main/resources/bookkeeper/checkstyle.xml
```

所以本分支已完成代码和文档整理、`git diff --check` 通过，但 E2E Maven 测试需要在资源更充足的机器上执行。
