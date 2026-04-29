#!/usr/bin/env python3
"""Validate RFC markdown files: frontmatter completeness, naming, ID uniqueness.

Usage: python tooling/validate_rfc.py rfcs/
Exits non-zero on any validation failure. Prints all errors before exiting.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REQUIRED_FRONTMATTER = {
    "rfc_id",
    "title",
    "author",
    "status",
    "date_created",
    "tags",
}

ALLOWED_STATUS = {"draft", "open-for-review", "accepted", "rejected", "deferred"}
ALLOWED_TIER = {"standard", "lightweight"}
FILENAME_RE = re.compile(r"^(\d{4})-[a-z0-9-]+\.md$")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def validate_file(path: Path, seen_ids: dict[str, Path]) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")

    m = FILENAME_RE.match(path.name)
    if not m:
        errors.append(f"{path}: filename must match XXXX-short-title.md")
        return errors
    file_id = m.group(1)

    fm_match = FRONTMATTER_RE.match(text)
    if not fm_match:
        errors.append(f"{path}: missing or malformed YAML frontmatter")
        return errors

    try:
        fm = yaml.safe_load(fm_match.group(1)) or {}
    except yaml.YAMLError as e:
        errors.append(f"{path}: invalid YAML frontmatter: {e}")
        return errors

    missing = REQUIRED_FRONTMATTER - fm.keys()
    if missing:
        errors.append(f"{path}: missing required frontmatter fields: {sorted(missing)}")

    rfc_id = str(fm.get("rfc_id", "")).zfill(4)
    if rfc_id != file_id:
        errors.append(
            f"{path}: frontmatter rfc_id ({rfc_id}) does not match filename ({file_id})"
        )

    if rfc_id in seen_ids:
        errors.append(
            f"{path}: duplicate rfc_id {rfc_id} (also in {seen_ids[rfc_id]})"
        )
    else:
        seen_ids[rfc_id] = path

    status = fm.get("status")
    if status not in ALLOWED_STATUS:
        errors.append(
            f"{path}: status '{status}' not in {sorted(ALLOWED_STATUS)}"
        )

    tier = fm.get("tier", "standard")
    if tier not in ALLOWED_TIER:
        errors.append(f"{path}: tier '{tier}' not in {sorted(ALLOWED_TIER)}")

    if not isinstance(fm.get("tags"), list):
        errors.append(f"{path}: tags must be a list")

    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate_rfc.py <rfcs-dir>", file=sys.stderr)
        return 2

    rfcs_dir = Path(argv[1])
    if not rfcs_dir.is_dir():
        print(f"Not a directory: {rfcs_dir}", file=sys.stderr)
        return 2

    files = sorted(p for p in rfcs_dir.glob("*.md") if not p.name.startswith("0000-"))
    if not files:
        print("No RFC files to validate.")
        return 0

    seen_ids: dict[str, Path] = {}
    all_errors: list[str] = []
    for f in files:
        all_errors.extend(validate_file(f, seen_ids))

    if all_errors:
        print("\n".join(all_errors), file=sys.stderr)
        return 1

    print(f"Validated {len(files)} RFC file(s) — OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
