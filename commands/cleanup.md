---
description: "Clean up iOS code, find dead code, unused resources, and technical debt"
argument-hint: "[target] [--type dead-code|imports|resources] [--fix]"
---

# /ios:cleanup

Inspect `$ARGUMENTS` for unused code/resources, imports or deprecated APIs. Report
by default; work directly unless delegation is explicitly requested.

- `--type dead-code|imports|resources|deprecated|all` selects scope (default: all).
- `--report` includes evidence and confidence.
- `--fix` applies confirmed cleanup within scope.
- `--dry-run` prevents edits and overrides `--fix`.
- `--aggressive` broadens detection; low-confidence results remain recommendations.

Check references across targets, packages, build scripts, Objective-C selectors,
storyboards, asset catalogs and dynamic loading before removal. Lack of a text
match alone does not prove dead code. Removing imports can affect exported symbols
or extension visibility; validate with the affected build.

Preserve public interfaces and dynamically referenced resources unless their removal
is part of the request and supported by evidence. Keep uncertain candidates intact.
Return locations, reasons, actions and build/test results.
