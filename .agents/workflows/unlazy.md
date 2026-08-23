# Unlazy Completion Gate

Unlazy is an anti-shortcut gate applied immediately before a completion claim.

Check for: unchecked required tasks; TODO/FIXME/placeholders; untested failure paths; skipped or stale validation; hidden assumptions; missing authorization proof; incomplete migrations/rollback; unresolved reviewer findings; spec/task/gate contradictions; missing browser/live evidence when those states are claimed; undocumented limitations; and handoff gaps.

Unlazy does not ask whether the implementation is plausible. It asks whether every required completion claim is supported now. Any required unmet gate changes the terminal state away from `complete`.