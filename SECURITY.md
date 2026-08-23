# Security Policy

## Scope

This repository contains public governance research, proposals, examples, and contribution material. It must not contain production credentials, private Alimango source code, customer data, or secrets.

## Reporting a security issue

Do **not** open a public issue for a vulnerability that could expose credentials, private repositories, production systems, customer data, or a practical exploit path.

Use GitHub's private vulnerability reporting feature for this repository when available. If private reporting is unavailable, contact the repository owner through a private channel rather than publishing exploit details.

## Security expectations for contributions

Contributions must not:

- introduce hidden network calls or telemetry,
- execute destructive actions by default,
- request broader permissions than the demonstrated use case needs,
- bypass approval or evidence gates to simplify an example,
- embed secrets or real credentials,
- treat public/community content as trusted production policy,
- weaken isolation, authentication, authorization, or provenance controls.

Security-sensitive examples should be fail-closed and should clearly distinguish demonstration behavior from production-ready controls.

## Authority boundary

Nothing in this public repository is production governance. Security fixes or ideas that may be useful to Alimango are independently evaluated and implemented in the private canonical governance repository before they can affect any Alimango project.
