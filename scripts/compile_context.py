#!/usr/bin/env python3
"""Compile a bounded, provenance-bearing public-safe context capsule."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUTHORITY_PATH = ROOT / "control/source-authority.json"


def fail(message: str) -> None:
    print(json.dumps({"status": "blocked", "error": message}, indent=2), file=sys.stderr)
    raise SystemExit(2)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def estimate_tokens(text: str) -> int:
    return max(1, math.ceil(len(text) / 4))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True, help="JSON request file")
    parser.add_argument("--output", help="Optional output JSON path")
    args = parser.parse_args()

    request_path = Path(args.request).resolve()
    try:
        request = json.loads(request_path.read_text(encoding="utf-8"))
        authority = json.loads(AUTHORITY_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"invalid compiler input: {exc}")

    task = str(request.get("task", "")).strip()
    budget = int(request.get("budget_tokens", 6000))
    sources = request.get("sources", [])
    if not task or budget <= 0 or not isinstance(sources, list) or not sources:
        fail("request requires task, positive budget_tokens, and non-empty sources")

    ranks = {entry["class"]: int(entry["priority"]) for entry in authority["order"]}
    prepared = []
    for raw in sources:
        if not isinstance(raw, dict):
            fail("each source must be an object")
        source_id = str(raw.get("id", "")).strip()
        source_class = str(raw.get("authority", "external"))
        sensitivity = str(raw.get("sensitivity", "public"))
        rel = Path(str(raw.get("path", "")))
        if not source_id or source_class not in ranks or not str(rel):
            fail(f"invalid source record: {raw}")
        if sensitivity != "public":
            fail(f"public compiler refuses non-public source '{source_id}' ({sensitivity})")
        path = (ROOT / rel).resolve()
        try:
            path.relative_to(ROOT)
        except ValueError:
            fail(f"source escapes repository root: {rel}")
        if not path.is_file():
            fail(f"source file missing: {rel}")
        text = path.read_text(encoding="utf-8")
        prepared.append({
            "id": source_id,
            "authority": source_class,
            "path": rel.as_posix(),
            "origin": rel.as_posix(),
            "content_hash": sha256_text(text),
            "freshness": raw.get("freshness", "current working revision"),
            "sensitivity": sensitivity,
            "reason": str(raw.get("reason", "task relevance")),
            "required": bool(raw.get("required", False)),
            "rank": ranks[source_class],
            "estimated_tokens": estimate_tokens(text),
            "text": text,
        })

    prepared.sort(key=lambda item: (not item["required"], -item["rank"], item["id"]))
    required_tokens = sum(item["estimated_tokens"] for item in prepared if item["required"])
    if required_tokens > budget:
        fail(f"required authority sources exceed budget ({required_tokens} > {budget})")

    selected = []
    used = 0
    for item in prepared:
        if item["required"] or used + item["estimated_tokens"] <= budget:
            selected.append(item)
            used += item["estimated_tokens"]

    if not any(item["authority"] == "constitution" for item in selected):
        fail("compiled context must include a constitution source")

    context_parts = []
    manifest_sources = []
    for item in selected:
        context_parts.append(f"## SOURCE {item['id']} [{item['authority']}]\n\n{item['text'].rstrip()}\n")
        manifest_sources.append({k: item[k] for k in (
            "id", "authority", "origin", "content_hash", "freshness", "sensitivity", "reason", "estimated_tokens"
        )})

    payload = {
        "status": "compiled",
        "task": task,
        "budget_tokens": budget,
        "estimated_tokens": used,
        "selected_source_count": len(selected),
        "skipped_source_count": len(prepared) - len(selected),
        "manifest": {"task": task, "budget": {"tokens": budget}, "sources": manifest_sources},
        "context": "\n".join(context_parts),
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
