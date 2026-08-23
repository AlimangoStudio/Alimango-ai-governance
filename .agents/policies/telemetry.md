# Telemetry Policy

Record enough metadata to reconstruct governed decisions without defaulting to sensitive content capture.

Useful fields include run/task id, governance revision, lifecycle event, capability decision, tool id, target class, latency, retry count, context size/source ids, evidence references, reviewer verdict, Unlazy/convergence result, token/cost estimates, and terminal state.

Redact secrets and protected payloads. Telemetry failure must not silently disable security controls; decide explicitly whether the affected action can continue.