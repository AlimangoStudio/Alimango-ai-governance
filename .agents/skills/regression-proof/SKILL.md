# Regression Proof

A change is not isolated because its diff is small. Identify the behaviors that must remain unchanged, choose the cheapest reliable evidence for each, and compare against an appropriate baseline when a failure may be pre-existing.

Output a non-regression map: protected behavior → affected surface → proof command/evidence → result → limitation. Do not use “unrelated” as a substitute for evidence when the change shares a dependency, policy, interface, or execution path.