# Tenant / Workspace / Scope Isolation Policy

Every data-bearing or side-effecting action must have an explicit scope: repository, workspace, tenant, organization, account, environment, or equivalent boundary.

Never infer cross-scope authority from visibility. Queries, caches, retrieval indexes, tool calls, logs, and generated artifacts must preserve the active scope. Global/platform operations are separate capabilities from tenant/workspace operations.

For systems without tenancy, apply the same principle to repository, environment, account, or user boundaries. Negative tests should prove that one scope cannot read or mutate another unless explicitly authorized.