#!/usr/bin/env python3
"""Public reference primitives for bounded governance recovery.

This reference preserves useful text/read-only behavior where safe but never
turns governance failure into authorization for a side effect.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any, Mapping

OMISSION_PLACEHOLDER = "[Data block omitted: Content failed safety verification]"
POLICY_DENIAL_CODES = {10, 11, 12, 13}
TRANSIENT_CODES = {70, 71, 72, 75}


class GateClass(str, Enum):
    QUALITY = "quality"
    HARD = "hard"


class FailureClass(str, Enum):
    POLICY_DENIAL = "policy_denial"
    TRANSIENT = "transient_infrastructure"
    INTERNAL = "internal_governance_error"
    QUALITY_FAILURE = "quality_failure"


class RecoveryStatus(str, Enum):
    SUCCESS = "SUCCESS"
    RETRY = "RETRY"
    BLOCKED = "BLOCKED"
    DEGRADED_READ_ONLY = "DEGRADED_READ_ONLY"
    SUSPENDED_HITL = "SUSPENDED_HITL"
    BEST_EFFORT_UNVERIFIED = "BEST_EFFORT_UNVERIFIED"


@dataclass(frozen=True)
class RecoveryDecision:
    status: RecoveryStatus
    retry: bool
    may_continue_text: bool
    may_dispatch_side_effect: bool
    claim_green: bool
    triage_required: bool
    message: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["status"] = self.status.value
        return data


class ProvenanceBlock(ValueError):
    pass


def digest_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def decide(
    *,
    failure_class: FailureClass,
    gate_class: GateClass,
    attempt: int,
    max_attempts: int = 3,
    production: bool = True,
    fallback_mode: str = "human_triage",
) -> RecoveryDecision:
    if attempt < 1 or max_attempts < 1:
        raise ValueError("attempts must be positive")
    if fallback_mode not in {"degrade_read_only", "human_triage"}:
        raise ValueError("unsupported fallback mode; bypass modes are prohibited")

    if failure_class == FailureClass.POLICY_DENIAL:
        return RecoveryDecision(
            RecoveryStatus.BLOCKED, False, True, False, False, False,
            "Deterministic governance denial remains blocking.",
        )

    if failure_class == FailureClass.QUALITY_FAILURE and gate_class == GateClass.QUALITY:
        if attempt < max_attempts:
            return RecoveryDecision(
                RecoveryStatus.RETRY, True, True, False, False, False,
                "Quality correction remains within its bounded attempt budget.",
            )
        return RecoveryDecision(
            RecoveryStatus.BEST_EFFORT_UNVERIFIED, False, True, False, False, False,
            "Quality correction exhausted; useful output may continue without a GREEN claim.",
        )

    if failure_class == FailureClass.TRANSIENT and attempt < max_attempts:
        return RecoveryDecision(
            RecoveryStatus.RETRY, True, True, False, False, False,
            "Transient governance infrastructure may retry within bounds.",
        )

    if production or fallback_mode == "human_triage":
        return RecoveryDecision(
            RecoveryStatus.SUSPENDED_HITL, False, True, False, False, True,
            "Protected action remains blocked pending durable human triage.",
        )

    return RecoveryDecision(
        RecoveryStatus.DEGRADED_READ_ONLY, False, True, False, False, False,
        "Development recovery is limited to text/read-only capability.",
    )


def omit_context(
    *,
    source_id: str,
    reason: str,
    content: str | None = None,
    mandatory_authority: bool = False,
    required_for_authorization: bool = False,
) -> tuple[str, dict[str, Any]]:
    if mandatory_authority:
        raise ProvenanceBlock(f"mandatory authority provenance failed: {source_id}")
    if required_for_authorization:
        raise ProvenanceBlock(f"authorization-critical provenance failed: {source_id}")
    return OMISSION_PLACEHOLDER, {
        "source_id": source_id,
        "included": False,
        "reason": reason,
        "content_sha256": digest_text(content) if content is not None else None,
        "mandatory_authority": False,
        "required_for_authorization": False,
    }


def redact(value: Any) -> Any:
    sensitive = {"password", "secret", "token", "access_token", "refresh_token", "authorization", "api_key", "cookie"}
    if isinstance(value, Mapping):
        return {
            str(key): "[REDACTED]" if str(key).lower() in sensitive else redact(item)
            for key, item in value.items()
        }
    if isinstance(value, (list, tuple)):
        return [redact(item) for item in value]
    return value


def main() -> int:
    payload = {
        "scope": "public-goods-reference",
        "max_quality_attempts": 3,
        "policy_denial_codes": sorted(POLICY_DENIAL_CODES),
        "transient_codes": sorted(TRANSIENT_CODES),
        "placeholder": OMISSION_PLACEHOLDER,
        "bypass_mode_allowed": False,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
