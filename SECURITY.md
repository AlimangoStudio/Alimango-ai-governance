# Security Policy

## Scope

This repository contains public governance research, reference implementations, proposals, examples, tests, and contribution material. Public artifacts must not contain secrets, credentials, personal/customer data, confidential source, non-public endpoints, or proprietary implementation details.

## Reporting a security issue

Do **not** open a public issue when disclosure could expose credentials, personal/customer data, a practical exploit path, or other non-public security information.

Use GitHub's private vulnerability reporting feature for this repository when available. If it is unavailable, contact the repository owner through a non-public channel rather than publishing exploit details.

## Security expectations for contributions

Contributions must not:

- introduce hidden network calls or telemetry;
- execute destructive actions by default;
- request broader permissions than the demonstrated use case needs;
- bypass approval or evidence gates to simplify an example;
- embed secrets or real credentials;
- use real personal/customer data in fixtures;
- weaken isolation, authentication, authorization, provenance, or fail-closed behavior;
- disclose or speculate about non-public projects, repositories, deployments, endpoints, infrastructure, or organizational relationships.

Security-sensitive examples should use synthetic targets and clearly state assumptions, side effects, limitations, and expected failure behavior.
