# Testing Policy

Use the narrowest test that proves the requirement, then add regression breadth proportional to blast radius.

At minimum consider: happy path, denied/failure path, malformed input, capability bypass, stale/missing context, concurrency/retry behavior where relevant, and compatibility with existing controls.

When claiming a failure is pre-existing, reproduce it against an appropriate baseline rather than relying on memory. Never convert skipped tests into a pass.