# Agent Control Plane

The reference architecture separates **model cognition** from **execution authority**.

## Layers

1. **Authority** — constitution, policy, repository overlay, specification, task.
2. **Routing** — task type, risk, affected domains, required skills/workflows.
3. **Capability** — explicit permissions and approval decision.
4. **Context** — bounded, source-attributed, freshness/sensitivity-aware input.
5. **Execution** — model/agent performs only the authorized task.
6. **Evidence** — tests, validators, negative paths, postconditions.
7. **Challenge** — independent review for material risk.
8. **Completion** — Unlazy + convergence determine terminal state.
9. **Telemetry** — structured records support audit and improvement.

## Core property

No layer may infer authority from model confidence. A model can recommend a destructive action while the control plane denies it. A model can claim completion while evidence/convergence returns `needs_changes`.

## Portable implementation

The `.agents/` directory is intentionally model-agnostic. Host adapters may translate these contracts into Codex, Claude Code, IDE agents, CI bots, or custom agents without changing the authority model.