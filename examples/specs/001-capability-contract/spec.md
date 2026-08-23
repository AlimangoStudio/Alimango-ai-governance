# Specification: Capability Contract Reference

**Status:** Complete

## Problem

An agent must not infer write permission from the existence of a repository-write tool.

## Desired outcome

A tool invocation is preceded by an explicit capability decision and yields postcondition evidence.

## Scope

Public synthetic repository-write example only.

## Requirements

- **R1:** Tool availability must not grant authorization.
- **R2:** The decision must name action, target, risk, capabilities, and result.
- **R3:** Material side effects must emit postcondition evidence.

## Acceptance evidence

Reference action policy, typed decision schema, example decision, and executable evaluator agree on the decision model.

## Public/private boundary

The fixture contains no private source, credentials, production targets, or automatic promotion path.
