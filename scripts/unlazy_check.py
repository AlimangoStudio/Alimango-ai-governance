#!/usr/bin/env python3
"""Reference Unlazy gate for completed Spec Kit artifacts."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

OPEN_BOX = re.compile(r"^- \[ \]", re.MULTILINE)
SHORTCUT = re.compile(r"\b(?:TODO|FIXME|TBD|HACK|PLACEHOLDER)\b", re.IGNORECASE)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("spec_dir")
    args = parser.parse_args()

    root = Path(args.spec_dir).resolve()
    findings: list[dict[str, str]] = []
    if not root.is_dir():
        findings.append({"kind": "missing", "detail": "spec directory does not exist"})
    else:
        for path in sorted(root.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            if OPEN_BOX.search(text):
                findings.append({"kind": "unchecked_task", "detail": path.name})
            if SHORTCUT.search(text):
                findings.append({"kind": "shortcut_marker", "detail": path.name})
            if path.name.lower() == "gates.md":
                for state in ("OPEN", "BLOCKED", "FAIL"):
                    if re.search(rf"\|\s*{state}\s*\|", text, flags=re.IGNORECASE):
                        findings.append({"kind": "open_gate", "detail": f"{path.name}: {state}"})

        convergence = root / "convergence.md"
        if not convergence.is_file() or "COMPLETE" not in convergence.read_text(encoding="utf-8"):
            findings.append({"kind": "terminal_state", "detail": "missing COMPLETE convergence verdict"})

    terminal = "complete" if not findings else "needs_changes"
    print(json.dumps({"terminal_state": terminal, "findings": findings}, indent=2))
    return 0 if not findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
