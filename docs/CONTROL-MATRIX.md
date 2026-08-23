# Control Coverage Matrix

| Failure mode | Primary control | Secondary proof |
| --- | --- | --- |
| agent acts outside request | task router + capability policy | action decision log |
| retrieved instruction overrides policy | authority order + context policy | context manifest |
| secret leakage | sensitivity policy + secret scan | negative fixture/check |
| destructive action without consent | action governance | explicit approval record |
| confident but incomplete implementation | Done-When + Unlazy | convergence verdict |
| self-review misses defect | independent reviewer | structured finding/verdict |
| stale context changes behavior | freshness/content identity | context manifest |
| third-party skill introduces hidden behavior | supply-chain review | pinned ref + license/network analysis |
| runaway retries/subagents | lifecycle + budgets | telemetry terminal state |
| green tests but broken requirement | Spec Kit acceptance contract | requirement-to-evidence mapping |
| policy drift across models | externalized controls | validator + manifest |
| untrusted contribution weakens controls | constitution + governed change process | CI + review + negative-path evidence |
| public artifact leaks confidential topology | public-scope policy | artifact hygiene + review |
