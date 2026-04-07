#!/usr/bin/env python3
"""Validate Progressive Crystallization state files.

This is a minimal transitional validator. It accepts both the older
single-object state shape and the newer split-state shape introduced by the
hardening work. The goal is not full formal verification; the goal is to catch
broken object shapes, invalid lifecycle states, and missing hardening records
for crystallized claims.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any


ALLOWED_STATUSES = {
    "tension": {"loose_tension", "structured_tension", "live", "reframed", "dissolved", "frontier"},
    "claim": {"candidate_claim", "working", "crystallized_claim", "weakened", "rejected"},
    "alternative": {"live", "narrowed", "hybridized", "ruled_out_by_first_principles", "ruled_out_by_measurement"},
    "test": {"new", "proposed", "specified", "runnable", "sharpened", "decisive", "exhausted", "blocked"},
}

REQUIRED_OBJECT_FIELDS = {
    "tension": {"id", "type", "description", "status", "origin_round", "last_updated_round"},
    "claim": {"id", "type", "description", "status", "origin_round", "last_updated_round"},
    "alternative": {"id", "type", "description", "status", "origin_round", "last_updated_round"},
    "test": {"id", "type", "description", "status", "origin_round", "last_updated_round"},
}

HARDENING_DECISION_FIELDS = {"round", "object", "trigger"}


def err(errors: list[str], path: str, message: str) -> None:
    errors.append(f"{path}: {message}")


def validate_object(
    obj: Any,
    expected_type: str,
    path: str,
    errors: list[str],
    seen_ids: dict[str, str],
) -> None:
    if not isinstance(obj, dict):
        err(errors, path, "must be an object")
        return

    missing = REQUIRED_OBJECT_FIELDS[expected_type] - set(obj.keys())
    if missing:
        err(errors, path, f"missing required fields: {sorted(missing)}")

    obj_id = obj.get("id")
    if not isinstance(obj_id, str) or not obj_id.strip():
        err(errors, path, "id must be a non-empty string")
    else:
        if obj_id in seen_ids and seen_ids[obj_id] != path:
            err(errors, path, f"duplicate id also seen at {seen_ids[obj_id]}")
        else:
            seen_ids[obj_id] = path

    obj_type = obj.get("type")
    if obj_type != expected_type:
        err(errors, path, f"type must be '{expected_type}', got {obj_type!r}")

    status = obj.get("status")
    if status not in ALLOWED_STATUSES[expected_type]:
        err(errors, path, f"invalid status {status!r} for type {expected_type}")

    for key in ("origin_round", "last_updated_round"):
        if key in obj and not isinstance(obj[key], int):
            err(errors, path, f"{key} must be an integer")

    if expected_type == "test":
        target = obj.get("target")
        if status in {"specified", "runnable", "decisive", "blocked"} and not isinstance(target, str):
            err(errors, path, "tests beyond proposed/new must declare a string target")


def validate_legacy_or_typed_test(
    item: Any,
    path: str,
    errors: list[str],
    seen_ids: dict[str, str],
) -> None:
    # Transitional support: older states often stored observable_tests as plain
    # strings while newer states store typed test objects.
    if isinstance(item, str):
        if not item.strip():
            err(errors, path, "legacy test string must be non-empty")
        return
    validate_object(item, "test", path, errors, seen_ids)


def validate_hardening_decision(
    item: Any,
    path: str,
    errors: list[str],
    seen_ids: set[str],
) -> None:
    if not isinstance(item, dict):
        err(errors, path, "must be an object")
        return

    missing = HARDENING_DECISION_FIELDS - set(item.keys())
    if missing:
        err(errors, path, f"missing required fields: {sorted(missing)}")

    obj = item.get("object")
    if isinstance(obj, str) and obj not in seen_ids:
        err(errors, path, f"references unknown object id {obj!r}")

    if "representational_decision" in item:
        allowed = {
            "stay_loose",
            "promote_to_structured_tension",
            "promote_to_candidate_claim",
            "stay_structured",
        }
        if item["representational_decision"] not in allowed:
            err(errors, path, "invalid representational_decision")

    if "operational_decision" in item:
        allowed = {
            "no_test_promotion",
            "promote_to_specified_test",
            "promote_to_runnable_test",
            "keep_existing_test_state",
        }
        if item["operational_decision"] not in allowed:
            err(errors, path, "invalid operational_decision")


def collect_list(state: dict[str, Any], key: str) -> list[Any]:
    value = state.get(key)
    return value if isinstance(value, list) else []


def validate_state_file(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text())
    except Exception as exc:  # noqa: BLE001
        return [f"{path}: failed to parse JSON: {exc}"]

    if not isinstance(data, dict):
        return [f"{path}: root must be a JSON object"]

    for key in ("question", "round", "status"):
        if key not in data:
            err(errors, str(path), f"missing top-level field {key!r}")

    seen_ids: dict[str, str] = {}

    object_lists = [
        ("tensions", "tension"),
        ("claims", "claim"),
        ("alternatives", "alternative"),
        ("tests", "test"),
    ]

    for key, expected_type in object_lists:
        for idx, item in enumerate(collect_list(data, key)):
            validate_object(item, expected_type, f"{path}:{key}[{idx}]", errors, seen_ids)

    core_state = data.get("core_state")
    if isinstance(core_state, dict):
        for key, expected_type in (
            ("tensions", "tension"),
            ("claims", "claim"),
            ("alternatives", "alternative"),
            ("tests", "test"),
        ):
            value = core_state.get(key, [])
            if not isinstance(value, list):
                err(errors, f"{path}:core_state.{key}", "must be a list")
                continue
            for idx, item in enumerate(value):
                validate_object(
                    item,
                    expected_type,
                    f"{path}:core_state.{key}[{idx}]",
                    errors,
                    seen_ids,
                )

    for idx, item in enumerate(collect_list(data, "observable_tests")):
        validate_legacy_or_typed_test(item, f"{path}:observable_tests[{idx}]", errors, seen_ids)

    known_ids = set(seen_ids.keys())
    for idx, item in enumerate(collect_list(data, "hardening_decisions")):
        validate_hardening_decision(item, f"{path}:hardening_decisions[{idx}]", errors, known_ids)

    crystallized_claim_ids = {
        obj.get("id")
        for obj in collect_list(data, "claims")
        if isinstance(obj, dict) and obj.get("status") == "crystallized_claim"
    }
    if isinstance(core_state, dict):
        crystallized_claim_ids.update(
            obj.get("id")
            for obj in collect_list(core_state, "claims")
            if isinstance(obj, dict) and obj.get("status") == "crystallized_claim"
        )

    hardening_targets = {
        item.get("object")
        for item in collect_list(data, "hardening_decisions")
        if isinstance(item, dict)
    }

    for claim_id in sorted(c for c in crystallized_claim_ids if isinstance(c, str)):
        if claim_id not in hardening_targets:
            err(
                errors,
                str(path),
                f"crystallized claim {claim_id!r} has no corresponding hardening_decision",
            )

    return errors


def expand_paths(paths: list[str]) -> list[Path]:
    expanded: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if p.is_dir():
            expanded.extend(sorted(p.rglob("*.json")))
        else:
            expanded.append(p)
    return expanded


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Progressive Crystallization state JSON files.")
    parser.add_argument("paths", nargs="+", help="JSON file(s) or directories to validate")
    args = parser.parse_args()

    targets = expand_paths(args.paths)
    if not targets:
        print("No JSON files found.", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    for path in targets:
        all_errors.extend(validate_state_file(path))

    if all_errors:
        for message in all_errors:
            print(message, file=sys.stderr)
        return 1

    for path in targets:
        print(f"OK {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
