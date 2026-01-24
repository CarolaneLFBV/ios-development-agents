# CORE.md - iOS Framework Core Principles

## Primary Directive

**Evidence > Assumptions | Code > Documentation | Apple HIG > Custom Patterns**

## SOLID for iOS

- **Single Responsibility**: One View = One Purpose, One ViewModel = One Feature
- **Open/Closed**: Protocol extensions, @Observable inheritance
- **Liskov Substitution**: Protocol-based abstractions for testability
- **Interface Segregation**: Small protocols (Identifiable, Codable, Sendable)
- **Dependency Inversion**: Repository pattern, protocol-based DI

## Operational Rules

### File Operations
- Read before Write/Edit/Update
- Use absolute paths only
- Batch operations when possible
- Never commit automatically

### Framework Compliance
- Check Package.swift before adding dependencies
- Follow existing project patterns
- Use @Observable over ObservableObject
- Prefer async/await over completion handlers
- SwiftData over CoreData for new projects

### Quality Gates (8-Step)

```yaml
1. syntax:      Swift compiler validation
2. types:       Type checking, inference
3. lint:        SwiftLint, code standards
4. security:    OWASP, Keychain usage, ATS
5. tests:       XCTest, coverage >=80%
6. performance: Instruments profiling
7. accessibility: VoiceOver, Dynamic Type
8. integration: Build validation, compatibility
```

## Symbol System

### Logic & Flow
| Symbol | Meaning | Example |
|--------|---------|---------|
| → | leads to | `View → ViewModel → Repository` |
| ⇒ | transforms | `UIKit ⇒ SwiftUI` |
| ← | rollback | `migration ← revert` |
| & | and | `SwiftUI & SwiftData` |
| \| | or | `MVVM\|TCA\|Clean` |
| » | sequence | `fetch » parse » display` |

### Status
| Symbol | Meaning | Action |
|--------|---------|--------|
| ✅ | pass | None |
| ❌ | fail | Immediate |
| ⚠️ | warning | Review |
| 🔄 | progress | Monitor |
| 🚨 | critical | Immediate |

### iOS Domains
| Symbol | Domain |
|--------|--------|
| 📱 | iOS/General |
| 🎨 | SwiftUI |
| ⚡ | Performance |
| 🔐 | Security |
| 🧪 | Testing |
| 📦 | Deployment |
| 🏗️ | Architecture |

## Abbreviations

```
impl → implementation    vm → ViewModel
vc → ViewController      nav → navigation
cfg → configuration      repo → repository
svc → service           mgr → manager
obs → Observable        ctx → context
req → request           res → response
```

## Do / Don't

### Do
✅ Read before Write/Edit
✅ Use @Observable for ViewModels
✅ Use async/await for concurrency
✅ Use SwiftData for persistence
✅ Check Context7 for Apple patterns
✅ Include accessibility support
✅ Follow Apple HIG

### Don't
❌ Use ObservableObject (legacy)
❌ Use completion handlers (legacy)
❌ Skip accessibility
❌ Force unwrap optionals
❌ Ignore memory management
❌ Auto-commit without permission
