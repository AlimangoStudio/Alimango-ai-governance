# Reference v1 Validation Record

This file exercises the pull-request governance CI against the public reference control plane.

Expected gates:

- public-scope validation
- mandatory agent-control surface validation
- capability-doctor self-check
- completed Spec Kit fixture validation
- Unlazy fixture validation
- reference harness unit tests
- Python syntax checks
- machine-readable JSON parsing
- deterministic audit fingerprint smoke check
- secret/non-public artifact-pattern scan
- whitespace validation

A passing CI run validates the checked repository revision against the open reference harness and its declared gates.
