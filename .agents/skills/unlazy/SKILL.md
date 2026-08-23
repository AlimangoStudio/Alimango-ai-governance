# Unlazy Skill

Before any completion claim, independently scan current artifacts and evidence for incomplete work: unchecked required tasks, TODO/FIXME/placeholders, skipped tests, stale results, unresolved findings, untested negative paths, missing approval, missing migration/rollback proof, missing UI/live proof where claimed, and contradictions among spec/tasks/gates.

Output a gate table and one of: `complete`, `blocked`, `partial`, or `needs_changes`. Do not repair evidence by weakening the requirement.