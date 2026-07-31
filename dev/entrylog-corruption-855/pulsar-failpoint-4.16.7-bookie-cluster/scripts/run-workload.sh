#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=common.sh
. "${SCRIPT_DIR}/common.sh"

detect_java
require_prepared

TOPIC="${TOPIC:-persistent://public/default/entrylog-failpoint}"
RATE="${RATE:-500}"
SIZE="${SIZE:-512}"
MESSAGES="${MESSAGES:-20000}"

mkdir -p "${LOG_DIR}/client"

env JAVA_HOME="${JAVA_HOME:-}" PULSAR_LOG_DIR="${LOG_DIR}/client" PULSAR_MEM="-Xms64m -Xmx256m -XX:MaxDirectMemorySize=128m" PULSAR_GC="${SMALL_GC}" \
  "${PULSAR_HOME}/bin/pulsar-perf" produce \
    -u pulsar://127.0.0.1:6650 \
    -r "${RATE}" \
    -s "${SIZE}" \
    -m "${MESSAGES}" \
    "${TOPIC}"

if grep -R "Injected entrylog partial flush failure" "${LOG_DIR}/bk1" >/dev/null 2>&1; then
  echo "bk1 failpoint fired."
else
  echo "bk1 failpoint has not fired yet. Increase MESSAGES or SIZE and rerun this script." >&2
fi
