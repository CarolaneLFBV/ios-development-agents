---
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, TodoWrite, Task]
description: "iOS feature implementation with SwiftUI/UIKit and architectural patterns"
argument-hint: "[feature] [--framework swiftui|uikit] [--pattern mvvm|tca]"
---

# /ios:implement - iOS Feature Implementation

Implement iOS features using `$ARGUMENTS` as the feature description.

## Arguments
- `--framework swiftui|uikit|hybrid` - UI framework (default: swiftui)
- `--pattern mvvm|tca|clean` - Architecture pattern (default: mvvm)
- `--swiftdata` - Include SwiftData integration
- `--cloudkit` - Enable CloudKit synchronization
- `--with-tests` - Generate XCTest unit tests
- `--accessibility` - Include comprehensive accessibility support

## Auto-Activation
- **swiftui-specialist**: Views, layouts, state management
- **architecture-specialist**: Patterns, SwiftData models
- **swift-specialist**: Advanced language features
- **testing-specialist**: Test generation (with --with-tests)

## Execution Workflow

### 1. Requirements Analysis
- Parse feature description and detect technology context
- Identify UI framework and architecture pattern
- Assess complexity and scope

### 2. Implementation
- Generate SwiftUI views or UIKit components
- Implement ViewModels with @Observable
- Create SwiftData models if needed
- Apply architectural pattern
- Ensure accessibility support

### 3. Validation
- Generate XCTests if requested
- Check accessibility compliance
- Verify iOS version compatibility

## Examples

### SwiftUI + MVVM
```bash
/ios:implement UserProfileView --framework swiftui --pattern mvvm
```

```swift
// UserProfileView.swift
struct UserProfileView: View {
    @State private var viewModel = UserProfileViewModel()

    var body: some View {
        ScrollView {
            VStack(spacing: 20) {
                AsyncImage(url: viewModel.user.avatarURL) { image in
                    image.resizable().aspectRatio(contentMode: .fill)
                } placeholder: { ProgressView() }
                .frame(width: 100, height: 100)
                .clipShape(Circle())

                Text(viewModel.user.name).font(.title)
                Text(viewModel.user.email).font(.subheadline).foregroundStyle(.secondary)
            }
            .padding()
        }
        .navigationTitle("Profile")
        .task { await viewModel.loadUser() }
    }
}

// UserProfileViewModel.swift
@Observable
class UserProfileViewModel {
    var user: User = User.placeholder
    var isLoading = false

    private let repository: UserRepositoryProtocol

    init(repository: UserRepositoryProtocol = UserRepository()) {
        self.repository = repository
    }

    func loadUser() async {
        isLoading = true
        defer { isLoading = false }
        do { user = try await repository.fetchCurrentUser() }
        catch { print("Error: \(error)") }
    }
}
```

### SwiftData Feature
```bash
/ios:implement TaskManager --swiftdata --pattern mvvm --with-tests
```

```swift
// Task.swift
@Model
final class Task {
    var id: UUID
    var title: String
    var isCompleted: Bool
    var createdAt: Date

    @Relationship(deleteRule: .nullify, inverse: \Category.tasks)
    var category: Category?

    init(title: String, category: Category? = nil) {
        self.id = UUID()
        self.title = title
        self.isCompleted = false
        self.createdAt = Date()
        self.category = category
    }
}

// TaskListViewModel.swift
@Observable
class TaskListViewModel {
    var tasks: [Task] = []
    private let modelContext: ModelContext

    init(modelContext: ModelContext) { self.modelContext = modelContext }

    func loadTasks() {
        let descriptor = FetchDescriptor<Task>(
            sortBy: [SortDescriptor(\.createdAt, order: .reverse)]
        )
        tasks = (try? modelContext.fetch(descriptor)) ?? []
    }

    func createTask(title: String) {
        let task = Task(title: title)
        modelContext.insert(task)
        try? modelContext.save()
        loadTasks()
    }
}

// TaskListViewModelTests.swift
final class TaskListViewModelTests: XCTestCase {
    var sut: TaskListViewModel!

    override func setUp() {
        let config = ModelConfiguration(isStoredInMemoryOnly: true)
        let container = try! ModelContainer(for: Task.self, configurations: config)
        sut = TaskListViewModel(modelContext: ModelContext(container))
    }

    func testCreateTask_AddsTaskToList() {
        sut.createTask(title: "Test Task")
        XCTAssertEqual(sut.tasks.count, 1)
        XCTAssertEqual(sut.tasks.first?.title, "Test Task")
    }
}
```

## Integration Features

### Accessibility-First
- VoiceOver labels by default
- Dynamic Type support
- Keyboard navigation
- Accessibility identifiers for testing

### Apple HIG Compliance
- Platform-appropriate controls
- Standard navigation patterns
- Consistent spacing and Safe Area handling

### SwiftData Integration
- @Model definitions with relationships
- ModelContainer configuration
- Query optimization with #Predicate
- CloudKit sync setup (if --cloudkit)

## Output Structure
```markdown
# Implementation: [Feature]
## Summary: Framework | Pattern | iOS Version | Complexity
## Files Created: Views, ViewModels, Models, Tests
## Key Features: [List]
## Accessibility: VoiceOver ✅ | Dynamic Type ✅ | Keyboard ✅
## Next Steps: Integration, testing, verification
```

## Best Practices
- Use @Observable for ViewModels
- Prefer composition over inheritance
- Keep views small and focused
- Use LazyVStack for lists
- Protocol-based abstractions for testability

---

**Delegates to**: swiftui-specialist (views), architecture-specialist (patterns), swift-specialist (language), testing-specialist (tests)
