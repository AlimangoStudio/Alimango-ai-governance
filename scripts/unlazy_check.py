#!/usr/bin/env python3
"""Reference Unlazy gate with bounded quality-correction semantics."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

OPEN_BOX = re.compile(r"^- \[ \]", re.MULTILINE)
SHORTCUT = re.compile(r"\b(?:TODO|FIXME|TBD|HACK|PLACEHOLDER)\b", re.IGNORECASE)
BEST_EFFORT_UNVERIFIED_EXIT = 20


def finding(kind: str, detail: str, severity: str) -> dict[str, str]:
    return {"kind": kind, "detail": detail, "severity": severity}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("spec_dir")
    parser.add_argument("--attempt", type=int, default=1, help="Current correction attempt (1-based)")
    parser.add_argument("--max-corrections", type=int, default=3, help="Maximum bounded quality corrections")
    args = parser.parse_args()

    if args.attempt < 1 or args.max_corrections < 1 or args.attempt > args.max_corrections:
        parser.error("attempt/max-corrections must satisfy 1 <= attempt <= max-corrections")

    root = Path(args.spec_dir).resolve()
    findings: list[dict[str, str]] = []
    if not root.is_dir():
        findings.append(finding("missing", "spec directory does not exist", "hard"))
    else:
        for path in sorted(root.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            if OPEN_BOX.search(text):
                findings.append(finding("unchecked_task", path.name, "quality"))
            if SHORTCUT.search(text):
                findings.append(finding("shortcut_marker", path.name, "quality"))
            if path.name.lower() == "gates.md":
                for state in ("OPEN", "BLOCKED", "FAIL"):
                    if re.search(rf"\|\s*{state}\s*\|", text, flags=re.IGNORECASE):
                        severity = "hard" if state in {"BLOCKED", "FAIL"} else "quality"
                        findings.append(finding("open_gate", f"{path.name}: {state}", severity))

        convergence = root / "convergence.md"
        if not convergence.is_file() or "COMPLETE" not in convergence.read_text(encoding="utf-8"):
            findings.append(finding("terminal_state", "missing COMPLETE convergence verdict", "quality"))

    hard_findings = [item for item in findings if item["severity"] == "hard"]
    quality_findings = [item for item in findings if item["severity"] == "quality"]

    if not findings:
        terminal = "complete"
        exit_code = 0
        claim_green = True
        may_continue_output = True
    elif hard_findings:
        terminal = "blocked"
        exit_code = 2
        claim_green = False
        may_continue_output = True
    elif args.attempt < args.max_corrections:
        terminal = "needs_correction"
        exit_code = 1
        claim_green = False
        may_continue_output = True
    else:
        terminal = "best_effort_unverified"
        # Non-zero by design: a shell/CI runner must not mistake unverified
        # continuation for successful validation. An orchestrator may handle
        # this explicit code and continue text/artifact output.
        exit_code = BEST_EFFORT_UNVERIFIED_EXIT
        claim_green = False
        may_continue_output = True

    print(json.dumps({
        "terminal_state": terminal,
        "correction_attempt": args.attempt,
        "max_corrections": args.max_corrections,
        "claim_green": claim_green,
        "may_continue_output": may_continue_output,
        "merge_or_deploy_allowed": terminal == "complete",
        "best_effort_unverified_exit_code": BEST_EFFORT_UNVERIFIED_EXIT,
        "hard_findings": hard_findings,
        "quality_findings": quality_findings,
        "findings": findings,
    }, indent=2))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
