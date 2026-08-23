#!/usr/bin/env python3
"""Dependency-free structural validator for the public Alimango AI Governance Lab."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "GOVERNANCE.md",
    "LICENSE",
    "docs/ADOPTION-BOUNDARY.md",
    "docs/ARCHITECTURE.md",
    "docs/CONTROL-TAXONOMY.md",
    "docs/THREAT-MODEL.md",
    "docs/EXPERIMENT-PROTOCOL.md",
    "docs/FAILURE-MODE-CATALOG.md",
    "docs/MATURITY-MODEL.md",
    "schemas/proposal.schema.json",
    "schemas/capability-contract.schema.json",
)

FORBIDDEN_SUFFIXES = (
    ".pem",
    ".p12",
    ".pfx",
    ".sqlite",
    ".sqlite3",
    ".db",
)

REQUIRED_PROPOSAL_FIELDS = {
    "schema_version",
    "id",
    "title",
    "status",
    "failure_modes",
    "control_classes",
    "problem",
    "control",
    "enforcement_point",
    "evidence",
    "security",
    "limitations",
    "private_adoption",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        fail("missing required repository files: " + ", ".join(missing))


def check_authority_boundary() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    boundary = (ROOT / "docs/ADOPTION-BOUNDARY.md").read_text(encoding="utf-8").lower()

    if "not" not in readme or "production governance" not in readme:
        fail("README must explicitly state that the public repo is not production governance")
    if "automatic" not in boundary or "private" not in boundary:
        fail("adoption boundary must explicitly address automatic public-to-private promotion")


def check_forbidden_artifacts() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        name = path.name.lower()
        if name == ".env" or any(name.endswith(suffix) for suffix in FORBIDDEN_SUFFIXES):
            fail(f"forbidden private/secret artifact pattern: {path.relative_to(ROOT)}")
        if name.endswith(".key") and path.name != "example.key":
            fail(f"forbidden private key artifact pattern: {path.relative_to(ROOT)}")


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def check_json_files() -> None:
    for path in ROOT.rglob("*.json"):
        if ".git" not in path.parts:
            load_json(path)


def check_proposals() -> None:
    examples = sorted((ROOT / "examples").glob("AGP-*.json"))
    if not examples:
        fail("at least one machine-readable AGP example is required")

    for path in examples:
        data = load_json(path)
        if not isinstance(data, dict):
            fail(f"proposal must be an object: {path.relative_to(ROOT)}")
        missing = REQUIRED_PROPOSAL_FIELDS - data.keys()
        if missing:
            fail(f"proposal {path.name} missing fields: {sorted(missing)}")
        if not re.fullmatch(r"AGP-[0-9]{3,}", str(data.get("id", ""))):
            fail(f"proposal {path.name} has invalid id")
        if data.get("schema_version") != "1.0":
            fail(f"proposal {path.name} must use schema_version 1.0")
        adoption = data.get("private_adoption")
        if not isinstance(adoption, dict):
            fail(f"proposal {path.name} missing private_adoption object")
        if adoption.get("authoritative") is not False:
            fail(f"proposal {path.name} cannot declare public content authoritative")
        if adoption.get("automatic_sync_allowed") is not False:
            fail(f"proposal {path.name} cannot allow automatic public-to-private sync")


def check_relative_markdown_links() -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in link_pattern.findall(text):
            target = target.strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                fail(f"markdown link escapes repository: {path.relative_to(ROOT)} -> {target}")
            if not resolved.exists():
                fail(f"broken relative markdown link: {path.relative_to(ROOT)} -> {target}")


def main() -> int:
    require_files()
    check_authority_boundary()
    check_forbidden_artifacts()
    check_json_files()
    check_proposals()
    check_relative_markdown_links()
    print("PASS: public/private authority boundary is explicit")
    print("PASS: required technical documentation is present")
    print("PASS: JSON artifacts and AGP examples are structurally valid")
    print("PASS: relative Markdown links resolve")
    print("PASS: obvious private artifact patterns are absent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
