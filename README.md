<div align="center">

# 🥭 Alimango AI Governance Lab

### Public ideas → hard review → private adoption

[![Public Lab](https://img.shields.io/badge/status-public%20lab-0969da?style=for-the-badge)](https://github.com/AlimangoStudio/Alimango-ai-governance)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-2da44e?style=for-the-badge)](CONTRIBUTING.md)
[![Production Authority](https://img.shields.io/badge/production%20authority-NO-d1242f?style=for-the-badge)](docs/ADOPTION-BOUNDARY.md)
[![Fail Closed](https://img.shields.io/badge/design-fail--closed-8250df?style=for-the-badge)](docs/REVIEW-PLAYBOOK.md)

**An open R&D surface for making AI engineering governance harder to fool, easier to verify, and cheaper to operate.**

</div>

---

Alimango uses a hard two-repository model:

```text
                    OPEN SIDE

      issue ─ discussion ─ experiment ─ PR
                    │
                    ▼
          ┌─────────────────────┐
          │  THIS PUBLIC LAB    │
          │  ideas + evidence   │
          └──────────┬──────────┘
                     │
              useful?│
            ┌────────┴────────┐
            │                 │
          no│                 │yes
            ▼                 ▼
        close/reject     independent review
                              │
                              ▼
                    re-derive, don't mirror
                              │
                              ▼
                    ┌───────────────────┐
                    │ PRIVATE GOVERNANCE│
                    │ canonical control │
                    └─────────┬─────────┘
                              │ pinned + fail-closed
                              ▼
                         webapps/apps

                  PRODUCTION SIDE
```


How the PAPPS governing harness works

The governing harness is the control system around development. It does not replace coding; it controls how work is planned, implemented, reviewed, tested, and declared complete.

Constitution — the highest authority
The Constitution defines the non-negotiable engineering rules: protect golden paths, preserve tenant isolation, fail closed, avoid destructive shortcuts, validate real behavior, keep deployment safe, and never call work “done” without evidence. Specs, agents, and implementation decisions must conform to it.
Spec Kit — defines exactly what is being built
Before a meaningful behavior change, the work gets a numbered spec with the required artifacts such as spec.md, plan.md, tasks.md, research/decisions where needed, and gate evidence. It establishes scope, acceptance criteria, blast radius, risks, migration/deployment requirements, and tests. This prevents an agent from improvising a solution without a contract.

Governing harness — controls execution
The .agents/ system routes the task, loads only the relevant context, applies engineering/security/performance policies, and determines the required Done-When gates. The normal flow is roughly:

Task → context → Spec Kit → blast-radius analysis → implementation → tests → security/tenancy/performance checks → browser/E2E where applicable → audit/review → convergence → Unlazy → commit/merge → safe deployment → live verification.

Different risk levels automatically require stronger evidence. Finance, clinical data, authentication, tenancy, integrations, migrations, and production infrastructure receive stricter treatment.

Audit/reviewer layer — challenges the implementation
The implementation is not trusted merely because the coding agent says it works. The audit system checks requirements, correctness, regressions, tenant isolation, security boundaries, financial/data integrity, concurrency, migrations, integrations, UI, and deployment. High-risk work ideally receives genuinely independent reviewer contexts.
Unlazy — the final anti-shortcut gate
Unlazy asks, effectively: “Is this actually finished, or did we stop when the code looked plausible?” It looks for unchecked tasks, TODOs, skipped validation, placeholder implementations, untested failure paths, missing browser/live proof, undocumented assumptions, stale evidence, and incomplete handoffs. A feature can compile and have passing unit tests and still fail Unlazy.
Convergence — reconcile everything before completion
Findings from implementation, tests, audits, browser QA, security review, and Unlazy are reconciled back against the spec. Open issues must either be fixed or explicitly recorded as remaining gates. The harness prevents contradictory states such as tasks.md saying complete while GATES.md still contains a blocker.

See [`docs/ADOPTION-BOUNDARY.md`](docs/ADOPTION-BOUNDARY.md) for the hard boundary.

## How to contribute

**Early idea?** Start a Discussion.  
**Concrete problem?** Open a Governance Improvement issue.  
**Reviewable solution or experiment?** Open a focused PR.

Before contributing, read:

- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution and review standard
- [`SECURITY.md`](SECURITY.md) — vulnerability and sensitive-data rules
- [`docs/REVIEW-PLAYBOOK.md`](docs/REVIEW-PLAYBOOK.md) — how proposals are evaluated
- [`proposals/PROPOSAL-TEMPLATE.md`](proposals/PROPOSAL-TEMPLATE.md) — proposal structure
- [`docs/WHY-TWO-REPOS.md`](docs/WHY-TWO-REPOS.md) — architecture rationale

## Repository map

```text
.github/       contribution templates + hygiene checks
proposals/     versioned governance proposals
examples/      synthetic, public-safe experiments
docs/          trust boundary + review model + contributor guides
```

## For maintainers

The default posture is simple:

```text
interesting ≠ correct
merged here ≠ adopted privately
public evidence ≠ production authority
available tool ≠ authorized action
```

Keep the lab open. Keep the production trust boundary hard.

---

<div align="center">

### Build governance that can survive skeptical review.

**Open ideas. Explicit evidence. Private authority.**

</div>
