---
description: "Design UI/UX and system architecture with Apple HIG compliance"
argument-hint: "[component] [--scope ui|architecture|system] [--pattern mvvm]"
---

# /ios:design

Design the component/system described by `$ARGUMENTS`. Use existing product,
platform and architecture constraints. Produce a design proposal; implementation
requires implementation intent in the request. Work directly unless delegation is requested.

- `--scope ui|architecture|system` selects scope (default: ui).
- `--style minimal|bold|professional` conveys visual preference (default: minimal).
- `--platform ios|ipados|macos|visionos` selects platform (default: ios).
- `--pattern mvvm|tca|clean|viper` requests a pattern; otherwise preserve existing architecture.
- `--modules` explores useful module boundaries.
- `--diagram` includes an appropriate architecture/data-flow diagram.
- `--dark-mode` includes light/dark appearance behavior.

Use SwiftUI expertise for UI and architecture expertise for boundaries/persistence.
Check current Apple HIG and API availability where the design depends on them.
Cover state ownership, errors, navigation and accessibility where relevant. Avoid
mandatory abstraction layers, arbitrary file counts, or a universal spacing grid.

Return the proposal, tradeoffs and actionable implementation steps.
