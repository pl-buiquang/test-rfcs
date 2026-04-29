#!/usr/bin/env python3
"""Stage rfcs/*.md into docs/rfcs/ and generate the index page.

Reads frontmatter to produce a sortable table of all RFCs.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
RFCS_DIR = ROOT / "rfcs"
DOCS_RFCS_DIR = ROOT / "docs" / "rfcs"
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}


def main() -> None:
    DOCS_RFCS_DIR.mkdir(parents=True, exist_ok=True)

    rows = []
    for src in sorted(RFCS_DIR.glob("*.md")):
        if src.name.startswith("0000-"):
            continue
        text = src.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        rows.append(
            {
                "id": str(fm.get("rfc_id", "")).zfill(4),
                "title": fm.get("title", src.stem),
                "status": fm.get("status", "?"),
                "author": fm.get("author", "?"),
                "team": fm.get("team", "?"),
                "tier": fm.get("tier", "standard"),
                "date": fm.get("date_created", ""),
                "file": src.name,
            }
        )
        shutil.copy2(src, DOCS_RFCS_DIR / src.name)

    rows.sort(key=lambda r: r["id"])

    lines = [
        "# All RFCs",
        "",
        f"_{len(rows)} RFC(s) in this repository._",
        "",
        "| ID | Title | Status | Tier | Author | Team | Created |",
        "|----|-------|--------|------|--------|------|---------|",
    ]
    for r in rows:
        link = f"[RFC-{r['id']}]({r['file']})"
        lines.append(
            f"| {link} | {r['title']} | `{r['status']}` | `{r['tier']}` | "
            f"{r['author']} | {r['team']} | {r['date']} |"
        )
    lines.append("")

    (DOCS_RFCS_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Staged {len(rows)} RFC(s) into {DOCS_RFCS_DIR}")


if __name__ == "__main__":
    main()
