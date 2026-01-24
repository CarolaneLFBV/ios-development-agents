# CAPABILITIES.md - iOS Framework Agents & MCP

## Agent System

### 7 Opus Specialists

| Agent | Domain | Auto-Keywords | MCP Primary |
|-------|--------|---------------|-------------|
| swift-specialist | Language, concurrency, memory | protocol, generic, async, actor | context7 |
| swiftui-specialist | Views, state, navigation | View, @State, NavigationStack | context7 |
| architecture-specialist | MVVM, TCA, SwiftData, DI | @Model, ViewModel, repository | context7 |
| performance-specialist | Instruments, memory, rendering | optimize, slow, memory, launch | context7 |
| testing-specialist | XCTest, UI testing, TDD | test, XCTest, coverage, mock | context7 |
| security-specialist | OWASP, Keychain, encryption | auth, Keychain, encryption | context7, sequential |
| devops-specialist | CI/CD, Xcode Cloud, Fastlane | CI, deploy, Fastlane, archive | context7 |

### Agent Delegation Rules

```yaml
swiftui-specialist:
  owns: Views, layouts, animations, state management
  delegates:
    - Architecture patterns → architecture-specialist
    - Language features → swift-specialist
    - Testing → testing-specialist

swift-specialist:
  owns: Generics, protocols, async/await, actors, memory
  delegates:
    - SwiftUI views → swiftui-specialist
    - Architecture → architecture-specialist
    - Testing → testing-specialist

architecture-specialist:
  owns: MVVM, TCA, Clean, SwiftData, dependency injection
  delegates:
    - UI implementation → swiftui-specialist
    - Language details → swift-specialist
    - Testing → testing-specialist

performance-specialist:
  owns: Instruments profiling, memory optimization, rendering
  delegates:
    - Code changes → swift-specialist, swiftui-specialist
    - Architecture changes → architecture-specialist

testing-specialist:
  owns: XCTest, UI testing, TDD, mocking, coverage
  delegates:
    - Implementation → appropriate specialist
    - Architecture → architecture-specialist

security-specialist:
  owns: OWASP, Keychain, auth, encryption, ATS, biometrics
  delegates:
    - Implementation → appropriate specialist
    - Architecture → architecture-specialist

devops-specialist:
  owns: CI/CD, Xcode Cloud, GitHub Actions, Fastlane, signing
  delegates:
    - Code changes → appropriate specialist
```

### Multi-Agent Coordination

```yaml
parallel:
  use_case: "Independent domain analysis"
  example: "/ios:analyze . --comprehensive"
  agents: [security, performance, architecture]

sequential:
  use_case: "Dependent task pipeline"
  example: "/ios:implement → /ios:test → /ios:document"
  workflow: implement → test → document

hierarchical:
  use_case: "Complex multi-phase"
  example: "/ios:migrate uikit swiftui"
  coordinator: architecture-specialist
  specialists: [swiftui, swift, testing]
```

## MCP Server Integration

### Context7 (REQUIRED)

**Purpose**: Apple documentation, HIG, framework patterns

**Auto-Activation**:
- All iOS commands
- Apple framework queries
- Best practices lookup

**Workflow**:
1. Detect framework (SwiftUI, SwiftData, etc.)
2. Query: resolve-library-id → get patterns
3. Apply official patterns
4. Cache for session reuse

**Library IDs**:
- `/apple/swift` - Swift language
- `/apple/swiftui` - SwiftUI framework
- `/apple/swiftdata` - SwiftData persistence
- `/apple/combine` - Combine framework
- `/pointfreeco/swift-composable-architecture` - TCA

### Sequential (Complex Analysis)

**Purpose**: Multi-step reasoning, architecture analysis

**Auto-Activation**:
- --think, --think-hard, --ultrathink flags
- Complex debugging
- Security audits
- Architecture decisions

**Thinking Modes**:
```yaml
--think:       4K tokens, module-level
--think-hard:  10K tokens, system-wide
--ultrathink:  32K tokens, critical analysis
```

## Persona Auto-Activation

### Scoring Algorithm

```yaml
keyword_match:    40%   # Domain keywords
file_context:     30%   # File patterns
command_context:  20%   # Command type
complexity:       10%   # Task assessment

threshold:
  auto_activate:  70%
  suggest:        50%
  multi_agent:    85%
```

### Activation Patterns

| Trigger | Agent | Additional |
|---------|-------|------------|
| SwiftUI views | swiftui-specialist | context7 |
| @Observable, ViewModel | architecture-specialist | context7 |
| async/await, actor | swift-specialist | context7 |
| Instruments, optimize | performance-specialist | context7 |
| XCTest, coverage | testing-specialist | context7 |
| Keychain, auth | security-specialist | context7, sequential |
| Fastlane, CI | devops-specialist | context7 |
