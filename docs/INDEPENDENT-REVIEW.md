# Independent Review

Independent review exists to break shared assumptions.

A reviewer should receive the contract, relevant diff/behavior, evidence, and necessary context without inheriting the implementer's mutable reasoning. Read-only posture is preferred.

Review lanes may include correctness, security, capability/side effects, context/provenance, supply chain, privacy/data boundaries, performance, UI/accessibility, and delivery/reproducibility.

Findings require severity, evidence, affected requirement/control, and disposition. Reviewer output is structured and does not mutate the implementation before the finding is visible.