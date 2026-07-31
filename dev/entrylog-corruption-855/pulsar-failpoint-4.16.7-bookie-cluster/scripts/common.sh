#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HARNESS_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
REPO_ROOT="$(cd "${HARNESS_DIR}/../../.." && pwd)"
RUNTIME_DIR="${HARNESS_DIR}/runtime"

PULSAR_VERSION="${PULSAR_VERSION:-3.2.4}"
BK_VERSION="${BK_VERSION:-4.16.7}"

PULSAR_HOME="${RUNTIME_DIR}/apache-pulsar-${PULSAR_VERSION}"
PULSAR_ARCHIVE="${RUNTIME_DIR}/downloads/apache-pulsar-${PULSAR_VERSION}-bin.tar.gz"
PULSAR_SHA512="${PULSAR_ARCHIVE}.sha512"
PULSAR_ARCHIVE_SEED="${PULSAR_ARCHIVE_SEED:-${REPO_ROOT}/dev/entrylog-corruption-855/pulsar-failpoint-local-cluster/runtime/downloads/apache-pulsar-${PULSAR_VERSION}-bin.tar.gz}"
PULSAR_SHA512_SEED="${PULSAR_SHA512_SEED:-${PULSAR_ARCHIVE_SEED}.sha512}"
PULSAR_URL="${PULSAR_URL:-https://mirrors.huaweicloud.com/apache/pulsar/pulsar-${PULSAR_VERSION}/apache-pulsar-${PULSAR_VERSION}-bin.tar.gz}"
PULSAR_SHA512_URL="${PULSAR_SHA512_URL:-https://archive.apache.org/dist/pulsar/pulsar-${PULSAR_VERSION}/apache-pulsar-${PULSAR_VERSION}-bin.tar.gz.sha512}"

BK_DIST_TARBALL="${BK_DIST_TARBALL:-/tmp/bookkeeper-4.16.7-failpoint/bookkeeper-dist/server/target/bookkeeper-server-${BK_VERSION}-bin.tar.gz}"
BK_ARCHIVE="${RUNTIME_DIR}/downloads/bookkeeper-server-${BK_VERSION}-bin.tar.gz"
BK_HOME="${RUNTIME_DIR}/bookkeeper/bookkeeper-server-${BK_VERSION}"

CONF_DIR="${RUNTIME_DIR}/conf"
DATA_DIR="${RUNTIME_DIR}/data"
LOG_DIR="${RUNTIME_DIR}/logs"
PIDS_DIR="${RUNTIME_DIR}/pids"
REPORT_DIR="${RUNTIME_DIR}/reports"

JAVA17_HOME="${JAVA17_HOME:-/usr/lib/jvm/java-17-openjdk-amd64}"
BOOKIE_MEM_OPTS="${BOOKIE_MEM_OPTS:-"-Xms128m -Xmx384m -XX:MaxDirectMemorySize=256m"}"
BROKER_MEM="${BROKER_MEM:-"-Xms128m -Xmx512m -XX:MaxDirectMemorySize=256m"}"
SMALL_GC="${SMALL_GC:-"-XX:+UseG1GC -XX:+PerfDisableSharedMem"}"

detect_java() {
  if [[ -z "${JAVA_HOME:-}" && -d "${JAVA17_HOME}" ]]; then
    export JAVA_HOME="${JAVA17_HOME}"
  fi
}

require_prepared() {
  if [[ ! -x "${PULSAR_HOME}/bin/pulsar" ]]; then
    echo "Pulsar distribution is not prepared. Run scripts/prepare-local-cluster.sh first." >&2
    exit 1
  fi
  if [[ ! -x "${BK_HOME}/bin/bookkeeper" ]]; then
    echo "BookKeeper ${BK_VERSION} distribution is not prepared. Run scripts/prepare-local-cluster.sh first." >&2
    exit 1
  fi
}

pid_file() {
  local name="$1"
  echo "${PIDS_DIR}/${name}.pid"
}

is_running() {
  local file="$1"
  [[ -f "${file}" ]] && kill -0 "$(cat "${file}")" 2>/dev/null
}

wait_for_tcp() {
  local host="$1"
  local port="$2"
  local timeout_seconds="$3"
  local deadline=$((SECONDS + timeout_seconds))
  while (( SECONDS < deadline )); do
    if timeout 1 bash -c "cat < /dev/null > /dev/tcp/${host}/${port}" 2>/dev/null; then
      return 0
    fi
    sleep 1
  done
  echo "Timed out waiting for ${host}:${port}" >&2
  return 1
}

assert_port_free() {
  local port="$1"
  if ss -ltn | awk '{print $4}' | grep -Eq "(^|:)${port}$"; then
    echo "Port ${port} is already in use." >&2
    exit 1
  fi
}

start_process() {
  local name="$1"
  shift
  local pid_path
  pid_path="$(pid_file "${name}")"
  if is_running "${pid_path}"; then
    echo "${name} is already running with pid $(cat "${pid_path}")" >&2
    exit 1
  fi
  mkdir -p "${PIDS_DIR}" "${LOG_DIR}/${name}"
  if command -v setsid >/dev/null 2>&1; then
    setsid "$@" > "${LOG_DIR}/${name}/stdout.log" 2>&1 < /dev/null &
  else
    nohup "$@" > "${LOG_DIR}/${name}/stdout.log" 2>&1 < /dev/null &
  fi
  echo "$!" > "${pid_path}"
  echo "Started ${name} pid $(cat "${pid_path}")"
}
