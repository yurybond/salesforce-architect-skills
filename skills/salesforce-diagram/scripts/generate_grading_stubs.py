#!/usr/bin/env python3
"""Generate grading.json stubs from eval expectations.

This helper reads eval expectations from evals/evals.json and writes
per-run grading.json skeletons into an iteration directory, for example:

  <iteration>/eval-01/with_skill/grading.json
  <iteration>/eval-01/without_skill/grading.json
  <iteration>/eval-01/old_skill/grading.json

The generated files follow the skill-creator grading schema field names:
- expectations[].text
- expectations[].passed
- expectations[].evidence
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

EVAL_DIR_RE = re.compile(r"^eval[-_](\d+)")
RUN_DIR_NAMES = ("with_skill", "without_skill", "old_skill")


def load_expectations(evals_path: Path) -> Dict[int, List[str]]:
    with evals_path.open("r", encoding="utf-8") as f:
        payload = json.load(f)

    result: Dict[int, List[str]] = {}
    for item in payload.get("evals", []):
        eval_id = item.get("id")
        expectations = item.get("expectations", [])
        if isinstance(eval_id, int) and isinstance(expectations, list):
            result[eval_id] = [str(x) for x in expectations]
    return result


def infer_eval_id(eval_dir_name: str) -> int | None:
    match = EVAL_DIR_RE.match(eval_dir_name)
    if not match:
        return None
    return int(match.group(1))


def find_run_dirs(iteration_dir: Path) -> Iterable[Tuple[int, Path]]:
    for child in sorted(iteration_dir.iterdir()):
        if not child.is_dir():
            continue
        eval_id = infer_eval_id(child.name)
        if eval_id is None:
            continue
        for run_name in RUN_DIR_NAMES:
            run_dir = child / run_name
            if run_dir.is_dir():
                yield eval_id, run_dir


def build_grading_stub(expectations: List[str]) -> dict:
    expectation_rows = [
        {
            "text": text,
            "passed": False,
            "evidence": "TODO: grade this expectation.",
        }
        for text in expectations
    ]

    total = len(expectation_rows)
    return {
        "expectations": expectation_rows,
        "summary": {
            "passed": 0,
            "failed": total,
            "total": total,
            "pass_rate": 0.0,
        },
        "execution_metrics": {
            "tool_calls": {},
            "total_tool_calls": 0,
            "total_steps": 0,
            "errors_encountered": 0,
            "output_chars": 0,
            "transcript_chars": 0,
        },
        "timing": {
            "executor_duration_seconds": 0.0,
            "grader_duration_seconds": 0.0,
            "total_duration_seconds": 0.0,
        },
        "claims": [],
        "user_notes_summary": {
            "uncertainties": [
                "Auto-generated grading stub. Replace placeholder evidence during grading."
            ],
            "needs_review": [],
            "workarounds": [],
        },
    }


def write_json(path: Path, payload: dict) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "iteration_dir",
        type=Path,
        help="Path to iteration directory containing eval-* folders.",
    )
    parser.add_argument(
        "--evals",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "evals" / "evals.json",
        help="Path to evals.json (default: ../evals/evals.json from this script).",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing grading.json files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions without writing files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    iteration_dir: Path = args.iteration_dir
    evals_path: Path = args.evals

    if not iteration_dir.exists() or not iteration_dir.is_dir():
        print(f"error: iteration_dir not found or not a directory: {iteration_dir}")
        return 2
    if not evals_path.exists() or not evals_path.is_file():
        print(f"error: evals.json not found: {evals_path}")
        return 2

    expectations_by_id = load_expectations(evals_path)
    created = 0
    skipped_existing = 0
    skipped_missing_eval = 0

    for eval_id, run_dir in find_run_dirs(iteration_dir):
        expectations = expectations_by_id.get(eval_id)
        if expectations is None:
            print(f"skip (no eval id {eval_id} in evals.json): {run_dir}")
            skipped_missing_eval += 1
            continue

        out_path = run_dir / "grading.json"
        if out_path.exists() and not args.overwrite:
            print(f"skip (exists): {out_path}")
            skipped_existing += 1
            continue

        payload = build_grading_stub(expectations)
        if args.dry_run:
            print(f"would write: {out_path} (expectations={len(expectations)})")
        else:
            write_json(out_path, payload)
            print(f"wrote: {out_path} (expectations={len(expectations)})")
        created += 1

    print(
        f"done: created={created} skipped_existing={skipped_existing} "
        f"skipped_missing_eval={skipped_missing_eval}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
