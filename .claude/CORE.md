# CORE.md - iOS Framework Core

## Primary Directive

**Evidence > Assumptions | Code > Documentation | Apple HIG > Custom Patterns**

## Operational Rules

- Read before Write/Edit/Update
- Check Package.swift before adding dependencies
- Follow existing project patterns
- Use @Observable over ObservableObject
- Prefer async/await over completion handlers
- SwiftData over CoreData for new projects
- Never commit automatically

## Quality Gates (8-Step)

```yaml
1. syntax:        Swift compiler validation
2. types:         Type checking, inference
3. lint:          SwiftLint, code standards
4. security:      OWASP, Keychain usage, ATS
5. tests:         XCTest, coverage >=80%
6. performance:   Instruments profiling
7. accessibility: VoiceOver, Dynamic Type
8. integration:   Build validation, compatibility
```

## Do / Don't

### Do
- Use @Observable for ViewModels
- Use async/await for concurrency
- Use SwiftData for persistence
- Check Context7 for Apple patterns
- Include accessibility support
- Follow Apple HIG

### Don't
- Use ObservableObject (legacy)
- Use completion handlers (legacy)
- Skip accessibility
- Force unwrap optionals
- Ignore memory management
- Auto-commit without permission

## 7 Opus Agents

| Agent | Domain | MCP |
|-------|--------|-----|
| swift-specialist | Generics, protocols, async/await, actors | context7 |
| swiftui-specialist | Views, state, navigation, animations | context7 |
| architecture-specialist | MVVM, TCA, SwiftData, DI | context7 |
| performance-specialist | Instruments, memory, rendering | context7 |
| testing-specialist | XCTest, UI testing, TDD | context7 |
| security-specialist | OWASP, Keychain, encryption | context7, sequential |
| devops-specialist | CI/CD, Xcode Cloud, Fastlane | context7 |

### Delegation Rules

```yaml
swiftui-specialist:
  owns: Views, layouts, animations, state management
  delegates: Architecture -> architecture, Language -> swift, Testing -> testing

swift-specialist:
  owns: Generics, protocols, async/await, actors, memory
  delegates: SwiftUI -> swiftui, Architecture -> architecture, Testing -> testing

architecture-specialist:
  owns: MVVM, TCA, Clean, SwiftData, dependency injection
  delegates: UI -> swiftui, Language -> swift, Testing -> testing

performance-specialist:
  owns: Instruments profiling, memory optimization, rendering
  delegates: Code -> swift/swiftui, Architecture -> architecture

testing-specialist:
  owns: XCTest, UI testing, TDD, mocking, coverage
  delegates: Implementation -> appropriate specialist

security-specialist:
  owns: OWASP, Keychain, auth, encryption, ATS, biometrics
  delegates: Implementation -> appropriate specialist

devops-specialist:
  owns: CI/CD, Xcode Cloud, GitHub Actions, Fastlane, signing
  delegates: Code -> appropriate specialist
```

### Multi-Agent Coordination

```yaml
parallel:     Independent domain analysis (security + performance + architecture)
sequential:   Dependent pipeline (implement -> test -> document)
hierarchical: Complex multi-phase with coordinator + specialists
```

## MCP Integration

### Context7 (REQUIRED before implementation)

Query Apple documentation, HIG, framework patterns.
Workflow: detect framework -> resolve-library-id -> apply patterns -> cache.

Library IDs:
- `/apple/swift` - Swift language
- `/apple/swiftui` - SwiftUI framework
- `/apple/swiftdata` - SwiftData persistence
- `/apple/combine` - Combine framework
- `/pointfreeco/swift-composable-architecture` - TCA

### Sequential (Complex Analysis)

Multi-step reasoning for --think/--think-hard/--ultrathink, security audits, architecture decisions.

```yaml
--think:       4K tokens, module-level
--think-hard:  10K tokens, system-wide
--ultrathink:  32K tokens, critical analysis
```

## Key Flags

| Flag | Purpose |
|------|---------|
| `--think` / `--think-hard` / `--ultrathink` | Analysis depth |
| `--framework swiftui\|uikit\|hybrid` | UI framework (default: swiftui) |
| `--pattern mvvm\|tca\|clean` | Architecture (default: mvvm) |
| `--to observable\|async\|actor\|swiftdata` | Refactoring target |
| `--with-tests` | Generate XCTests |
| `--review` / `--checklist` / `--score` | Code review mode |
| `--focus security\|performance\|quality\|architecture` | Analysis focus |
| `--debug` / `--breakpoints` / `--trace` | Debug mode |
| `--owasp` / `--keychain` | Security audit |
| `--safe` | Conservative changes |
