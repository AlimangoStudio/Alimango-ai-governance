<div align="center">

# 🥭 Alimango AI Governance Lab

### Public research, reference patterns, experiments, and contribution intake for governed AI-agent engineering

[![Reference](https://img.shields.io/badge/reference-v1.0-111827?style=for-the-badge)](VERSION)
[![Public Goods](https://img.shields.io/badge/scope-public%20goods-0969da?style=for-the-badge)](docs/PUBLIC-SCOPE.md)
[![CI](https://img.shields.io/github/actions/workflow/status/AlimangoStudio/Alimango-ai-governance/public-hygiene.yml?branch=main&style=for-the-badge&label=public%20CI)](.github/workflows/public-hygiene.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-2da44e?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-1f883d?style=for-the-badge)](CONTRIBUTING.md)

**Spec-driven engineering · capability control · bounded context · evidence gates · adversarial review · Unlazy · convergence**

</div>

---

> [!CAUTION]
> **This repository is not Alimango's governance authority and must not be consumed as governance by any Alimango product or internal project.** It is a public idea, research, experiment, and contribution-intake surface. A public merge, release, proposal status, or passing CI run does **not** mean an idea has been adopted internally. Internal adoption, if any, is separately re-derived, reviewed, tested, and governed outside this public repository.

> [!IMPORTANT]
> Everything here must remain public-safe and self-contained. Do not submit credentials, personal/customer data, confidential source, proprietary implementation details, non-public endpoints, private repository names, deployment details, customers, or organizational topology.

## Why this exists

AI-agent control ideas improve when failure modes, schemas, fixtures, and experiments can be challenged in public. This lab provides a place to publish and test those ideas without making the public repository an operational dependency or source of authority.

The intended flow is:

```text
public idea / failure case / experiment
                ↓
          public review + CI
                ↓
       accepted-for-lab reference
                ↓
      optional independent adoption
      outside this public repository
```

There is intentionally **no automatic promotion path** from public `main` into any private or production governance system.

## What is included

| Area | Public reference material |
| --- | --- |
| Capability/action control | typed action/tool schemas, approval/deny patterns, synthetic fixtures |
| Context governance | authority-aware RAG/CAG patterns, provenance, freshness, bounded-context experiments |
| Evidence/completion | Done-When, Unlazy, convergence, review/evidence patterns |
| Security | prompt injection, SSRF, secrets, isolation, least-capability reference controls |
| Agent methods | public-safe skills/workflows for studying governance behavior inside this lab |
| Proposals | stable AGP design records intended for challenge and improvement |
| Experiments/benchmarks | reproducible public-safe ways to measure governance cost and effectiveness |

The `.agents/`, `.specify/`, `control/`, `harness/`, `schemas/`, `scripts/`, and `tests/` trees govern or exercise **this public lab itself**. Their presence does not make this repository an authority for another repository.

## Current proposals

| Proposal | Focus |
| --- | --- |
| [`AGP-001`](proposals/AGP-001-capability-gated-tool-execution.md) | capability-gated tool execution |
| [`AGP-002`](proposals/AGP-002-authority-aware-context-compilation.md) | authority-aware context compilation |
| [`AGP-003`](proposals/AGP-003-evidence-gated-completion.md) | evidence-gated completion |
| [`AGP-004`](proposals/AGP-004-verified-evidence-memory-supply-design.md) | structural evidence coverage, verified memory, skill supply chain, and design contracts |

`accepted-for-lab` means only that a proposal is useful enough to keep as a public reference. It never means production or private adoption.

## Run the public lab harness

Core checks require Python 3.11+.

```bash
python scripts/validate_public_lab.py
python scripts/validate_agent_controls.py
python scripts/capability_doctor.py --require python --require AGENTS.md
python scripts/spec_check.py examples/specs/001-capability-contract
python scripts/unlazy_check.py examples/specs/001-capability-contract
python scripts/compile_context.py --request examples/context-request.json
python -m unittest discover -s tests -p 'test_*.py' -v
```

Or:

```bash
make validate
make test
make fingerprint
```

Passing these commands proves only the state of this public lab revision.

## Contribution lifecycle

```text
idea / failure case
      ↓
issue / AGP / experiment
      ↓
small enforceable reference control
      ↓
positive + negative evidence
      ↓
independent challenge
      ↓
public CI
      ↓
merge / reject / supersede
```

Useful public work may later inspire a separately governed implementation elsewhere. Contributors should not assume or claim that this happened.

## Technical references

- [`docs/PUBLIC-SCOPE.md`](docs/PUBLIC-SCOPE.md)
- [`docs/SPEC-KIT.md`](docs/SPEC-KIT.md)
- [`docs/UNLAZY.md`](docs/UNLAZY.md)
- [`docs/THREAT-MODEL.md`](docs/THREAT-MODEL.md)
- [`docs/CONTROL-MATRIX.md`](docs/CONTROL-MATRIX.md)
- [`docs/TOOL-CONTRACTS.md`](docs/TOOL-CONTRACTS.md)
- [`docs/CONTEXT-ENGINEERING.md`](docs/CONTEXT-ENGINEERING.md)
- [`docs/INDEPENDENT-REVIEW.md`](docs/INDEPENDENT-REVIEW.md)
- [`docs/MCP-AND-CONNECTORS.md`](docs/MCP-AND-CONNECTORS.md)
- [`docs/FAILURE-MODE-CATALOG.md`](docs/FAILURE-MODE-CATALOG.md)
- [`CONTRIBUTING.md`](CONTRIBUTING.md)

---

<div align="center">

### Open ideas. Explicit evidence. No authority confusion.

</div>
