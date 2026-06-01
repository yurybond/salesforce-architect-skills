#!/usr/bin/env python3
"""Recompute grading summary fields from expectations in grading.json files.

Updates these fields under summary:
- passed
- failed
- total
- pass_rate

Usage examples:
  python3 update_grading_summary.py /path/to/iteration-1
  python3 update_grading_summary.py /path/to/eval-01/with_skill/grading.json
  python3 update_grading_summary.py /path/to/iteration-1 --dry-run
  python3 update_grading_summary.py /path/to/iteration-1 --check
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable, Tuple


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "path",
        type=Path,
        help="Path to a grading.json file or a directory containing grading.json files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without writing files.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero if any grading summary is stale.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail if expectations entries are malformed.",
    )
    return parser.parse_args()


def find_grading_files(path: Path) -> Iterable[Path]:
    if path.is_file():
        if path.name != "grading.json":
            return []
        return [path]
    if path.is_dir():
        return sorted(path.rglob("grading.json"))
    return []


def compute_summary(payload: dict, strict: bool = False) -> Tuple[dict, int]:
    expectations = payload.get("expectations", [])
    if not isinstance(expectations, list):
        if strict:
            raise ValueError("expectations must be a list")
        expectations = []

    total = 0
    passed = 0
    malformed = 0

    for item in expectations:
        if not isinstance(item, dict):
            malformed += 1
            if strict:
                raise ValueError("each expectation must be an object")
            continue

        value = item.get("passed")
        if isinstance(value, bool):
            total += 1
            if value:
                passed += 1
        else:
            malformed += 1
            if strict:
                raise ValueError("expectation.passed must be boolean")

    failed = total - passed
    pass_rate = round((passed / total) if total else 0.0, 4)

    summary = {
        "passed": passed,
        "failed": failed,
        "total": total,
        "pass_rate": pass_rate,
    }
    return summary, malformed


def read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, payload: dict) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")


def main() -> int:
    args = parse_args()
    targets = list(find_grading_files(args.path))
    if not targets:
        print(f"error: no grading.json files found under: {args.path}")
        return 2

    updated = 0
    stale = 0
    malformed_total = 0

    for file_path in targets:
        try:
            payload = read_json(file_path)
            summary, malformed = compute_summary(payload, strict=args.strict)
            malformed_total += malformed

            before = payload.get("summary")
            is_changed = before != summary
            if is_changed:
                stale += 1
                payload["summary"] = summary
                if args.dry_run or args.check:
                    print(f"stale: {file_path}")
                else:
                    write_json(file_path, payload)
                    print(f"updated: {file_path}")
                    updated += 1
            else:
                print(f"ok: {file_path}")
        except Exception as exc:  # pylint: disable=broad-except
            print(f"error: {file_path}: {exc}")
            return 2

    print(
        f"done: files={len(targets)} stale={stale} updated={updated} "
        f"malformed_expectations={malformed_total}"
    )

    if args.check and stale > 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
