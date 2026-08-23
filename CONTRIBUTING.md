# Contributing to the Alimango AI Governance Lab

This public repository exists to collect and improve ideas that may strengthen Alimango's private AI engineering governance system.

## Before you contribute

This repository is **advisory only**. A merged issue, discussion, or pull request does not become production governance and does not create a dependency for PAPPS or any other Alimango project.

Do not submit:

- secrets, credentials, tokens, private keys, or environment files
- patient/client/customer data or other private production data
- proprietary source code you do not have permission to disclose
- private Alimango project internals
- malware, credential harvesting, hidden network callbacks, or destructive payloads
- copied third-party material whose license does not permit redistribution

## Good proposals

A strong proposal usually states:

1. **Failure mode** — what can go wrong today?
2. **Scope** — what part of agent/governance behavior changes?
3. **Proposed control** — what concrete mechanism addresses the problem?
4. **Evidence** — tests, examples, measurements, prior incidents, or reproducible demonstrations.
5. **Trade-offs** — complexity, latency, token cost, false positives, or compatibility impact.
6. **Security impact** — whether permissions, secrets, network access, side effects, tenancy, privacy, or supply-chain trust are affected.
7. **Adoption notes** — what would need to be independently verified before a private implementation could be considered.

## Pull-request expectations

- Keep PRs focused and reviewable.
- Prefer executable checks over prose-only guardrails when practical.
- Do not weaken fail-closed controls to make an example easier to run.
- Do not assume a third-party tool, model, repository, benchmark, or article is authoritative.
- Pin or identify external sources precisely enough for reviewers to verify them.
- Make hidden assumptions explicit.
- Avoid adding a second framework when a small improvement to an existing concept is sufficient.
- Avoid generated bulk content that has not been manually reviewed for relevance and correctness.

## Review outcomes

Maintainers may:

- merge a contribution because it is useful to keep in the public lab,
- request changes,
- close it as redundant, unsafe, unverifiable, or out of scope,
- extract only the underlying idea and reimplement it differently elsewhere,
- decide not to adopt a merged public contribution into private governance.

A public merge means **retained for public exploration**, not **adopted by Alimango production governance**.

## Private adoption boundary

Any idea selected for private use is re-evaluated separately. Private adoption may involve rewriting, reducing, combining, or rejecting parts of the public proposal after security, compatibility, regression, and governance review.

The public repository never automatically synchronizes into the private governance repository.
