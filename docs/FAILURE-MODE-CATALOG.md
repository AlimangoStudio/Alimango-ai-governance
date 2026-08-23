# Agent Failure-Mode Catalog

Use these as test targets, not just warnings.

- **FM-01 Prompt compliance drift:** model follows the latest persuasive text instead of authority.
- **FM-02 Tool availability = permission:** agent assumes an exposed tool is authorized.
- **FM-03 Scope creep:** agent changes adjacent systems to make its preferred design easier.
- **FM-04 Fail-open fallback:** missing governance/auth/context silently downgrades safety.
- **FM-05 Evidence substitution:** compile/lint or self-report is presented as proof of behavior.
- **FM-06 Stale context:** agent acts on an old API, branch, schema, or policy.
- **FM-07 Public supply-chain poisoning:** external skill/repo becomes trusted through popularity or convenience.
- **FM-08 Reviewer coupling:** reviewer shares assumptions/context and misses the same defect.
- **FM-09 Runaway autonomy:** retries, subagents, or tool loops expand cost and blast radius.
- **FM-10 Secret/data exfiltration:** sensitive input leaks into logs, prompts, caches, PRs, or external tools.
- **FM-11 Destructive ambiguity:** target or scope is insufficiently resolved before irreversible action.
- **FM-12 Completion drift:** tasks/gates/findings disagree but final message says done.
- **FM-13 Governance self-disable:** a migration removes the control required to validate the migration.
- **FM-14 Hidden permission expansion:** a dependency or implementation adds network/filesystem/external-write capability.
- **FM-15 Unbounded retrieval:** context size/cost explodes and critical controls are diluted.
