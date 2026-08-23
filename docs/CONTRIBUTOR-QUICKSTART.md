# Contributor Quickstart

1. Read `README.md`, `GOVERNANCE.md`, `AGENTS.md`, and `docs/PUBLIC-SCOPE.md`.
2. Pick a concrete failure mode from `docs/FAILURE-MODE-CATALOG.md` or propose one.
3. Start with a small issue or proposal that states failure mode, control, bypasses, and evidence.
4. If changing repository behavior, use the templates under `.specify/templates/`.
5. Add synthetic tests/examples and machine-readable contracts when practical.
6. Run `python scripts/validate_public_lab.py` and `python scripts/validate_agent_controls.py`.
7. Open a focused PR; keep secrets, personal/customer data, confidential source, non-public endpoints, and proprietary implementation details out.

Good first contributions include new adversarial fixtures, schema improvements, deterministic validators, clearer failure modes, control comparisons, and reproducible experiments.
