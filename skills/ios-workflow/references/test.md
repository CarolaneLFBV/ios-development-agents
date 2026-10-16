<!-- Generated from commands/ by scripts/framework.py. -->

# /ios:test

Generate or run the tests requested in `$ARGUMENTS` using testing specialist
expertise. Work directly unless delegation is explicitly requested.

- `--type unit|ui|snapshot|performance|all` selects tests (default: unit).
- `--coverage` collects and reports coverage with available project tooling.
- `--generate` adds meaningful regression tests for existing behavior.
- `--fix` repairs demonstrated failures within scope, preserving intended behavior.

Inspect target/toolchain compatibility and existing suites. Use Swift Testing for
suitable new unit tests; preserve XCTest, and use XCTest/XCUITest for UI/performance.
Check the target's testing requirements and existing snapshot solution before
adding dependencies.

Keep fixtures isolated and async synchronization deterministic. Never start a Task
and immediately assume its loading-state mutation ran. Discover actual schemes,
test plans and installed simulators; use `swift test` for compatible packages.

Run relevant tests when possible. Report exact commands, passed/failed/skipped
results, measured coverage and blockers. Generated tests are not automatically passed tests.
