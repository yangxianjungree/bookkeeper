#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=common.sh
. "${SCRIPT_DIR}/common.sh"

detect_java
require_prepared

TOPIC="${TOPIC:-persistent://public/default/entrylog-ldpreload}"
RATE="${RATE:-500}"
SIZE="${SIZE:-512}"
MESSAGES="${MESSAGES:-20000}"
RUN_LOG="${LOG_DIR}/client/pulsar-perftest.log"

mkdir -p "${LOG_DIR}/client"
: > "${RUN_LOG}"

set +e
env JAVA_HOME="${JAVA_HOME:-}" PULSAR_LOG_DIR="${LOG_DIR}/client" PULSAR_MEM="-Xms64m -Xmx256m -XX:MaxDirectMemorySize=128m" PULSAR_GC="${SMALL_GC}" \
  "${PULSAR_HOME}/bin/pulsar-perf" produce \
    -u pulsar://127.0.0.1:6650 \
    -r "${RATE}" \
    -s "${SIZE}" \
    -m "${MESSAGES}" \
    "${TOPIC}" 2>&1 | tee -a "${RUN_LOG}"
workload_rc=${PIPESTATUS[0]}
set -e

echo "workload_rc=${workload_rc}" | tee -a "${RUN_LOG}"
if [[ "${workload_rc}" -ne 0 ]]; then
  echo "pulsar-perf produce exited with ${workload_rc}" >&2
  exit "${workload_rc}"
fi

fault_log="${BK_ENTRYLOG_FAULT_LOG:-${LOG_DIR}/bk1/ldpreload-entrylog-fault.log}"
if [[ -f "${fault_log}" ]] && grep -q "bk-entrylog-fault: triggering" "${fault_log}"; then
  echo "bk1 LD_PRELOAD fault fired." | tee -a "${RUN_LOG}"
elif [[ -f "${fault_log}" ]] && grep -q "bk-entrylog-fault: dry-run-would-trigger" "${fault_log}"; then
  echo "bk1 LD_PRELOAD fault dry-run matched but did not inject." | tee -a "${RUN_LOG}"
else
  echo "bk1 LD_PRELOAD fault has not fired yet. Increase MESSAGES or SIZE, or lower BK_ENTRYLOG_FAULT_AFTER_MATCHES/MIN_WRITE_BYTES." | tee -a "${RUN_LOG}" >&2
fi
