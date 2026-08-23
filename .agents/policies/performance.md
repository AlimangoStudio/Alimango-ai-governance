# Performance and Budget Policy

Agent governance must be affordable enough to remain enabled.

- Bound context, retrieval, tool calls, retries, subagents, and validation fan-out.
- Prefer selective loading over whole-repository prompting.
- Cache only immutable/public-safe material by content hash when appropriate.
- Track latency/token/cost changes for governance mechanisms that can materially increase execution cost.
- Do not remove a safety gate only because it is expensive; optimize the gate or make risk-proportional execution explicit.