# Spec Kit

Spec Kit prevents an agent from implementing an interpretation that was never made explicit.

The reference lifecycle is:

```text
specify → plan → tasks → analyze → checklist → implement → validate → converge
```

A spec captures problem, scope, requirements, threats, capabilities, context/data impact, acceptance evidence, compatibility, and rollback. The plan connects those requirements to architecture and tests. Tasks make execution checkable. Analysis challenges contradictions and missing assumptions. Checklist converts the contract into gates. Convergence reconciles actual evidence with the original contract.

When numbered specs are used, inspect the repository's actual spec tree and active branches before assigning a number; never infer the next number from conversation memory.