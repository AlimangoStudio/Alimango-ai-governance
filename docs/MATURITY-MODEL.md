# Governance Control Maturity Model

This model helps reviewers compare proposals without pretending all controls are equally strong.

| Level | Name | Characteristics |
| --- | --- | --- |
| **L0** | Unspecified | Behavior depends on agent judgment or undocumented convention. |
| **L1** | Documented | Rule exists in prose, but enforcement is manual or optional. |
| **L2** | Observable | Violations produce logs, warnings, or audit findings. |
| **L3** | Enforced | A deterministic gate blocks known-invalid behavior. |
| **L4** | Fail-closed | Missing/invalid authority, policy, identity, or evidence blocks sensitive execution. |
| **L5** | Adversarially verified | Enforcement has bypass tests, independent review, and regression evidence. |

## Evaluation dimensions

A control's maturity should be evaluated separately across:

- authority integrity,
- capability scope,
- tenant/data isolation,
- approval integrity,
- side-effect safety,
- context provenance,
- reproducibility,
- observability,
- rollback/containment,
- performance/cost.

A control should not be called L5 merely because one dimension is well tested.

## Example

A rule saying "do not force push" is L1. A wrapper that rejects force pushes is L3. A wrapper that also blocks execution when policy cannot be loaded, emits an audit record, and has bypass/regression tests can reach L4-L5 depending on evidence.
