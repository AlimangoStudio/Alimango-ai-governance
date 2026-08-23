#!/usr/bin/env python3
"""Create a deterministic content fingerprint for public governance audit inputs."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def collect(raw_paths: list[str]) -> list[Path]:
    found: set[Path] = set()
    for raw in raw_paths:
        path = (ROOT / raw).resolve()
        try:
            path.relative_to(ROOT)
        except ValueError as exc:
            raise SystemExit(f"path escapes repository root: {raw}") from exc
        if path.is_file():
            found.add(path)
        elif path.is_dir():
            for child in path.rglob("*"):
                if child.is_file() and ".git" not in child.parts:
                    found.add(child)
        else:
            raise SystemExit(f"path does not exist: {raw}")
    return sorted(found, key=lambda p: p.relative_to(ROOT).as_posix())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", help="Repository-relative files or directories")
    args = parser.parse_args()

    records = []
    aggregate = hashlib.sha256()
    for path in collect(args.paths):
        rel = path.relative_to(ROOT).as_posix()
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        records.append({"path": rel, "sha256": digest})
        aggregate.update(f"{rel}\0{digest}\n".encode("utf-8"))

    print(json.dumps({"file_count": len(records), "fingerprint": aggregate.hexdigest(), "files": records}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
