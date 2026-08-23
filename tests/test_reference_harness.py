from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def run_script(script: str, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [PYTHON, str(ROOT / "scripts" / script), *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


class ReferenceHarnessTests(unittest.TestCase):
    def test_repository_validators(self) -> None:
        for script in ("validate_public_lab.py", "validate_agent_controls.py"):
            result = run_script(script)
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

    def test_r4_requires_approval(self) -> None:
        result = run_script(
            "evaluate_action.py", "--action-id", "deploy_example", "--target", "synthetic", "--risk", "R4", "--capability", "deploy"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["decision"], "require_approval")

    def test_r4_with_approval_still_requires_evidence(self) -> None:
        result = run_script(
            "evaluate_action.py", "--action-id", "deploy_example", "--target", "synthetic", "--risk", "R4", "--capability", "deploy", "--approval-reference", "synthetic-approval"
        )
        payload = json.loads(result.stdout)
        self.assertEqual(payload["decision"], "allow_with_evidence")
        self.assertTrue(payload["required_evidence"])

    def test_automatic_public_to_private_promotion_is_denied(self) -> None:
        result = run_script(
            "evaluate_action.py", "--action-id", "automatic_public_to_private_governance_promotion", "--target", "private-governance", "--risk", "R1", "--capability", "repo_write"
        )
        self.assertEqual(json.loads(result.stdout)["decision"], "deny")

    def test_context_compiler_preserves_constitution(self) -> None:
        result = run_script("compile_context.py", "--request", "examples/context-request.json")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["status"], "compiled")
        self.assertIn("## SOURCE constitution [constitution]", payload["context"])
        self.assertLessEqual(payload["estimated_tokens"], payload["budget_tokens"])

    def test_context_compiler_rejects_non_public_source(self) -> None:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False) as handle:
            json.dump({
                "task": "negative sensitivity fixture",
                "budget_tokens": 2000,
                "sources": [{
                    "id": "constitution", "authority": "constitution", "path": ".specify/memory/constitution.md",
                    "sensitivity": "restricted", "reason": "negative test", "required": True
                }]
            }, handle)
            path = handle.name
        try:
            result = run_script("compile_context.py", "--request", path)
            self.assertEqual(result.returncode, 2)
            self.assertIn("refuses non-public source", result.stderr)
        finally:
            Path(path).unlink(missing_ok=True)

    def test_completed_spec_passes_spec_and_unlazy_checks(self) -> None:
        fixture = "examples/specs/001-capability-contract"
        for script in ("spec_check.py", "unlazy_check.py"):
            result = run_script(script, fixture)
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

    def test_audit_fingerprint_is_deterministic(self) -> None:
        first = run_script("audit_fingerprint.py", "AGENTS.md", ".agents/manifest.json", ".specify/memory/constitution.md")
        second = run_script("audit_fingerprint.py", "AGENTS.md", ".agents/manifest.json", ".specify/memory/constitution.md")
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(json.loads(first.stdout)["fingerprint"], json.loads(second.stdout)["fingerprint"])


if __name__ == "__main__":
    unittest.main()
