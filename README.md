# iOS Development Framework

> Unified iOS development framework with 13 specialized commands and 5 expert agents for Swift 6.2, SwiftUI, and SwiftData

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-2.1.0-brightgreen.svg)](https://github.com/CarolaneLFBV/ios-development-agents)
[![Swift 6.2](https://img.shields.io/badge/Swift-6.2-orange.svg)](https://swift.org)
[![SwiftUI](https://img.shields.io/badge/SwiftUI-Latest-blue.svg)](https://developer.apple.com/swiftui/)
[![SwiftData](https://img.shields.io/badge/SwiftData-Latest-green.svg)](https://developer.apple.com/swiftdata/)
[![Claude Code](https://img.shields.io/badge/Claude-Code-8A2BE2.svg)](https://claude.com/code)

## 🌟 Features

- 🎯 **Unified Framework** - Single powerful plugin with comprehensive iOS development capabilities
- 🚀 **13 Specialized Commands** - Complete workflow coverage from design to deployment
- 👥 **5 Expert Agents** - SwiftUI, Architecture, Performance, Testing, and Swift specialists
- 📱 **Swift 6.2 Native** - Latest language features (InlineArray, nonisolated async, Observations)
- ⚡ **Production-Ready** - Enterprise-grade code patterns and best practices
- 🧩 **Integrated Workflow** - Seamless coordination between commands and agents
- 🔧 **Complete Toolchain** - From implementation to App Store submission
- 📚 **Modern Stack** - SwiftUI, SwiftData, CloudKit, and iOS 18 support

## 📦 Installation

### Add Marketplace

```bash
/plugin marketplace add CarolaneLFBV/ios-development-agents
```

### Install Framework

```bash
# Install the unified iOS framework
/plugin install ios@ios-development
```

That's it! The single `ios` plugin provides all 13 commands and 5 expert agents.

## 🚀 Quick Start

### Design App Architecture

```bash
/ios:design "habit tracking app with SwiftData persistence"
```

### Implement a Feature

```bash
/ios:implement "user profile screen with avatar, name, bio, and edit button"
```

### Review and Improve Code

```bash
/ios:review UserProfileView.swift
/ios:improve --focus performance
```

### Migrate to Modern Patterns

```bash
/ios:migrate "UIKit to SwiftUI" --strategy incremental
```

### Test Your App

```bash
/ios:test --coverage --platform ios
```

### Deploy to App Store

```bash
/ios:publish --validate --screenshots
```

## 📚 Framework Components (v2.1.0)

### 13 Specialized Commands

| Category | Commands | Description |
|----------|----------|-------------|
| **Development** | `implement`, `design`, `refactor` | Feature implementation, architecture design, code refactoring |
| **Quality** | `review`, `improve`, `test` | Code review, quality improvement, testing workflows |
| **Migration** | `migrate`, `optimize` | Framework migration, performance optimization |
| **Analysis** | `analyze`, `debug` | Code analysis, debugging workflows |
| **Delivery** | `accessibility`, `localize`, `publish` | Accessibility audit, i18n/l10n, App Store submission |

### 5 Expert Agents

| Agent | Specialization | Key Capabilities |
|-------|---------------|------------------|
| **swiftui-specialist** | UI/UX Development | View composition, state management, animations, custom modifiers |
| **architecture-specialist** | System Design | MVVM, TCA, Clean Architecture, dependency injection, design patterns |
| **performance-specialist** | Optimization | Instruments profiling, memory optimization, rendering performance, Core Web Vitals |
| **testing-specialist** | Quality Assurance | XCTest, UI testing, snapshot testing, test coverage, CI/CD integration |
| **swift-specialist** | Language Features | Swift 6.2 features, generics, protocols, concurrency, modern patterns |

### Agent Activation

Agents are **automatically activated** based on command context:
- `/ios:implement` → **swiftui-specialist** + **architecture-specialist**
- `/ios:optimize` → **performance-specialist**
- `/ios:review` → **architecture-specialist** + **testing-specialist**
- `/ios:test` → **testing-specialist**
- `/ios:refactor` → **swift-specialist** + **architecture-specialist**

## 🗺️ Future Enhancements

The unified framework can be extended with additional specialized commands and agents:

### Potential Command Additions
- **Advanced Testing**: Visual regression testing, performance testing, load testing
- **Platform Extensions**: watchOS, macOS, tvOS, visionOS specific workflows
- **Framework Integration**: WidgetKit, HealthKit, MapKit, StoreKit specialized commands
- **DevOps**: Fastlane automation, Xcode Cloud integration, CI/CD workflows
- **Advanced Analysis**: Security auditing, dependency analysis, technical debt tracking

### Potential Agent Additions
- **security-specialist**: Security audits, vulnerability scanning, compliance checks
- **devops-specialist**: CI/CD automation, deployment workflows, release management
- **platform-specialist**: Cross-platform development, multi-platform optimization
- **localization-specialist**: i18n/l10n workflows, cultural adaptation, translation management

## 🎯 Command Reference

### Development Commands

#### `/ios:implement`
Implements features, components, or functionality using SwiftUI, SwiftData, and modern iOS patterns.

```bash
/ios:implement "user authentication with biometric support"
/ios:implement LoginView.swift --pattern MVVM
```

#### `/ios:design`
Designs app architecture, data models, and system structure.

```bash
/ios:design "e-commerce app with product catalog and cart"
/ios:design --pattern TCA --focus scalability
```

#### `/ios:refactor`
Refactors code to modern patterns, improves structure, reduces technical debt.

```bash
/ios:refactor LegacyViewController.swift --to SwiftUI
/ios:refactor --pattern @Observable
```

### Quality Commands

#### `/ios:review`
Comprehensive code review covering architecture, quality, security, and best practices.

```bash
/ios:review UserManager.swift
/ios:review --focus security --comprehensive
```

#### `/ios:improve`
Improves code quality, performance, maintainability, and best practices adherence.

```bash
/ios:improve --focus performance
/ios:improve NetworkLayer.swift --metrics
```

#### `/ios:test`
Generates tests, creates test strategies, and improves test coverage.

```bash
/ios:test AuthenticationService.swift
/ios:test --coverage --ui-tests
```

### Migration Commands

#### `/ios:migrate`
Migrates between frameworks, patterns, or iOS versions.

```bash
/ios:migrate "UIKit to SwiftUI" --incremental
/ios:migrate "CoreData to SwiftData"
```

#### `/ios:optimize`
Optimizes performance using Instruments profiling and best practices.

```bash
/ios:optimize --profile memory
/ios:optimize ListView.swift --rendering
```

### Analysis Commands

#### `/ios:analyze`
Deep code analysis for quality, security, performance, and architecture.

```bash
/ios:analyze --comprehensive
/ios:analyze AppDelegate.swift --focus security
```

#### `/ios:debug`
Advanced debugging workflows and crash analysis.

```bash
/ios:debug crash-report.txt
/ios:debug --instruments --memory-leaks
```

### Delivery Commands

#### `/ios:accessibility`
Comprehensive accessibility audit and implementation (VoiceOver, Dynamic Type, etc.).

```bash
/ios:accessibility ProfileView.swift
/ios:accessibility --audit --wcag
```

#### `/ios:localize`
i18n/l10n implementation and string extraction.

```bash
/ios:localize --extract-strings
/ios:localize --language fr --validate
```

#### `/ios:publish`
App Store submission preparation and validation.

```bash
/ios:publish --validate --screenshots
/ios:publish --testflight --release-notes
```

## 🏗️ Architecture Philosophy

### Unified Framework Approach

**iOS Framework v2.0.0** consolidates specialized capabilities into a single, powerful plugin:

- **Integrated Commands**: 13 specialized commands covering the complete iOS development lifecycle
- **Expert Agents**: 5 domain specialists that activate automatically based on context
- **Seamless Coordination**: Commands and agents work together without manual orchestration
- **Production-Ready**: Enterprise-grade patterns and best practices built-in
- **Swift 6.2 Native**: Leverages the latest language features and modern iOS APIs

### Design Principles

1. **Context-Aware Activation**: Agents activate automatically based on the command and task context
2. **Comprehensive Coverage**: From architecture design to App Store submission
3. **Quality-First**: Every command enforces best practices and modern patterns
4. **Developer-Friendly**: Clear command syntax with intuitive parameters
5. **Extensible**: Easy to add new commands and agents as the framework evolves

### Agent Coordination

Unlike fragmented plugin systems, the unified framework provides:

- **Automatic Routing**: Commands select the right agents without manual configuration
- **Shared Context**: Agents maintain full context across the workflow
- **Consistent Quality**: Unified standards and best practices across all operations
- **Efficient Execution**: Optimized coordination without redundant context switching

## 🤝 Contributing

Contributions welcome! Ways to contribute:

1. **Enhance Commands** - Improve existing command workflows and capabilities
2. **Add New Agents** - Create specialized agents for new domains
3. **Expand Command Coverage** - Add new commands for additional workflows
4. **Improve Documentation** - Better examples, guides, and tutorials
5. **Report Issues** - Bug reports and feature requests

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built for the [Claude Code](https://docs.claude.com/claude-code) ecosystem
- Designed for Swift 6.2, SwiftUI, and modern Apple platforms
- Inspired by best practices from the iOS development community

## 🔗 Links

- [Repository](https://github.com/CarolaneLFBV/ios-development-agents)
- [Issues](https://github.com/CarolaneLFBV/ios-development-agents/issues)
- [Marketplace](https://github.com/CarolaneLFBV/ios-development-agents)
- [Claude Code Docs](https://docs.claude.com/claude-code)

---

**Built with ❤️ for the iOS development community**

*Version 2.1.0 • Swift 6.2 • SwiftUI • SwiftData • 13 Commands • 5 Expert Agents*
