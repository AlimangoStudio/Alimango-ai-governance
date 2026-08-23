# Plan: [TITLE]

## Constitution check

- authority order preserved
- fail-closed behavior preserved
- least capability preserved
- external inputs independently verified
- sensitive/private information excluded
- evidence gates defined before implementation

## Current-state inspection

Record actual files, interfaces, constraints, and existing controls inspected before design.

## Design

Describe the smallest architecture that satisfies the specification.

## Blast radius

List affected policies, workflows, schemas, validators, examples, CI, docs, and contributor behavior.

## Risk classification

`R0` research/read-only · `R1` reversible local change · `R2` governed external side effect · `R3` secrets/auth/data/deploy · `R4` destructive/irreversible/high-impact.

## Validation plan

List positive, negative, bypass, regression, and compatibility checks.

## Independent review

State reviewer scope and evidence to provide.

## Rollback

State how to revert without weakening existing controls.