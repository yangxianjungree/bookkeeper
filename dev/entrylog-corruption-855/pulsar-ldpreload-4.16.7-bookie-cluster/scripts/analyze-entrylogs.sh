#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=common.sh
. "${SCRIPT_DIR}/common.sh"

mkdir -p "${REPORT_DIR}"

python3 "${REPO_ROOT}/dev/entrylog-corruption-855/tools/pulsar_cluster_entrylog_report.py" \
  --cluster-dir "${RUNTIME_DIR}" \
  --write-buffer-bytes 65536 \
  --json-out "${REPORT_DIR}/entrylog-cluster-report.json" \
  "$@" | tee "${REPORT_DIR}/entrylog-cluster-report.md"
