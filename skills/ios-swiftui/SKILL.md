---
name: ios-swiftui
description: "Build or fix SwiftUI views, state, navigation, animations, accessibility, and localization. Use for UI behavior and layout, rather than language diagnostics or storage architecture."
---

# SwiftUI

Inspect nearby views, deployment targets, and the design system before editing.
Verify uncertain or new modifiers in Apple documentation or the installed SDK.
Context7 is optional; resolve its library ID instead of assuming an Apple catalog.

- Use Observation when supported (iOS 17+): `@State` owns view-local values or an
  observable reference; `@Binding` borrows parent state; `@Bindable` exposes bindings;
  `@Environment` reads injected state. Observation does not provide actor isolation.
  Preserve working `ObservableObject`/Combine implementations unless migration is
  requested or needed for the change.
- Follow existing navigation. Keep route identity stable, prefer identifiers over
  mutable model payloads, and distinguish modal tasks from drill-down navigation.
- Use `.task`/`.task(id:)` for view-scoped async work. Handle cancellation, loading,
  empty and failure states; prevent stale results from overwriting newer requests.
- Choose `List`, lazy stacks or eager stacks for actual content and interaction
  needs. Do not replace every stack with a lazy stack or assume extraction alone
  prevents view recomputation. Preserve stable collection IDs.
- Support Dynamic Type, VoiceOver, Reduce Motion, contrast and adaptive layouts.
  A semantic color or an accessibility label alone does not establish accessibility.
- Preserve existing localization resources. Prefer String Catalogs for modern
  Xcode projects, including plurals, translator comments and locale-aware formatting.
  Validate long text, RTL, and accessibility sizes when relevant.

Handle the requested UI work directly without recursive delegation. Run available
targeted checks; report which previews, simulator/device flows, and assistive
technology checks actually ran. Keep unverified behavior explicit.
