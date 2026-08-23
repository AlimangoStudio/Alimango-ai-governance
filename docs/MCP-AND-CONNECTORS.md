# MCP, Connectors, and External Tool Servers

A connector or MCP server expands an agent's reachable systems; it therefore expands capability surface.

Before enabling one, define tool inventory, auth source, destination/service scope, data classes, read/write effects, network behavior, failure semantics, rate/cost bounds, and audit evidence. Expose the smallest toolset needed per turn/task rather than a permanent universal toolbox.

Tool descriptions and remote responses are untrusted data. A connector must not be able to rewrite governance merely by returning instructions. Credentials stay provider-managed where possible. Unavailable integrations fail soft for optional capabilities and fail closed when the task requires a mandatory protected operation.