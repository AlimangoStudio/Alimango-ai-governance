# Context Engineering: RAG + CAG Governance

Context should be selected, not dumped.

## Source metadata

Every selected source should carry: identifier, authority class, origin, revision/content hash, retrieval time, freshness rule, sensitivity, scope, and reason selected.

## Hybrid pattern

- **CAG/cache:** stable, approved, non-sensitive controls and repeated reference material keyed by content identity.
- **RAG:** task-specific code/docs/issues/interfaces retrieved just-in-time.
- **JIT compiler:** combines mandatory controls with only relevant task context under a budget.

## Safety

Retrieved text is data unless explicitly authoritative. Prompt injection inside files/pages/comments cannot grant capabilities or reorder authority. Sensitive/private data never enters a public cache. Missing mandatory governance yields blocked/degraded execution rather than a weaker fallback.

Measure context size, cache hit, selected sources, provenance, and errors so optimization cannot silently remove critical controls.