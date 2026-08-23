# AGP-004 — Verified Evidence, Project Memory, Skill Supply Chain, and Design Contracts

- **Status:** accepted-for-lab
- **Scope:** public reference proposal only
- **Authority:** advisory; no AGP status implies production or private adoption

## Failure modes

Agent engineering systems commonly blur four different concerns:

1. a dependency tool returns nothing and the agent treats that as proof that nothing depends on a file;
2. persistent agent memory becomes stale but is treated as source truth;
3. reusable skills change without a deterministic integrity signal;
4. UI generation jumps from a vague prompt directly to code, or mandates expensive visual effects regardless of device constraints.

These are distinct failure modes but share one principle: **an acceleration layer must never silently become an authority layer**.

## Pattern A — explicit structural-evidence coverage

Dependency, importer, caller, hub, or code-map evidence should expose a coverage state:

- `complete`
- `partial`
- `unavailable`

Individual sources may be `authoritative`, `mixed`, `fallback`, `timeout`, `failed`, or `unavailable`.

Rules:

- partial/unavailable is uncertainty, not proof of absence;
- native ecosystem resolution is preferred over generic matching;
- material gaps require another evidence lane;
- empty results from a failed/timed-out scan must carry failure provenance.

This pattern is useful for blast-radius review without making any particular code-map tool authoritative.

## Pattern B — revision-bound advisory project memory

Persistent memory may store concepts, architecture, decisions, relationships, and file references to reduce repeated orientation cost.

A useful memory record should carry:

- stable concept id/kind,
- summary,
- source repository revision,
- relevant file references,
- verification revision/state,
- authority=`advisory`,
- freshness state such as `fresh`, `stale`, `conflicted`, or `unverified`.

Rules:

- repository drift can make memory stale;
- stale memory may guide discovery but cannot satisfy material correctness/authorization/completion gates;
- conflicts are preserved and resolved against current source;
- memory writes are side effects and should be governed;
- sensitive project context must remain scoped to its project/workspace.

## Pattern C — deterministic skill supply-chain integrity

Agent skills are executable instructions and deserve supply-chain treatment.

A portable control can:

- enumerate governed shared skills;
- lock each skill file to a deterministic digest;
- recompute digests in CI;
- fail on missing, extra, or unexpectedly changed skills;
- record compatibility/dependency metadata;
- keep upgrades reviewable and rollbackable through versioned repository history.

Public skill catalogs remain advisory inputs. A consuming system should independently review and pin what it adopts rather than track a public catalog automatically.

## Pattern D — frontend design contract before implementation

For material UI work, a portable `DESIGN.md`-style artifact can establish a contract before code generation. Useful sections include:

1. visual theme/accessibility intent,
2. color roles/tokens,
3. typography,
4. component states,
5. layout/spacing,
6. elevation/depth,
7. motion/interaction,
8. explicit do/don't rules,
9. responsive/touch behavior.

Implementation is then audited against the agreed contract.

A design contract must not automatically require 3D, WebGL, large animation runtimes, parallax, cursor effects, autoplay media, or other CPU/GPU-heavy spectacle. Performance, reduced-motion, accessibility, and the target-device envelope remain higher-priority constraints.

## Threat/bypass analysis

- **Authority laundering:** a graph, memory store, skill registry, or design reference is called "the source of truth." Mitigation: explicit advisory/evidence classification and boundary checks.
- **False negatives:** a partial dependency scan looks empty. Mitigation: coverage status + failure provenance.
- **Stale certainty:** memory from an old revision is presented as current. Mitigation: revision/freshness binding.
- **Instruction drift:** a skill changes without review. Mitigation: deterministic lock validation.
- **Aesthetic overreach:** a design system forces heavy effects onto low-end clients. Mitigation: performance/accessibility constraints outrank spectacle.

## Public inspirations

This proposal was informed by public patterns observed in:

- `JordanCoin/codemap` — coverage-aware structural/dependency evidence;
- `0xK3vin/MegaMemory` — persistent concept-oriented project memory;
- `rampstackco/claude-skills` — skill integrity/catalog discipline;
- `cosmicstack-labs/mercury-agent-skills` — portable skill packaging/versioning ideas;
- `xiaopu-ai/web-design` — spec-first frontend design workflow.

The proposal intentionally does not vendor or require any of those projects.

## Public/private adoption boundary

`accepted-for-lab` means this design is retained as a useful public reference. It creates **no claim** that any private or production system uses the same implementation, schema, names, tools, or policy. External adopters should re-evaluate the failure mode and implement the smallest control appropriate to their own authority model.
