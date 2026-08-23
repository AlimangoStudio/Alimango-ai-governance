#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate_schema(value: object, schema: dict[str, object], path: str = "$") -> list[str]:
    errors: list[str] = []
    expected = schema.get("type")
    type_map = {"object": dict, "array": list, "string": str, "boolean": bool, "integer": int}
    if expected in type_map and (not isinstance(value, type_map[expected]) or expected == "integer" and isinstance(value, bool)):
        return [f"{path}: expected {expected}"]
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: value is not in enum")
    if isinstance(value, str):
        if len(value) < int(schema.get("minLength", 0)):
            errors.append(f"{path}: string is too short")
        if pattern := schema.get("pattern"):
            if re.search(str(pattern), value) is None:
                errors.append(f"{path}: string does not match pattern")
    if isinstance(value, list):
        if len(value) < int(schema.get("minItems", 0)):
            errors.append(f"{path}: array has too few items")
        if schema.get("uniqueItems") and len({json.dumps(item, sort_keys=True) for item in value}) != len(value):
            errors.append(f"{path}: array items are not unique")
        if isinstance(schema.get("items"), dict):
            for index, item in enumerate(value):
                errors.extend(validate_schema(item, schema["items"], f"{path}[{index}]"))
    if isinstance(value, dict):
        for required in schema.get("required", []):
            if required not in value:
                errors.append(f"{path}: missing {required}")
        properties = schema.get("properties", {})
        if isinstance(properties, dict):
            for key, item in value.items():
                if key in properties:
                    errors.extend(validate_schema(item, properties[key], f"{path}.{key}"))
                elif schema.get("additionalProperties") is False:
                    errors.append(f"{path}: unexpected property {key}")
    if isinstance(value, int) and not isinstance(value, bool) and value < int(schema.get("minimum", value)):
        errors.append(f"{path}: value is below minimum")
    return errors

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

    tool_schema = json.loads((ROOT / "schemas/tool-contract.schema.json").read_text(encoding="utf-8"))
    for path in (ROOT / "examples/tool-contracts/valid").glob("*.json"):
        errors = validate_schema(json.loads(path.read_text(encoding="utf-8")), tool_schema)
        if errors:
            fail(f"invalid tool contract {path.name}: " + "; ".join(errors))
    negative = ROOT / "examples/tool-contracts/invalid/over-broad-network.json"
    if not validate_schema(json.loads(negative.read_text(encoding="utf-8")), tool_schema):
        fail("over-broad tool contract must be rejected")

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
