# Parallel Work Harness

A coordinator creates bounded work packets containing role, objective, allowed files/surfaces, context sources, capabilities, budget, dependencies, and expected evidence.

Workers should not overlap writes unless explicitly coordinated. Read-only reviewers remain independent. Nesting depth and worker count are bounded. The coordinator reconciles conflicts, verifies worker claims, and performs final convergence.

Parallelism optimizes elapsed time; it must not multiply authority or bypass approval.