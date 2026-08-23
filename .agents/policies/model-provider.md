# Model and Provider Policy

Governance must remain valid across model/provider changes.

- Models propose reasoning and actions; policy determines authorization.
- Provider-specific system features may strengthen controls but cannot be the only copy of a critical invariant.
- Do not grant broader tools because a model is described as more capable or more aligned.
- Record model/provider/version when it materially affects reproducibility.
- Bound retries, tool loops, subagent recursion, and spend.
- Provider failure must resolve to an explicit blocked/degraded state, not uncontrolled fallback to a weaker policy path.