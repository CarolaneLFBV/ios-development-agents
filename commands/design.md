---
allowed-tools: [Read, Write, Edit, Glob, TodoWrite, Task]
description: "Design UI/UX and system architecture with Apple HIG compliance"
argument-hint: "[component] [--scope ui|architecture|system] [--style minimal]"
---

# /ios:design - UI/UX & Architecture Design

Design `$ARGUMENTS` following Apple Human Interface Guidelines and iOS architecture best practices.

## Arguments
- `--scope ui|architecture|system` - Design scope
- `--style minimal|bold|playful|professional` - UI design style
- `--platform ios|ipados|macos|watchos|visionos` - Target platform
- `--dark-mode` - Include dark mode design
- `--accessibility` - Comprehensive accessibility support
- `--pattern mvvm|tca|clean|viper` - Architecture pattern
- `--modules` - Modular architecture design
- `--diagram` - Generate architecture diagrams

## UI/UX Design (--scope ui)

### Apple HIG Compliance
- Typography: SF Pro, Dynamic Type support
- Colors: System colors, semantic colors
- Spacing: 8pt grid system
- Safe Area handling
- Platform idioms (iOS vs iPadOS vs macOS)

### Component Design
```swift
// Modern SwiftUI component structure
struct FeatureView: View {
    @State private var viewModel = FeatureViewModel()

    var body: some View {
        NavigationStack {
            content
                .navigationTitle("Feature")
                .toolbar { toolbarContent }
        }
    }

    private var content: some View {
        List { /* ... */ }
    }

    @ToolbarContentBuilder
    private var toolbarContent: some ToolbarContent {
        ToolbarItem(placement: .primaryAction) {
            Button("Add", systemImage: "plus") { }
        }
    }
}
```

## Architecture Design (--scope architecture)

### MVVM Pattern (--pattern mvvm)
```swift
// View
struct UserView: View {
    @State private var viewModel = UserViewModel()
    var body: some View {
        List(viewModel.users) { UserRow(user: $0) }
            .task { await viewModel.loadUsers() }
    }
}

// ViewModel
@Observable
class UserViewModel {
    var users: [User] = []
    private let repository: UserRepositoryProtocol

    init(repository: UserRepositoryProtocol = UserRepository()) {
        self.repository = repository
    }

    func loadUsers() async {
        users = (try? await repository.fetchAll()) ?? []
    }
}

// Repository
protocol UserRepositoryProtocol { func fetchAll() async throws -> [User] }
```

### TCA Pattern (--pattern tca)
```swift
@Reducer
struct UserFeature {
    @ObservableState
    struct State: Equatable {
        var users: [User] = []
        var isLoading = false
    }

    enum Action {
        case loadUsers
        case usersLoaded([User])
    }

    @Dependency(\.userClient) var userClient

    var body: some ReducerOf<Self> {
        Reduce { state, action in
            switch action {
            case .loadUsers:
                state.isLoading = true
                return .run { send in
                    let users = try await userClient.fetchAll()
                    await send(.usersLoaded(users))
                }
            case .usersLoaded(let users):
                state.users = users
                state.isLoading = false
                return .none
            }
        }
    }
}
```

### Clean Architecture (--pattern clean)
```
┌─────────────────────────────────────────────────┐
│                 Presentation                     │
│  ┌─────────┐  ┌──────────────┐  ┌───────────┐  │
│  │  Views  │──│  ViewModels  │──│ Formatters│  │
│  └─────────┘  └──────────────┘  └───────────┘  │
├─────────────────────────────────────────────────┤
│                    Domain                        │
│  ┌──────────┐  ┌───────────┐  ┌─────────────┐  │
│  │ Entities │  │ Use Cases │  │ Repositories│  │
│  └──────────┘  └───────────┘  │ (Protocols) │  │
├─────────────────────────────────────────────────┤
│                     Data                         │
│  ┌──────────┐  ┌───────────┐  ┌─────────────┐  │
│  │ Network  │  │ Database  │  │   Mappers   │  │
│  └──────────┘  └───────────┘  └─────────────┘  │
└─────────────────────────────────────────────────┘
```

## System Design (--scope system)

### Modular Architecture (--modules)
```
App/
├── Core/                    # Shared utilities
│   ├── Networking/
│   ├── Storage/
│   └── Extensions/
├── Features/                # Feature modules
│   ├── Auth/
│   │   ├── Views/
│   │   ├── ViewModels/
│   │   └── Services/
│   ├── Home/
│   └── Profile/
├── Design/                  # Design system
│   ├── Components/
│   ├── Tokens/
│   └── Themes/
└── App/                     # App assembly
    ├── Navigation/
    └── Dependencies/
```

### Dependency Injection
```swift
// Protocol-based DI
protocol Dependencies {
    var userRepository: UserRepositoryProtocol { get }
    var authService: AuthServiceProtocol { get }
    var networkClient: NetworkClientProtocol { get }
}

// Production implementation
final class AppDependencies: Dependencies {
    lazy var networkClient: NetworkClientProtocol = NetworkClient()
    lazy var userRepository: UserRepositoryProtocol = UserRepository(network: networkClient)
    lazy var authService: AuthServiceProtocol = AuthService(network: networkClient)
}

// Test implementation
final class MockDependencies: Dependencies {
    var userRepository: UserRepositoryProtocol = MockUserRepository()
    var authService: AuthServiceProtocol = MockAuthService()
    var networkClient: NetworkClientProtocol = MockNetworkClient()
}
```

## Output Structure

```markdown
# Design: [Component/System]
## Overview: Purpose and scope
## Architecture Diagram: [If --diagram]
## Components: Detailed breakdown
## Patterns: Applied patterns with rationale
## Dependencies: External dependencies
## Implementation Plan: Prioritized steps
```

## Examples
```bash
# UI/UX Design
/ios:design "user profile screen" --scope ui --style minimal
/ios:design "habit tracker" --scope ui --platform ios --dark-mode

# Architecture Design
/ios:design "e-commerce app" --scope architecture --pattern mvvm
/ios:design "social app" --scope architecture --pattern tca --modules

# System Design
/ios:design "banking app" --scope system --pattern clean --diagram
/ios:design "fitness tracker" --scope system --modules
```

---

**Delegates to**: swiftui-specialist (UI), architecture-specialist (arch/system)
