# AGP-003: Evidence-Gated Completion with Unlazy and Convergence

**Status:** accepted-for-lab  
**Control family:** completion / evidence / review

## Failure mode

Agents often collapse several states into “done”: code was written, syntax passed, a focused test passed, review was attempted, or a deployment command returned successfully. The implementation can still have unchecked tasks, skipped negative tests, unresolved findings, missing approval, or no live verification.

## Control

Separate three mechanisms:

### Done-When / Proof

Define acceptance gates before implementation where practical. Each requirement maps to evidence, result, revision/time, and limitations.

### Unlazy

Immediately before a completion claim, search for shortcut indicators: unchecked required tasks, placeholder markers, stale/skipped validation, untested failure paths, open findings, missing approval, missing migration/rollback proof, and claims stronger than available browser/live evidence.

### Convergence

Reconcile specification, plan, tasks, checklist, implementation, evidence, reviewer findings, and Unlazy. Contradictions are fixed or remain explicit open gates. They are never resolved by deleting inconvenient evidence.

Terminal states are explicit:

`complete` · `blocked` · `partial` · `needs_changes` · `cancelled`.

## Why tests are not enough

A test suite can be green while the wrong requirements were implemented or while deployment/review obligations are still open. Evidence gating therefore validates both behavioral proof and the delivery contract.

## Evidence

Reference surfaces:

- `.agents/skills/done-when-proof/SKILL.md`
- `.agents/workflows/unlazy.md`
- `.agents/workflows/convergence.md`
- `schemas/evidence.schema.json`
- `scripts/spec_check.py`
- `scripts/unlazy_check.py`
- completed Spec Kit fixture under `examples/specs/001-capability-contract/`

## Trade-offs

Overly broad completion checklists become ritual. Gates should be risk- and scope-proportional, executable where possible, and tied to concrete acceptance criteria.

## Public/private boundary

The public terminal-state model is a reference for research and contribution. Private systems may impose stronger gates and project-specific golden-path evidence.