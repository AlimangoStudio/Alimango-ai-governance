#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_NAMES = {".env", "id_rsa", "id_ed25519"}
FORBIDDEN_SUFFIXES = {".pem", ".p12", ".pfx", ".sqlite", ".db"}


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> int:
    bad = []
    for p in ROOT.rglob("*"):
        if not p.is_file() or ".git" in p.parts:
            continue
        if p.name in FORBIDDEN_NAMES or p.suffix.lower() in FORBIDDEN_SUFFIXES:
            bad.append(str(p.relative_to(ROOT)))
    if bad:
        fail("forbidden private/secret artifact patterns: " + ", ".join(bad))

    readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    governance = (ROOT / "GOVERNANCE.md").read_text(encoding="utf-8").lower()
    boundary = (ROOT / "docs/ADOPTION-BOUNDARY.md").read_text(encoding="utf-8").lower()
    if "not alimango production governance" not in readme:
        fail("README must deny production authority")
    if "public" not in governance or "production" not in governance:
        fail("GOVERNANCE.md missing authority boundary")
    if "never automatically" not in boundary and "never be automatic" not in boundary:
        fail("adoption boundary must reject automatic public-to-private promotion")

    print("PASS: public-lab privacy and authority boundary checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
