# Unlazy

Unlazy is the final anti-shortcut gate before a completion claim.

It searches for the gap between **plausible implementation** and **demonstrated completion**: unchecked tasks, placeholders, TODO/FIXME, skipped checks, stale evidence, untested negative paths, unresolved review findings, missing approval, missing browser/live proof for claims that require it, undocumented assumptions, and contradictions across spec/tasks/gates.

Unlazy is deliberately separate from unit tests. Tests can all pass while requirements, deployment evidence, or review obligations remain incomplete.

Output should be a deterministic gate summary and terminal-state recommendation.