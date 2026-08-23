# Reference Consumer Model

Teams using a centralized governance repository should separate reusable governance from project truth.

```text
private organization governance (pinned revision)
              ↓
project overlay / golden paths / data boundaries
              ↓
current spec
              ↓
current task
```

A consumer lock records an immutable governance revision. A bootstrap verifies the expected source/revision and fails closed if unavailable. Project-specific constraints remain local. Public research repositories are not fallback authority.

The templates under `templates/consumer/` are illustrative and deliberately point to a hypothetical private governance repository, never this public lab.