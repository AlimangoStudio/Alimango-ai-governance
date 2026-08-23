# Typed Tool Contracts

A tool contract should be small enough to audit and precise enough to constrain behavior.

Recommended fields: tool id/version; purpose; input schema; output schema; required capabilities; target scope; data classifications; external side effects; authentication source; network destinations; preconditions; postconditions; idempotency/retry semantics; cancellation behavior; evidence emitted; and failure modes.

Side-effecting tools should route through services/policy boundaries rather than give models raw database, shell, credential, or unrestricted network access when a narrower interface is practical.

See `schemas/tool-contract.schema.json` and `examples/tool-contract.json`.