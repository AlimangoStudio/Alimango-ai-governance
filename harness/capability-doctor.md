# Capability Doctor

Run a preflight before planning work that depends on tools or external systems.

Check required executables/connectors, authenticated access, read/write scope, network availability, browser/runtime availability, secret availability without exposing values, and whether the task requires approval-only capabilities.

The doctor reports `available`, `unavailable`, or `blocked_by_policy`. Missing capability changes the plan; it does not justify bypassing governance.