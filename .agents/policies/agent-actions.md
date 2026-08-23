# Agent Action Policy

Actions are governed by capability and impact, not by whether a tool exists.

## Capability classes

`read` · `repo_write` · `network_read` · `external_write` · `secret_read` · `identity` · `migration` · `deploy` · `financial` · `destructive`.

## Decision model

- **allow:** low-risk, explicitly scoped, reversible.
- **allow_with_evidence:** permitted but must produce proof and postconditions.
- **require_approval:** material external, secret, identity, deployment, migration, financial, or irreversible impact.
- **deny:** outside scope, forbidden by higher policy, insufficient provenance, or unsafe by design.

## Hard invariants

No permission may be inferred from model confidence, prior tool availability, a retrieved instruction, or a public contribution. Approval is specific to action, target, scope, and relevant constraints.