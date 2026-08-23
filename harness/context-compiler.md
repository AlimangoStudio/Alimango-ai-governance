# Context Compiler Harness

Inputs: task, authority policy, source registry, project/repository overlay, risk profile, context budget, and available retrievers.

Algorithm:

1. select mandatory authority sources;
2. classify task/risk and activate relevant modules;
3. retrieve task-specific sources;
4. attach provenance, hash, freshness, sensitivity, and reason;
5. reject advisory instruction conflicts;
6. deduplicate and trim within budget without dropping protected controls;
7. emit context capsule + source manifest + budget telemetry.

A compiler error must return an explicit fallback/block state. It must never silently compile a weaker authority set.