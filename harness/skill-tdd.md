# Skill TDD Harness

Reusable agent skills should have behavioral fixtures.

For each skill, define representative task inputs, expected decisions/artifacts, forbidden outcomes, negative/adversarial cases, and compatibility assumptions. Test the skill as a contract rather than evaluating whether its prose “sounds good.”

Changes to a skill rerun its fixtures and any dependent control tests. A skill that broadens capability requires action-governance review.