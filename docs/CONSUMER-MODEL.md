# Reference Adoption Model

The control plane is designed to be portable. A project adopting the reference can separate reusable governance from project-specific truth:

```text
pinned governance revision
          ↓
project overlay / golden paths / data boundaries
          ↓
current spec
          ↓
current task
```

A revision lock records the exact governance version or commit used. A bootstrap verifies the expected source and revision before governed execution. Project-specific constraints remain local to the adopting project.

The examples under `templates/consumer/` use placeholders only. Replace them with values appropriate to your own environment and keep confidential implementation details out of public contributions.

This is an integration pattern, not a requirement. Forking, vendoring, packaging, or selectively adapting controls are also valid when provenance and authority remain explicit.
