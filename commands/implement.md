---
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, TodoWrite, Task]
description: "iOS feature implementation with SwiftUI/UIKit and architectural patterns"
wave-enabled: true
category: "Development & Implementation"
auto-persona: ["swiftui-specialist", "architecture-specialist", "swift-specialist"]
mcp-servers: ["context7"]
---

# /ios:implement - iOS Feature Implementation

## Purpose
Implement iOS features, components, and functionality with SwiftUI/UIKit, following Apple Human Interface Guidelines and modern architectural patterns.

## Usage
```bash
/ios:implement [feature-description] [--framework <framework>] [--pattern <pattern>] [--<flags>]
```

## Arguments
- `[feature-description]` - Clear description of the feature to implement
- `--framework swiftui|uikit|hybrid` - UI framework (default: swiftui)
- `--pattern mvvm|tca|clean` - Architecture pattern (default: mvvm)
- `--swiftdata` - Include SwiftData integration
- `--cloudkit` - Enable CloudKit synchronization
- `--with-tests` - Generate XCTest unit tests
- `--accessibility` - Include comprehensive accessibility support
- `--safe` - Use conservative, well-tested patterns
- `--agent <agent-name>` - Manually activate specific agent

## Auto-Activation Patterns

### Agents (Context-Dependent)
- **swiftui-specialist**: SwiftUI views, layouts, state management
  - Keywords: View, SwiftUI, layout, navigation, @State
  - Files: `*.swift` with SwiftUI imports

- **architecture-specialist**: Architecture patterns, SwiftData models
  - Keywords: MVVM, TCA, repository, SwiftData, @Model
  - Complex features requiring architectural decisions

- **swift-specialist**: Advanced Swift language features
  - Keywords: protocol, generic, async/await, InlineArray
  - Language-level implementations

- **testing-specialist**: Test generation (with --with-tests)
  - Auto-activates when --with-tests flag is used

## MCP Servers
- **context7**: Apple documentation, HIG guidelines, framework patterns

## Execution Workflow

### 1. Requirements Analysis
```
- Parse feature description and detect technology context
- Identify UI framework (SwiftUI vs UIKit)
- Determine architectural pattern requirements
- Assess complexity and scope
```

### 2. Agent & Pattern Selection
```
- Auto-activate relevant specialists
- Select architecture pattern (MVVM/TCA/Clean)
- Determine data persistence strategy
- Route to specialized agents if needed
```

### 3. Implementation Phase
```
- Generate SwiftUI views or UIKit components
- Implement ViewModels with @Observable
- Create SwiftData models if needed
- Apply architectural pattern
- Follow Apple HIG guidelines
- Ensure accessibility support
```

### 4. Testing & Validation
```
- Generate XCTests if requested
- Validate against requirements
- Check accessibility compliance
- Ensure Safe Area handling
- Verify iOS version compatibility
```

### 5. Documentation & Integration
```
- Document implementation decisions
- Provide usage examples
- List integration steps
- Suggest testing strategies
```

## Examples

### SwiftUI View with MVVM
```bash
/ios:implement UserProfileView --framework swiftui --pattern mvvm
```

Expected Output:
```swift
// UserProfileView.swift
import SwiftUI

struct UserProfileView: View {
    @State private var viewModel = UserProfileViewModel()

    var body: some View {
        ScrollView {
            VStack(spacing: 20) {
                AsyncImage(url: viewModel.user.avatarURL) { image in
                    image
                        .resizable()
                        .aspectRatio(contentMode: .fill)
                } placeholder: {
                    ProgressView()
                }
                .frame(width: 100, height: 100)
                .clipShape(Circle())

                Text(viewModel.user.name)
                    .font(.title)

                Text(viewModel.user.email)
                    .font(.subheadline)
                    .foregroundStyle(.secondary)

                Button("Edit Profile") {
                    viewModel.showEditProfile()
                }
                .buttonStyle(.bordered)
            }
            .padding()
        }
        .navigationTitle("Profile")
        .task {
            await viewModel.loadUser()
        }
    }
}

// UserProfileViewModel.swift
import Foundation
import Observation

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

        do {
            user = try await repository.fetchCurrentUser()
        } catch {
            print("Error loading user: \(error)")
        }
    }

    func showEditProfile() {
        // Navigation logic
    }
}
```

### SwiftData Feature
```bash
/ios:implement TaskManager --swiftdata --pattern mvvm --with-tests
```

Expected Output:
```swift
// Task.swift (SwiftData Model)
import Foundation
import SwiftData

@Model
final class Task {
    var id: UUID
    var title: String
    var isCompleted: Bool
    var createdAt: Date
    var dueDate: Date?

    @Relationship(deleteRule: .nullify, inverse: \Category.tasks)
    var category: Category?

    init(title: String, category: Category? = nil, dueDate: Date? = nil) {
        self.id = UUID()
        self.title = title
        self.isCompleted = false
        self.createdAt = Date()
        self.dueDate = dueDate
        self.category = category
    }
}

// TaskListViewModel.swift
import Foundation
import SwiftData
import Observation

@Observable
class TaskListViewModel {
    var tasks: [Task] = []
    var isLoading = false

    private let modelContext: ModelContext

    init(modelContext: ModelContext) {
        self.modelContext = modelContext
    }

    func loadTasks() {
        let descriptor = FetchDescriptor<Task>(
            sortBy: [SortDescriptor(\.createdAt, order: .reverse)]
        )

        do {
            tasks = try modelContext.fetch(descriptor)
        } catch {
            print("Error fetching tasks: \(error)")
        }
    }

    func createTask(title: String) {
        let task = Task(title: title)
        modelContext.insert(task)

        do {
            try modelContext.save()
            loadTasks()
        } catch {
            print("Error creating task: \(error)")
        }
    }

    func toggleTask(_ task: Task) {
        task.isCompleted.toggle()

        do {
            try modelContext.save()
        } catch {
            print("Error updating task: \(error)")
        }
    }

    func deleteTask(_ task: Task) {
        modelContext.delete(task)

        do {
            try modelContext.save()
            loadTasks()
        } catch {
            print("Error deleting task: \(error)")
        }
    }
}

// TaskListView.swift
import SwiftUI
import SwiftData

struct TaskListView: View {
    @Environment(\.modelContext) private var modelContext
    @State private var viewModel: TaskListViewModel?
    @State private var newTaskTitle = ""

    var body: some View {
        NavigationStack {
            Group {
                if let viewModel {
                    List {
                        ForEach(viewModel.tasks) { task in
                            TaskRow(task: task, onToggle: {
                                viewModel.toggleTask(task)
                            })
                        }
                        .onDelete { indexSet in
                            for index in indexSet {
                                viewModel.deleteTask(viewModel.tasks[index])
                            }
                        }
                    }
                } else {
                    ProgressView()
                }
            }
            .navigationTitle("Tasks")
            .toolbar {
                ToolbarItem(placement: .primaryAction) {
                    Button("Add", systemImage: "plus") {
                        // Show add task sheet
                    }
                }
            }
            .onAppear {
                if viewModel == nil {
                    viewModel = TaskListViewModel(modelContext: modelContext)
                    viewModel?.loadTasks()
                }
            }
        }
    }
}

// TaskListViewModelTests.swift (if --with-tests)
import XCTest
import SwiftData
@testable import TaskApp

final class TaskListViewModelTests: XCTestCase {
    var sut: TaskListViewModel!
    var modelContext: ModelContext!

    override func setUp() {
        super.setUp()

        let config = ModelConfiguration(isStoredInMemoryOnly: true)
        let container = try! ModelContainer(
            for: Task.self,
            configurations: config
        )
        modelContext = ModelContext(container)
        sut = TaskListViewModel(modelContext: modelContext)
    }

    func testCreateTask_AddsTaskToList() throws {
        // Given
        let title = "Test Task"

        // When
        sut.createTask(title: title)

        // Then
        XCTAssertEqual(sut.tasks.count, 1)
        XCTAssertEqual(sut.tasks.first?.title, title)
        XCTAssertFalse(sut.tasks.first!.isCompleted)
    }

    func testToggleTask_ChangesCompletionStatus() throws {
        // Given
        sut.createTask(title: "Test")
        let task = sut.tasks.first!

        // When
        sut.toggleTask(task)

        // Then
        XCTAssertTrue(task.isCompleted)
    }
}
```

### TCA Implementation
```bash
/ios:implement CounterFeature --pattern tca
```

### Full-Stack Feature
```bash
/ios:implement UserAuthentication --swiftdata --cloudkit --with-tests --accessibility
```

## Integration Features

### Framework Detection
- Auto-detects existing project framework
- Adapts code style to project conventions
- Uses project dependencies and Swift version

### Accessibility-First
- VoiceOver labels by default
- Dynamic Type support
- Keyboard navigation
- Sufficient color contrast
- Accessibility identifiers for testing

### Apple HIG Compliance
- Platform-appropriate controls
- Standard navigation patterns
- Consistent spacing and layout
- Native gestures and interactions
- Safe Area handling

### SwiftData Integration
- @Model definitions with proper relationships
- ModelContainer configuration
- Query optimization with #Predicate
- Migration strategy
- CloudKit sync setup (if --cloudkit)

## Output Structure

```markdown
# Implementation: [Feature Name]

## Summary
- Framework: SwiftUI/UIKit/Hybrid
- Pattern: MVVM/TCA/Clean
- iOS Version: 17.0+
- Complexity: Low/Medium/High

## Files Created
- `Views/FeatureView.swift` - Main view implementation
- `ViewModels/FeatureViewModel.swift` - Business logic
- `Models/Feature.swift` - SwiftData models (if applicable)
- `Tests/FeatureTests.swift` - Unit tests (if --with-tests)

## Architecture
[Diagram or description of component relationships]

## Key Features
- [Feature 1]
- [Feature 2]
- [Feature 3]

## Accessibility
- VoiceOver support: ✅
- Dynamic Type: ✅
- Keyboard navigation: ✅
- Color contrast: ✅

## Next Steps
1. Add to app navigation
2. Run tests: `⌘U`
3. Test on device
4. Verify accessibility with VoiceOver

## Integration Example
[Code showing how to integrate the feature]
```

## Best Practices

### Code Quality
- Follow Swift API Design Guidelines
- Use @Observable for ViewModels (iOS 17+)
- Prefer composition over inheritance
- Keep views small and focused
- Extract complex logic to ViewModels

### Performance
- Use LazyVStack/LazyHStack for lists
- Implement task modifier for async operations
- Avoid expensive computations in view body
- Optimize images and assets

### Architecture
- Clear separation of concerns
- Protocol-based abstractions
- Dependency injection
- Testable design

### Testing
- Unit tests for ViewModels
- UI tests for critical flows
- Snapshot tests for visual regression
- Mock repositories for testing

## Related Commands
- `/ios:improve` - Enhance existing implementation
- `/ios:refactor` - Refactor to different pattern
- `/ios:test` - Add or improve tests
- `/ios:review` - Code review
- `/ios:optimize` - Performance optimization

## Troubleshooting

### Common Issues

**SwiftData not saving**
```swift
// Ensure you call save()
try modelContext.save()
```

**@Observable not updating views**
```swift
// Make sure class is marked @Observable
@Observable
class ViewModel { }
```

**Safe Area issues in Safari**
```swift
// Use proper Safe Area handling
.safeAreaInset(edge: .bottom) {
    Color.clear.frame(height: 0)
}
```

---

**Delegates to**: swiftui-specialist (views), architecture-specialist (patterns), swift-specialist (language features), testing-specialist (tests)
