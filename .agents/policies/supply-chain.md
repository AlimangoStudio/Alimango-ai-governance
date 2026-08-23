# Supply-Chain Policy

For dependencies, skills, actions, containers, models, repositories, and generated bundles:

- pin immutable versions for reproducible/high-risk use;
- verify publisher/source and license;
- inspect install hooks, scripts, network behavior, binary artifacts, and requested permissions;
- avoid unreviewed remote execution patterns;
- minimize dependencies used only for convenience;
- document breaking changes and upgrade steps;
- never allow a public upstream to become an automatic authority feed.

A green upstream badge is evidence about upstream CI, not proof of local safety.