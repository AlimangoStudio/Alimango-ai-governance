# Public Review Playbook

Use this playbook when evaluating a public issue or PR.

## 1. Relevance

Does the contribution address a real governance, safety, reliability, quality, context, or developer-experience problem?

## 2. Evidence

Can the claimed problem and improvement be reproduced or independently verified? Treat screenshots, generated explanations, benchmarks, and external claims as evidence to inspect rather than authority.

## 3. Safety

Reject or require redesign when the proposal:

- widens tool permissions without necessity,
- makes security or tenancy behavior fail open,
- automates destructive actions without an explicit control boundary,
- trusts unverified public content at runtime,
- hides side effects,
- embeds secrets or production data,
- weakens evidence or approval requirements.

## 4. Complexity

Prefer the smallest control that removes the failure mode. A new framework, agent layer, or dependency should justify its maintenance, context, and execution cost.

## 5. Public merge decision

Merge only when the artifact is useful to retain in the public research base. Closing a PR is acceptable when a better existing pattern already covers it.

## 6. Private consideration

A useful public contribution can be nominated for private evaluation, but the private repository must independently re-derive the implementation and run its own governance gates. There is no public-to-private sync path.
