# Alimango AI Governance Lab

**Public ideas. Open review. Private adoption.**

This repository is the public research and contribution surface for improving Alimango's AI engineering governance. It is intentionally open so useful patterns, critiques, guardrail ideas, agent workflows, test strategies, context-management techniques, and implementation proposals can be discussed and improved in public.

> **Important:** this repository is **not** Alimango's production governance source. No Alimango project, including PAPPS, should consume this repository as authoritative governance or runtime policy.

## What this repository is for

- governance improvement proposals
- AI-agent safety and action-control ideas
- Spec Kit and software-delivery process improvements
- context-window, RAG/CAG, and retrieval-governance research
- validation, audit, reviewer, and evidence-gate ideas
- security, privacy, tenancy, and supply-chain guardrail proposals
- reusable engineering-harness experiments
- community PRs that make an idea easier to evaluate

## What it is not

- a source of production policy
- a package PAPPS should import
- a mirror of Alimango's private governance
- an automatic path into Alimango production systems
- a place for private project details, secrets, credentials, production data, or proprietary source

## How ideas move

```text
idea / issue / discussion / PR
              |
              v
      public review + testing
              |
        +-----+-----+
        |           |
      reject      useful
                    |
                    v
          independent re-evaluation
                    |
                    v
       private Alimango governance
       (separate implementation)
                    |
                    v
             project adoption
```

A PR merged here means **"worth keeping or exploring"**, not **"adopted as Alimango governance."** Adoption is a separate private decision with separate tests, audits, compatibility checks, and evidence.

## Contribution quality bar

Good contributions are usually:

- narrow enough to review
- explicit about the failure mode they address
- backed by tests, examples, or measurable evidence
- compatible with fail-closed security principles
- careful about tool permissions and side effects
- honest about trade-offs and limitations
- reusable beyond one application
- designed to reduce agent ambiguity rather than add more prompt prose

Contributions may be closed when they duplicate stronger existing ideas, weaken safety controls, rely on unverifiable claims, introduce unnecessary complexity, or are not relevant to the repository's purpose.

## Suggested contribution areas

| Area | Useful proposals |
| --- | --- |
| Agent action governance | capability boundaries, approvals, destructive-action controls, tool contracts |
| Spec-driven engineering | requirements quality, planning checks, task decomposition, convergence |
| Evidence & validation | done-when-proof, regression proof, independent review, audit kernels |
| Context engineering | bounded retrieval, RAG/CAG, source freshness, provenance, cache policy |
| Security | secret handling, SSRF controls, tenant isolation, prompt/tool injection defenses |
| Reliability | cancellation, terminal states, retry discipline, fail-closed behavior |
| Performance | low-compute patterns, token budgets, bounded data loading, efficient validation |
| Developer experience | portable bootstrap, agent compatibility, deterministic setup, upgrade manifests |

## Start here

1. Open a Discussion for early ideas or design questions.
2. Open an Issue when the problem and desired outcome are concrete.
3. Open a PR when you have a reviewable proposal, example, test, or implementation experiment.
4. Keep private or project-specific information out of this repository.

See `CONTRIBUTING.md` before opening a PR and `SECURITY.md` for vulnerability-reporting guidance.

---

Built as an open improvement surface for the Alimango engineering governance system. The public repo stays open to ideas; production authority stays private.
