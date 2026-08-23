from __future__ import annotations

import importlib.util
import json
import math
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECOVERY_PATH = ROOT / "scripts/governance_recovery.py"
COMPILE_PATH = ROOT / "scripts/compile_context.py"
UNLAZY_PATH = ROOT / "scripts/unlazy_check.py"


def load_recovery():
    spec = importlib.util.spec_from_file_location("public_governance_recovery", RECOVERY_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


RECOVERY = load_recovery()


def estimate_tokens(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    return max(1, math.ceil(len(text) / 4))


class RecoveryDecisionTests(unittest.TestCase):
    def test_policy_denial_never_retries_or_dispatches(self) -> None:
        decision = RECOVERY.decide(
            failure_class=RECOVERY.FailureClass.POLICY_DENIAL,
            gate_id="authorization",
            attempt=1,
            production=False,
            fallback_mode="degrade_read_only",
        )
        self.assertEqual(decision.status, RECOVERY.RecoveryStatus.BLOCKED)
        self.assertFalse(decision.retry)
        self.assertFalse(decision.may_dispatch_side_effect)

    def test_approval_required_is_distinct_hitl(self) -> None:
        self.assertEqual(
            RECOVERY.classify_exit_code(11, "authorization"),
            RECOVERY.FailureClass.APPROVAL_REQUIRED,
        )
        decision = RECOVERY.decide(
            failure_class=RECOVERY.FailureClass.APPROVAL_REQUIRED,
            gate_id="authorization",
            attempt=1,
            production=False,
            fallback_mode="degrade_read_only",
        )
        self.assertEqual(decision.status, RECOVERY.RecoveryStatus.SUSPENDED_HITL)
        self.assertTrue(decision.triage_required)
        self.assertFalse(decision.retry)
        self.assertFalse(decision.may_dispatch_side_effect)

    def test_unknown_gate_defaults_hard(self) -> None:
        self.assertEqual(RECOVERY.resolve_gate_class("misspelled-unlazy"), RECOVERY.GateClass.HARD)
        self.assertEqual(
            RECOVERY.classify_exit_code(1, "misspelled-unlazy"),
            RECOVERY.FailureClass.POLICY_DENIAL,
        )
        injected = RECOVERY.decide(
            failure_class=RECOVERY.FailureClass.QUALITY_FAILURE,
            gate_id="authorization",
            attempt=3,
            production=False,
            fallback_mode="degrade_read_only",
        )
        self.assertEqual(injected.status, RECOVERY.RecoveryStatus.BLOCKED)
        self.assertFalse(injected.may_dispatch_side_effect)

    def test_quality_exhaustion_is_unverified_not_green(self) -> None:
        first = RECOVERY.decide(
            failure_class=RECOVERY.FailureClass.QUALITY_FAILURE,
            gate_id="unlazy",
            attempt=1,
            max_attempts=3,
        )
        final = RECOVERY.decide(
            failure_class=RECOVERY.FailureClass.QUALITY_FAILURE,
            gate_id="unlazy",
            attempt=3,
            max_attempts=3,
        )
        self.assertEqual(first.status, RECOVERY.RecoveryStatus.RETRY)
        self.assertEqual(final.status, RECOVERY.RecoveryStatus.BEST_EFFORT_UNVERIFIED)
        self.assertTrue(final.may_continue_text)
        self.assertFalse(final.claim_green)
        self.assertFalse(final.may_dispatch_side_effect)

    def test_bypass_mode_rejected(self) -> None:
        with self.assertRaises(ValueError):
            RECOVERY.decide(
                failure_class=RECOVERY.FailureClass.TRANSIENT,
                gate_id="authorization",
                attempt=3,
                production=False,
                fallback_mode="bypass_warn",
            )

    def test_optional_omission_and_required_block(self) -> None:
        placeholder, evidence = RECOVERY.omit_context(
            source_id="synthetic-advisory",
            reason="PROVENANCE_VERIFICATION_FAILED",
            content="synthetic public content",
        )
        self.assertEqual(placeholder, RECOVERY.OMISSION_PLACEHOLDER)
        self.assertFalse(evidence["included"])
        self.assertTrue(evidence["content_sha256"])
        with self.assertRaises(RECOVERY.ProvenanceBlock):
            RECOVERY.omit_context(
                source_id="required-authority",
                reason="PROVENANCE_VERIFICATION_FAILED",
                mandatory_authority=True,
            )
        with self.assertRaises(RECOVERY.ProvenanceBlock):
            RECOVERY.omit_context(
                source_id="authorization-evidence",
                reason="PROVENANCE_VERIFICATION_FAILED",
                required_for_authorization=True,
            )


class ContextCompilerRecoveryTests(unittest.TestCase):
    def run_compile(self, request: dict[str, object]) -> subprocess.CompletedProcess[str]:
        with tempfile.NamedTemporaryFile("w", suffix=".json", encoding="utf-8", delete=False) as handle:
            json.dump(request, handle)
            request_path = Path(handle.name)
        try:
            return subprocess.run(
                [sys.executable, str(COMPILE_PATH), "--request", str(request_path)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
        finally:
            request_path.unlink(missing_ok=True)

    def base_sources(self) -> list[dict[str, object]]:
        return [{
            "id": "constitution",
            "authority": "constitution",
            "path": ".specify/memory/constitution.md",
            "required": True,
            "sensitivity": "public",
        }]

    def test_optional_public_provenance_failure_is_omitted(self) -> None:
        sources = self.base_sources() + [{
            "id": "optional-advisory",
            "authority": "external",
            "path": "README.md",
            "sensitivity": "public",
            "provenance_verified": False,
        }]
        result = self.run_compile({"task": "synthetic test", "budget_tokens": 50000, "sources": sources})
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["status"], "compiled_with_omissions")
        self.assertEqual(payload["omitted_source_count"], 1)
        self.assertIn(RECOVERY.OMISSION_PLACEHOLDER, payload["context"])
        self.assertEqual(payload["manifest"]["omissions"][0]["reason"], "PROVENANCE_VERIFICATION_FAILED")

    def test_authorization_critical_provenance_failure_blocks(self) -> None:
        sources = self.base_sources() + [{
            "id": "authorization-evidence",
            "authority": "external",
            "path": "README.md",
            "sensitivity": "public",
            "provenance_verified": False,
            "required_for_authorization": True,
        }]
        result = self.run_compile({"task": "synthetic test", "budget_tokens": 50000, "sources": sources})
        self.assertEqual(result.returncode, 2)
        self.assertIn("authorization-critical source provenance unavailable", result.stderr)

    def test_authorization_critical_source_cannot_be_budget_dropped(self) -> None:
        constitution = ROOT / ".specify/memory/constitution.md"
        readme = ROOT / "README.md"
        constitution_tokens = estimate_tokens(constitution)
        readme_tokens = estimate_tokens(readme)
        budget = constitution_tokens + max(1, readme_tokens // 2)
        sources = self.base_sources() + [{
            "id": "authorization-evidence",
            "authority": "external",
            "path": "README.md",
            "sensitivity": "public",
            "required_for_authorization": True,
        }]
        result = self.run_compile({"task": "synthetic test", "budget_tokens": budget, "sources": sources})
        self.assertEqual(result.returncode, 2)
        self.assertIn("required authority/authorization sources exceed budget", result.stderr)

    def test_non_public_source_remains_hard_block(self) -> None:
        sources = self.base_sources() + [{
            "id": "forbidden-source",
            "authority": "external",
            "path": "README.md",
            "sensitivity": "private",
            "provenance_verified": False,
        }]
        result = self.run_compile({"task": "synthetic test", "budget_tokens": 50000, "sources": sources})
        self.assertEqual(result.returncode, 2)
        self.assertIn("public compiler refuses non-public source", result.stderr)


class UnlazyRecoveryTests(unittest.TestCase):
    def run_unlazy(self, root: Path, attempt: int) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(UNLAZY_PATH), str(root), "--attempt", str(attempt), "--max-corrections", "3"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_third_quality_attempt_is_distinct_nonzero_unverified(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "spec.md").write_text("# Spec\n\nTODO improve wording\n", encoding="utf-8")
            (root / "convergence.md").write_text("# Convergence\n\nCOMPLETE\n", encoding="utf-8")
            result = self.run_unlazy(root, 3)
            self.assertEqual(result.returncode, 20)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["terminal_state"], "best_effort_unverified")
            self.assertFalse(payload["claim_green"])
            self.assertTrue(payload["may_continue_output"])
            self.assertFalse(payload["merge_or_deploy_allowed"])

    def test_hard_gate_never_becomes_best_effort(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "GATES.md").write_text("| gate | state |\n| --- | --- |\n| auth | BLOCKED |\n", encoding="utf-8")
            (root / "convergence.md").write_text("# Convergence\n\nCOMPLETE\n", encoding="utf-8")
            result = self.run_unlazy(root, 3)
            self.assertEqual(result.returncode, 2)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["terminal_state"], "blocked")
            self.assertFalse(payload["merge_or_deploy_allowed"])


if __name__ == "__main__":
    unittest.main()
