# Agent Governance Maturity Model

| Level | Characteristics |
| --- | --- |
| **0 — Prompt-only** | safety depends on instructions and model compliance |
| **1 — Documented** | explicit policies/specs but weak enforcement |
| **2 — Checked** | validators, schemas, CI, negative tests |
| **3 — Governed** | capability decisions, context provenance, evidence gates, explicit lifecycle |
| **4 — Independently challenged** | read-only reviewers, adversarial tests, convergence, drift detection |
| **5 — Measured** | telemetry, budgets, failure-rate analysis, controlled upgrades, reproducible governance revisions |

The goal is not bureaucracy. The goal is to move critical safety/correctness properties out of model memory and into inspectable mechanisms.