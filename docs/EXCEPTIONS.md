# Controlled Exceptions

Mature governance needs an explicit way to handle genuine exceptions without teaching agents to bypass policy.

A waiver record should include control id, exact scope, rationale, approving authority, issued/expiry times or conditions, compensating controls, required evidence, and review/rollback path. Machine-readable exceptions should be validated before use.

Exceptions never reorder authority globally. They apply only to the named control/action/scope and expire closed. See `schemas/exception.schema.json`.