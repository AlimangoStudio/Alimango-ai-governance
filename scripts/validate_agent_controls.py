#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "AGENTS.md",
    "GOVERNANCE.md",
    ".specify/memory/constitution.md",
    ".agents/README.md",
    ".agents/manifest.json",
    ".agents/workflows/spec-kit.md",
    ".agents/workflows/action-governance.md",
    ".agents/workflows/context-compile.md",
    ".agents/workflows/independent-review.md",
    ".agents/workflows/unlazy.md",
    ".agents/workflows/convergence.md",
    ".agents/skills/task-router/SKILL.md",
    ".agents/skills/done-when-proof/SKILL.md",
    ".agents/skills/adversarial-review/SKILL.md",
    "schemas/tool-contract.schema.json",
    "schemas/action-decision.schema.json",
    "schemas/evidence.schema.json",
    "schemas/context-manifest.schema.json",
    "schemas/review-verdict.schema.json",
    "schemas/agent-event.schema.json",
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> int:
    missing = [p for p in REQUIRED if not (ROOT / p).is_file()]
    if missing:
        fail("missing agent-control files: " + ", ".join(missing))

    manifest = json.loads((ROOT / ".agents/manifest.json").read_text(encoding="utf-8"))
    if manifest.get("production_authority") is not False:
        fail("public control manifest must explicitly deny production authority")

    required_workflows = {"spec-kit", "action-governance", "context-compile", "independent-review", "unlazy", "convergence"}
    if not required_workflows.issubset(set(manifest.get("required_workflows", []))):
        fail("control manifest is missing mandatory workflows")

    for path in ROOT.glob("schemas/*.json"):
        json.loads(path.read_text(encoding="utf-8"))
    for path in ROOT.glob("examples/*.json"):
        json.loads(path.read_text(encoding="utf-8"))

    constitution = (ROOT / ".specify/memory/constitution.md").read_text(encoding="utf-8").lower()
    for marker in ("fail closed", "least capability", "spec-driven", "independent challenge", "no overclaiming"):
        if marker not in constitution:
            fail(f"constitution missing invariant: {marker}")

    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8").lower()
    if "not alimango production governance" not in agents:
        fail("AGENTS.md must preserve public/private authority boundary")
    if "tool availability is not authorization" not in agents:
        fail("AGENTS.md must preserve tool-authorization invariant")

    print(f"PASS: {len(REQUIRED)} mandatory agent-control surfaces present")
    print("PASS: schemas/examples parse and authority boundary is explicit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
