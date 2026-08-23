# Action Governance Workflow

Before a side effect:

1. Identify action, target, data scope, and reversibility.
2. Resolve required capability classes.
3. Check higher-authority prohibitions.
4. Check provenance of arguments and targets.
5. Classify risk R0–R4.
6. Produce `allow`, `allow_with_evidence`, `require_approval`, or `deny`.
7. If permitted, execute only the approved scope.
8. Verify postconditions and record evidence.

Approval for one action does not authorize adjacent actions. A tool call that changes external state should be service/policy mediated when practical.