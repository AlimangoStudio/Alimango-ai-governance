# AGP-001: Capability-Gated Tool Execution

**Status:** accepted-for-reference  
**Control family:** capability / action governance

## Failure mode

Agent runtimes commonly expose tools before a task is fully resolved. A model can therefore mistake **availability** for **authorization**: because a shell, repository write, network, deployment, or credential tool exists, the model assumes it may use it.

This failure is amplified when tool descriptions are broad, retrieved content contains instructions, or a task evolves during execution.

## Control

Separate tool exposure from action authorization.

Every material side effect is classified by:

- action and exact target,
- risk level (`R0`–`R4`),
- required capability classes,
- provenance of target/arguments,
- reversibility and data scope,
- approval requirement,
- postcondition evidence.

The policy result is one of:

`allow` · `allow_with_evidence` · `require_approval` · `deny`.

A tool call may execute only after the corresponding decision permits the exact action and target. Approval for one target does not authorize adjacent targets or future retries with changed scope.

## Why capability classes

Capabilities make permission expansion visible. Reading a repository is not the same capability as writing it; network read is not external write; secret access is not ordinary context; deployment, migration, financial, identity, and destructive operations are separate high-impact classes.

This lets a task router, policy engine, reviewer, and audit trail reason about the same vocabulary.

## Bypass analysis

The control fails if:

- a tool has hidden side effects not declared in its contract;
- an agent can invoke an unrestricted lower-level tool around the governed service;
- approval is represented as ambiguous prose instead of a scoped record;
- a retry changes target/scope but reuses an old decision;
- retrieved text is allowed to mutate the capability policy.

Mitigations include narrow service-mediated tools, typed contracts, immutable decision records, per-action target checks, and authority separation.

## Evidence

The reference includes:

- `control/action-policy.json`
- `schemas/action-decision.schema.json`
- `schemas/tool-contract.schema.json`
- `scripts/evaluate_action.py`
- `examples/action-decision.json`
- negative tests for R4 approval and unauthorized external writes

## Cost / trade-offs

Capability checks add implementation and logging overhead. Overly coarse classes create false blocks; overly granular classes make policy difficult to maintain. The reference therefore keeps a small set of impact-oriented classes and allows tools to add narrower target constraints.

## Portability

This AGP defines a control pattern, not a specific deployment architecture. Adopters may use different enforcement mechanisms as long as tool availability remains separate from authorization and the resulting decisions are scoped, reviewable, and evidenced.
