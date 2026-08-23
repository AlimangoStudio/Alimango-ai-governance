# Delivery and Release Policy

Implementation, test, review, merge, release, deployment, and live verification are distinct states.

Release/deployment actions require explicit capability and, for material environments, approval according to risk. Prefer reproducible versioned artifacts and approved automation over direct environment hotfixes. Define rollback/forward-repair before high-risk changes.

Post-deploy verification is required before claiming live success when deployment is in scope. A merged change is not automatically deployed.