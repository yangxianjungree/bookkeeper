#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=common.sh
. "${SCRIPT_DIR}/common.sh"

mkdir -p "${PIDS_DIR}"

for name in broker bk3 bk2 bk1 zk; do
  pid_path="$(pid_file "${name}")"
  if is_running "${pid_path}"; then
    pid="$(cat "${pid_path}")"
    echo "Stopping ${name} pid ${pid}"
    kill "${pid}" 2>/dev/null || true
  fi
done

sleep 5

for name in broker bk3 bk2 bk1 zk; do
  pid_path="$(pid_file "${name}")"
  if is_running "${pid_path}"; then
    pid="$(cat "${pid_path}")"
    echo "Force stopping ${name} pid ${pid}"
    kill -9 "${pid}" 2>/dev/null || true
  fi
  rm -f "${pid_path}"
done

echo "Stopped local Pulsar cluster. Runtime data is preserved under ${RUNTIME_DIR}."
