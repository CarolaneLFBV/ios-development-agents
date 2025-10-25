---
allowed-tools: [Read, Grep, Glob, Edit, TodoWrite, Task]
description: "Improve iOS code quality, performance, and maintainability"
wave-enabled: true
category: "Quality & Enhancement"
auto-persona: ["swiftui-specialist", "performance-specialist", "swift-specialist"]
mcp-servers: ["context7"]
---

# /ios:improve - iOS Code Improvement

## Purpose
Apply systematic improvements to iOS code including Swift modernization, SwiftUI optimization, performance enhancements, and architectural refactoring.

## Usage
```bash
/ios:improve [target] [--focus <area>] [--type <type>] [--<flags>]
```

## Arguments
- `[target]` - Files, directories, or specific components to improve
- `--focus performance|accessibility|architecture|quality` - Improvement focus area
- `--type swift-modern|swiftui|swiftdata|patterns` - Specific improvement type
- `--safe` - Apply only safe, low-risk improvements
- `--preview` - Show improvements without applying
- `--iterative` - Apply improvements in multiple passes

## Auto-Activation Patterns

### Agents
- **performance-specialist**: Performance optimization focus
- **swiftui-specialist**: SwiftUI-specific improvements
- **swift-specialist**: Swift 6.2 modernization
- **architecture-specialist**: Pattern improvements

### MCP Servers
- **context7**: Apple best practices, performance guides

## Improvement Types

### 1. Swift Modernization (--type swift-modern)

```bash
/ios:improve UserViewModel.swift --type swift-modern
```

**Before**:
```swift
class UserViewModel: ObservableObject {
    @Published var user: User?
    @Published var isLoading = false

    func loadUser() {
        isLoading = true

        Task {
            do {
                user = try await repository.fetchUser()
            } catch {
                print("Error: \(error)")
            }
            isLoading = false
        }
    }
}
```

**After**:
```swift
@Observable
class UserViewModel {
    var user: User?
    var isLoading = false

    private let repository: UserRepositoryProtocol

    init(repository: UserRepositoryProtocol = UserRepository()) {
        self.repository = repository
    }

    func loadUser() async {
        isLoading = true
        defer { isLoading = false }

        do {
            user = try await repository.fetchUser()
        } catch {
            print("Error: \(error)")
        }
    }
}
```

### 2. Performance Optimization (--focus performance)

```bash
/ios:improve ContentView.swift --focus performance
```

**Before**:
```swift
ScrollView {
    VStack {
        ForEach(items) { item in
            ItemRow(item: item)
        }
    }
}
```

**After**:
```swift
ScrollView {
    LazyVStack(spacing: 8, pinnedViews: [.sectionHeaders]) {
        ForEach(items, id: \.id) { item in
            ItemRow(item: item)
                .id(item.id)
        }
    }
}
```

### 3. Accessibility Improvements (--focus accessibility)

```bash
/ios:improve ProfileView.swift --focus accessibility
```

**Before**:
```swift
Button(action: { viewModel.save() }) {
    Image(systemName: "checkmark")
}
```

**After**:
```swift
Button(action: { viewModel.save() }) {
    Image(systemName: "checkmark")
}
.accessibilityLabel("Save profile")
.accessibilityHint("Saves your profile changes")
.accessibilityIdentifier("saveButton")
```

### 4. Architecture Improvements (--focus architecture)

```bash
/ios:improve DataService.swift --focus architecture
```

**Before**:
```swift
class DataService {
    func fetchData() async throws -> [Item] {
        let url = URL(string: "https://api.example.com/items")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode([Item].self, from: data)
    }
}
```

**After**:
```swift
protocol DataServiceProtocol {
    func fetchData() async throws -> [Item]
}

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

### Swift 6.2 Modernization
- ✅ Replace ObservableObject with @Observable
- ✅ Adopt async/await over completion handlers
- ✅ Use InlineArray for fixed-size collections
- ✅ Apply string interpolation defaults
- ✅ Leverage method key paths

### SwiftUI Optimization
- ✅ Replace VStack with LazyVStack where appropriate
- ✅ Use task modifier for async operations
- ✅ Optimize view updates with proper state
- ✅ Implement view identity for better diffing
- ✅ Extract subviews for reusability

### Memory Management
- ✅ Fix strong reference cycles with weak/unowned
- ✅ Use proper capture lists in closures
- ✅ Optimize image loading and caching
- ✅ Implement proper autoreleasepool usage

### Code Quality
- ✅ Extract magic numbers to constants
- ✅ Improve naming for clarity
- ✅ Reduce function complexity
- ✅ Apply SOLID principles
- ✅ Add documentation comments

## Examples

### Comprehensive Improvement
```bash
/ios:improve Views/ --focus quality --safe --preview
```

### Performance Audit
```bash
/ios:improve ProductListView.swift --focus performance --iterative
```

### Accessibility Compliance
```bash
/ios:improve . --focus accessibility
```

### Architecture Refactoring
```bash
/ios:improve Services/ --focus architecture --type patterns
```

## Output Structure

```markdown
# Improvements: [Target]

## Summary
- Files analyzed: X
- Issues found: Y
- Improvements applied: Z
- Risk level: Low/Medium/High

## Changes Made

### File: ContentView.swift
**Issue**: Using VStack for large lists causes performance issues
**Solution**: Replaced with LazyVStack
**Impact**: ⬆️ Performance, ⬇️ Memory usage

### File: UserViewModel.swift
**Issue**: Using deprecated ObservableObject
**Solution**: Migrated to @Observable macro
**Impact**: ⬆️ Code clarity, ⬇️ Boilerplate

## Performance Impact
- Load time: 2.5s → 0.8s (68% improvement)
- Memory usage: 45MB → 28MB (38% reduction)
- Frame rate: 45fps → 60fps

## Next Steps
1. Run tests to verify improvements
2. Profile with Instruments
3. Test on real devices
4. Monitor crash analytics
```

## Best Practices

### Safe Improvements (--safe)
- Non-breaking API changes only
- Preserve existing behavior
- No architectural changes
- Focus on optimization and cleanup

### Iterative Approach (--iterative)
1. First pass: Quick wins (naming, formatting)
2. Second pass: Performance optimizations
3. Third pass: Architectural improvements
4. Fourth pass: Comprehensive refactoring

### Risk Assessment
- **Low Risk**: Formatting, naming, comments
- **Medium Risk**: Algorithm optimization, caching
- **High Risk**: Architecture changes, API modifications

## Integration

### Pre-improvement Checklist
- [ ] Review existing functionality
- [ ] Check for existing tests
- [ ] Identify critical user paths
- [ ] Note performance baselines

### Post-improvement Validation
- [ ] Run all tests
- [ ] Profile with Instruments
- [ ] Verify accessibility
- [ ] Check memory usage
- [ ] Test on multiple devices

## Related Commands
- `/ios:optimize` - Performance-focused optimization
- `/ios:refactor` - Architectural refactoring
- `/ios:review` - Code review
- `/ios:analyze` - Deep analysis

---

**Delegates to**: performance-specialist (performance), swiftui-specialist (UI), swift-specialist (modernization), architecture-specialist (patterns)
