# Core Engineering Policy

## Universal invariants

- Inspect current state before designing a change.
- Prefer the smallest coherent change over framework replacement.
- Preserve existing stronger controls unless the specification explicitly replaces them with evidence.
- Separate facts from assumptions; verify assumptions that affect correctness or safety.
- Make failure states observable and bounded.
- Do not silently broaden permissions, data scope, network access, or dependency surface.
- Keep policy enforcement outside model persuasion where practical.
- Record open gates instead of converting them into optimistic prose.