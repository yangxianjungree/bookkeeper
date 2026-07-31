#!/usr/bin/env python3
#
# Offline scanner for BookKeeper entrylog physical/logical position drift.
#
# This is intentionally dependency-free. It performs structural checks:
#   - entrylog header parsing
#   - physical entry framing scans
#   - ledgers map discovery/parsing
#   - ledger size accounting checks
#   - optional V3 digest checks for complete entries
#   - optional E2E properties/candidate indexed-location checks

import argparse
import hashlib
import hmac
from collections import defaultdict
import json
import mmap
from pathlib import Path
import struct
import sys
import zlib


LOGFILE_HEADER_SIZE = 1024
INVALID_LID = -1
LEDGERS_MAP_ENTRY_ID = -2
MAP_MARKER = struct.pack(">qq", INVALID_LID, LEDGERS_MAP_ENTRY_ID)
METADATA_LENGTH = 32
ENTRY_HEADER = struct.Struct(">iqqq")
MAP_BATCH_HEADER = struct.Struct(">iqqi")


def build_crc32c_table():
    table = []
    polynomial = 0x82F63B78
    for value in range(256):
        crc = value
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ polynomial
            else:
                crc >>= 1
        table.append(crc & 0xFFFFFFFF)
    return table


CRC32C_TABLE = build_crc32c_table()


def read_properties(path):
    props = {}
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            props[key] = value
    return props


def to_int(value, default=None):
    if value is None:
        return default
    return int(value, 0)


def unpack_i32(buf, pos):
    if pos < 0 or pos + 4 > len(buf):
        return None
    return struct.unpack_from(">i", buf, pos)[0]


def unpack_i64(buf, pos):
    if pos < 0 or pos + 8 > len(buf):
        return None
    return struct.unpack_from(">q", buf, pos)[0]


def parse_header(buf):
    if len(buf) < 24:
        return {"valid": False, "reason": "file shorter than entrylog header prefix"}
    magic = bytes(buf[0:4])
    return {
        "valid": magic == b"BKLO",
        "magic": magic.decode("ascii", "replace"),
        "version": unpack_i32(buf, 4),
        "ledgersMapOffset": unpack_i64(buf, 8),
        "ledgersCount": unpack_i32(buf, 16),
    }


def parse_entry(buf, pos):
    if pos < 0 or pos + ENTRY_HEADER.size > len(buf):
        return None
    size, ledger_id, entry_id, lac = ENTRY_HEADER.unpack_from(buf, pos)
    return {
        "pos": pos,
        "size": size,
        "bodyPos": pos + 4,
        "ledgerId": ledger_id,
        "entryId": entry_id,
        "lac": lac,
        "next": pos + 4 + size,
        "bytes": 4 + size,
    }


def is_plausible_entry(entry, file_size, scan_limit, max_entry_size):
    if entry is None:
        return False
    if entry["size"] < 24 or entry["size"] > max_entry_size:
        return False
    if entry["next"] > file_size or entry["next"] > scan_limit:
        return False
    if entry["ledgerId"] < 0:
        return False
    if entry["entryId"] < 0:
        return False
    if entry["lac"] < -1 or entry["lac"] > entry["entryId"]:
        return False
    return True


def parse_map_batch(buf, start):
    if start < 0 or start + MAP_BATCH_HEADER.size > len(buf):
        return None
    size, ledger_id, entry_id, batch_size = MAP_BATCH_HEADER.unpack_from(buf, start)
    if ledger_id != INVALID_LID or entry_id != LEDGERS_MAP_ENTRY_ID:
        return None
    if batch_size < 0 or size != 20 + 16 * batch_size:
        return None
    end = start + 4 + size
    if end > len(buf):
        return None
    ledgers = []
    pos = start + 24
    for _ in range(batch_size):
        lid = unpack_i64(buf, pos)
        total_size = unpack_i64(buf, pos + 8)
        if lid is None or total_size is None:
            return None
        ledgers.append({"ledgerId": lid, "totalSize": total_size})
        pos += 16
    return {
        "start": start,
        "sizeField": size,
        "batchSize": batch_size,
        "end": end,
        "ledgers": ledgers,
    }


def parse_map_chain(buf, start):
    batches = []
    ledgers = []
    pos = start
    while pos < len(buf):
        batch = parse_map_batch(buf, pos)
        if batch is None:
            break
        batches.append(batch)
        ledgers.extend(batch["ledgers"])
        pos = batch["end"]
    if not batches:
        return None
    return {
        "start": start,
        "end": pos,
        "batchCount": len(batches),
        "ledgerCount": len(ledgers),
        "ledgers": ledgers,
        "endsAtEof": pos == len(buf),
    }


def find_map_chains(buf):
    chains = []
    pos = 0
    seen = set()
    while True:
        marker = buf.find(MAP_MARKER, pos)
        if marker < 0:
            break
        start = marker - 4
        if start >= 0 and start not in seen:
            chain = parse_map_chain(buf, start)
            if chain is not None:
                chains.append(chain)
                seen.add(start)
        pos = marker + 1
    chains.sort(key=lambda item: (not item["endsAtEof"], item["start"]))
    return chains


def choose_true_map(chains, header):
    if not chains:
        return None
    header_count = header.get("ledgersCount")
    for chain in chains:
        if chain["endsAtEof"] and chain["ledgerCount"] == header_count:
            return chain
    for chain in chains:
        if chain["endsAtEof"]:
            return chain
    return chains[0]


def scan_prefix(buf, physical_start, max_entry_size):
    entries = []
    pos = LOGFILE_HEADER_SIZE
    crossing = None
    bad = None
    while pos < physical_start:
        entry = parse_entry(buf, pos)
        if not is_plausible_entry(entry, len(buf), len(buf), max_entry_size):
            bad = {"pos": pos, "entry": entry}
            break
        if entry["next"] <= physical_start:
            entries.append(entry)
            pos = entry["next"]
        else:
            crossing = entry
            break
    return {
        "entries": entries,
        "end": pos,
        "crossing": crossing,
        "bad": bad,
    }


def scan_chain(buf, start, stop, max_entry_size):
    entries = []
    pos = start
    bad = None
    while pos < stop:
        entry = parse_entry(buf, pos)
        if not is_plausible_entry(entry, len(buf), stop, max_entry_size):
            bad = {"pos": pos, "entry": entry}
            break
        entries.append(entry)
        pos = entry["next"]
    return {
        "start": start,
        "stop": stop,
        "end": pos,
        "entries": entries,
        "bad": bad,
        "reachesStop": pos == stop and bad is None,
    }


def ledger_size_totals(entries):
    totals = defaultdict(int)
    for entry in entries:
        totals[entry["ledgerId"]] += entry["bytes"]
    return dict(sorted(totals.items()))


def map_size_totals(map_chain):
    if map_chain is None:
        return {}
    totals = defaultdict(int)
    for item in map_chain["ledgers"]:
        totals[item["ledgerId"]] += item["totalSize"]
    return dict(sorted(totals.items()))


def compare_totals(parsed_totals, map_totals):
    all_ledgers = sorted(set(parsed_totals) | set(map_totals))
    mismatches = []
    for ledger_id in all_ledgers:
        parsed = parsed_totals.get(ledger_id, 0)
        mapped = map_totals.get(ledger_id, 0)
        if parsed != mapped:
            mismatches.append({
                "ledgerId": ledger_id,
                "parsedSize": parsed,
                "mapSize": mapped,
                "delta": parsed - mapped,
            })
    return {
        "matches": not mismatches,
        "parsedTotalSize": sum(parsed_totals.values()),
        "mapTotalSize": sum(map_totals.values()),
        "mismatches": mismatches,
    }


def crc32c_update(crc, data):
    crc ^= 0xFFFFFFFF
    for byte in data:
        crc = CRC32C_TABLE[(crc ^ byte) & 0xFF] ^ (crc >> 8)
    return (crc ^ 0xFFFFFFFF) & 0xFFFFFFFF


def mac_key(password):
    digest = hashlib.sha1()
    digest.update(b"mac")
    digest.update(password)
    return digest.digest()


def digest_layout(digest_type):
    normalized = digest_type.lower()
    if normalized == "crc32":
        return {"type": normalized, "length": 8}
    if normalized == "crc32c":
        return {"type": normalized, "length": 4}
    if normalized == "mac":
        return {"type": normalized, "length": 20}
    if normalized in ("none", "dummy"):
        return {"type": normalized, "length": 0}
    raise ValueError(f"unsupported digest type: {digest_type}")


def compute_digest_bytes(digest_type, metadata, payload, password):
    layout = digest_layout(digest_type)
    kind = layout["type"]
    if kind in ("none", "dummy"):
        return b""
    if kind == "crc32":
        crc = zlib.crc32(metadata)
        crc = zlib.crc32(payload, crc) & 0xFFFFFFFF
        return struct.pack(">Q", crc)
    if kind == "crc32c":
        crc = crc32c_update(0, metadata)
        crc = crc32c_update(crc, payload)
        return struct.pack(">I", crc)
    if kind == "mac":
        digest = hmac.new(mac_key(password), digestmod=hashlib.sha1)
        digest.update(metadata)
        digest.update(payload)
        return digest.digest()
    raise ValueError(f"unsupported digest type: {digest_type}")


def verify_entry_digest(buf, entry, digest_type, password):
    layout = digest_layout(digest_type)
    mac_length = layout["length"]
    if layout["type"] in ("none", "dummy"):
        return {"checked": False, "ok": None, "reason": "digest disabled"}
    if entry["size"] < METADATA_LENGTH + mac_length:
        return {"checked": True, "ok": False, "reason": "entry smaller than digest metadata"}

    body_pos = entry["bodyPos"]
    digest_pos = body_pos + METADATA_LENGTH
    payload_pos = digest_pos + mac_length
    entry_end = body_pos + entry["size"]

    metadata = memoryview(buf)[body_pos:digest_pos]
    received = bytes(memoryview(buf)[digest_pos:payload_pos])
    payload = memoryview(buf)[payload_pos:entry_end]
    expected = compute_digest_bytes(digest_type, metadata, payload, password)
    ok = received == expected
    return {
        "checked": True,
        "ok": ok,
        "ledgerId": entry["ledgerId"],
        "entryId": entry["entryId"],
        "pos": entry["pos"],
        "bodyPos": entry["bodyPos"],
        "size": entry["size"],
        "received": received.hex() if not ok else None,
        "expected": expected.hex() if not ok else None,
        "reason": None if ok else "digest mismatch",
    }


def verify_entries_digest(buf, entries, digest_type, password, sample_limit=20):
    layout = digest_layout(digest_type)
    if layout["type"] in ("none", "dummy"):
        return {
            "enabled": False,
            "digestType": layout["type"],
            "checked": 0,
            "ok": 0,
            "failed": 0,
            "failures": [],
        }

    checked = 0
    ok = 0
    failures = []
    for entry in entries:
        result = verify_entry_digest(buf, entry, layout["type"], password)
        if not result["checked"]:
            continue
        checked += 1
        if result["ok"]:
            ok += 1
        elif len(failures) < sample_limit:
            failures.append(result)

    return {
        "enabled": True,
        "digestType": layout["type"],
        "checked": checked,
        "ok": ok,
        "failed": checked - ok,
        "failures": failures,
    }


def find_boundary_chain(buf, true_map_start, write_buffer_bytes, max_entry_size):
    if not write_buffer_bytes or not true_map_start:
        return None
    candidates = []
    boundary = write_buffer_bytes
    while boundary < true_map_start:
        entry = parse_entry(buf, boundary)
        if is_plausible_entry(entry, len(buf), true_map_start, max_entry_size):
            chain = scan_chain(buf, boundary, true_map_start, max_entry_size)
            if chain["reachesStop"]:
                candidates.append({
                    "physicalStart": boundary,
                    "entryCount": len(chain["entries"]),
                })
        boundary += write_buffer_bytes
    if not candidates:
        return None
    return candidates[0]


def parse_candidate(value):
    parts = value.split(":")
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("candidate must be ledgerId:entryId:indexedPosition")
    return {
        "ledgerId": int(parts[0], 0),
        "entryId": int(parts[1], 0),
        "indexedPosition": int(parts[2], 0),
    }


def entry_body_tuple(buf, body_pos):
    if body_pos < 0 or body_pos + 24 > len(buf):
        return None
    return {
        "bodyPos": body_pos,
        "sizeAtPrefix": unpack_i32(buf, body_pos - 4),
        "ledgerId": unpack_i64(buf, body_pos),
        "entryId": unpack_i64(buf, body_pos + 8),
        "lac": unpack_i64(buf, body_pos + 16),
    }


def check_candidate(buf, candidate, deltas):
    checks = []
    indexed = candidate["indexedPosition"]
    for name, delta in deltas:
        if delta in (None, 0):
            continue
        pos = indexed + delta
        body = entry_body_tuple(buf, pos)
        checks.append({
            "deltaName": name,
            "delta": delta,
            "bodyPos": pos,
            "body": body,
            "matches": bool(body
                            and body["ledgerId"] == candidate["ledgerId"]
                            and body["entryId"] == candidate["entryId"]),
        })
    stale_body = entry_body_tuple(buf, indexed)
    return {
        "candidate": candidate,
        "indexedBody": stale_body,
        "indexedMatches": bool(stale_body
                               and stale_body["ledgerId"] == candidate["ledgerId"]
                               and stale_body["entryId"] == candidate["entryId"]),
        "adjustedChecks": checks,
    }


def candidate_deltas(map_delta, properties):
    deltas = []
    seen = set()
    for name, delta in (
            ("mapDelta", map_delta),
            ("injectedDelta", int(properties["injectedDelta"]))
            if properties and "injectedDelta" in properties else ("injectedDelta", None)):
        if delta is None or delta in seen:
            continue
        seen.add(delta)
        deltas.append((name, delta))
    return deltas


def analyze_entrylog(path, *, properties=None, write_buffer_bytes=None, physical_start=None,
                     candidate=None, max_entry_size=64 * 1024 * 1024,
                     digest_type="none", password=b""):
    with open(path, "rb") as handle:
        with mmap.mmap(handle.fileno(), 0, access=mmap.ACCESS_READ) as buf:
            header = parse_header(buf)
            map_chains = find_map_chains(buf)
            true_map = choose_true_map(map_chains, header)
            true_map_start = true_map["start"] if true_map else None
            header_map = header.get("ledgersMapOffset")
            header_map_chain = parse_map_chain(buf, header_map) if header_map is not None else None
            map_delta = true_map_start - header_map if true_map_start is not None and header_map is not None else None

            if physical_start is None and map_delta not in (None, 0):
                boundary = find_boundary_chain(buf, true_map_start, write_buffer_bytes, max_entry_size)
                if boundary:
                    physical_start = boundary["physicalStart"]

            prefix = None
            post_chain = None
            strict_chain = None
            parsed_totals = {}
            size_compare = None
            suspect_range = None
            complete_entries = []
            if physical_start is not None:
                post_stop = true_map_start if true_map_start is not None else len(buf)
                prefix = scan_prefix(buf, physical_start, max_entry_size)
                post_chain = scan_chain(buf, physical_start, post_stop, max_entry_size)
                complete_entries = prefix["entries"] + post_chain["entries"]
                parsed_totals = ledger_size_totals(complete_entries)
                if true_map is not None:
                    size_compare = compare_totals(parsed_totals, map_size_totals(true_map))

                if prefix["crossing"]:
                    suspect_start = prefix["crossing"]["pos"]
                elif prefix["bad"]:
                    suspect_start = prefix["bad"]["pos"]
                else:
                    suspect_start = prefix["end"]
                suspect_range = {
                    "start": suspect_start,
                    "end": physical_start,
                    "bytes": max(0, physical_start - suspect_start),
                }
            else:
                strict_stop = true_map_start if true_map_start is not None else len(buf)
                strict_chain = scan_chain(buf, LOGFILE_HEADER_SIZE, strict_stop, max_entry_size)
                if strict_chain["reachesStop"]:
                    complete_entries = strict_chain["entries"]
                    parsed_totals = ledger_size_totals(strict_chain["entries"])
                    if true_map is not None:
                        size_compare = compare_totals(parsed_totals, map_size_totals(true_map))

            candidate_check = check_candidate(buf, candidate, candidate_deltas(map_delta, properties)) \
                if candidate else None
            digest_check = verify_entries_digest(buf, complete_entries, digest_type, password)

            return {
                "path": str(path),
                "fileSize": len(buf),
                "header": header,
                "mapChains": map_chains,
                "trueMap": true_map,
                "headerMapValid": bool(header_map_chain and header_map_chain["start"] == header_map),
                "mapDelta": map_delta,
                "writeBufferBytes": write_buffer_bytes,
                "physicalStart": physical_start,
                "strictChain": summarize_chain(strict_chain),
                "prefix": summarize_prefix(prefix),
                "postChain": summarize_chain(post_chain),
                "suspectRange": suspect_range,
                "ledgerSizeCompare": size_compare,
                "candidateCheck": candidate_check,
                "digestCheck": digest_check,
            }


def summarize_prefix(prefix):
    if prefix is None:
        return None
    return {
        "entryCount": len(prefix["entries"]),
        "end": prefix["end"],
        "crossing": summarize_entry(prefix["crossing"]),
        "bad": summarize_bad(prefix["bad"]),
    }


def summarize_chain(chain):
    if chain is None:
        return None
    return {
        "start": chain["start"],
        "stop": chain["stop"],
        "end": chain["end"],
        "entryCount": len(chain["entries"]),
        "reachesStop": chain["reachesStop"],
        "first": summarize_entry(chain["entries"][0]) if chain["entries"] else None,
        "last": summarize_entry(chain["entries"][-1]) if chain["entries"] else None,
        "bad": summarize_bad(chain["bad"]),
    }


def summarize_entry(entry):
    if entry is None:
        return None
    return {
        "pos": entry["pos"],
        "size": entry["size"],
        "ledgerId": entry["ledgerId"],
        "entryId": entry["entryId"],
        "lac": entry["lac"],
        "next": entry["next"],
    }


def summarize_bad(bad):
    if bad is None:
        return None
    return {
        "pos": bad["pos"],
        "entry": summarize_entry(bad["entry"]),
    }


def candidate_from_properties(props):
    required = ("ledgerId", "candidateEntryId", "indexedPosition")
    if not all(key in props for key in required):
        return None
    return {
        "ledgerId": int(props["ledgerId"]),
        "entryId": int(props["candidateEntryId"]),
        "indexedPosition": int(props["indexedPosition"]),
    }


def role_candidate_from_properties(props, role):
    prefix = f"{role}Indexed"
    required = ("ledgerId", "candidateEntryId", f"{prefix}Position")
    if not all(key in props for key in required):
        return None
    return {
        "ledgerId": int(props["ledgerId"]),
        "entryId": int(props["candidateEntryId"]),
        "indexedPosition": int(props[f"{prefix}Position"]),
    }


def e2e_log_path(props, props_path):
    copied = props.get("copiedLogFile")
    if copied and Path(copied).exists():
        return Path(copied)
    run_id = props.get("runId", props_path.stem)
    candidate = props_path.with_name(f"{run_id}-0.log")
    if candidate.exists():
        return candidate
    return None


def path_from_property(props, key):
    value = props.get(key)
    if not value:
        return None
    path = Path(value)
    return path if path.exists() else None


def paths_from_property(props, key):
    value = props.get(key)
    if not value:
        return []
    paths = []
    for raw in value.split(","):
        path = Path(raw.strip())
        if path.exists() and path.stat().st_size > 0:
            paths.append(path)
    return paths


def entrylog_id_from_filename(path):
    stem = path.name[:-4] if path.name.endswith(".log") else path.stem
    token = stem.rsplit("-", 1)[-1]
    try:
        return int(token, 16)
    except ValueError:
        return None


def injected_log_id(props):
    path = props.get("injectedLogFile")
    if not path:
        return None
    return entrylog_id_from_filename(Path(path))


def print_single_report(result):
    header = result["header"]
    true_map = result["trueMap"]
    print(f"path: {result['path']}")
    print(f"fileSize: {result['fileSize']}")
    print(f"header: magic={header.get('magic')} version={header.get('version')} "
          f"ledgersMapOffset={header.get('ledgersMapOffset')} ledgersCount={header.get('ledgersCount')}")
    if true_map:
        print(f"trueMap: start={true_map['start']} end={true_map['end']} "
              f"ledgerCount={true_map['ledgerCount']} endsAtEof={true_map['endsAtEof']}")
    else:
        print("trueMap: not found")
    print(f"headerMapValid: {result['headerMapValid']}")
    print(f"mapDelta: {result['mapDelta']}")
    print(f"physicalStart: {result['physicalStart']}")
    if result["strictChain"]:
        chain = result["strictChain"]
        print(f"strictChain: entries={chain['entryCount']} reachesMap={chain['reachesStop']} "
              f"start={chain['start']} end={chain['end']}")
        print(f"strictChain.first: {format_entry(chain['first'])}")
        print(f"strictChain.last: {format_entry(chain['last'])}")
    if result["prefix"]:
        prefix = result["prefix"]
        print(f"prefix: entries={prefix['entryCount']} end={prefix['end']} "
              f"crossing={format_entry(prefix['crossing'])} bad={prefix['bad']}")
    if result["postChain"]:
        chain = result["postChain"]
        print(f"postChain: entries={chain['entryCount']} reachesMap={chain['reachesStop']} "
              f"start={chain['start']} end={chain['end']}")
        print(f"postChain.first: {format_entry(chain['first'])}")
        print(f"postChain.last: {format_entry(chain['last'])}")
    if result["suspectRange"]:
        sr = result["suspectRange"]
        print(f"suspectRange: {sr['start']}..{sr['end']} bytes={sr['bytes']}")
    if result["ledgerSizeCompare"]:
        cmp_result = result["ledgerSizeCompare"]
        print(f"ledgerSizeCompare: matches={cmp_result['matches']} "
              f"parsedTotal={cmp_result['parsedTotalSize']} mapTotal={cmp_result['mapTotalSize']} "
              f"mismatches={len(cmp_result['mismatches'])}")
        for mismatch in cmp_result["mismatches"][:20]:
            print(f"  mismatch ledger={mismatch['ledgerId']} parsed={mismatch['parsedSize']} "
                  f"map={mismatch['mapSize']} delta={mismatch['delta']}")
    digest = result["digestCheck"]
    if digest["enabled"]:
        print(f"digestCheck: type={digest['digestType']} checked={digest['checked']} "
              f"ok={digest['ok']} failed={digest['failed']}")
        for failure in digest["failures"]:
            print(f"  digest failure pos={failure['pos']} ledger={failure['ledgerId']} "
                  f"entry={failure['entryId']} reason={failure['reason']} "
                  f"received={failure['received']} expected={failure['expected']}")
    if result["candidateCheck"]:
        cc = result["candidateCheck"]
        print(f"candidate: ledger={cc['candidate']['ledgerId']} entry={cc['candidate']['entryId']} "
              f"indexedPosition={cc['candidate']['indexedPosition']} indexedMatches={cc['indexedMatches']}")
        for check in cc["adjustedChecks"]:
            print(f"  adjusted[{check['deltaName']}={check['delta']}]: "
                  f"bodyPos={check['bodyPos']} matches={check['matches']} body={check['body']}")


def format_entry(entry):
    if not entry:
        return "none"
    return (f"{entry['pos']}..{entry['next']} "
            f"lid={entry['ledgerId']} eid={entry['entryId']} size={entry['size']}")


def result_status(result):
    digest = result.get("digestCheck") or {}
    digest_ok = not digest.get("enabled") or digest.get("failed") == 0
    size_compare = result.get("ledgerSizeCompare")
    size_ok = size_compare is None or size_compare.get("matches")

    if result.get("postChain"):
        if result["postChain"]["reachesStop"] and size_ok and digest_ok:
            return "DRIFT_OK" if result.get("mapDelta") not in (None, 0) else "SPLIT_OK"
        return "DRIFT_CHECK"

    strict = result.get("strictChain")
    if strict and strict["reachesStop"] and size_ok and digest_ok:
        return "SEALED_OK" if result.get("trueMap") else "UNSEALED_OK"
    if strict:
        return "STRICT_CHECK"
    return "NO_CHAIN"


def print_e2e_table(results):
    print("| run | role | status | delta | physicalStart | strictEntries | prefixEntries | suspectRange | postEntries | "
          "chainToMap | parsedSize | mapSize | sizeMatch | digest | candidateIndexed | candidateAdjusted | "
          "headerDelta |")
    print("|---|---|---|---:|---:|---:|---:|---|---:|---|---:|---:|---|---|---|---|---:|")
    for item in results:
        run_id = item["runId"]
        role = item["role"]
        result = item["result"]
        cmp_result = result.get("ledgerSizeCompare") or {}
        digest = result.get("digestCheck") or {}
        digest_text = "off"
        if digest.get("enabled"):
            digest_text = f"{digest.get('ok')}/{digest.get('checked')}"
        candidate = result.get("candidateCheck") or {}
        indexed_ok = candidate.get("indexedMatches")
        adjusted_ok = any(item.get("matches") for item in candidate.get("adjustedChecks", []))
        sr = result.get("suspectRange")
        sr_text = f"{sr['start']}..{sr['end']}" if sr else "n/a"
        print(f"| {run_id} | {role} | {result_status(result)} | "
              f"{result.get('mapDelta')} | {result.get('physicalStart')} | "
              f"{(result.get('strictChain') or {}).get('entryCount')} | "
              f"{(result.get('prefix') or {}).get('entryCount')} | {sr_text} | "
              f"{(result.get('postChain') or {}).get('entryCount')} | "
              f"{(result.get('postChain') or {}).get('reachesStop')} | "
              f"{cmp_result.get('parsedTotalSize')} | {cmp_result.get('mapTotalSize')} | "
              f"{cmp_result.get('matches')} | {digest_text} | {indexed_ok} | {adjusted_ok} | "
              f"{result.get('mapDelta')} |")


def run_e2e_dir(args):
    base = Path(args.e2e_dir)
    results = []
    for props_path in sorted(base.glob("*.properties")):
        props = read_properties(props_path)
        if "runId" not in props:
            continue

        run_id = props.get("runId", props_path.stem)
        cases = []

        if args.all_logs:
            injected_id = injected_log_id(props)
            target_indexed_log_id = to_int(props.get("targetIndexedLogId"), to_int(props.get("indexedLogId")))
            healthy_indexed_log_id = to_int(props.get("healthyIndexedLogId"))

            target_paths = paths_from_property(props, "copiedTargetLogs")
            if not target_paths:
                target_log = path_from_property(props, "copiedTargetLogFile") or e2e_log_path(props, props_path)
                target_paths = [target_log] if target_log is not None else []
            for path in target_paths:
                log_id = entrylog_id_from_filename(path)
                is_injected_log = log_id is not None and (log_id == injected_id or log_id == target_indexed_log_id)
                cases.append({
                    "role": f"target-{log_id}" if log_id is not None else "target",
                    "path": path,
                    "physicalStart": to_int(props.get("injectedPhysicalPosition")) if is_injected_log else None,
                    "candidate": (role_candidate_from_properties(props, "target") or candidate_from_properties(props))
                    if log_id == target_indexed_log_id else None,
                    "properties": props if is_injected_log else None,
                })

            for path in paths_from_property(props, "copiedHealthyLogs"):
                log_id = entrylog_id_from_filename(path)
                cases.append({
                    "role": f"healthy-{log_id}" if log_id is not None else "healthy",
                    "path": path,
                    "physicalStart": None,
                    "candidate": role_candidate_from_properties(props, "healthy")
                    if log_id == healthy_indexed_log_id else None,
                    "properties": None,
                })
        else:
            target_log = path_from_property(props, "copiedTargetLogFile") or e2e_log_path(props, props_path)
            if target_log is not None:
                cases.append({
                    "role": "target",
                    "path": target_log,
                    "physicalStart": to_int(props.get("injectedPhysicalPosition")),
                    "candidate": role_candidate_from_properties(props, "target") or candidate_from_properties(props),
                    "properties": props,
                })

            healthy_log = path_from_property(props, "copiedHealthyLogFile")
            if healthy_log is not None:
                cases.append({
                    "role": "healthy",
                    "path": healthy_log,
                    "physicalStart": None,
                    "candidate": role_candidate_from_properties(props, "healthy"),
                    "properties": None,
                })

        if not cases:
            print(f"warning: no log found for {props_path}", file=sys.stderr)
            continue

        for case in cases:
            result = analyze_entrylog(
                case["path"],
                properties=case["properties"],
                write_buffer_bytes=to_int(props.get("writeBufferBytes")),
                physical_start=case["physicalStart"],
                candidate=case["candidate"],
                max_entry_size=args.max_entry_size,
                digest_type=args.digest_type,
                password=args.password_bytes,
            )
            results.append({"runId": run_id, "role": case["role"], "result": result})
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print_e2e_table(results)


def run_self_test():
    crc32c = crc32c_update(0, b"123456789")
    if crc32c != 0xE3069283:
        raise AssertionError(f"crc32c self-test failed: {crc32c:#x}")

    metadata = struct.pack(">qqqq", 7, 9, 8, 5)
    payload = b"hello"
    body = metadata + compute_digest_bytes("crc32", metadata, payload, b"") + payload
    entry_bytes = struct.pack(">i", len(body)) + body
    entry = parse_entry(entry_bytes, 0)
    result = verify_entry_digest(entry_bytes, entry, "crc32", b"")
    if not result["ok"]:
        raise AssertionError(f"crc32 V3 entry self-test failed: {result}")

    print("self-test: ok")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Scan BookKeeper entrylog files for physical/logical drift.")
    parser.add_argument("log", nargs="?", type=Path, help="entrylog file to scan")
    parser.add_argument("--properties", type=Path, help="E2E .properties file for candidate/index metadata")
    parser.add_argument("--candidate", type=parse_candidate, help="candidate as ledgerId:entryId:indexedPosition")
    parser.add_argument("--physical-start", type=lambda value: int(value, 0),
                        help="known physical chain start after the suspect region")
    parser.add_argument("--write-buffer-bytes", type=lambda value: int(value, 0),
                        help="write buffer size; used to auto-detect boundary chain start")
    parser.add_argument("--max-entry-size", type=lambda value: int(value, 0), default=64 * 1024 * 1024)
    parser.add_argument("--digest-type", choices=("none", "crc32", "crc32c", "mac", "dummy"), default="none",
                        help="verify V3 entry digest for complete entries")
    parser.add_argument("--password", default="", help="ledger password for MAC digest; defaults to empty")
    parser.add_argument("--password-hex", help="ledger password bytes as hex")
    parser.add_argument("--e2e-dir", type=Path, help="scan run*.properties/run*-0.log artifacts in a directory")
    parser.add_argument("--all-logs", action="store_true",
                        help="in --e2e-dir mode, scan all copiedTargetLogs/copiedHealthyLogs, not only candidate logs")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument("--self-test", action="store_true", help="run built-in checksum/layout self tests")
    args = parser.parse_args(argv)
    args.password_bytes = bytes.fromhex(args.password_hex) if args.password_hex else args.password.encode("utf-8")

    if args.self_test:
        run_self_test()
        return 0

    if args.e2e_dir:
        run_e2e_dir(args)
        return 0

    if args.log is None:
        parser.error("log is required unless --e2e-dir is used")

    props = read_properties(args.properties) if args.properties else None
    candidate = args.candidate or (candidate_from_properties(props) if props else None)
    write_buffer_bytes = args.write_buffer_bytes or (to_int(props.get("writeBufferBytes")) if props else None)
    physical_start = args.physical_start or (to_int(props.get("injectedPhysicalPosition")) if props else None)
    result = analyze_entrylog(
        args.log,
        properties=props,
        write_buffer_bytes=write_buffer_bytes,
        physical_start=physical_start,
        candidate=candidate,
        max_entry_size=args.max_entry_size,
        digest_type=args.digest_type,
        password=args.password_bytes,
    )
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_single_report(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
