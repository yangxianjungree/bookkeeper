#!/usr/bin/env python3
#
# Build a BookKeeper entrylog comparison report for the local Pulsar cluster
# harness. The report is intentionally based on parsed bytes and runtime logs,
# not fixed offsets from the investigation documents.

import argparse
import hashlib
import json
import mmap
from pathlib import Path
import re
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from entrylog_drift_scanner import (  # noqa: E402
    LOGFILE_HEADER_SIZE,
    analyze_entrylog,
    choose_true_map,
    compare_totals,
    entrylog_id_from_filename,
    find_boundary_chain,
    find_map_chains,
    format_entry,
    ledger_size_totals,
    map_size_totals,
    parse_header,
    parse_map_chain,
    result_status,
    scan_chain,
    scan_prefix,
)


FAILPOINT_RE = re.compile(
    r"Injected entrylog partial flush failure: logId=(?P<log_id>\d+), "
    r"logFile=(?P<log_file>.*?), logicalPosition=(?P<logical>\d+), "
    r"physicalPosition=(?P<physical>\d+), bytes=(?P<bytes>\d+)"
)

LD_PRELOAD_FAULT_RE = re.compile(
    r"bk-entrylog-fault: (?P<kind>dry-run-would-trigger|triggering) "
    r"op=(?P<op>\w+) fd=(?P<fd>\d+) path=(?P<path>.*) count=(?P<count>\d+) "
    r"offset=(?P<offset>-?\d+) real_rc=(?P<real_rc>-?\d+) match=(?P<match>\d+) "
    r"trigger=(?P<trigger>\d+) errno=EIO"
)


def parse_versions(cluster_dir):
    path = cluster_dir / "versions.properties"
    versions = {}
    if not path.exists():
        return versions
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        versions[key] = value
    return versions


def parse_failpoint_events(cluster_dir):
    events = []
    logs_dir = cluster_dir / "logs" / "bk1"
    if not logs_dir.exists():
        return events
    for path in sorted(logs_dir.rglob("*")):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for line in text.splitlines():
            match = FAILPOINT_RE.search(line)
            if not match:
                match = LD_PRELOAD_FAULT_RE.search(line)
                if not match:
                    continue
                log_file = Path(match.group("path"))
                try:
                    log_id = int(log_file.stem, 16)
                except ValueError:
                    log_id = None
                events.append({
                    "kind": "ldpreload",
                    "sourceLog": str(path),
                    "logId": log_id,
                    "logFile": str(log_file),
                    "logFileName": log_file.name,
                    "logicalPosition": None,
                    "physicalPosition": None,
                    "bytes": int(match.group("count")),
                    "op": match.group("op"),
                    "offset": int(match.group("offset")),
                    "realRc": int(match.group("real_rc")),
                    "match": int(match.group("match")),
                    "trigger": int(match.group("trigger")),
                    "line": line,
                })
                continue
            log_file = Path(match.group("log_file"))
            events.append({
                "kind": "java-failpoint",
                "sourceLog": str(path),
                "logId": int(match.group("log_id")),
                "logFile": str(log_file),
                "logFileName": log_file.name,
                "logicalPosition": int(match.group("logical")),
                "physicalPosition": int(match.group("physical")),
                "bytes": int(match.group("bytes")),
                "op": None,
                "offset": None,
                "realRc": None,
                "match": None,
                "trigger": None,
                "line": line,
            })
    return events


def event_for_path(events, path, role=None):
    if role is not None and role != "bk1":
        return None

    resolved = str(path.resolve())
    log_id = entrylog_id_from_filename(path)
    for event in events:
        event_path = Path(event["logFile"])
        if event_path.exists() and str(event_path.resolve()) == resolved:
            return event
        if role == "bk1" and event.get("logId") == log_id and event.get("logFileName") == path.name:
            return event
    return None


def cell(value):
    return "" if value is None else value


def read_log_lines(path):
    if not path.exists():
        return []
    try:
        return path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return []


def extract_log_snippets(path, patterns, limit=6, tag="match"):
    lines = read_log_lines(path)
    compiled = [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
    snippets = []
    for line_no, line in enumerate(lines, start=1):
        if any(pattern.search(line) for pattern in compiled):
            snippets.append({"line": line_no, "tag": tag, "text": line})
            if len(snippets) >= limit:
                break
    return snippets


def extract_log_snippets_by_group(path, groups, per_group_limit=4):
    lines = read_log_lines(path)
    snippets = []
    selected_lines = set()

    for tag, patterns in groups:
        compiled = [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
        group_count = 0
        for line_no, line in enumerate(lines, start=1):
            if line_no in selected_lines:
                continue
            if any(pattern.search(line) for pattern in compiled):
                snippets.append({"line": line_no, "tag": tag, "text": line})
                selected_lines.add(line_no)
                group_count += 1
                if group_count >= per_group_limit:
                    break
    return snippets


def extract_client_exit(cluster_dir):
    path = cluster_dir / "logs" / "client" / "pulsar-perftest.log"
    for line in reversed(read_log_lines(path)):
        match = re.search(r"workload_rc=(\d+)", line)
        if match:
            return int(match.group(1))
    return None


def collect_runtime_behavior(cluster_dir):
    bookie_groups = [
        ("bookie-fault", [
            r"Exception flushing ledgers",
            r"Input/output error",
        ]),
        ("entrylog-io", [
            r"Created new entry log file",
            r"Flushing entry logger",
            r"Synced entry logger",
        ]),
        ("bookie-lifecycle", [
            r"Turning bookie to read only during shut down",
            r"Triggering shutdown of Bookie-\d+ with exitCode",
            r"BookieDeathWatcher noticed the bookie is not running any more",
            r"Triggered exceptionHandler of Component: bookie-server",
            r"Shutting down BookieServer",
        ]),
    ]
    behavior = {
        "clientExit": extract_client_exit(cluster_dir),
        "broker": extract_log_snippets_by_group(
            cluster_dir / "logs" / "broker" / "stdout.log",
            [
                ("bk-client-init", [
                    r"MetadataDrivers - BookKeeper metadata driver",
                    r"BookKeeperClientFactoryImpl",
                    r"bookkeeper client configuration",
                ]),
                ("bookie-discovery", [
                    r"NetworkTopologyImpl - Adding a new node: .*127\.0\.0\.1:318[0-9]",
                    r"BookieInfoReader",
                    r"Update BookieInfoCache",
                ]),
                ("bookie-channel", [
                    r"PerChannelBookieClient - Successfully connected to bookie",
                    r"PerChannelBookieClient - connection .* authenticated as BookKeeperPrincipal",
                ]),
                ("managed-ledger", [
                    r"ManagedLedger.*Closing managed ledger",
                    r"ManagedLedger.*ConnectionLost",
                    r"ManagedLedger.*WARN",
                    r"ManagedLedger.*ERROR",
                    r"ManagedLedger.*failed",
                    r"ManagedLedger.*exception",
                ]),
                ("broker-error", [
                    r"PerChannelBookieClient - Exception caught on:.*Connection reset",
                    r"Disconnected from bookie channel",
                    r"java\.net\.SocketException: Connection reset",
                    r"write failed",
                    r"failed .* write",
                    r"Connection loss while executing batch operation",
                    r"ZooKeeper client is disconnected",
                    r"Session .* SessionExpiredException",
                    r"Connection refused",
                ]),
            ],
            per_group_limit=6,
        ),
        "client": extract_log_snippets_by_group(
            cluster_dir / "logs" / "client" / "pulsar-perftest.log",
            [
                ("client-progress", [
                    r"Throughput produced",
                    r"Aggregated throughput stats",
                    r"Aggregated latency stats",
                ]),
                ("client-completion", [
                    r"DONE",
                    r"workload_rc=",
                ]),
                ("client-error", [
                    r"failure [1-9]",
                    r"error",
                    r"exception",
                ]),
            ],
            per_group_limit=8,
        ),
    }
    for role in ("bk1", "bk2", "bk3"):
        behavior[role] = extract_log_snippets_by_group(
            cluster_dir / "logs" / role / "stdout.log",
            bookie_groups,
            per_group_limit=6,
        )
    return behavior


def replica_comparison_applicable(versions):
    ensemble = versions.get("managedLedgerDefaultEnsembleSize")
    write_quorum = versions.get("managedLedgerDefaultWriteQuorum")
    try:
        return int(ensemble) == int(write_quorum)
    except (TypeError, ValueError):
        return True


def collect_entries(path, physical_start, write_buffer_bytes, max_entry_size):
    with open(path, "rb") as handle:
        with mmap.mmap(handle.fileno(), 0, access=mmap.ACCESS_READ) as buf:
            header = parse_header(buf)
            map_chains = find_map_chains(buf)
            true_map = choose_true_map(map_chains, header)
            true_map_start = true_map["start"] if true_map else None
            header_map = header.get("ledgersMapOffset")
            header_map_chain = parse_map_chain(buf, header_map) if header_map is not None else None
            map_delta = true_map_start - header_map if true_map_start is not None and header_map is not None else None

            detected_physical_start = physical_start
            if detected_physical_start is None and map_delta not in (None, 0):
                boundary = find_boundary_chain(buf, true_map_start, write_buffer_bytes, max_entry_size)
                if boundary:
                    detected_physical_start = boundary["physicalStart"]

            if detected_physical_start is not None:
                stop = true_map_start if true_map_start is not None else len(buf)
                prefix = scan_prefix(buf, detected_physical_start, max_entry_size)
                post_chain = scan_chain(buf, detected_physical_start, stop, max_entry_size)
                complete_entries = prefix["entries"] + post_chain["entries"]
                strict_chain = None
            else:
                stop = true_map_start if true_map_start is not None else len(buf)
                strict_chain = scan_chain(buf, LOGFILE_HEADER_SIZE, stop, max_entry_size)
                prefix = None
                post_chain = None
                complete_entries = strict_chain["entries"]

            entries = []
            for entry in complete_entries:
                raw = bytes(buf[entry["pos"]:entry["next"]])
                entries.append({
                    "ledgerId": entry["ledgerId"],
                    "entryId": entry["entryId"],
                    "pos": entry["pos"],
                    "next": entry["next"],
                    "size": entry["size"],
                    "bytes": entry["bytes"],
                    "sha256": hashlib.sha256(raw).hexdigest(),
                })

            parsed_totals = ledger_size_totals(complete_entries)
            ledger_map_totals = map_size_totals(true_map)
            size_compare = compare_totals(parsed_totals, ledger_map_totals) if true_map else None

            return {
                "header": header,
                "trueMap": true_map,
                "headerMapValid": bool(header_map_chain and header_map_chain["start"] == header_map),
                "mapDelta": map_delta,
                "detectedPhysicalStart": detected_physical_start,
                "strictChain": strict_chain,
                "prefix": prefix,
                "postChain": post_chain,
                "entries": entries,
                "parsedTotals": parsed_totals,
                "mapTotals": ledger_map_totals,
                "ledgerSizeCompare": size_compare,
            }


def find_entrylogs(cluster_dir):
    roles = []
    for role in ("bk1", "bk2", "bk3"):
        candidates = [
            cluster_dir / "data" / role / "ledgers" / "current",
            cluster_dir / "entrylogs" / role,
        ]
        current = next((candidate for candidate in candidates if candidate.exists()), None)
        if current is None:
            continue
        for path in sorted(current.glob("*.log")):
            if path.stat().st_size > 0:
                roles.append((role, path))
    return roles


def compact_result(result):
    header = result["header"]
    true_map = result["trueMap"]
    strict = result["strictChain"]
    prefix = result["prefix"]
    post = result["postChain"]
    size_compare = result["ledgerSizeCompare"] or {}
    return {
        "header": header,
        "trueMapStart": true_map["start"] if true_map else None,
        "trueMapEnd": true_map["end"] if true_map else None,
        "trueMapLedgerCount": true_map["ledgerCount"] if true_map else None,
        "headerMapValid": result["headerMapValid"],
        "mapDelta": result["mapDelta"],
        "detectedPhysicalStart": result["detectedPhysicalStart"],
        "strictEntries": len(strict["entries"]) if strict else None,
        "strictReachesMap": strict["reachesStop"] if strict else None,
        "prefixEntries": len(prefix["entries"]) if prefix else None,
        "postEntries": len(post["entries"]) if post else None,
        "postReachesMap": post["reachesStop"] if post else None,
        "entryCount": len(result["entries"]),
        "parsedTotalSize": size_compare.get("parsedTotalSize"),
        "mapTotalSize": size_compare.get("mapTotalSize"),
        "sizeMatch": size_compare.get("matches"),
    }


def entry_index(logs):
    indexed = {}
    duplicates = {}
    for item in logs:
        role = item["role"]
        for entry in item["entries"]:
            key = f"{entry['ledgerId']}:{entry['entryId']}"
            value = {
                "role": role,
                "log": item["path"],
                "logId": item["logId"],
                "pos": entry["pos"],
                "next": entry["next"],
                "size": entry["size"],
                "sha256": entry["sha256"],
            }
            if key in indexed:
                duplicates.setdefault(role, []).append({"key": key, "first": indexed[key], "duplicate": value})
            indexed[key] = value
    return indexed, duplicates


def compare_indexes(target_name, target_index, control_name, control_index, sample_limit):
    target_keys = set(target_index)
    control_keys = set(control_index)
    common = sorted(target_keys & control_keys)
    missing_in_target = sorted(control_keys - target_keys)
    missing_in_control = sorted(target_keys - control_keys)
    mismatches = []
    for key in common:
        if target_index[key]["sha256"] != control_index[key]["sha256"]:
            mismatches.append({
                "key": key,
                target_name: target_index[key],
                control_name: control_index[key],
            })
    return {
        "target": target_name,
        "control": control_name,
        "targetEntries": len(target_keys),
        "controlEntries": len(control_keys),
        "commonEntries": len(common),
        "missingInTarget": len(missing_in_target),
        "missingInControl": len(missing_in_control),
        "hashMismatches": len(mismatches),
        "missingInTargetSample": missing_in_target[:sample_limit],
        "missingInControlSample": missing_in_control[:sample_limit],
        "hashMismatchSample": mismatches[:sample_limit],
    }


def role_logs(parsed_logs, role):
    return [item for item in parsed_logs if item["role"] == role]


def print_report(report):
    versions = report["versions"]
    print("# Entrylog Cluster Report")
    print()
    print(f"- clusterDir: `{report['clusterDir']}`")
    print(f"- pulsarVersion: `{versions.get('pulsarVersion', 'unknown')}`")
    print(f"- bookieVersion: `{versions.get('bookieVersion', 'unknown')}`")
    print(f"- bookieCount: `{versions.get('bookieCount', 'unknown')}`")
    print(
        f"- managedLedgerQuorum: `{versions.get('managedLedgerDefaultEnsembleSize', 'unknown')}/"
        f"{versions.get('managedLedgerDefaultWriteQuorum', 'unknown')}/"
        f"{versions.get('managedLedgerDefaultAckQuorum', 'unknown')}`"
    )
    print(f"- failpointEvents: `{len(report['failpointEvents'])}`")
    print()

    print("## Failpoint Events")
    print()
    if not report["failpointEvents"]:
        print("No fault event found in bk1 logs.")
    else:
        print("| kind | logId | logFile | logical | physical | bytes | op | offset | realRc | match | trigger |")
        print("|---|---:|---|---:|---:|---:|---|---:|---:|---:|---:|")
        for event in report["failpointEvents"]:
            print(
                f"| {cell(event.get('kind', 'unknown'))} | {cell(event.get('logId'))} | `{event['logFile']}` | "
                f"{cell(event.get('logicalPosition'))} | {cell(event.get('physicalPosition'))} | "
                f"{cell(event.get('bytes'))} | {cell(event.get('op'))} | {cell(event.get('offset'))} | "
                f"{cell(event.get('realRc'))} | {cell(event.get('match'))} | {cell(event.get('trigger'))} |"
            )
    print()

    print("## Log Structure")
    print()
    print("| role | log | status | fileSize | headerMap | trueMap | delta | headerMapValid | "
          "entries | strict | prefix | post | parsedSize | mapSize | sizeMatch |")
    print("|---|---|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---|")
    for item in report["logs"]:
        summary = item["summary"]
        header = summary["header"]
        status = item["status"]
        strict_entries = summary["strictEntries"]
        prefix_entries = summary["prefixEntries"]
        post_entries = summary["postEntries"]
        print(f"| {item['role']} | `{Path(item['path']).name}` | {status} | {item['fileSize']} | "
              f"{header.get('ledgersMapOffset')} | {summary['trueMapStart']} | {summary['mapDelta']} | "
              f"{summary['headerMapValid']} | {summary['entryCount']} | {strict_entries} | "
              f"{prefix_entries} | {post_entries} | {summary['parsedTotalSize']} | "
              f"{summary['mapTotalSize']} | {summary['sizeMatch']} |")
    print()

    print("## Replica Entry Comparison")
    print()
    if not report["replicaComparisonApplicable"]:
        print("Skipped: write quorum is smaller than ensemble size, so entries are intentionally single-copy distributed across bookies.")
        print()
    else:
        print("| target | control | targetEntries | controlEntries | common | missingInTarget | "
              "missingInControl | hashMismatches |")
        print("|---|---|---:|---:|---:|---:|---:|---:|")
        for comparison in report["comparisons"]:
            print(f"| {comparison['target']} | {comparison['control']} | {comparison['targetEntries']} | "
                  f"{comparison['controlEntries']} | {comparison['commonEntries']} | "
                  f"{comparison['missingInTarget']} | {comparison['missingInControl']} | "
                  f"{comparison['hashMismatches']} |")
        print()

        for comparison in report["comparisons"]:
            if comparison["hashMismatches"] or comparison["missingInTarget"] or comparison["missingInControl"]:
                print(f"### Samples: {comparison['target']} vs {comparison['control']}")
                print()
                if comparison["missingInTargetSample"]:
                    print(f"- missingInTarget: `{', '.join(comparison['missingInTargetSample'])}`")
                if comparison["missingInControlSample"]:
                    print(f"- missingInControl: `{', '.join(comparison['missingInControlSample'])}`")
                if comparison["hashMismatchSample"]:
                    samples = [item["key"] for item in comparison["hashMismatchSample"]]
                    print(f"- hashMismatches: `{', '.join(samples)}`")
                print()

    print("## Runtime Behavior")
    print()
    print(f"- clientExit: `{report['runtimeBehavior'].get('clientExit')}`")
    print()
    runtime_roles = ("bk1", "bk2", "bk3", "broker", "client")
    for index, role in enumerate(runtime_roles):
        print(f"### {role}")
        print()
        snippets = report["runtimeBehavior"].get(role) or []
        if not snippets:
            print("No matching log lines found.")
        else:
            print("| line | tag | log |")
            print("|---:|---|---|")
            for snippet in snippets:
                print(f"| {snippet['line']} | {snippet.get('tag', '')} | `{snippet['text']}` |")
        if index != len(runtime_roles) - 1:
            print()


def build_report(args):
    cluster_dir = args.cluster_dir.resolve()
    versions = parse_versions(cluster_dir)
    events = parse_failpoint_events(cluster_dir)
    runtime_behavior = collect_runtime_behavior(cluster_dir)
    parsed_logs = []

    for role, path in find_entrylogs(cluster_dir):
        event = event_for_path(events, path, role)
        physical_start = event["physicalPosition"] if event else None
        analysis = analyze_entrylog(
            path,
            write_buffer_bytes=args.write_buffer_bytes,
            physical_start=physical_start,
            max_entry_size=args.max_entry_size,
        )
        collected = collect_entries(path, physical_start, args.write_buffer_bytes, args.max_entry_size)
        log_id = entrylog_id_from_filename(path)
        parsed_logs.append({
            "role": role,
            "path": str(path),
            "logId": log_id,
            "fileSize": path.stat().st_size,
            "event": event,
            "status": result_status(analysis),
            "analysis": analysis,
            "summary": compact_result(collected),
            "entries": collected["entries"],
            "parsedTotals": collected["parsedTotals"],
            "mapTotals": collected["mapTotals"],
        })

    indexes = {}
    duplicates = {}
    present_roles = sorted({item["role"] for item in parsed_logs})
    for role in present_roles:
        index, role_duplicates = entry_index(role_logs(parsed_logs, role))
        indexes[role] = index
        duplicates[role] = role_duplicates

    comparison_applicable = replica_comparison_applicable(versions)
    comparisons = []
    if comparison_applicable and "bk2" in indexes and "bk3" in indexes:
        comparisons.append(compare_indexes("bk2", indexes["bk2"], "bk3", indexes["bk3"], args.sample_limit))
    if comparison_applicable and "bk1" in indexes:
        for control in ("bk2", "bk3"):
            if control in indexes:
                comparisons.append(compare_indexes("bk1", indexes["bk1"], control, indexes[control], args.sample_limit))

    return {
        "clusterDir": str(cluster_dir),
        "versions": versions,
        "failpointEvents": events,
        "logs": parsed_logs,
        "comparisons": comparisons,
        "replicaComparisonApplicable": comparison_applicable,
        "duplicates": duplicates,
        "runtimeBehavior": runtime_behavior,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Compare BookKeeper entrylogs from the local Pulsar harness.")
    parser.add_argument("--cluster-dir", type=Path, required=True, help="Harness runtime directory")
    parser.add_argument("--write-buffer-bytes", type=lambda value: int(value, 0), default=65536)
    parser.add_argument("--max-entry-size", type=lambda value: int(value, 0), default=64 * 1024 * 1024)
    parser.add_argument("--sample-limit", type=int, default=12)
    parser.add_argument("--json-out", type=Path, help="Write full report JSON to this path")
    args = parser.parse_args(argv)

    report = build_report(args)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print_report(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
