<!-- Generated from commands/ by scripts/framework.py. -->

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
The UI role covers UIKit/hybrid UI; platform expertise owns system execution and
extensions. Separate purchase entitlement policy from App Store release preparation.
Check current Apple HIG and API availability where the design depends on them.
Cover state ownership, errors, navigation and accessibility where relevant.

Return the proposal, tradeoffs and actionable implementation steps.
