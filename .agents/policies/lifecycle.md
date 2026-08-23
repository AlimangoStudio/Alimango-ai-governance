# Lifecycle and Cancellation Policy

Every governed run should have an explicit lifecycle and terminal state. Side effects occur only after governance loading, routing, and authorization.

Retries are bounded. Cancellation prevents new actions, interrupts cancellable work where possible, records partial side effects/evidence, and terminates as `cancelled` or another explicit non-complete state.

Agent/subagent recursion must be bounded by count, depth, time, and/or cost. A crashed or interrupted run does not become complete by absence of an error report.