#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=common.sh
. "${SCRIPT_DIR}/common.sh"

detect_java
require_prepared

if (( BOOKIE_COUNT < 2 || BOOKIE_COUNT > 3 )); then
  echo "BOOKIE_COUNT must be 2 or 3 for this local harness; got ${BOOKIE_COUNT}" >&2
  exit 1
fi

ports=(2181 3181 3182 6650 8080)
if (( BOOKIE_COUNT >= 3 )); then
  ports+=(3183)
fi

for port in "${ports[@]}"; do
  assert_port_free "${port}"
done

mkdir -p "${PIDS_DIR}" "${LOG_DIR}" "${DATA_DIR}"

start_process zk \
  env JAVA_HOME="${JAVA_HOME:-}" PULSAR_LOG_DIR="${LOG_DIR}/zk" PULSAR_MEM="-Xms64m -Xmx128m -XX:MaxDirectMemorySize=128m" PULSAR_GC="${SMALL_GC}" PULSAR_ZK_CONF="${CONF_DIR}/zookeeper.conf" \
  "${PULSAR_HOME}/bin/pulsar" zookeeper

wait_for_tcp 127.0.0.1 2181 60

if [[ ! -f "${RUNTIME_DIR}/metadata-initialized" ]]; then
  env JAVA_HOME="${JAVA_HOME:-}" PULSAR_LOG_DIR="${LOG_DIR}/init" PULSAR_MEM="-Xms64m -Xmx128m -XX:MaxDirectMemorySize=128m" PULSAR_GC="${SMALL_GC}" \
    "${PULSAR_HOME}/bin/pulsar" initialize-cluster-metadata \
      --cluster test \
      --zookeeper 127.0.0.1:2181 \
      --configuration-store 127.0.0.1:2181 \
      --web-service-url http://127.0.0.1:8080/ \
      --broker-service-url pulsar://127.0.0.1:6650/
  touch "${RUNTIME_DIR}/metadata-initialized"
fi

common_bookie_opts="-Dio.netty.leakDetectionLevel=disabled -Dio.netty.recycler.maxCapacityPerThread=4096"
bk1_fault_log="${LOG_DIR}/bk1/ldpreload-entrylog-fault.log"

start_process bk1 \
  env JAVA_HOME="${JAVA_HOME:-}" BOOKIE_CONF="${CONF_DIR}/bk1.conf" BOOKIE_LOG_DIR="${LOG_DIR}/bk1" BOOKIE_LOG_FILE="bookkeeper.log" BOOKIE_ROOT_LOG_APPENDER="CONSOLE" BOOKIE_MEM_OPTS="${BOOKIE_MEM_OPTS}" BOOKIE_GC_OPTS="${SMALL_GC}" BOOKIE_EXTRA_OPTS="${common_bookie_opts}" \
    LD_PRELOAD="${LD_PRELOAD_FAULT_LIB}" \
    BK_ENTRYLOG_FAULT_ENABLED="${BK_ENTRYLOG_FAULT_ENABLED:-1}" \
    BK_ENTRYLOG_FAULT_DRY_RUN="${BK_ENTRYLOG_FAULT_DRY_RUN:-0}" \
    BK_ENTRYLOG_FAULT_MIN_WRITE_BYTES="${BK_ENTRYLOG_FAULT_MIN_WRITE_BYTES:-32768}" \
    BK_ENTRYLOG_FAULT_EXACT_WRITE_BYTES="${BK_ENTRYLOG_FAULT_EXACT_WRITE_BYTES:-0}" \
    BK_ENTRYLOG_FAULT_AFTER_MATCHES="${BK_ENTRYLOG_FAULT_AFTER_MATCHES:-1}" \
    BK_ENTRYLOG_FAULT_MAX_TRIGGERS="${BK_ENTRYLOG_FAULT_MAX_TRIGGERS:-1}" \
    BK_ENTRYLOG_FAULT_PATH_CONTAINS="${BK_ENTRYLOG_FAULT_PATH_CONTAINS:-${DATA_DIR}/bk1/ledgers/current/}" \
    BK_ENTRYLOG_FAULT_FILE_SUFFIX="${BK_ENTRYLOG_FAULT_FILE_SUFFIX:-.log}" \
    BK_ENTRYLOG_FAULT_LOG="${BK_ENTRYLOG_FAULT_LOG:-${bk1_fault_log}}" \
  "${BK_HOME}/bin/bookkeeper" bookie

start_process bk2 \
  env JAVA_HOME="${JAVA_HOME:-}" BOOKIE_CONF="${CONF_DIR}/bk2.conf" BOOKIE_LOG_DIR="${LOG_DIR}/bk2" BOOKIE_LOG_FILE="bookkeeper.log" BOOKIE_ROOT_LOG_APPENDER="CONSOLE" BOOKIE_MEM_OPTS="${BOOKIE_MEM_OPTS}" BOOKIE_GC_OPTS="${SMALL_GC}" BOOKIE_EXTRA_OPTS="${common_bookie_opts}" \
  "${BK_HOME}/bin/bookkeeper" bookie

if (( BOOKIE_COUNT >= 3 )); then
  start_process bk3 \
    env JAVA_HOME="${JAVA_HOME:-}" BOOKIE_CONF="${CONF_DIR}/bk3.conf" BOOKIE_LOG_DIR="${LOG_DIR}/bk3" BOOKIE_LOG_FILE="bookkeeper.log" BOOKIE_ROOT_LOG_APPENDER="CONSOLE" BOOKIE_MEM_OPTS="${BOOKIE_MEM_OPTS}" BOOKIE_GC_OPTS="${SMALL_GC}" BOOKIE_EXTRA_OPTS="${common_bookie_opts}" \
    "${BK_HOME}/bin/bookkeeper" bookie
fi

bookie_ports=(3181 3182)
if (( BOOKIE_COUNT >= 3 )); then
  bookie_ports+=(3183)
fi

for port in "${bookie_ports[@]}"; do
  wait_for_tcp 127.0.0.1 "${port}" 90
done

deadline=$((SECONDS + 90))
while (( SECONDS < deadline )); do
  if output="$(env JAVA_HOME="${JAVA_HOME:-}" BOOKIE_CONF="${CONF_DIR}/bk1.conf" BOOKIE_LOG_DIR="${LOG_DIR}/shell" BOOKIE_MEM_OPTS="-Xms64m -Xmx128m -XX:MaxDirectMemorySize=128m" BOOKIE_GC_OPTS="${SMALL_GC}" "${BK_HOME}/bin/bookkeeper" shell listbookies -rw 2>&1)"; then
    printf "%s\n" "${output}" > "${LOG_DIR}/shell/last-listbookies-rw.log"
    all_expected=1
    for port in "${bookie_ports[@]}"; do
      if ! printf "%s\n" "${output}" | grep -q "${port}"; then
        all_expected=0
      fi
    done
    if [[ "${all_expected}" == "1" ]]; then
      printf "%s\n" "${output}" > "${LOG_DIR}/shell/listbookies-rw.log"
      break
    fi
  else
    printf "%s\n" "${output:-}" > "${LOG_DIR}/shell/last-listbookies-rw.log"
  fi
  sleep 2
done

if [[ ! -f "${LOG_DIR}/shell/listbookies-rw.log" ]]; then
  echo "Timed out waiting for ${BOOKIE_COUNT} writable bookies." >&2
  exit 1
fi

start_process broker \
  env JAVA_HOME="${JAVA_HOME:-}" PULSAR_LOG_DIR="${LOG_DIR}/broker" PULSAR_MEM="${BROKER_MEM}" PULSAR_GC="${SMALL_GC}" PULSAR_BROKER_CONF="${CONF_DIR}/broker.conf" \
  "${PULSAR_HOME}/bin/pulsar" broker

wait_for_tcp 127.0.0.1 6650 120
wait_for_tcp 127.0.0.1 8080 120

echo "Local Pulsar cluster is up with ${BOOKIE_COUNT} unmodified external BookKeeper ${BK_VERSION} bookies."
echo "bk1 LD_PRELOAD fault log: ${bk1_fault_log}"
