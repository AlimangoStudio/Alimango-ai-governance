# Action Governance Skill

For each proposed side effect, produce a structured decision containing action, target, risk level, required capabilities, provenance of critical arguments, decision state, rationale, approval reference if required, and postcondition evidence.

Use `schemas/action-decision.schema.json` as the reference shape. Execute only after an `allow` or `allow_with_evidence` decision, or after the specific required approval is satisfied.