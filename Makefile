.PHONY: validate test fingerprint

validate:
	python scripts/validate_public_lab.py
	python scripts/validate_agent_controls.py
	python scripts/capability_doctor.py --require python --require AGENTS.md
	python scripts/spec_check.py examples/specs/001-capability-contract
	python scripts/unlazy_check.py examples/specs/001-capability-contract

test:
	python -m unittest discover -s tests -p 'test_*.py' -v

fingerprint:
	python scripts/audit_fingerprint.py AGENTS.md .agents .specify control schemas harness
