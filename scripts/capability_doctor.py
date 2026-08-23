#!/usr/bin/env python3
"""Reference capability preflight. Reports availability; never grants authorization."""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--require", action="append", default=[], help="Executable or repo-relative path")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    results = []
    for item in args.require:
        path = root / item
        available = path.exists() or shutil.which(item) is not None
        results.append({"capability_probe": item, "available": available, "authorized": False})

    status = "available" if all(x["available"] for x in results) else "unavailable"
    print(json.dumps({"status": status, "note": "availability is not authorization", "checks": results}, indent=2))
    return 0 if status == "available" else 2


if __name__ == "__main__":
    raise SystemExit(main())
