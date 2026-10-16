---
description: "Implement an iOS feature using the project's UI framework and architecture."
argument-hint: "[feature] [--framework swiftui|uikit] [--pattern mvvm|tca]"
---

# /ios:implement

Implement the feature in `$ARGUMENTS`. Inspect nearby code, targets, dependencies
and tests first. Work directly by default; delegate bounded work only when the
user explicitly requests specialists, sequencing dependent changes.

- `--framework swiftui|uikit|hybrid` chooses UI technology; otherwise follow the project (SwiftUI for an unconstrained new UI).
- `--pattern mvvm|tca|clean` requests architecture; otherwise preserve the existing design.
- `--swiftdata` includes persistence after checking deployment and schema requirements.
- `--cloudkit` includes sync after verifying compatible schema and capabilities.
- `--with-tests` adds meaningful tests using the target's supported framework.
- `--accessibility` requests a focused accessibility verification pass.

Use relevant architecture, SwiftUI, Swift and testing expertise without loading every
specialist. The UI role also owns UIKit/hybrid screens and its interop reference.
Use platform expertise for background work, notifications and extensions, architecture
for data/network policy, and StoreKit expertise for purchases and entitlements.
Verify uncertain APIs in primary documentation or the installed SDK.

Handle loading, errors, cancellation and applicable accessibility needs. Run
checks for affected behavior and report files changed, verified results and
remaining integration checks.
