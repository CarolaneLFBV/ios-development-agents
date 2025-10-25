# PRINCIPLES.md - iOS Development Principles

Core principles for iOS development following Apple's Human Interface Guidelines and Swift best practices.

## Apple Human Interface Guidelines

### Design Principles

**1. Clarity**
- Text is legible at every size
- Icons are precise and lucid
- Adornments are subtle and appropriate
- Functionality drives design

**2. Deference**
- Fluid motion and crisp interface help people understand
- Content fills the entire screen
- Translucency and blurring hint at more content
- Minimal use of bezels, gradients, and shadows

**3. Depth**
- Visual layers and realistic motion convey hierarchy
- Touch and discoverability heighten delight
- Transitions provide context
- Maintain clarity and efficiency

### Interface Essentials

**Navigation**
- Hierarchical (drill down)
- Flat (switch between categories)
- Content-driven (move freely)

**User Input**
- Touch gestures
- Keyboards
- Voice and dictation
- Game controllers

**Visual Design**
- Color and contrast
- Typography
- SF Symbols
- Animation and motion

## Swift Best Practices

### Swift 6.2 Modern Patterns

**1. Observable Macro**
```swift
// ✅ GOOD: Modern @Observable
@Observable
class ViewModel {
    var items: [Item] = []
}

// ❌ AVOID: Legacy ObservableObject
class ViewModel: ObservableObject {
    @Published var items: [Item] = []
}
```

**2. Async/Await**
```swift
// ✅ GOOD: Structured concurrency
func loadData() async throws -> Data {
    try await networkService.fetchData()
}

// ❌ AVOID: Completion handlers
func loadData(completion: @escaping (Result<Data, Error>) -> Void) {
    // Old pattern
}
```

**3. Value Semantics**
```swift
// ✅ GOOD: Struct for data models
struct User {
    let id: UUID
    var name: String
}

// ❌ AVOID: Class for simple data
class User {
    let id: UUID
    var name: String
}
```

### Swift API Design Guidelines

1. **Clarity at the point of use** is your most important goal
2. **Clarity is more important than brevity**
3. **Write a documentation comment** for every declaration
4. **Omit needless words**
5. **Name variables, parameters, and associated types** according to their roles
6. **Compensate for weak type information**
7. **Strive for fluent usage**
8. **Begin names of factory methods with "make"**
9. **Name functions and methods according to their side effects**

## Architecture Patterns

### MVVM (Recommended for most apps)

```swift
// Model
struct User { }

// View
struct UserView: View {
    @State private var viewModel = UserViewModel()
    var body: some View { }
}

// ViewModel
@Observable
class UserViewModel {
    var user: User?

    func loadUser() async { }
}
```

**When to use MVVM**:
- Standard iOS apps
- Simple to moderate complexity
- Team familiar with pattern
- SwiftUI-first development

### TCA (The Composable Architecture)

```swift
@Reducer
struct Feature {
    @ObservableState
    struct State { }

    enum Action { }

    var body: some ReducerOf<Self> { }
}
```

**When to use TCA**:
- Complex state management
- Predictable state changes
- Comprehensive testing needs
- Large teams

### Clean Architecture

```
Presentation ← Domain → Data
(Views, VMs)  (Entities) (Repos)
```

**When to use Clean**:
- Large applications
- Multiple platforms
- Long-term maintenance
- Strict separation needs

## SwiftUI Best Practices

### View Composition

```swift
// ✅ GOOD: Small, focused views
struct ProfileView: View {
    var body: some View {
        VStack {
            ProfileHeader()
            ProfileContent()
            ProfileActions()
        }
    }
}

// ❌ AVOID: Monolithic views
struct ProfileView: View {
    var body: some View {
        VStack {
            // 200 lines of UI code
        }
    }
}
```

### State Management

```swift
// ✅ GOOD: Appropriate state scope
struct ContentView: View {
    @State private var isExpanded = false // Local state

    var body: some View {
        ExpandableSection(isExpanded: $isExpanded)
    }
}

// ❌ AVOID: Over-scoped state
@Observable
class AppState {
    var isExpanded = false // Too global
}
```

### Performance

```swift
// ✅ GOOD: LazyVStack for lists
ScrollView {
    LazyVStack {
        ForEach(items) { item in
            ItemRow(item: item)
        }
    }
}

// ❌ AVOID: VStack for long lists
ScrollView {
    VStack {
        ForEach(items) { item in
            ItemRow(item: item)
        }
    }
}
```

## SwiftData Best Practices

### Model Design

```swift
// ✅ GOOD: Clean model with relationships
@Model
final class Task {
    var title: String
    var isCompleted: Bool

    @Relationship(deleteRule: .cascade)
    var subtasks: [Task]

    init(title: String) {
        self.title = title
        self.isCompleted = false
    }
}

// ❌ AVOID: Business logic in models
@Model
final class Task {
    var title: String

    func validate() -> Bool { } // Business logic
}
```

### Query Optimization

```swift
// ✅ GOOD: Filtered and sorted queries
@Query(
    filter: #Predicate<Task> { $0.isCompleted == false },
    sort: [SortDescriptor(\.createdAt, order: .reverse)]
)
var activeTasks: [Task]

// ❌ AVOID: Unfiltered queries
@Query var tasks: [Task]
var activeTasks: [Task] {
    tasks.filter { !$0.isCompleted }
}
```

## Accessibility Principles

### VoiceOver Support

```swift
// ✅ GOOD: Descriptive labels
Button("Save") {
    save()
}
.accessibilityLabel("Save profile")
.accessibilityHint("Saves your profile changes")

// ❌ AVOID: Missing labels
Button(action: save) {
    Image(systemName: "checkmark")
}
```

### Dynamic Type

```swift
// ✅ GOOD: Dynamic Type support
Text("Title")
    .font(.title)

// ❌ AVOID: Fixed font sizes
Text("Title")
    .font(.system(size: 24))
```

### Color Contrast

```swift
// ✅ GOOD: Semantic colors
Text("Important")
    .foregroundStyle(.primary)

// ❌ AVOID: Fixed colors
Text("Important")
    .foregroundColor(.black)
```

## Performance Principles

### Memory Management

```swift
// ✅ GOOD: Weak references
class ViewController {
    var completion: (() -> Void)?

    func setup() {
        someService.onComplete = { [weak self] in
            self?.completion?()
        }
    }
}

// ❌ AVOID: Strong reference cycles
class ViewController {
    var completion: (() -> Void)?

    func setup() {
        someService.onComplete = {
            self.completion?()
        }
    }
}
```

### Async Work

```swift
// ✅ GOOD: Background work
Task.detached(priority: .background) {
    let result = await heavyComputation()
    await MainActor.run {
        updateUI(with: result)
    }
}

// ❌ AVOID: Blocking main thread
let result = heavyComputation()
updateUI(with: result)
```

## Testing Principles

### Test Pyramid

```
     /\
    /E2E\      ← Few (UI tests)
   /------\
  / Integ  \   ← Some (Integration)
 /----------\
/   Unit     \ ← Many (Unit tests)
/--------------\
```

### Test Quality

```swift
// ✅ GOOD: Descriptive test names
func testUserViewModel_LoadUsers_SetsLoadingState() async {
    // Given
    let viewModel = UserViewModel()

    // When
    let loadTask = Task { await viewModel.loadUsers() }

    // Then
    XCTAssertTrue(viewModel.isLoading)
    await loadTask.value
}

// ❌ AVOID: Vague names
func testLoad() {
    // Test code
}
```

## Security Principles

### Secure Storage

```swift
// ✅ GOOD: Keychain for sensitive data
KeychainManager.save(apiKey, for: "apiKey")

// ❌ AVOID: UserDefaults for secrets
UserDefaults.standard.set(apiKey, forKey: "apiKey")
```

### Network Security

```swift
// ✅ GOOD: HTTPS only
let url = URL(string: "https://api.example.com")!

// ❌ AVOID: HTTP
let url = URL(string: "http://api.example.com")!
```

## Code Organization

### File Structure

```
MyApp/
├── App/
│   ├── MyApp.swift
│   └── AppDelegate.swift
├── Features/
│   ├── Authentication/
│   │   ├── Views/
│   │   ├── ViewModels/
│   │   └── Models/
│   └── Profile/
├── Core/
│   ├── Networking/
│   ├── Storage/
│   └── Utilities/
└── Resources/
    ├── Assets.xcassets
    └── Localizable.strings
```

### Swift Package Structure

```
Package/
├── Package.swift
├── Sources/
│   ├── Core/
│   ├── UI/
│   └── Models/
└── Tests/
    ├── CoreTests/
    └── UITests/
```

## Quality Standards

### Code Review Checklist
- [ ] Follows Swift API Design Guidelines
- [ ] Apple HIG compliance
- [ ] Accessibility support (WCAG AA)
- [ ] Unit tests (≥80% coverage)
- [ ] Performance considerations
- [ ] Security best practices
- [ ] Documentation comments
- [ ] No force unwrapping
- [ ] Proper error handling

### Definition of Done
- [ ] Feature implemented
- [ ] Tests written and passing
- [ ] Code reviewed and approved
- [ ] Documentation updated
- [ ] Accessibility validated
- [ ] Performance profiled
- [ ] Security checked
- [ ] Integrated and tested

---

**Remember**: These principles guide decisions, but context matters. Always consider the specific needs of your app and users.
