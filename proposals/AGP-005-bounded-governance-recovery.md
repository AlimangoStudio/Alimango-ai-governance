# AGP-005 — Bounded Governance Recovery

- **Status:** accepted-for-lab
- **Scope:** public reference proposal only
- **Authority:** advisory; no AGP status implies production or private adoption

## Problem

Governed agents can become operationally useless when a validator, tool contract, provenance check, or quality gate fails repeatedly. A naive escape hatch creates the opposite failure: a governance error becomes permission to continue unsafe side effects.

This proposal separates **availability of useful non-mutating output** from **authorization of protected actions**.

> Capability degradation is permitted. Governance degradation is not.

## Reference behavior

### 1. Distinguish failure classes

Deterministic policy denial, capability denial, and invalid governance input are non-retryable authorization outcomes. Approval-required is also non-retryable but is a distinct outcome that parks the protected action for human triage.

Transient validator/dependency/lock failures may retry within a bounded attempt budget. Internal governance/configuration/integrity failures remain fail-closed for protected actions.

Reference exit codes:

- `0`: validator/check passed; this alone does not authorize a protected side effect;
- `10`: policy denied;
- `11`: human approval required -> durable HITL, no retry/dispatch;
- `12`: capability not allowed;
- `13`: invalid governance input;
- `70,71,72,75`: transient infrastructure outcomes;
- `80+`: internal/configuration/integrity errors.

### 2. Bound quality correction

Quality-only rewrite/correction loops stop after three unsuccessful attempts. Only explicitly allowlisted quality gates (`unlazy`, `formatting`, `documentation`, `optimization`) may receive best-effort treatment. Unknown or misspelled gates default to **hard**.

The terminal quality result is `BEST_EFFORT_UNVERIFIED`:

- useful text/artifact output may continue;
- side effects remain unauthorized unless separately governed;
- the result cannot claim GREEN, validated completion, merge readiness, or deployment readiness.

The reference `unlazy_check.py` uses exit code `20` for this terminal condition so a raw shell/CI runner cannot mistake unverified continuation for successful validation. An orchestrator may handle that explicit code and continue non-mutating output.

Hard gates such as security, authorization, isolation, secrets, destructive actions, governance integrity, or required regulatory evidence never convert into best-effort approval.

### 3. Degrade capability, not governance

A development/reference implementation may fall back to reasoning, text output, local analysis, or already-authorized read-only work when mandatory governance infrastructure is unavailable after bounded retries.

The result must be visibly degraded and cannot dispatch the protected side effect. Passing an individual recovery/quality validator also does not itself grant dispatch authorization; protected side effects still require the separate action-governance decision.

There is no `bypass_warn` production pattern in this proposal.

### 4. Provenance-safe omission

Optional/advisory **public** context that fails provenance verification may be replaced by:

`[Data block omitted: Content failed safety verification]`

The compiler records omission evidence containing source identity, reason, inclusion=false, digest when safely available, and whether the source was mandatory or authorization-critical.

Mandatory authority/context still blocks compilation. Authorization-critical evidence is treated as budget-mandatory and cannot be silently dropped because the context budget is full. Public-hygiene violations such as a non-public source remain hard-blocking rather than being converted into an omission.

### 5. Durable human triage

Production-style recovery should park unresolved protected actions in durable triage rather than volatile local state.

Technology is implementation-specific: a database queue, Redis, RabbitMQ, Celery, cloud queue, workflow engine, or equivalent may satisfy the reference if it provides durable visibility and replay-safe resume.

Human approval does not directly execute a stale parked action. Resume should reload current state, validate identity/scope/policy/checkpoint/idempotency, rerun governance, and dispatch only after a current `allow` decision.

### 6. Evidence minimization

Recovery state must not become a credential or protected-data dumping surface. Prefer stable identifiers, digests, redaction, and minimum-necessary routing metadata.

## Public reference artifacts

- `control/recovery-policy.json` — machine-readable reference policy;
- `scripts/governance_recovery.py` — small stdlib-only recovery primitives;
- `scripts/compile_context.py` — optional provenance omission with mandatory authorization evidence;
- `scripts/unlazy_check.py` — bounded quality correction with distinct unverified exit status;
- `tests/test_governance_recovery.py` — executable positive/negative regression cases.

## Negative cases

A conforming reference should show that:

1. policy denial is never retried into success;
2. approval-required is distinct HITL and cannot retry or dispatch;
3. unknown/misspelled gates default hard;
4. degraded execution cannot dispatch a protected side effect;
5. an individual passing recovery check does not itself authorize a side effect;
6. quality correction stops after three attempts;
7. best-effort output cannot claim GREEN or return a normal validation-success signal;
8. hard gates remain blocking;
9. `bypass_warn` is rejected;
10. optional provenance failure emits the neutral placeholder plus evidence;
11. mandatory/authorization-critical provenance failure blocks;
12. authorization-critical evidence cannot be budget-dropped;
13. triage approval requires current-state revalidation and governance rerun;
14. recovery evidence avoids raw secrets/protected payloads.

## Public/private adoption boundary

`accepted-for-lab` means this design is retained as a useful public reference. It creates **no claim** that any private or production system uses the same implementation, schema, names, tools, or policy. External adopters should re-evaluate the failure mode and implement the smallest control appropriate to their own authority model.
