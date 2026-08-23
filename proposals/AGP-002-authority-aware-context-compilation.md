# AGP-002: Authority-Aware Bounded Context Compilation

**Status:** accepted-for-reference  
**Control family:** context / RAG / CAG / prompt-injection defense

## Failure mode

Large agent contexts often mix constitutions, project policy, code, tickets, web pages, logs, and model-generated summaries into one undifferentiated prompt. This creates three problems:

1. advisory material can appear as authoritative as policy;
2. stale or poisoned retrieved text can steer execution;
3. whole-repository loading increases token cost and dilutes load-bearing controls.

## Control

Compile context as a governed artifact rather than concatenate text blindly.

Each source carries:

- source id and origin,
- authority class,
- content identity/hash,
- freshness metadata,
- sensitivity class,
- selection reason,
- estimated context cost.

Mandatory authority is selected first. Task-specific retrieval is then added under a budget. Advisory or retrieved sources remain lower authority even when their content contains imperative language.

Stable public-safe controls may be cache-augmented by content hash. Sensitive inputs require an appropriate protected-data policy and must not be placed in public fixtures, caches, logs, or examples.

## Fail-closed behavior

Compilation blocks when mandatory authority is missing, required authority exceeds the declared budget, a source escapes its allowed root, or the public reference compiler is asked to compile a non-public source.

There is no fallback that silently drops the constitution to make the prompt fit.

## Prompt-injection property

The compiler does not need to prove that retrieved text is benign. Instead, it preserves the source's external/advisory authority label. A hostile document can be included for analysis without acquiring permission to reorder policy or grant tools.

## Evidence

Reference surfaces:

- `control/source-authority.json`
- `control/context-compiler.json`
- `schemas/context-manifest.schema.json`
- `scripts/compile_context.py`
- `examples/context-request.json`
- `tests/fixtures/prompt-injection.md`
- unit tests that preserve constitution-first ordering and reject restricted input

## Metrics

Useful measurements include selected/omitted sources, estimated tokens, authority coverage, cache hit rate, compile errors, stale-source rate, and task success/regression rate.

## Portability

The compiler is a reference mechanism. Adopters may implement retrieval and caching differently, but should preserve explicit authority, provenance, sensitivity, freshness, bounded context, and fail-closed handling of mandatory sources.
