#!/usr/bin/env python3
"""Fail CI if any Red/Amber record is marked export_allowed=true.

Expected optional input file:
- policies/export_records.json
  [
    {"id": "LOT-2025-0019", "data_class": "Red", "export_allowed": false}
  ]
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

ALLOWED_EXPORT_CLASSES = {"green", "public"}
RECORD_FILE = Path("policies/export_records.json")


def main() -> int:
    if not RECORD_FILE.exists():
        print("No policies/export_records.json found; nothing to validate.")
        return 0

    try:
        records = json.loads(RECORD_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON in {RECORD_FILE}: {exc}", file=sys.stderr)
        return 1

    violations: list[str] = []
    for rec in records:
        rec_id = str(rec.get("id", "<unknown>"))
        data_class = str(rec.get("data_class", "")).strip().lower()
        export_allowed = bool(rec.get("export_allowed", False))

        if export_allowed and data_class not in ALLOWED_EXPORT_CLASSES:
            violations.append(
                f"{rec_id}: data_class={data_class!r}, export_allowed={export_allowed}"
            )

    if violations:
        print("Export policy violations detected:", file=sys.stderr)
        for v in violations:
            print(f" - {v}", file=sys.stderr)
        return 1

    print("Export policy check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
