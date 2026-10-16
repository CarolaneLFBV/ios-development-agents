---
description: "Improve iOS code quality, performance, and maintainability"
argument-hint: "[target] [--focus performance|accessibility] [--to observable]"
---

# /ios:improve

Improve `$ARGUMENTS` within the requested scope. Inspect current behavior and
preserve the project's architecture and compatibility. Work directly unless
specialist delegation is explicitly requested.

- `--focus performance|accessibility|architecture|quality` selects expertise (default: quality).
- `--to observable|swiftdata|async|actor` requests a specific migration.
- `--safe` limits changes to low-risk improvements supported by evidence.
- `--preview` reports a proposed diff/plan without editing.
- `--iterative` permits small implementation/validation passes, stopping when the requested outcome is met.

Use the relevant specialist guidance. Establish a baseline before performance
claims. Observation does not provide actor isolation; async conversion must preserve
cancellation/errors; actors introduce reentrancy; persistence migrations must protect
existing data. Verify version support before adopting a newer API.

Avoid broad style rewrites, mandatory protocol layers or automatic lazy containers.
Run targeted regression checks after changes. Return applied/proposed changes,
rationale, actual verification and material limitations.
