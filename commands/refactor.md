---
allowed-tools: [Read, Edit, TodoWrite, Task]
description: "Refactor iOS code to modern patterns (MVVM, TCA, @Observable, SwiftData)"
category: "Development & Refactoring"
auto-persona: ["architecture-specialist", "swift-specialist", "swiftui-specialist"]
mcp-servers: ["context7"]
---

# /ios:refactor - iOS Code Refactoring

## Purpose
Refactor iOS code to modern Swift/SwiftUI patterns including @Observable migration, SwiftData adoption, and architectural pattern changes.

## Usage
```bash
/ios:refactor [target] [--pattern <pattern>] [--to <target>]
```

## Arguments
- `[target]` - Files or components to refactor
- `--pattern mvvm|tca|clean` - Target architecture pattern
- `--to observable|swiftdata|async` - Specific refactoring
- `--safe` - Conservative refactoring
- `--with-tests` - Update tests accordingly

## Refactoring Types

### 1. ObservableObject → @Observable
```bash
/ios:refactor UserViewModel.swift --to observable
```

### 2. CoreData → SwiftData
```bash
/ios:refactor Models/ --to swiftdata
```

### 3. Completion Handlers → Async/Await
```bash
/ios:refactor NetworkService.swift --to async
```

### 4. UIKit → SwiftUI
```bash
/ios:refactor ProfileViewController.swift --to swiftui
```

### 5. Pattern Migration
```bash
/ios:refactor . --pattern tca
```

## Examples

**Before (ObservableObject)**:
```swift
class ViewModel: ObservableObject {
    @Published var items: [Item] = []
}
```

**After (@Observable)**:
```swift
@Observable
class ViewModel {
    var items: [Item] = []
}
```

---

**Delegates to**: architecture-specialist (patterns), swift-specialist (language features), swiftui-specialist (UI patterns)
