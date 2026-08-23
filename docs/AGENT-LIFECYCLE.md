# Governed Agent Lifecycle

Recommended states:

```text
RECEIVED → GOVERNANCE_LOADED → ROUTED → SPECIFIED → AUTHORIZED
   → EXECUTING → VALIDATING → REVIEWING → UNLAZY → CONVERGING
   → COMPLETE | BLOCKED | PARTIAL | NEEDS_CHANGES | CANCELLED
```

## Invariants

- A side-effecting action cannot occur before `AUTHORIZED`.
- Cancellation must stop new actions and reach an explicit terminal state.
- Retries are bounded and observable.
- A subagent inherits no capability merely because its parent has it; delegation scopes capability explicitly.
- `COMPLETE` requires mandatory evidence and convergence.
- Errors do not silently reset the lifecycle into an ungoverned retry.

Persist material state transitions when recovery, audit, or multi-agent coordination depends on them.