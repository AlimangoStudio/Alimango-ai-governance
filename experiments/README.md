# Governance Experiments

This directory is for reproducible, public-safe experiments comparing agent-control mechanisms.

Good experiments isolate a failure mode and compare controls such as:

- prompt warning vs capability enforcement,
- self-review vs independent review,
- whole-repository prompt vs bounded context compilation,
- untyped tool vs typed service-mediated tool,
- unbounded retry vs explicit lifecycle/cancellation budget.

Use `EXPERIMENT-TEMPLATE.md`. Never use real credentials, private source, customer data, production systems, or destructive targets.