# iOS Development Framework

**Complete iOS development framework with 13 specialized commands and 5 expert agents** for Swift 6.2, SwiftUI, SwiftData, and modern iOS patterns.

## Overview

The iOS Development Framework provides a comprehensive, command-driven approach to iOS development. Inspired by the WD Framework methodology, it offers specialized commands for every aspect of iOS development, from implementation to deployment.

**Version**: 2.0.0
**Swift**: 6.2+
**Xcode**: 17.0+
**Platforms**: iOS 17+, iPadOS 17+, macOS 15+

---

## Features

### 🎯 13 Specialized Commands

| Category | Commands | Purpose |
|----------|----------|---------|
| **Development** | `/ios:implement`, `/ios:refactor` | Feature implementation and refactoring |
| **Quality** | `/ios:improve`, `/ios:review`, `/ios:optimize` | Code enhancement and optimization |
| **Design** | `/ios:design` | UI/UX with Apple HIG compliance |
| **Testing** | `/ios:test` | XCTest generation and execution |
| **Analysis** | `/ios:analyze`, `/ios:debug` | Code analysis and debugging |
| **Migration** | `/ios:migrate` | Framework and version migrations |
| **Accessibility** | `/ios:accessibility` | WCAG compliance and VoiceOver |
| **Deployment** | `/ios:publish` | App Store submission |
| **Localization** | `/ios:localize` | i18n/l10n implementation |

### 🤖 5 Expert Agents

1. **swiftui-specialist** - SwiftUI views, state management, navigation, animations
2. **swift-specialist** - Swift 6.2 language features (InlineArray, @Observable, async/await)
3. **architecture-specialist** - MVVM, TCA, Clean Architecture, SwiftData integration
4. **performance-specialist** - Performance optimization with Instruments
5. **testing-specialist** - XCTest, UI testing, snapshot testing, TDD

### 🎨 Architecture Patterns

- **MVVM** with @Observable (Recommended for most apps)
- **TCA** (The Composable Architecture) for complex state
- **Clean Architecture** for large-scale applications
- **SwiftData** integration for modern persistence

---

## Installation

### Via Claude Code Plugin Marketplace

```bash
# Add marketplace from GitHub
/plugin marketplace add CarolaneLFBV/ios-development-agents

# Install the framework
/plugin install ios-framework@ios-development
```

### Manual Installation

```bash
# Clone the repository
git clone https://github.com/CarolaneLFBV/ios-development-agents.git

# The framework is automatically available in Claude Code
```

---

## Quick Start

### Implement a New Feature

```bash
# SwiftUI view with MVVM pattern
/ios:implement UserProfileView --framework swiftui --pattern mvvm

# Full feature with SwiftData and tests
/ios:implement TaskManager --swiftdata --pattern mvvm --with-tests --accessibility

# TCA implementation
/ios:implement CounterFeature --pattern tca
```

### Improve Existing Code

```bash
# Performance optimization
/ios:improve ContentView.swift --focus performance

# Swift 6.2 modernization
/ios:improve . --type swift-modern --safe

# Architecture improvements
/ios:improve Services/ --focus architecture
```

### Code Review

```bash
# Comprehensive review
/ios:review UserAuth/ --focus security

# Quality audit
/ios:review . --format report --export review.md
```

### Refactoring

```bash
# Migrate to @Observable
/ios:refactor UserViewModel.swift --to observable

# SwiftData migration
/ios:refactor Models/ --to swiftdata

# Async/await adoption
/ios:refactor NetworkService.swift --to async
```

---

## Command Reference

### Development & Implementation

#### `/ios:implement`
**Purpose**: Implement iOS features with SwiftUI/UIKit

```bash
/ios:implement [feature] [--framework swiftui|uikit] [--pattern mvvm|tca|clean]
                        [--swiftdata] [--with-tests] [--accessibility]
```

**Examples**:
```bash
# Basic SwiftUI view
/ios:implement LoginView --framework swiftui

# Complete feature with tests
/ios:implement UserAuth --pattern mvvm --swiftdata --with-tests

# Accessible UI
/ios:implement OnboardingFlow --accessibility --pattern mvvm
```

#### `/ios:refactor`
**Purpose**: Refactor to modern patterns

```bash
/ios:refactor [target] [--pattern mvvm|tca|clean] [--to observable|swiftdata|async]
```

**Examples**:
```bash
/ios:refactor UserViewModel.swift --to observable
/ios:refactor . --pattern tca
/ios:refactor NetworkService.swift --to async
```

### Quality & Enhancement

#### `/ios:improve`
**Purpose**: Improve code quality and performance

```bash
/ios:improve [target] [--focus performance|accessibility|architecture|quality]
                     [--type swift-modern|swiftui|swiftdata]
```

**Examples**:
```bash
/ios:improve ProductList.swift --focus performance
/ios:improve . --type swift-modern --safe
/ios:improve UserAuth/ --focus security
```

#### `/ios:review`
**Purpose**: Comprehensive code review

```bash
/ios:review [target] [--focus security|performance|quality|architecture]
                    [--format report|checklist|metrics]
```

#### `/ios:optimize`
**Purpose**: Performance optimization

```bash
/ios:optimize [target] [--metric launch|render|memory|battery]
                      [--goal <value>] [--instruments]
```

### Testing & Quality

#### `/ios:test`
**Purpose**: XCTest generation and execution

```bash
/ios:test [target] [--type unit|ui|snapshot|performance|all]
                  [--coverage] [--generate] [--fix]
```

**Examples**:
```bash
/ios:test UserViewModel --generate --type unit
/ios:test LoginFlow --type ui
/ios:test . --coverage --type all
```

### Analysis & Debugging

#### `/ios:analyze`
**Purpose**: Deep code analysis

```bash
/ios:analyze [target] [--focus performance|security|architecture|quality]
                     [--instruments] [--export <path>]
```

#### `/ios:debug`
**Purpose**: Advanced debugging

```bash
/ios:debug [issue] [--type crash|hang|memory|ui] [--reproduce] [--fix]
```

### Migration & Transformation

#### `/ios:migrate`
**Purpose**: Framework and version migrations

```bash
/ios:migrate [source] [target] [--strategy incremental|complete|hybrid]
                               [--validate] [--backup]
```

**Examples**:
```bash
/ios:migrate uikit swiftui --strategy incremental
/ios:migrate coredata swiftdata --backup
/ios:migrate swift5 swift6 --validate
```

### Design & Accessibility

#### `/ios:design`
**Purpose**: UI/UX design with Apple HIG

```bash
/ios:design [component] [--style minimal|bold|playful|professional]
                       [--platform ios|ipados|macos]
```

#### `/ios:accessibility`
**Purpose**: Accessibility compliance

```bash
/ios:accessibility [target] [--level a|aa|aaa] [--fix] [--audit-only]
```

### Deployment & Localization

#### `/ios:publish`
**Purpose**: App Store submission

```bash
/ios:publish [--validate] [--screenshots] [--metadata] [--export]
```

#### `/ios:localize`
**Purpose**: i18n/l10n implementation

```bash
/ios:localize [target] [--languages <langs>] [--extract] [--generate]
```

---

## Workflows

### Full Feature Implementation Workflow

```bash
# 1. Design the UI
/ios:design UserProfile --style professional

# 2. Implement with architecture
/ios:implement UserProfile --pattern mvvm --swiftdata --with-tests

# 3. Ensure accessibility
/ios:accessibility UserProfile --level aa --fix

# 4. Run comprehensive tests
/ios:test UserProfile --type all --coverage

# 5. Code review
/ios:review UserProfile --format report
```

### Performance Optimization Workflow

```bash
# 1. Analyze performance
/ios:analyze App --focus performance --instruments

# 2. Optimize bottlenecks
/ios:optimize App --metric launch --goal "launch<1s"

# 3. Validate improvements
/ios:test App --type performance

# 4. Review changes
/ios:review App --focus performance
```

### Migration Workflow

```bash
# 1. Analyze current state
/ios:analyze . --focus architecture

# 2. Migrate framework
/ios:migrate uikit swiftui --strategy incremental --backup

# 3. Update tests
/ios:test . --type all

# 4. Final review
/ios:review . --focus quality
```

---

## Architecture

### Agent System

The framework uses 5 specialized agents that auto-activate based on context:

```yaml
swiftui-specialist:
  expertise: [SwiftUI, Views, State, Navigation]
  auto-activation: ["View", "@State", "NavigationStack"]

swift-specialist:
  expertise: [Swift 6.2, Generics, Protocols, InlineArray]
  auto-activation: ["protocol", "generic", "@Observable"]

architecture-specialist:
  expertise: [MVVM, TCA, SwiftData, Patterns]
  auto-activation: ["MVVM", "TCA", "@Model"]

performance-specialist:
  expertise: [Optimization, Instruments, Profiling]
  auto-activation: ["performance", "optimize", "slow"]

testing-specialist:
  expertise: [XCTest, UI Testing, TDD]
  auto-activation: ["test", "XCTest", "--with-tests"]
```

### Quality Gates

All code changes pass through 8 validation steps:

1. **Syntax** - Swift compiler validation
2. **Type Safety** - Type checking
3. **Code Quality** - SwiftLint standards
4. **Security** - Vulnerability scanning
5. **Testing** - XCTest execution (≥80% coverage)
6. **Performance** - Performance benchmarks
7. **Accessibility** - VoiceOver, Dynamic Type, WCAG
8. **Integration** - Build validation

---

## Best Practices

### Command Selection
- Use `/ios:implement` for new features
- Use `/ios:improve` for enhancements
- Use `/ios:refactor` for pattern changes
- Use `/ios:optimize` for performance issues

### Flag Usage
- Always use `--safe` for production code
- Use `--preview` to review changes before applying
- Include `--with-tests` for critical features
- Use `--accessibility` for user-facing features

### Architecture Patterns
- **Simple apps**: MVVM with @Observable
- **Complex state**: TCA
- **Large teams**: Clean Architecture
- **Data-heavy**: MVVM + SwiftData

---

## Examples

### SwiftUI MVVM App

```bash
# 1. Create models
/ios:implement Task --pattern mvvm --swiftdata

# 2. Create views
/ios:implement TaskListView --framework swiftui --pattern mvvm

# 3. Add tests
/ios:test TaskListView --generate --type unit

# 4. Ensure accessibility
/ios:accessibility TaskListView --level aa --fix
```

### TCA Counter App

```bash
/ios:implement CounterFeature --pattern tca --with-tests
```

### Performance Optimization

```bash
# Profile and optimize
/ios:analyze ProductList --focus performance --instruments
/ios:optimize ProductList --metric render
/ios:improve ProductList.swift --focus performance
```

---

## Configuration

### Global Settings

Create `.ios-framework.yml` in project root:

```yaml
framework:
  default_pattern: mvvm
  default_framework: swiftui
  ios_version: 17.0

quality:
  test_coverage_minimum: 80
  accessibility_level: aa
  swift_lint: enabled

performance:
  launch_time_goal: 1.0s
  memory_limit: 100MB
```

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

MIT License - See [LICENSE](LICENSE) for details.

---

## Resources

- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Swift API Design Guidelines](https://www.swift.org/documentation/api-design-guidelines/)
- [SwiftUI Documentation](https://developer.apple.com/documentation/swiftui/)
- [SwiftData Documentation](https://developer.apple.com/documentation/swiftdata)
- [The Composable Architecture](https://github.com/pointfreeco/swift-composable-architecture)

---

## Support

- **Issues**: [GitHub Issues](https://github.com/CarolaneLFBV/ios-development-agents/issues)
- **Discussions**: [GitHub Discussions](https://github.com/CarolaneLFBV/ios-development-agents/discussions)
- **Email**: carolanelefebvre@okorp.fr

---

**Built with ❤️ for the iOS development community**
