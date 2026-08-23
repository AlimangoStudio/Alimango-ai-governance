# Reference Metrics

## Safety / correctness

- unauthorized-action rate
- policy-bypass success rate
- secret/private-data exposure rate
- negative-path pass rate
- requirement coverage
- regression rate
- independent-review finding yield
- false-complete rate
- false-block rate

## Context

- selected context tokens
- protected-authority coverage
- irrelevant-context ratio
- cache hit rate
- stale-source rate
- compile-fallback/block rate

## Execution

- tool-call count
- retry count
- subagent count/depth
- cancellation latency
- terminal-state distribution

## Cost / performance

- end-to-end latency
- model tokens/cost
- validation runtime
- maintainer review time

Benchmarks should report trade-offs rather than optimize a single metric at the expense of safety or correctness.