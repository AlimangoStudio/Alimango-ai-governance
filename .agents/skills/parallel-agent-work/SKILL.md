# Parallel Agent Work

Parallelize only separable work with explicit ownership, inputs, outputs, and budgets.

Avoid overlapping writes, uncontrolled subagent nesting, duplicated research, and review by an agent that shares the implementer's mutable context when independence matters. Each worker returns concise evidence and unresolved questions; a coordinator performs final convergence.