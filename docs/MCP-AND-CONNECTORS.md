# MCP, Connectors, and External Tool Servers

A connector or MCP server expands an agent's reachable systems; it therefore expands capability surface.

Before enabling one, define tool inventory, auth source, destination/service scope, data classes, read/write effects, network behavior, failure semantics, rate/cost bounds, and audit evidence. Expose the smallest toolset needed per turn/task rather than a permanent universal toolbox.

Tool descriptions and remote responses are untrusted data. A connector must not be able to rewrite governance merely by returning instructions. Credentials stay provider-managed where possible. Unavailable integrations fail soft for optional capabilities and fail closed when the task requires a mandatory protected operation.

## Synthetic contract fixtures

[`examples/tool-contracts/`](../examples/tool-contracts/) contains schema-checked examples for read-only search, scoped repository write, messaging, and secret-backed API access. Each declares target scope, authentication source, destinations, data classes, side effects, bounded retries, cancellation, and postcondition evidence.

The intentionally invalid `over-broad-network.json` uses wildcard targets and destinations. It demonstrates why an agent-selected network boundary must be rejected rather than treated as least-capability.
