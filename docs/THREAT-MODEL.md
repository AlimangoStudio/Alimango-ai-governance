# Threat Model

The public lab studies controls for AI-assisted software engineering. This threat model focuses on failure modes that governance systems should detect or prevent.

## Assets

- instruction authority and precedence
- credentials and private data
- tenant/workspace isolation
- source and dependency integrity
- production state
- financial or external side effects
- audit evidence and completion claims
- context provenance and freshness

## Adversaries and failure sources

The model includes both malicious and non-malicious causes:

- prompt or tool injection,
- compromised or misleading external repositories,
- unsafe public contributions,
- stale context and incorrect memory,
- over-permissioned agents,
- accidental destructive commands,
- hidden network access or callbacks,
- cross-tenant/workspace data leakage,
- false completion claims,
- reviewer self-approval,
- dependency or supply-chain compromise,
- unbounded retries, recursion, or cost.

## Trust boundaries

```text
untrusted public input
        │
        ▼
 normalization / provenance
        │
        ▼
 policy + capability evaluation
        │
   ┌────┴────┐
 deny       allow
             │
             ▼
      governed tool/service
             │
             ▼
       observable side effect
             │
             ▼
        evidence + review
```

## Required questions for security-relevant proposals

1. What asset is protected?
2. What actor or failure can violate it?
3. Where is the enforcement point?
4. Does missing policy/evidence fail open or fail closed?
5. What capability is required?
6. Can the control be bypassed through another tool/path?
7. What telemetry proves the control ran?
8. What is the rollback or containment path?

## Non-goals

This repository does not publish private Alimango threat intelligence, production architecture, credentials, customer data, or exploitable private-system details. Synthetic examples should be used instead.
