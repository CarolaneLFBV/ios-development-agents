---
allowed-tools: [Read, Edit, TodoWrite, Task]
description: "Migration paths for iOS (UIKit→SwiftUI, CoreData→SwiftData, Swift 5→6)"
argument-hint: "[source] [target] [--strategy incremental|complete]"
---

# /ios:migrate - iOS Migration

Migrate `$ARGUMENTS` between frameworks, patterns, and Swift versions.

## Arguments
- `[target]` - Target framework/version
- `--strategy incremental|complete|hybrid` - Migration strategy
- `--validate` - Validate migration
- `--backup` - Create backup before migration

## Migration Paths
1. UIKit → SwiftUI
2. CoreData → SwiftData
3. Swift 5.x → Swift 6.2
4. ObservableObject → @Observable
5. Completion handlers → async/await
6. MVC → MVVM/TCA

## Examples
```bash
/ios:migrate uikit swiftui --strategy incremental
/ios:migrate coredata swiftdata --backup
/ios:migrate swift5 swift6 --validate
```

---

**Delegates to**: swift-specialist, swiftui-specialist, architecture-specialist
