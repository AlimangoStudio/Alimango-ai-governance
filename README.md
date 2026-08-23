<div align="center">

# 🥭 Alimango AI Governance Lab

### Open reference control plane for governed AI-agent engineering

[![Public Lab](https://img.shields.io/badge/status-public%20R%26D-0969da?style=for-the-badge)](docs/ADOPTION-BOUNDARY.md)
[![Agent Controls](https://img.shields.io/badge/agent%20controls-spec%20%7C%20capability%20%7C%20evidence-8250df?style=for-the-badge)](.agents/README.md)
[![CI](https://img.shields.io/github/actions/workflow/status/AlimangoStudio/Alimango-ai-governance/public-hygiene.yml?branch=main&style=for-the-badge&label=governance%20CI)](.github/workflows/public-hygiene.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-2da44e?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-1f883d?style=for-the-badge)](CONTRIBUTING.md)

**Spec-driven engineering · fail-closed actions · capability control · bounded context · evidence gates · adversarial review · Unlazy · convergence**

This repository publishes a complete, public-safe reference implementation of the control ideas used to govern AI coding and engineering agents.

</div>

---

> [!IMPORTANT]
> **This repository is not Alimango production governance.** It is a public research, reference, and contribution surface. Production Alimango projects do not consume it as authority or as a runtime fallback. Useful ideas are independently re-derived and validated in the private governance system before any production adoption.

## Why this exists

AI agents are useful precisely because they can act. That also means quality cannot depend on a model remembering a long prompt or sounding confident. The control plane needs explicit authority, permissions, context provenance, executable evidence, independent challenge, and terminal-state discipline.

This lab makes those controls inspectable and improvable in public.

## Control plane

```mermaid
flowchart TD
    A[Task / Request] --> B[Authority Resolution]
    B --> C[Task Router + Risk Classification]
    C --> D[Spec Kit Contract]
    D --> E[Capability Decision]
    E --> F[Bounded Context Compile]
    F --> G[Agent Execution]
    G --> H[Validation + Evidence]
    H --> I[Independent Review]
    I --> J[Unlazy]
    J --> K[Convergence]
    K --> L{Terminal State}
    L -->|all gates pass| M[Complete]
    L -->|required gate open| N[Blocked / Partial / Needs Changes]
```

The model is intentionally **not** the policy engine. Models propose actions. Governance decides whether those actions are authorized and whether the evidence is sufficient.

## What is included

| Control family | Reference implementation |
| --- | --- |
| **Constitution / authority** | `.specify/memory/constitution.md`, `AGENTS.md`, `GOVERNANCE.md` |
| **Spec Kit** | `.specify/templates/`, `.agents/workflows/spec-kit.md` |
| **Task routing** | `.agents/skills/task-router/` |
| **Action governance** | capability classes, risk levels, allow/approval/deny decisions |
| **Tool contracts** | machine-readable schemas for scope, side effects, auth, pre/postconditions |
| **Context governance** | authority-aware RAG/CAG concepts, provenance, freshness, sensitivity, budgets |
| **Supply-chain controls** | source/ref/license/install/network/permission review |
| **Done-When / Proof** | acceptance gates defined before implementation |
| **Independent review** | read-only adversarial challenge with structured verdicts |
| **Unlazy** | final anti-shortcut completion gate |
| **Convergence** | reconciliation of spec, tasks, gates, evidence, review, and reality |
| **Lifecycle / cancellation** | explicit states and terminal outcomes |
| **Telemetry** | structured action, evidence, timing, and terminal-state events |
| **Testing / performance / UI** | reusable quality policies with risk-proportional evidence |

## Repository architecture

```text
AGENTS.md                     repo-local agent entry point
GOVERNANCE.md                 public-lab authority boundary
.specify/
  memory/constitution.md      highest repo-local authority
  templates/                  Spec Kit contracts
.agents/
  manifest.json               machine-readable control registry
  policies/                   standing constraints
  workflows/                  execution state machines
  skills/                     reusable agent methods
schemas/                      typed control/evidence contracts
examples/                     synthetic public-safe examples
docs/                         architecture, threats, controls, review model
scripts/                      deterministic validators
proposals/                    community governance proposals
.github/                      contribution templates + CI
```

## The operating model

```text
public idea / issue / PR
        │
        ▼
public experiment + skeptical review
        │
        ├── weak / unsafe / redundant ──► reject or close
        │
        └── useful ──► retain as public reference
                           │
                           ▼
                  independent private re-derivation
                           │
                           ▼
                  private tests + audit + versioning
                           │
                           ▼
                    possible production adoption
```

A merge here means **useful enough to retain publicly**. It does not mean adopted as Alimango production governance.

## Design principles

We prefer controls that are difficult to hand-wave around:

```text
executable proof
  > deterministic validator
    > typed contract / schema
      > capability boundary
        > reviewable workflow
          > prose reminder
```

Strong contributions usually identify a concrete failure mode, propose the smallest enforceable control, include negative-path evidence, state capability/context costs, and document bypasses or limitations.

## Quick start

Read [`AGENTS.md`](AGENTS.md) to understand how agents are governed in this repo, then [`docs/AGENT-CONTROL-PLANE.md`](docs/AGENT-CONTROL-PLANE.md) for the architecture. For a concrete change, use the Spec Kit templates under [`.specify/templates/`](.specify/templates/) and follow [`CONTRIBUTING.md`](CONTRIBUTING.md).

Useful starting points:

- [`docs/SPEC-KIT.md`](docs/SPEC-KIT.md)
- [`docs/UNLAZY.md`](docs/UNLAZY.md)
- [`docs/THREAT-MODEL.md`](docs/THREAT-MODEL.md)
- [`docs/CONTROL-MATRIX.md`](docs/CONTROL-MATRIX.md)
- [`docs/TOOL-CONTRACTS.md`](docs/TOOL-CONTRACTS.md)
- [`docs/CONTEXT-ENGINEERING.md`](docs/CONTEXT-ENGINEERING.md)
- [`docs/INDEPENDENT-REVIEW.md`](docs/INDEPENDENT-REVIEW.md)
- [`docs/FAILURE-MODE-CATALOG.md`](docs/FAILURE-MODE-CATALOG.md)

## What we want contributions on

Agent permissions and approvals; prompt/tool injection defenses; context selection and cache invalidation; code-graph/RAG/CAG controls; deterministic validators; agent lifecycle/cancellation; independent reviewer methods; supply-chain verification; provenance; typed tool interfaces; test/evidence quality; token/latency budgets; and new reproducible failure cases.

## Contribution boundary

Never submit credentials, keys, private Alimango code, customer/tenant/patient data, proprietary project internals, or a mechanism that automatically promotes public content into private production governance. See [`docs/ADOPTION-BOUNDARY.md`](docs/ADOPTION-BOUNDARY.md) and [`SECURITY.md`](SECURITY.md).

---

<div align="center">

### Build agent governance that survives skeptical review.

**Open controls. Explicit evidence. Private production authority.**

</div>
