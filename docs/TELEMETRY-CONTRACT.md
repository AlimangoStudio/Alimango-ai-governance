# Agent Telemetry Contract

Telemetry exists to answer: what was attempted, why was it authorized, what tools ran, what evidence was produced, what did it cost, and how did the run end?

Recommended events: governance_loaded, task_routed, capability_decision, context_compiled, tool_started, tool_finished, evidence_recorded, review_completed, unlazy_completed, convergence_completed, cancelled, terminal_state.

Fields may include run/task ids, timestamps, control revision, capability class, tool id, latency, retry count, token/cost estimates, evidence references, and terminal state.

Default to metadata and references rather than raw sensitive payloads. Redact secrets and protected data.