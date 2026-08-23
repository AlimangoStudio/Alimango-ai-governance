# Experiment Protocol

The lab should make governance claims testable. Use this protocol for experiments, benchmarks, and proof-of-concept controls.

## Minimum experiment record

A useful experiment should state:

- **Hypothesis** — the failure/control relationship being tested.
- **Baseline** — behavior without the proposed control.
- **Intervention** — the exact control or change.
- **Inputs** — synthetic prompts, fixtures, tool definitions, or repository state.
- **Metrics** — what is measured and how.
- **Expected failure behavior** — especially whether the system fails closed.
- **Results** — raw counts or reproducible outputs, not only interpretation.
- **Limitations** — what the experiment does not prove.

## Suggested metrics

Depending on the proposal:

- unsafe action escape rate,
- false block rate,
- policy decision latency,
- context tokens selected,
- provenance coverage,
- stale-context rejection rate,
- permission surface size,
- tool-call count,
- retry depth,
- audit/evidence completeness,
- reviewer finding recall,
- compute or monetary cost.

## Reproducibility

Prefer deterministic fixtures and pinned dependency/model/tool versions where possible. If model behavior is stochastic, report enough runs to show variance and record sampling parameters.

Do not claim general security from a single happy-path example.

## Negative tests

Every preventive control should include at least one attempted bypass. Examples:

- alternate tool path,
- missing policy file,
- malformed authority metadata,
- stale or conflicting context,
- unauthorized tenant/workspace identifier,
- hidden side-effect request,
- approval token replay,
- dependency/source substitution.

## Evidence format

Keep evidence compact and reviewable. Prefer machine-readable summaries plus the smallest human-readable explanation necessary to interpret them.
