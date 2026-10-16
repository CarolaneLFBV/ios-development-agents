---
description: "Migration paths for iOS (UIKit→SwiftUI, CoreData→SwiftData, Swift 5→6)"
argument-hint: "[source] [target] [--strategy incremental|complete]"
---

# /ios:migrate

Migrate the source/target described by `$ARGUMENTS`. Inspect compatibility,
dependencies, store formats and public behavior before changing them. Work directly
using the owning specialist's expertise unless delegation is explicitly requested.

- `--strategy incremental|complete|hybrid` selects approach (default: incremental).
- `--validate` emphasizes compatibility and regression verification.
- `--backup` creates a non-destructive backup appropriate to the affected data/files.
- `--adr` records the decision and tradeoffs.

Route UIKit/Observation UI work to SwiftUI expertise, data/architecture work to
architecture expertise, and language/concurrency work to Swift expertise.
Separate compiler upgrades from Swift language-mode and isolation-setting changes.
Preserve error/cancellation behavior when converting callbacks to async.

Do not default Core Data-to-SwiftData migrations to full replacement. Plan schema
mapping, representative existing-store upgrade tests, CloudKit implications and
recovery. Empty in-memory tests do not establish migration safety.

Apply bounded steps and run relevant checks. Report changed behavior, preserved
compatibility, validation evidence and unresolved rollout/data risks.
