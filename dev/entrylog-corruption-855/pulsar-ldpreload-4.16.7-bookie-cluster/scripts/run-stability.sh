#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=common.sh
. "${SCRIPT_DIR}/common.sh"

ROUNDS="${ROUNDS:-5}"
RUN_ID="${RUN_ID:-stability-$(date +%Y%m%d-%H%M%S)}"
RUN_DIR="${HARNESS_DIR}/runs/${RUN_ID}"
SUMMARY_CSV="${RUN_DIR}/summary.csv"
SUMMARY_MD="${RUN_DIR}/summary.md"
COPY_ENTRYLOGS="${COPY_ENTRYLOGS:-1}"
FAULT_MIN_BYTES="${BK_ENTRYLOG_FAULT_MIN_WRITE_BYTES:-32768}"
FAULT_EXACT_BYTES="${BK_ENTRYLOG_FAULT_EXACT_WRITE_BYTES:-0}"

messages_values=(12000 16000 20000 24000 28000)
size_values=(512 768 1024 384 1536)
rate_values=(500 700 900 600 1000)
after_values=(1 2 3 1 2)

mkdir -p "${RUN_DIR}"

write_summary_header() {
  cat > "${SUMMARY_CSV}" <<'EOF'
round,bookieCount,ensemble,writeQuorum,ackQuorum,replicaComparisonApplicable,messages,size,rate,faultAfter,faultMinBytes,faultExactBytes,workloadRc,clientExit,faultEvents,faultKind,faultLogId,faultBytes,realRc,bk1Status,bk1Log,bk1Delta,bk1HeaderMapValid,bk2Status,bk2Delta,bk3Status,bk3Delta,bk2Bk3MissingInTarget,bk2Bk3MissingInControl,bk2Bk3HashMismatches,bk1Bk2MissingInTarget,bk1Bk2MissingInControl,bk1Bk2HashMismatches,bk1Bk3MissingInTarget,bk1Bk3MissingInControl,bk1Bk3HashMismatches,bk1Eio,bk2Eio,bk3Eio,brokerBookieConnected,brokerConnectionReset,brokerManagedLedgerClose,clientDone
EOF
}

round_value() {
  local name="$1"
  local default_value="$2"
  local variable="${name}_${round}"
  printf "%s" "${!variable:-${default_value}}"
}

append_summary_row() {
  local round="$1"
  local messages="$2"
  local size="$3"
  local rate="$4"
  local fault_after="$5"
  local fault_min_bytes="$6"
  local fault_exact_bytes="$7"
  local workload_rc="$8"
  local report_json="$9"

  python3 - "${round}" "${messages}" "${size}" "${rate}" "${fault_after}" "${fault_min_bytes}" "${fault_exact_bytes}" "${workload_rc}" "${report_json}" "${SUMMARY_CSV}" <<'PY'
import csv
import json
import sys

round_id, messages, size, rate, fault_after, fault_min_bytes, fault_exact_bytes, workload_rc, report_json, summary_csv = sys.argv[1:]

with open(report_json, encoding="utf-8") as handle:
    report = json.load(handle)

versions = report.get("versions") or {}
events = report.get("failpointEvents") or []
event = events[0] if events else {}
logs = report.get("logs") or []

def by_role_and_log(role, log_id):
    if log_id is None:
        return None
    for item in logs:
        if item.get("role") == role and item.get("logId") == log_id:
            return item
    return None

def target_log():
    found = by_role_and_log("bk1", event.get("logId"))
    if found:
        return found
    candidates = [item for item in logs if item.get("role") == "bk1"]
    candidates.sort(key=lambda item: abs((item.get("summary") or {}).get("mapDelta") or 0), reverse=True)
    return candidates[0] if candidates else None

def summary_value(item, key):
    if not item:
        return ""
    return (item.get("summary") or {}).get(key, "")

def status(item):
    return item.get("status", "") if item else ""

def basename(item):
    if not item:
        return ""
    return item.get("path", "").rsplit("/", 1)[-1]

def comparison(target, control):
    for item in report.get("comparisons") or []:
        if item.get("target") == target and item.get("control") == control:
            return item
    return {}

def snippets_contain(role, text):
    runtime = report.get("runtimeBehavior") or {}
    snippets = runtime.get(role) or []
    needle = text.lower()
    return any(needle in (item.get("text") or "").lower() for item in snippets)

target = target_log()
target_log_id = target.get("logId") if target else event.get("logId")
bk2 = by_role_and_log("bk2", target_log_id)
bk3 = by_role_and_log("bk3", target_log_id)
runtime = report.get("runtimeBehavior") or {}
bk2_bk3 = comparison("bk2", "bk3")
bk1_bk2 = comparison("bk1", "bk2")
bk1_bk3 = comparison("bk1", "bk3")

row = {
    "round": round_id,
    "bookieCount": versions.get("bookieCount", ""),
    "ensemble": versions.get("managedLedgerDefaultEnsembleSize", ""),
    "writeQuorum": versions.get("managedLedgerDefaultWriteQuorum", ""),
    "ackQuorum": versions.get("managedLedgerDefaultAckQuorum", ""),
    "replicaComparisonApplicable": report.get("replicaComparisonApplicable", ""),
    "messages": messages,
    "size": size,
    "rate": rate,
    "faultAfter": fault_after,
    "faultMinBytes": fault_min_bytes,
    "faultExactBytes": fault_exact_bytes,
    "workloadRc": workload_rc,
    "clientExit": runtime.get("clientExit", ""),
    "faultEvents": len(events),
    "faultKind": event.get("kind", ""),
    "faultLogId": event.get("logId", ""),
    "faultBytes": event.get("bytes", ""),
    "realRc": event.get("realRc", ""),
    "bk1Status": status(target),
    "bk1Log": basename(target),
    "bk1Delta": summary_value(target, "mapDelta"),
    "bk1HeaderMapValid": summary_value(target, "headerMapValid"),
    "bk2Status": status(bk2),
    "bk2Delta": summary_value(bk2, "mapDelta"),
    "bk3Status": status(bk3),
    "bk3Delta": summary_value(bk3, "mapDelta"),
    "bk2Bk3MissingInTarget": bk2_bk3.get("missingInTarget", ""),
    "bk2Bk3MissingInControl": bk2_bk3.get("missingInControl", ""),
    "bk2Bk3HashMismatches": bk2_bk3.get("hashMismatches", ""),
    "bk1Bk2MissingInTarget": bk1_bk2.get("missingInTarget", ""),
    "bk1Bk2MissingInControl": bk1_bk2.get("missingInControl", ""),
    "bk1Bk2HashMismatches": bk1_bk2.get("hashMismatches", ""),
    "bk1Bk3MissingInTarget": bk1_bk3.get("missingInTarget", ""),
    "bk1Bk3MissingInControl": bk1_bk3.get("missingInControl", ""),
    "bk1Bk3HashMismatches": bk1_bk3.get("hashMismatches", ""),
    "bk1Eio": snippets_contain("bk1", "Input/output error"),
    "bk2Eio": snippets_contain("bk2", "Input/output error"),
    "bk3Eio": snippets_contain("bk3", "Input/output error"),
    "brokerBookieConnected": snippets_contain("broker", "Successfully connected to bookie"),
    "brokerConnectionReset": snippets_contain("broker", "Connection reset by peer"),
    "brokerManagedLedgerClose": snippets_contain("broker", "Closing managed ledger"),
    "clientDone": snippets_contain("client", "DONE"),
}

with open(summary_csv, "a", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(row), lineterminator="\n")
    writer.writerow(row)
PY
}

write_summary_md() {
  python3 - "${SUMMARY_CSV}" "${SUMMARY_MD}" <<'PY'
import csv
import sys

summary_csv, summary_md = sys.argv[1:]
columns = [
    "round",
    "bookieCount",
    "ensemble",
    "writeQuorum",
    "ackQuorum",
    "replicaComparisonApplicable",
    "messages",
    "size",
    "rate",
    "faultAfter",
    "faultExactBytes",
    "workloadRc",
    "clientExit",
    "faultEvents",
    "faultBytes",
    "realRc",
    "bk1Status",
    "bk1Log",
    "bk1Delta",
    "bk1HeaderMapValid",
    "bk2Status",
    "bk2Delta",
    "bk3Status",
    "bk3Delta",
    "bk2Bk3MissingInTarget",
    "bk2Bk3MissingInControl",
    "bk2Bk3HashMismatches",
    "bk1Bk2MissingInTarget",
    "bk1Bk2HashMismatches",
    "bk1Bk3MissingInTarget",
    "bk1Bk3HashMismatches",
    "bk1Eio",
    "bk2Eio",
    "bk3Eio",
    "brokerBookieConnected",
    "brokerConnectionReset",
    "brokerManagedLedgerClose",
    "clientDone",
]

with open(summary_csv, encoding="utf-8", newline="") as handle:
    rows = list(csv.DictReader(handle))

with open(summary_md, "w", encoding="utf-8") as handle:
    handle.write("# LD_PRELOAD Stability Summary\n\n")
    handle.write("| " + " | ".join(columns) + " |\n")
    handle.write("|" + "|".join(["---"] * len(columns)) + "|\n")
    for row in rows:
        handle.write("| " + " | ".join(str(row.get(column, "")) for column in columns) + " |\n")
PY
}

copy_round_artifacts() {
  local round_dir="$1"
  mkdir -p "${round_dir}/logs/bk1" "${round_dir}/logs/broker" "${round_dir}/logs/client"
  cp -f "${RUNTIME_DIR}/versions.properties" "${round_dir}/versions.properties" 2>/dev/null || true
  cp -f "${REPORT_DIR}/entrylog-cluster-report.md" "${round_dir}/entrylog-cluster-report.md" 2>/dev/null || true
  cp -f "${REPORT_DIR}/entrylog-cluster-report.json" "${round_dir}/entrylog-cluster-report.json" 2>/dev/null || true
  cp -f "${LOG_DIR}/bk1/ldpreload-entrylog-fault.log" "${round_dir}/logs/bk1/" 2>/dev/null || true
  cp -f "${LOG_DIR}/bk1/stdout.log" "${round_dir}/logs/bk1/" 2>/dev/null || true
  cp -f "${LOG_DIR}/broker/stdout.log" "${round_dir}/logs/broker/" 2>/dev/null || true
  cp -f "${LOG_DIR}/client/pulsar-perftest.log" "${round_dir}/logs/client/" 2>/dev/null || true

  if [[ "${COPY_ENTRYLOGS}" == "1" ]]; then
    for role in bk1 bk2 bk3; do
      local source_dir="${DATA_DIR}/${role}/ledgers/current"
      local target_dir="${round_dir}/entrylogs/${role}"
      if [[ -d "${source_dir}" ]]; then
        mkdir -p "${target_dir}"
        cp -f "${source_dir}"/*.log "${target_dir}/" 2>/dev/null || true
      fi
    done
  fi
}

write_summary_header

for ((round = 1; round <= ROUNDS; round++)); do
  index=$(( (round - 1) % ${#messages_values[@]} ))
  messages="$(round_value MESSAGES "${messages_values[$index]}")"
  size="$(round_value SIZE "${size_values[$index]}")"
  rate="$(round_value RATE "${rate_values[$index]}")"
  fault_after="$(round_value BK_ENTRYLOG_FAULT_AFTER_MATCHES "${after_values[$index]}")"
  round_id="$(printf "round-%02d" "${round}")"
  round_dir="${RUN_DIR}/${round_id}"

  echo "=== ${round_id}: bookies=${BOOKIE_COUNT} quorum=${MANAGED_LEDGER_DEFAULT_ENSEMBLE_SIZE}/${MANAGED_LEDGER_DEFAULT_WRITE_QUORUM}/${MANAGED_LEDGER_DEFAULT_ACK_QUORUM} messages=${messages} size=${size} rate=${rate} faultAfter=${fault_after} exactBytes=${FAULT_EXACT_BYTES} ==="
  mkdir -p "${round_dir}"

  RESET_RUNTIME=1 \
    BOOKIE_COUNT="${BOOKIE_COUNT}" \
    MANAGED_LEDGER_DEFAULT_ENSEMBLE_SIZE="${MANAGED_LEDGER_DEFAULT_ENSEMBLE_SIZE}" \
    MANAGED_LEDGER_DEFAULT_WRITE_QUORUM="${MANAGED_LEDGER_DEFAULT_WRITE_QUORUM}" \
    MANAGED_LEDGER_DEFAULT_ACK_QUORUM="${MANAGED_LEDGER_DEFAULT_ACK_QUORUM}" \
    "${SCRIPT_DIR}/prepare-local-cluster.sh"
  BOOKIE_COUNT="${BOOKIE_COUNT}" \
    BK_ENTRYLOG_FAULT_MIN_WRITE_BYTES="${FAULT_MIN_BYTES}" \
    BK_ENTRYLOG_FAULT_EXACT_WRITE_BYTES="${FAULT_EXACT_BYTES}" \
    BK_ENTRYLOG_FAULT_AFTER_MATCHES="${fault_after}" \
    "${SCRIPT_DIR}/start-local-cluster.sh"

  set +e
  MESSAGES="${messages}" SIZE="${size}" RATE="${rate}" TOPIC="persistent://public/default/entrylog-ldpreload-${round_id}" \
    "${SCRIPT_DIR}/run-workload.sh"
  workload_rc=$?
  set -e

  "${SCRIPT_DIR}/stop-local-cluster.sh"

  set +e
  "${SCRIPT_DIR}/analyze-entrylogs.sh"
  analyze_rc=$?
  set -e
  if [[ "${analyze_rc}" -ne 0 ]]; then
    echo "analyze-entrylogs.sh exited with ${analyze_rc} for ${round_id}" >&2
  fi

  copy_round_artifacts "${round_dir}"

  report_json="${REPORT_DIR}/entrylog-cluster-report.json"
  if [[ -f "${report_json}" ]]; then
    append_summary_row "${round_id}" "${messages}" "${size}" "${rate}" "${fault_after}" "${FAULT_MIN_BYTES}" "${FAULT_EXACT_BYTES}" "${workload_rc}" "${report_json}"
    write_summary_md
  else
    echo "Missing report JSON for ${round_id}: ${report_json}" >&2
  fi

  if [[ "${workload_rc}" -ne 0 ]]; then
    echo "${round_id} workload exited with ${workload_rc}; continuing to next round." >&2
  fi
done

echo "Stability run archived under ${RUN_DIR}"
echo "Summary: ${SUMMARY_MD}"
