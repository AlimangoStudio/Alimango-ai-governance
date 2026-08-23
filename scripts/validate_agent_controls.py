#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "AGENTS.md", "CLAUDE.md", "GOVERNANCE.md", ".specify/memory/constitution.md",
    ".github/copilot-instructions.md", "adapters/README.md", "adapters/codex.md", "adapters/claude-code.md",
    ".agents/README.md", ".agents/manifest.json",
    ".agents/policies/secrets.md", ".agents/policies/isolation.md", ".agents/policies/self-protection.md",
    ".agents/workflows/spec-kit.md", ".agents/workflows/action-governance.md",
    ".agents/workflows/context-compile.md", ".agents/workflows/independent-review.md",
    ".agents/workflows/unlazy.md", ".agents/workflows/convergence.md",
    ".agents/skills/task-router/SKILL.md", ".agents/skills/done-when-proof/SKILL.md",
    ".agents/skills/adversarial-review/SKILL.md", ".agents/skills/regression-proof/SKILL.md",
    ".agents/skills/compound-engineering/SKILL.md", ".agents/skills/governance-validation/SKILL.md",
    "harness/audit-kernel.md", "harness/capability-doctor.md", "harness/context-compiler.md",
    "harness/skill-tdd.md", "harness/external-adoption.md", "harness/parallel-work.md",
    "control/source-authority.json", "control/action-policy.json", "control/context-compiler.json",
    "schemas/tool-contract.schema.json", "schemas/action-decision.schema.json",
    "schemas/evidence.schema.json", "schemas/context-manifest.schema.json",
    "schemas/review-verdict.schema.json", "schemas/agent-event.schema.json",
    "schemas/upgrade-manifest.schema.json", "schemas/exception.schema.json"
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> int:
    missing = [p for p in REQUIRED if not (ROOT / p).is_file()]
    if missing:
        fail("missing agent-control files: " + ", ".join(missing))

    manifest = json.loads((ROOT / ".agents/manifest.json").read_text(encoding="utf-8"))
    if manifest.get("scope") != "public-goods-reference":
        fail("control manifest must declare public-goods-reference scope")

    required_workflows = {"spec-kit", "action-governance", "context-compile", "independent-review", "unlazy", "convergence"}
    if not required_workflows.issubset(set(manifest.get("required_workflows", []))):
        fail("control manifest is missing mandatory workflows")

    for path in list(ROOT.glob("schemas/*.json")) + list(ROOT.glob("examples/*.json")) + list(ROOT.glob("control/*.json")):
        json.loads(path.read_text(encoding="utf-8"))

    authority = json.loads((ROOT / "control/source-authority.json").read_text(encoding="utf-8"))
    if authority.get("order", [{}])[-1].get("class") != "external":
        fail("external/advisory authority must remain lowest")

    action = json.loads((ROOT / "control/action-policy.json").read_text(encoding="utf-8"))
    if action["risk"]["R4"]["default_decision"] != "require_approval":
        fail("R4 actions must require approval in reference policy")
    if "unauthorized_external_write" not in action.get("always_deny_in_public_lab", []):
        fail("unauthorized external writes must remain denied")

    constitution = (ROOT / ".specify/memory/constitution.md").read_text(encoding="utf-8").lower()
    for marker in ("fail closed", "least capability", "spec-driven", "independent challenge", "public-goods hygiene", "no overclaiming"):
        if marker not in constitution:
            fail(f"constitution missing invariant: {marker}")

    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8").lower()
    if "tool availability is not authorization" not in agents:
        fail("AGENTS.md must preserve tool-authorization invariant")
    if "non-public project names" not in agents:
        fail("AGENTS.md must preserve public-scope confidentiality invariant")

    print(f"PASS: {len(REQUIRED)} mandatory agent-control surfaces present")
    print("PASS: machine-readable policies/schemas parse and authority/action/public-scope invariants hold")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
