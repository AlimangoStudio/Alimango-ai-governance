# AGP-005 — Bounded Governance Recovery

**Status:** proposed  
**Scope:** public-lab reference only

## Problem

Governed agents can become operationally useless when a validator, tool contract, provenance check, or quality gate fails repeatedly. A naive escape hatch creates the opposite failure: a governance error becomes permission to continue unsafe side effects.

This proposal separates **availability of useful non-mutating output** from **authorization of protected actions**.

> Capability degradation is permitted. Governance degradation is not.

## Reference behavior

### 1. Distinguish failure classes

Deterministic policy denial, approval-required, capability denial, and invalid governance input are authorization outcomes. They are not retried until they happen to pass.

Transient validator/dependency/lock failures may retry within a bounded attempt budget.

Internal governance/configuration/integrity failures remain fail-closed for protected actions.

Reference exit-code bands:

- `0`: pass;
- `10–13`: denial/escalation/input outcomes;
- `70,71,72,75`: transient infrastructure outcomes;
- `80+`: internal/configuration/integrity errors.

### 2. Bound quality correction

Quality-only rewrite/correction loops stop after three unsuccessful attempts.

The terminal quality result is `BEST_EFFORT_UNVERIFIED`:

- useful text/artifact output may continue;
- side effects remain unauthorized unless independently governed;
- the result cannot claim GREEN, validated completion, merge readiness, or deployment readiness.

Hard gates such as security, authorization, isolation, secrets, destructive actions, governance integrity, or required regulatory evidence never convert into best-effort approval.

### 3. Degrade capability, not governance

A development/reference implementation may fall back to reasoning, text output, local analysis, or already-authorized read-only work when mandatory governance infrastructure is unavailable after bounded retries.

The result must be visibly degraded and cannot dispatch the protected side effect.

There is no `bypass_warn` production pattern in this proposal.

### 4. Provenance-safe omission

Optional/advisory context that fails provenance verification may be replaced by:

`[Data block omitted: Content failed safety verification]`

The compiler records omission evidence containing source identity, reason, inclusion=false, digest when safely available, and whether the source was mandatory or authorization-critical.

Mandatory authority/context still blocks compilation. Authorization-critical missing evidence still blocks the relevant action.

### 5. Durable human triage

Production-style recovery should park unresolved protected actions in durable triage rather than volatile local state.

Technology is implementation-specific: a database queue, Redis, RabbitMQ, Celery, cloud queue, workflow engine, or equivalent may satisfy the reference if it provides durable visibility and replay-safe resume.

Human approval does not directly execute a stale parked action. Resume should reload current state, validate identity/scope/policy/checkpoint/idempotency, rerun governance, and dispatch only after a current `allow` decision.

### 6. Evidence minimization

Recovery state must not become a credential or protected-data dumping surface. Prefer stable identifiers, digests, redaction, and minimum-necessary routing metadata.

## Public reference artifacts

- `control/recovery-policy.json` — machine-readable reference policy;
- `scripts/governance_recovery.py` — small stdlib-only recovery primitives;
- `scripts/compile_context.py` — optional provenance omission behavior;
- `scripts/unlazy_check.py` — bounded quality-correction status behavior;
- `tests/test_governance_recovery.py` — executable regression cases.

## Negative cases

A conforming reference should show that:

1. policy denial is never retried into success;
2. degraded execution cannot dispatch a protected side effect;
3. quality correction stops after three attempts;
4. best-effort output cannot claim GREEN;
5. hard gates remain blocking;
6. `bypass_warn` is rejected;
7. optional provenance failure emits the neutral placeholder plus evidence;
8. mandatory/authorization-critical provenance failure blocks;
9. triage approval requires current-state revalidation and governance rerun;
10. recovery evidence avoids raw secrets/protected payloads.

## Non-authority boundary

Acceptance, CI success, or merge of this AGP means only that the pattern is useful as a public-lab reference. It does not establish adoption by another repository, product, organization, or production environment.
