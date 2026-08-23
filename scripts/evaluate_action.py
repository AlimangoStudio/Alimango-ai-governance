#!/usr/bin/env python3
"""Reference action-governance evaluator.

This CLI demonstrates policy-mediated authorization. It does not execute the action.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "control/action-policy.json"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--action-id", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--risk", choices=["R0", "R1", "R2", "R3", "R4"], required=True)
    parser.add_argument("--capability", action="append", default=[])
    parser.add_argument("--approval-reference")
    args = parser.parse_args()

    policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
    forbidden = set(policy.get("always_deny_in_public_lab", []))

    if args.action_id in forbidden:
        decision = "deny"
        reason = "action is explicitly denied by the public-lab policy"
    else:
        decision = policy["risk"][args.risk]["default_decision"]
        reason = f"default decision for {args.risk} under public-lab reference policy"
        if decision == "require_approval" and args.approval_reference:
            decision = "allow_with_evidence"
            reason = "required approval reference supplied; execution would still require scoped postcondition evidence"

    payload = {
        "action": args.action_id,
        "target": args.target,
        "risk": args.risk,
        "capabilities": sorted(set(args.capability)),
        "decision": decision,
        "reason": reason,
        "approval_reference": args.approval_reference,
        "required_evidence": ["authorization decision", "postcondition proof"] if decision == "allow_with_evidence" else [],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
