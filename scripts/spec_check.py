#!/usr/bin/env python3
"""Deterministic reference checks for a completed Spec Kit directory."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REQUIRED_FILES = ("spec.md", "plan.md", "tasks.md", "checklist.md", "convergence.md")
PLACEHOLDER_PATTERNS = (
    re.compile(r"\[(?:TITLE|DATE|OWNER|item)\]", re.IGNORECASE),
    re.compile(r"\b(?:TODO|TBD|FIXME)\b", re.IGNORECASE),
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("spec_dir")
    args = parser.parse_args()

    root = Path(args.spec_dir).resolve()
    findings: list[str] = []
    for name in REQUIRED_FILES:
        path = root / name
        if not path.is_file():
            findings.append(f"missing required artifact: {name}")

    for path in root.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        for pattern in PLACEHOLDER_PATTERNS:
            if pattern.search(text):
                findings.append(f"placeholder marker in {path.name}: {pattern.pattern}")
        if path.name in {"tasks.md", "checklist.md"} and re.search(r"^- \[ \]", text, flags=re.MULTILINE):
            findings.append(f"unchecked required item in {path.name}")

    convergence = root / "convergence.md"
    if convergence.is_file() and "COMPLETE" not in convergence.read_text(encoding="utf-8"):
        findings.append("convergence.md does not contain explicit COMPLETE verdict")

    status = "pass" if not findings else "fail"
    print(json.dumps({"status": status, "spec_dir": str(root), "findings": findings}, indent=2))
    return 0 if not findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
