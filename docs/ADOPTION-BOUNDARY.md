# Public-to-Private Adoption Boundary

The public governance lab is deliberately separated from Alimango's private governance authority.

## Never automatic

There is no supported workflow in which public `main` becomes private governance through mirroring, syncing, vendoring, package updates, submodules, CI downloads, or runtime retrieval.

## Allowed flow

A public contribution may trigger a private evaluation. The private implementation must independently establish:

- the problem is real and relevant,
- the proposal is compatible with stronger existing controls,
- security and privacy boundaries are preserved,
- external dependencies and licenses are understood,
- tests/evidence support the claimed improvement,
- token/compute/maintenance cost is justified,
- the change fits the private governance architecture,
- rollback or migration implications are explicit.

The private implementation may be materially different from the public proposal.

## Meaning of a public merge

A merge here records that the contribution is useful to retain in the public research base. It does not create an Alimango standard, requirement, guarantee, or production dependency.
