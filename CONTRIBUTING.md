# Contributing to Alimango AI Governance Lab

This repository is for people who want to make AI-agent engineering controls more explicit, testable, portable, and difficult to bypass.

> A public merge means **retained for research/reference**, not adopted into private Alimango production governance.

## Good contribution shapes

- a reproducible agent failure case;
- a smaller/stronger capability or approval mechanism;
- a typed tool/context/evidence contract;
- an adversarial test fixture;
- an improvement to Spec Kit, Done-When, Unlazy, convergence, or review;
- a measurable context/RAG/CAG optimization that preserves authority;
- a supply-chain, prompt-injection, privacy, isolation, secrets, or network-safety control;
- a model/host adapter that preserves the shared control semantics;
- a comparison showing why one control mechanism is stronger or cheaper than another.

## Start with the failure mode

State what can go wrong, the smallest scenario that reproduces it, and why existing controls are insufficient. Then describe the proposed control, bypasses, and evidence.

For substantial repository behavior changes, use the Spec Kit templates under `.specify/templates/`. New control families should also use the AGP process in `proposals/`.

## Quality bar

Prefer executable proof > deterministic validator > typed contract > service/capability boundary > workflow > prose-only reminder.

A strong PR is focused, public-safe, explicit about permissions and side effects, honest about limitations, and includes negative-path evidence where practical.

## Local validation

Core checks require Python 3.11+ and no third-party packages:

```bash
python scripts/validate_public_lab.py
python scripts/validate_agent_controls.py
python scripts/capability_doctor.py --require python --require AGENTS.md
python scripts/spec_check.py examples/specs/001-capability-contract
python scripts/unlazy_check.py examples/specs/001-capability-contract
python scripts/compile_context.py --request examples/context-request.json
python -m unittest discover -s tests -p 'test_*.py' -v
```

On systems with `make`, `make validate` and `make test` run the same reference gates.

## Do not submit

Secrets, credentials, keys, customer/patient/tenant data, private Alimango source, proprietary project internals, malware, hidden callbacks, destructive payloads, material you lack rights to redistribute, or any automatic public-to-private governance sync/runtime dependency.

## Review criteria

Maintainers review relevance, control strength, bypass resistance, least capability, fail-closed behavior, evidence, compatibility, dependency/supply-chain cost, context/token/latency impact, and whether the proposal duplicates a stronger mechanism.

Maintainers may merge, request changes, close, extract only the idea, or reimplement it differently elsewhere. Public acceptance never obligates private adoption.

See `docs/CONTRIBUTOR-QUICKSTART.md`, `docs/RFC-PROCESS.md`, `docs/THREAT-MODEL.md`, `docs/ADOPTION-BOUNDARY.md`, and `SECURITY.md`.