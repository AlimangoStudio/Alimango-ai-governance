# Agent Control Harness

The public lab harness is a reference implementation for controlling agent execution through explicit authority, capability, context, evidence, and review layers.

```text
request
  ↓
authority resolution
  ↓
task routing + risk classification
  ↓
Spec Kit contract
  ↓
capability decision
  ↓
bounded context compile
  ↓
implementation / research
  ↓
validation + evidence
  ↓
independent challenge
  ↓
Unlazy
  ↓
convergence
  ↓
terminal state
```

The harness is deliberately model-agnostic. Model output is treated as proposed work, not proof. Side effects are governed independently of model confidence.

See `manifest.json` for the machine-readable control registry.