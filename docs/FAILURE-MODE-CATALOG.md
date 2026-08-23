# Failure-Mode Catalog

A proposal is easier to review when it names the failure class it addresses.

| ID | Failure mode | Typical symptom | Useful control families |
| --- | --- | --- | --- |
| **AGF-001** | Authority confusion | public/stale instructions override canonical policy | authority, provenance, pinning |
| **AGF-002** | Capability overreach | agent uses a tool/action beyond task need | capability, allowlists, per-turn toolsets |
| **AGF-003** | Approval bypass | risky action occurs without required human review | approval, action tokens, service gates |
| **AGF-004** | Tool-contract ambiguity | malformed arguments or oversized outputs create unsafe behavior | schemas, typed contracts, bounded outputs |
| **AGF-005** | Direct side-effect coupling | agent writes DB/secrets/external systems directly | service-mediated actions, transactions |
| **AGF-006** | Context poisoning | untrusted retrieved content becomes instruction authority | provenance, source classes, injection filters |
| **AGF-007** | Stale context | agent acts on obsolete project/repository state | freshness, ref pinning, tree inspection |
| **AGF-008** | Tenant/workspace bleed | data crosses isolation boundary | scoped identity, mandatory filters, tests |
| **AGF-009** | Secret exposure | credentials enter context/logs/public artifacts | secret isolation, redaction, scanners |
| **AGF-010** | SSRF/network escape | tool reaches unapproved/internal endpoints | URL validation, egress allowlists |
| **AGF-011** | Destructive action drift | broad delete/force/reset command exceeds intent | destructive-action policy, dry-run, approval |
| **AGF-012** | Infinite/expensive execution | runaway retries, nested agents, token or tool explosion | budgets, depth caps, cancellation |
| **AGF-013** | False completion | agent reports done without current evidence | done-when-proof, executable gates |
| **AGF-014** | Reviewer dependence | implementer silently fixes and self-approves | independent read-only review |
| **AGF-015** | Supply-chain substitution | dependency/repo/source changes under same name | immutable refs, provenance, integrity checks |
| **AGF-016** | Observability gap | no trace of policy/tool decisions | structured telemetry, terminal events |
| **AGF-017** | Governance self-disablement | migration removes the guardrail needed to validate migration | staged compatibility, fail-closed bootstrap |
| **AGF-018** | Prompt-only control decay | important safety depends on prose the agent can ignore | executable validators, policy engines, wrappers |

## Adding a failure mode

New catalog entries should be concrete enough to produce a test. Avoid overlapping IDs when an existing class can be extended with a narrower example.
