# Agent Host Adapters

The control model is host-independent. Adapters translate repository authority into host conventions without changing semantics.

Reference adapters:

- `generic.md` — any agent/runtime
- `codex.md` — Codex-style repository agents
- `claude-code.md` — Claude Code-style repository agents

An adapter may add host-specific ergonomics, but cannot weaken Constitution, capability, approval, context, evidence, review, Unlazy, or convergence rules.
