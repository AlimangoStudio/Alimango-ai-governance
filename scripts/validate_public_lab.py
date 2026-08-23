#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_NAMES = {".env", "id_rsa", "id_ed25519"}
FORBIDDEN_SUFFIXES = {".pem", ".p12", ".pfx", ".sqlite", ".db"}
REQUIRED_PUBLIC_FILES = {
    "README.md",
    "GOVERNANCE.md",
    "SECURITY.md",
    "docs/PUBLIC-SCOPE.md",
}


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> int:
    missing = [name for name in sorted(REQUIRED_PUBLIC_FILES) if not (ROOT / name).is_file()]
    if missing:
        fail("missing public-scope files: " + ", ".join(missing))

    bad = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.name in FORBIDDEN_NAMES or path.suffix.lower() in FORBIDDEN_SUFFIXES:
            bad.append(str(path.relative_to(ROOT)))
    if bad:
        fail("forbidden secret/non-public artifact patterns: " + ", ".join(bad))

    readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    governance = (ROOT / "GOVERNANCE.md").read_text(encoding="utf-8").lower()
    public_scope = (ROOT / "docs/PUBLIC-SCOPE.md").read_text(encoding="utf-8").lower()

    if "public goods" not in readme:
        fail("README must describe the project as public goods")
    if "public-goods boundary" not in governance:
        fail("GOVERNANCE.md missing public-goods boundary")
    if "self-contained public goods" not in public_scope:
        fail("PUBLIC-SCOPE.md missing self-contained public scope")

    print("PASS: public-scope and artifact hygiene checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
