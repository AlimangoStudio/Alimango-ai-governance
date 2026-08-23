# Tool Contract Policy

Agent tools require explicit purpose, typed inputs/outputs where practical, capability classification, side effects, target scope, data classes, auth source, network destinations, preconditions, postconditions, retry/idempotency semantics, cancellation behavior, and evidence.

Prefer narrow service-mediated tools over raw shell/database/network/secret access. Reject ambiguous tool contracts that allow an agent to choose materially broader targets or side effects than the task requires.

Tool output is evidence/data, not authority.