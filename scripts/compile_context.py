#!/usr/bin/env python3
"""Compile a bounded, provenance-bearing public-safe context capsule."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

from governance_recovery import OMISSION_PLACEHOLDER, digest_text

ROOT = Path(__file__).resolve().parents[1]
AUTHORITY_PATH = ROOT / "control/source-authority.json"


def fail(message: str) -> None:
    print(json.dumps({"status": "blocked", "error": message}, indent=2), file=sys.stderr)
    raise SystemExit(2)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def estimate_tokens(text: str) -> int:
    return max(1, math.ceil(len(text) / 4))


def omission_record(
    *,
    source_id: str,
    source_class: str,
    rel: Path,
    reason: str,
    content: str | None,
    required_for_authorization: bool,
    mandatory_authority: bool,
) -> dict[str, object]:
    return {
        "id": source_id,
        "authority": source_class,
        "origin": rel.as_posix(),
        "included": False,
        "reason": reason,
        "content_hash": digest_text(content) if content is not None else None,
        "required_for_authorization": required_for_authorization,
        "mandatory_authority": mandatory_authority,
        "placeholder": OMISSION_PLACEHOLDER,
    }


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
    prepared: list[dict[str, object]] = []
    omissions: list[dict[str, object]] = []

    for raw in sources:
        if not isinstance(raw, dict):
            fail("each source must be an object")
        source_id = str(raw.get("id", "")).strip()
        source_class = str(raw.get("authority", "external"))
        sensitivity = str(raw.get("sensitivity", "public"))
        rel = Path(str(raw.get("path", "")))
        required = bool(raw.get("required", False))
        required_for_authorization = bool(raw.get("required_for_authorization", False))
        mandatory_authority = bool(raw.get("mandatory_authority", False)) or source_class == "constitution"
        provenance_verified = raw.get("provenance_verified", True) is True

        if not source_id or source_class not in ranks or not str(rel):
            fail(f"invalid source record: {raw}")

        # Public-scope hygiene is a hard gate, not an optional provenance omission.
        if sensitivity != "public":
            fail(f"public compiler refuses non-public source '{source_id}' ({sensitivity})")

        path = (ROOT / rel).resolve()
        try:
            path.relative_to(ROOT)
        except ValueError:
            fail(f"source escapes repository root: {rel}")

        text: str | None = None
        if path.is_file():
            try:
                text = path.read_text(encoding="utf-8")
            except OSError as exc:
                if required or mandatory_authority or required_for_authorization:
                    fail(f"required source unreadable: {rel}: {exc}")
        elif required or mandatory_authority or required_for_authorization:
            fail(f"required source file missing: {rel}")

        if not provenance_verified or text is None:
            reason = "PROVENANCE_VERIFICATION_FAILED" if not provenance_verified else "OPTIONAL_SOURCE_UNAVAILABLE"
            if required or mandatory_authority:
                fail(f"mandatory source provenance unavailable: {source_id}")
            if required_for_authorization:
                fail(f"authorization-critical source provenance unavailable: {source_id}")
            omissions.append(omission_record(
                source_id=source_id,
                source_class=source_class,
                rel=rel,
                reason=reason,
                content=text,
                required_for_authorization=False,
                mandatory_authority=False,
            ))
            continue

        prepared.append({
            "id": source_id,
            "authority": source_class,
            "path": rel.as_posix(),
            "origin": rel.as_posix(),
            "content_hash": sha256_text(text),
            "freshness": raw.get("freshness", "current working revision"),
            "sensitivity": sensitivity,
            "reason": str(raw.get("reason", "task relevance")),
            "required": required or mandatory_authority,
            "required_for_authorization": required_for_authorization,
            "rank": ranks[source_class],
            "estimated_tokens": estimate_tokens(text),
            "text": text,
        })

    prepared.sort(key=lambda item: (not bool(item["required"]), -int(item["rank"]), str(item["id"])))
    required_tokens = sum(int(item["estimated_tokens"]) for item in prepared if bool(item["required"]))
    if required_tokens > budget:
        fail(f"required authority sources exceed budget ({required_tokens} > {budget})")

    selected: list[dict[str, object]] = []
    used = 0
    for item in prepared:
        item_tokens = int(item["estimated_tokens"])
        if bool(item["required"]) or used + item_tokens <= budget:
            selected.append(item)
            used += item_tokens

    if not any(item["authority"] == "constitution" for item in selected):
        fail("compiled context must include a verified constitution source")

    context_parts: list[str] = []
    manifest_sources: list[dict[str, object]] = []
    for item in selected:
        context_parts.append(f"## SOURCE {item['id']} [{item['authority']}]\n\n{str(item['text']).rstrip()}\n")
        manifest_sources.append({
            key: item[key]
            for key in (
                "id", "authority", "origin", "content_hash", "freshness", "sensitivity",
                "reason", "estimated_tokens", "required_for_authorization"
            )
        })

    for omitted in omissions:
        context_parts.append(f"## SOURCE {omitted['id']} [omitted]\n\n{OMISSION_PLACEHOLDER}\n")

    payload = {
        "status": "compiled_with_omissions" if omissions else "compiled",
        "task": task,
        "budget_tokens": budget,
        "estimated_tokens": used,
        "selected_source_count": len(selected),
        "omitted_source_count": len(omissions),
        "skipped_source_count": len(prepared) - len(selected),
        "manifest": {
            "task": task,
            "budget": {"tokens": budget},
            "sources": manifest_sources,
            "omissions": omissions,
        },
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
