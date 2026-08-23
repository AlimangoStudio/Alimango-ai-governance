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

## The one rule that matters

> **Nothing in this repository is Alimango production governance.**
>
> PAPPS and other Alimango projects must never consume this repository as authoritative policy, runtime governance, or an automatic update source.

This repo is where ideas get challenged in public. The private Alimango governance repository is where selected ideas are independently re-derived, tested, audited, versioned, and—only then—made authoritative.

## Why this exists

AI-agent governance improves faster when people can challenge assumptions, show failure cases, compare approaches, and submit experiments without getting a write path into production policy.

So Alimango uses a hard two-repository model:

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
                     PAPPS / future apps

                  PRODUCTION SIDE
```

A public PR being merged means **“this is useful enough to keep exploring.”** It does **not** mean **“Alimango adopted this.”**

## What we want to explore

| Track | Good contributions |
| --- | --- |
| **Agent action governance** | capability boundaries, approvals, destructive-action controls, typed tool contracts |
| **Spec-driven engineering** | stronger requirements, planning checks, task decomposition, convergence gates |
| **Evidence & validation** | Done-When/Proof, regression proof, independent review, audit kernels |
| **Context engineering** | bounded retrieval, RAG/CAG, freshness, provenance, cache invalidation |
| **Security** | secrets, SSRF, tenant/workspace isolation, prompt/tool injection defenses |
| **Reliability** | cancellation, terminal states, bounded retries, fail-closed behavior |
| **Performance** | low-compute patterns, context/token budgets, efficient validation |
| **Developer experience** | deterministic bootstrap, multi-agent compatibility, upgrade manifests |

## The quality bar

The best contributions do more than say *“agents should be careful.”* They make the safe behavior easier to enforce.

We prefer:

```text
executable test
    > validator / static gate
        > schema / typed contract
            > safer service boundary
                > reusable workflow
                    > prose-only warning
```

A strong proposal normally includes:

- a concrete failure mode,
- the smallest control that removes it,
- evidence or a reproducible example,
- security and side-effect analysis,
- context/compute/maintenance cost,
- known limitations and trade-offs.

## What gets rejected quickly

We are comfortable closing PRs that are:

- weaker than an existing pattern,
- unsafe or fail-open,
- unverifiable,
- generated bulk noise,
- secretly permission-expanding,
- a large framework looking for a problem,
- dependent on trusting public content at runtime,
- unrelated to engineering/agent governance.

**Good ideas survive review. Bad ideas do not need backwards compatibility.**

## Trust boundary

This repository must never contain:

- Alimango private source code,
- production credentials or tokens,
- private keys or environment files,
- customer/patient/tenant data,
- proprietary project internals,
- a workflow that automatically promotes public changes into private governance.

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
