# iOS Development Framework

> Unified iOS development framework with 15 specialized commands, 7 expert Opus agents, 4 auto-injected skills, and smart hooks for Swift, SwiftUI, and SwiftData

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-3.0.0-brightgreen.svg)](https://github.com/CarolaneLFBV/ios-development-agents)
[![Swift](https://img.shields.io/badge/Swift-6.2-orange.svg)](https://swift.org)
[![SwiftUI](https://img.shields.io/badge/SwiftUI-Latest-blue.svg)](https://developer.apple.com/swiftui/)
[![SwiftData](https://img.shields.io/badge/SwiftData-Latest-green.svg)](https://developer.apple.com/swiftdata/)
[![Claude Code](https://img.shields.io/badge/Claude-Code-8A2BE2.svg)](https://claude.com/code)

## What's New in v3.0.0

- **Opus Agents**: All 7 expert agents now use Claude Opus for maximum intelligence
- **Streamlined Commands**: 15 focused commands (consolidated from 19)
- **4 Auto-Injected Skills**: SwiftData, SwiftUI, Concurrency, and Testing patterns
- **Smart Hooks**: Best practices reminders when editing Swift files
- **Token Optimized**: ~70% reduction in agent size

## Features

- **15 Specialized Commands** - Complete workflow from design to deployment
- **7 Expert Opus Agents** - SwiftUI, Architecture, Performance, Testing, Swift, Security, and DevOps specialists
- **4 Auto-Injected Skills** - Context-aware pattern injection
- **Smart Hooks** - Automatic best practices reminders
- **Swift 6.2 Native** - Latest language features and modern iOS APIs
- **Production-Ready** - Enterprise-grade code patterns

## Installation

```bash
# Add marketplace
/plugin marketplace add CarolaneLFBV/ios-development-agents

# Install framework
/plugin install ios@ios-development
```

## Quick Start

```bash
# Implement a feature
/ios:implement "user profile screen with avatar and edit button"

# Review code
/ios:analyze UserProfileView.swift --review --checklist

# Troubleshoot an issue
/ios:troubleshoot "crash on launch" --type crash --debug

# Design architecture
/ios:design "e-commerce app" --scope architecture --pattern mvvm

# Refactor to modern patterns
/ios:improve ViewModel.swift --to observable
```

## Components

### 15 Commands

| Category | Commands | Description |
|----------|----------|-------------|
| **Development** | `implement`, `design` | Feature implementation, UI/UX + system architecture |
| **Quality** | `improve`, `test`, `cleanup`, `security` | Code quality, refactoring, testing, security audit |
| **Documentation** | `document` | README, API docs, DocC, inline comments |
| **Migration** | `migrate`, `optimize` | Framework migration, performance optimization |
| **Analysis** | `analyze`, `troubleshoot` | Code analysis, review, debugging, issue diagnosis |
| **Delivery** | `accessibility`, `localize`, `publish` | Accessibility, i18n/l10n, App Store |
| **Planning** | `brainstorm` | Idea generation and solution exploration |

### 7 Opus Agents

| Agent | Model | Expertise |
|-------|-------|-----------|
| **swift-specialist** | Opus | Generics, protocols, async/await, actors, memory |
| **swiftui-specialist** | Opus | Views, layouts, state, navigation, animations |
| **architecture-specialist** | Opus | MVVM, TCA, Clean Architecture, SwiftData, DI |
| **performance-specialist** | Opus | Instruments, memory, rendering, launch time |
| **testing-specialist** | Opus | XCTest, UI testing, snapshot testing, TDD |
| **security-specialist** | Opus | OWASP, Keychain, authentication, encryption, ATS |
| **devops-specialist** | Opus | CI/CD, Xcode Cloud, GitHub Actions, Fastlane |

### 4 Auto-Injected Skills

| Skill | Auto-Inject When |
|-------|------------------|
| **swiftdata-patterns** | `@Model` or SwiftData imports detected |
| **swiftui-components** | SwiftUI View detected |
| **concurrency-patterns** | `async/await` or `actor` detected |
| **testing-patterns** | XCTest or test files detected |

### Smart Hooks

- **iOS Best Practices Hook**: Reminds you of modern patterns when editing Swift files
  - Suggests `@Observable` over `ObservableObject`
  - Warns about force unwrapping
  - Recommends `LazyVStack` for lists
  - Suggests `@MainActor` over `DispatchQueue.main`

## Command Examples

### Development

```bash
/ios:implement "login screen with biometric auth" --framework swiftui --pattern mvvm
/ios:design "habit tracker app" --scope ui --style minimal --platform ios
/ios:design "social app" --scope architecture --pattern tca --modules
```

### Quality

```bash
/ios:analyze AuthService.swift --review --checklist --score
/ios:improve Views/ --focus performance --safe
/ios:improve ViewModel.swift --to observable
/ios:test UserViewModel --generate --type unit
/ios:cleanup . --type dead-code --report
/ios:security . --owasp --report
```

### Documentation

```bash
/ios:document . --type readme --export README.md
/ios:document Services/ --type api --update
```

### Migration

```bash
/ios:migrate coredata swiftdata --backup
/ios:optimize ProductList --metric render
```

### Analysis

```bash
/ios:analyze . --focus architecture
/ios:troubleshoot "EXC_BAD_ACCESS" --type crash --debug --trace
/ios:troubleshoot "list stutters" --type performance --instruments
```

### Delivery

```bash
/ios:accessibility LoginView.swift --level aa --fix
/ios:localize . --extract --languages "en,fr,es"
/ios:publish --validate --screenshots
```

### Planning

```bash
/ios:brainstorm "offline-first sync" --depth deep --focus data
```

## Architecture

```
.claude-plugin/plugin.json     # Plugin configuration
commands/                      # 15 specialized commands
agents/                        # 7 Opus expert agents
skills/                        # 4 auto-injected skills
hooks/                         # Smart hooks for best practices
```

## Contributing

Contributions welcome:
1. Enhance commands or agents
2. Add new skills for common patterns
3. Improve hooks with more best practices
4. Better documentation and examples

## License

MIT License - see [LICENSE](LICENSE) file.

---

**Built with ❤️ for the iOS development community**

*Version 3.0.0 • Swift 6.2 • SwiftUI • SwiftData • 15 Commands • 7 Opus Agents • 4 Skills • Hooks*
