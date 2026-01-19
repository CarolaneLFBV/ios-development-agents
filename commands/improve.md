---
allowed-tools: [Read, Grep, Glob, Edit, TodoWrite, Task]
description: "Improve iOS code quality, performance, and maintainability"
argument-hint: "[target] [--focus performance|accessibility|architecture]"
---

# /ios:improve - iOS Code Improvement

Improve code from `$ARGUMENTS` for quality, performance, and maintainability.

## Arguments
- `--focus performance|accessibility|architecture|quality` - Improvement focus
- `--type swift-modern|swiftui|swiftdata|patterns` - Specific improvement type
- `--safe` - Apply only safe, low-risk improvements
- `--preview` - Show improvements without applying
- `--iterative` - Apply improvements in multiple passes
- `--to observable|swiftdata|async|actor` - Refactor to modern pattern
- `--extract` - Extract components, protocols, or modules
- `--rename` - Rename with codebase-wide updates

## Auto-Activation
- **performance-specialist**: Performance optimization
- **swiftui-specialist**: SwiftUI improvements
- **swift-specialist**: Swift modernization
- **architecture-specialist**: Pattern improvements

## Improvement Types

### Swift Modernization (--type swift-modern)
```swift
// Before:
class UserViewModel: ObservableObject {
    @Published var user: User?
    func loadUser() { Task { user = try await repository.fetchUser() } }
}

// After:
@Observable
class UserViewModel {
    var user: User?
    private let repository: UserRepositoryProtocol

    init(repository: UserRepositoryProtocol = UserRepository()) {
        self.repository = repository
    }

    func loadUser() async {
        isLoading = true
        defer { isLoading = false }
        user = try? await repository.fetchUser()
    }
}
```

### Performance (--focus performance)
```swift
// Before:
VStack { ForEach(items) { ItemRow(item: $0) } }

// After:
LazyVStack(spacing: 8, pinnedViews: [.sectionHeaders]) {
    ForEach(items, id: \.id) { ItemRow(item: $0).id($0.id) }
}
```

### Accessibility (--focus accessibility)
```swift
// Before:
Button(action: { viewModel.save() }) { Image(systemName: "checkmark") }

// After:
Button(action: { viewModel.save() }) { Image(systemName: "checkmark") }
    .accessibilityLabel("Save profile")
    .accessibilityHint("Saves your profile changes")
    .accessibilityIdentifier("saveButton")
```

### Architecture (--focus architecture)
```swift
// Before:
class DataService {
    func fetchData() async throws -> [Item] {
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode([Item].self, from: data)
    }
}

// After:
protocol DataServiceProtocol { func fetchData() async throws -> [Item] }

final class DataService: DataServiceProtocol {
    private let networkClient: NetworkClientProtocol
    init(networkClient: NetworkClientProtocol = NetworkClient()) {
        self.networkClient = networkClient
    }
    func fetchData() async throws -> [Item] {
        try await networkClient.request(endpoint: .items)
    }
}
```

## Improvement Strategies

### Swift Modernization
- Replace ObservableObject with @Observable
- Adopt async/await over completion handlers
- Use proper capture lists in closures

### SwiftUI Optimization
- Replace VStack with LazyVStack where appropriate
- Use task modifier for async operations
- Optimize view updates with proper state

### Memory Management
- Fix strong reference cycles with weak/unowned
- Optimize image loading and caching

### Code Quality
- Extract magic numbers to constants
- Improve naming for clarity
- Apply SOLID principles

## Refactoring Patterns (--to)

### To Observable (--to observable)
```swift
// Before:
class ViewModel: ObservableObject {
    @Published var items: [Item] = []
}

// After:
@Observable
class ViewModel {
    var items: [Item] = []
}
```

### To SwiftData (--to swiftdata)
```swift
// Before (Core Data):
@objc(ItemEntity)
class ItemEntity: NSManagedObject {
    @NSManaged var name: String
}

// After (SwiftData):
@Model
final class Item {
    var name: String
    init(name: String) { self.name = name }
}
```

### To Async/Await (--to async)
```swift
// Before:
func fetchData(completion: @escaping (Result<Data, Error>) -> Void) {
    URLSession.shared.dataTask(with: url) { data, _, error in
        completion(error.map { .failure($0) } ?? .success(data!))
    }.resume()
}

// After:
func fetchData() async throws -> Data {
    let (data, _) = try await URLSession.shared.data(from: url)
    return data
}
```

### To Actor (--to actor)
```swift
// Before:
class DataCache {
    private var cache: [String: Data] = [:]
    private let lock = NSLock()
    func get(_ key: String) -> Data? { lock.lock(); defer { lock.unlock() }; return cache[key] }
}

// After:
actor DataCache {
    private var cache: [String: Data] = [:]
    func get(_ key: String) -> Data? { cache[key] }
}
```

## Examples
```bash
/ios:improve Views/ --focus quality --safe --preview
/ios:improve ProductListView.swift --focus performance --iterative
/ios:improve . --focus accessibility
/ios:improve Services/ --focus architecture --type patterns
/ios:improve ViewModel.swift --to observable
/ios:improve DataService.swift --to async
/ios:improve Cache.swift --to actor
```

## Output Structure
```markdown
# Improvements: [Target]
## Summary: Files analyzed | Issues found | Applied | Risk level
## Changes Made: File | Issue | Solution | Impact
## Performance Impact: Before → After metrics
## Next Steps: Tests, profiling, verification
```

## Risk Assessment
- **Low Risk**: Formatting, naming, comments
- **Medium Risk**: Algorithm optimization, caching
- **High Risk**: Architecture changes, API modifications

---

**Delegates to**: performance-specialist (perf), swiftui-specialist (UI), swift-specialist (modernization), architecture-specialist (patterns)
