---
allowed-tools: [Read, Edit, TodoWrite, Task]
description: "Migration paths for iOS (UIKit→SwiftUI, CoreData→SwiftData, Swift 5→6)"
category: "Migration & Transformation"
auto-persona: ["swift-specialist", "swiftui-specialist", "architecture-specialist"]
mcp-servers: ["context7"]
---

# /ios:migrate - iOS Migration

## Purpose
Migrate iOS projects between frameworks, patterns, and Swift versions.

## Usage
```bash
/ios:migrate [source] [target] [--strategy <strategy>]
```

## Arguments
- `[source]` - Source framework/version
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
