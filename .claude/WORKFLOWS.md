# Workflow policy

For a small fix, inspect the affected code, make the change and validate the relevant
behavior. For larger changes, map dependencies and proceed in verifiable increments.
Use a plan or ADR when it captures a real decision or the user requests one.

Data migrations need representative existing-store tests and a recovery strategy.
Security-sensitive changes need verification of affected trust boundaries. Release
preparation needs current Apple requirements and actual signing/distribution checks.
These are conditional requirements, not mandatory steps for every edit.

Report outcomes, evidence, and unresolved checks. Stop when the requested result is
achieved; do not continue speculative cleanup or repeated validation without cause.
