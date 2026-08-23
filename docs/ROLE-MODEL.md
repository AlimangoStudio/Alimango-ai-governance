# Agent Role and Delegation Model

Roles exist to narrow responsibilities and reduce correlated failure. They do not supersede policy.

A delegation contract should state: role, exact objective, allowed context, capability set, time/token/tool budget, write ownership, expected evidence, and terminal output.

Independent review requires separation from the implementer's mutable work where practical. Parallel agents should own non-overlapping changes or explicit read-only analyses. Uncontrolled nesting is prohibited because it obscures authority, cost, and provenance.