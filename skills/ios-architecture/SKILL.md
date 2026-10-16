---
name: ios-architecture
description: "Design or change iOS module boundaries, dependency injection, and SwiftData/Core Data persistence. Use for architectural decisions and data migrations, rather than routine view or language edits."
---

# Architecture and persistence

Inspect existing boundaries, package versions, supported OS versions, and data
requirements. Preserve the established architecture; introduce a layer or dependency
only when it resolves a concrete need. Consult Apple/framework documentation for
version-sensitive behavior; Context7 is optional and library IDs must be resolved.

- Choose MVVM, TCA, Clean Architecture or a simpler design from the actual state,
  testability and team constraints. Do not add repositories or protocols by quota.
  Use the project's installed TCA version when touching reducers or dependencies.
- Make dependencies explicit at boundaries. Preserve useful error states and
  cancellation rather than converting failures to empty collections with `try?`.
- Choose SwiftData or Core Data from deployment, existing stores, migration and
  sync needs; do not automatically replace a working persistent store.
- Confine `ModelContext` and mutable models to their intended isolation domain.
  Use `@ModelActor` where appropriate for actor-owned persistence. Do not inject an
  arbitrary context into an unrelated actor or transfer live mutable models across
  isolation boundaries; use identifiers or Sendable snapshots when needed.
- Verify relationship inverses and delete direction. A cascade on a child-to-parent
  relationship can delete the parent. For CloudKit, verify schema compatibility,
  relationship optionality, defaults, and uniqueness restrictions against the SDK.
- For schema changes, preserve user data and test upgrade paths using representative
  old stores. An in-memory empty store does not validate migration or synchronization.

Work directly within scope without recursive delegation. Record durable decisions
only when useful or requested. Validate affected builds and persistence behavior;
report evidence, tradeoffs and checks requiring device or iCloud access.
