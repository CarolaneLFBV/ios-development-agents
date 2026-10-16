---
description: "Audit or improve iOS accessibility, including VoiceOver and Dynamic Type."
argument-hint: "[target] [--level a|aa|aaa] [--fix]"
---

# /ios:accessibility

Audit `$ARGUMENTS` for VoiceOver, Dynamic Type, contrast, focus/keyboard behavior,
Reduce Motion, hit targets, and adaptive layout. Use SwiftUI specialist expertise;
work directly unless the user explicitly requests delegation.

- `--level a|aa|aaa` selects the WCAG reference level (default: aa).
- `--audit-only` leaves files unchanged and overrides `--fix`.
- `--fix` applies scoped, verifiable improvements.

Inspect actual labels, reading order, custom controls, images and error states.
Semantic colors alone do not prove contrast; measure the rendered combinations.
Use Accessibility Inspector and simulator/device assistive technology checks when
available. Include large accessibility sizes and long localized text for affected UI.
A static code review does not establish WCAG conformance.

Return prioritized findings with locations, changes, checks actually performed,
and remaining manual checks.
