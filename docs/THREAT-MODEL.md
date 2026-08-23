# Threat Model

## Protected assets

Authority rules, capability decisions, secrets, private data, source integrity, evidence integrity, deployment boundaries, human approvals, and auditability.

## Adversaries / failure sources

A malicious contributor; compromised dependency; prompt/tool injection in retrieved content; stale or poisoned context; over-permissioned agent; hallucinated target; accidental destructive command; self-approving reviewer; compromised cache; and ordinary implementation error.

## Trust boundaries

Model ↔ policy engine; retrieved content ↔ authoritative context; agent ↔ tool/service; public repo ↔ private governance; developer environment ↔ external systems; implementation agent ↔ independent reviewer.

## Required properties

- fail closed when authority/capability is unresolved;
- no secret-bearing public artifacts;
- no public-to-private automatic authority path;
- explicit side-effect classification;
- content provenance and freshness;
- independent challenge for material risk;
- evidence bound to relevant revision;
- bounded retries/cancellation;
- terminal states that cannot silently convert failure into success.

Threat-model contributions should include a concrete attack path and the control that breaks it.