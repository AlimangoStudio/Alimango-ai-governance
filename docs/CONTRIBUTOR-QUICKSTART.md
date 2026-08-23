# Contributor Quickstart

## 1. Pick a failure mode

Start with `docs/FAILURE-MODE-CATALOG.md`. If your idea does not map cleanly, describe the new failure class first.

## 2. Choose the smallest useful artifact

- discussion for an early design question,
- issue for a concrete gap,
- proposal document for a control design,
- synthetic example for a reproducible mechanism,
- PR for code/docs/tests that reviewers can execute.

## 3. Build the evidence chain

A strong contribution usually looks like:

```text
failure mode -> control objective -> enforcement point -> evidence -> bypass test
```

Read `docs/EXPERIMENT-PROTOCOL.md` before making benchmark or security claims.

## 4. Validate locally

```bash
python scripts/validate_public_lab.py
```

The validator intentionally has no third-party Python dependencies.

## 5. Open a focused PR

Explain:

- what fails today,
- what your change enforces,
- where it is enforced,
- what evidence supports it,
- what it costs in complexity/latency/tokens,
- what it does **not** prove.

## Hard boundary

Never include private Alimango source, credentials, customer data, production architecture, or a mechanism that automatically promotes public changes into private governance.
