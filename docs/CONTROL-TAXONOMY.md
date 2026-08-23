# Governance Control Taxonomy

This taxonomy gives contributors a shared technical vocabulary for classifying proposals.

## Control classes

| Class | Purpose | Typical mechanism |
| --- | --- | --- |
| **Authority** | Decide which instruction/source may govern | signed/pinned refs, precedence rules, source identity |
| **Capability** | Limit what an agent can do | allowlists, scoped tools, per-turn capability assembly |
| **Approval** | Require human authorization for material actions | approve/edit/reject gates, step-up confirmation |
| **Boundary** | Protect data, tenancy, network, and trust zones | tenant filters, SSRF guards, secret isolation |
| **Context** | Govern what enters model context | bounded retrieval, provenance, freshness, compaction |
| **Action** | Govern side effects | service-mediated tools, idempotency, transactional checks |
| **Evidence** | Prove claims and completion | executable tests, manifests, hashes, audit records |
| **Review** | Independently challenge implementation | read-only reviewer lanes, adversarial test cases |
| **Lifecycle** | Control task/run state | cancellation, terminal events, retries, budgets |
| **Observability** | Make behavior inspectable | structured traces, tool-call telemetry, cost/latency data |
| **Supply chain** | Reduce dependency and contribution risk | provenance, pinning, license review, integrity checks |

## Enforcement strength

Controls should identify their enforcement level:

1. **Informational** — guidance only.
2. **Detective** — reports violations after/during execution.
3. **Preventive** — blocks a forbidden action.
4. **Fail-closed preventive** — blocks execution when required evidence/control is unavailable.

Proposals that claim to be preventive should include a bypass test.

## Scope dimensions

Every proposal should state whether it affects:

- one tool or all tools,
- one agent role or all roles,
- one turn, session, project, or organization,
- read-only or side-effecting behavior,
- public, private, tenant, or regulated data,
- local, CI, staging, or production environments.

## Preferred pattern

A good control has a clear chain:

```text
threat / failure mode
        ↓
control objective
        ↓
enforcement point
        ↓
evidence artifact
        ↓
bypass / regression test
```

If a proposal cannot identify an enforcement point, it is probably policy prose rather than a technical control.
