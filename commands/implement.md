---
description: "iOS feature implementation with SwiftUI/UIKit and architectural patterns"
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
specialist. Verify uncertain APIs in primary documentation or an available MCP;
resolve Context7 library IDs instead of assuming them.

Handle loading, errors, cancellation and applicable accessibility needs. Run
checks for affected behavior and report files changed, verified results and
remaining integration checks. Do not infer successful builds or accessibility from a template.
