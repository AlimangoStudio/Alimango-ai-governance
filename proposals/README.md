# Alimango Governance Proposals (AGPs)

AGPs are stable, reviewable public design records for substantive agent-control ideas. They make the lab useful as a technical reference without turning public proposals into production authority.

## Current reference proposals

| AGP | Status | Control family |
| --- | --- | --- |
| [AGP-001](AGP-001-capability-gated-tool-execution.md) | accepted-for-lab | capability / action governance |
| [AGP-002](AGP-002-authority-aware-context-compilation.md) | accepted-for-lab | context / RAG / CAG |
| [AGP-003](AGP-003-evidence-gated-completion.md) | accepted-for-lab | evidence / Unlazy / convergence |
| [AGP-004](AGP-004-verified-evidence-memory-supply-design.md) | accepted-for-lab | evidence coverage / memory / skill supply / frontend design contract |

## Process

Recommended naming: `AGP-001-short-title.md`.

Statuses: `draft`, `experiment`, `accepted-for-lab`, `rejected`, `superseded`.

Use `PROPOSAL-TEMPLATE.md` for new proposals. Substantive proposals should identify the failure mode, threat/bypass analysis, smallest enforceable control, capability/context impact, evidence plan, cost, alternatives, and public/private adoption boundary.

**No AGP status means private, internal, or production adoption.** A public merge is acceptance into this lab only. Any external adoption is a separate decision with its own authority, implementation, testing, and evidence.
