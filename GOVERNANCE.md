# Repository Governance

This document governs the **public Alimango AI Governance Lab**. It does not describe Alimango production governance.

## Decision model

The public lab is maintainer-led and evidence-oriented. Maintainers may merge, request changes, or close contributions based on technical merit, safety, scope, clarity, maintenance cost, and fit with the lab's research goals.

A merge here means **accepted for public exploration**. It does not mean the idea is used by Alimango production systems.

## Maintainer responsibilities

Maintainers should:

- keep the public/private trust boundary explicit,
- prefer narrow controls over framework sprawl,
- require reproducible evidence for strong claims,
- challenge permission expansion and hidden side effects,
- preserve contributor attribution,
- close unsafe, unverifiable, or redundant proposals quickly,
- document material changes in `CHANGELOG.md`.

## Proposal lifecycle

```text
DRAFT -> REVIEW -> EXPERIMENTAL -> RETAINED
                \-> REJECTED
```

`RETAINED` means useful in this public lab. Private adoption, if any, is a separate implementation and review process.

## Conflict resolution

Technical disagreements should be resolved using the smallest reproducible test or strongest available evidence. When evidence is incomplete, the repository should state uncertainty rather than manufacture consensus.

## Security boundary

No maintainer decision in this repository may authorize an automatic public-to-private synchronization path. No public artifact is allowed to become an implicit production dependency.
