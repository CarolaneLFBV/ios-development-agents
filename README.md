# iOS Development Framework

> Unified iOS development framework with 15 commands, 7 Opus agents with MCP integration, smart auto-activation, and BMAD workflows for Swift, SwiftUI, and SwiftData

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-5.0.0-brightgreen.svg)](https://github.com/CarolaneLFBV/ios-development-agents)
[![Swift](https://img.shields.io/badge/Swift-6.2-orange.svg)](https://swift.org)
[![SwiftUI](https://img.shields.io/badge/SwiftUI-Latest-blue.svg)](https://developer.apple.com/swiftui/)
[![SwiftData](https://img.shields.io/badge/SwiftData-Latest-green.svg)](https://developer.apple.com/swiftdata/)
[![Claude Code](https://img.shields.io/badge/Claude-Code-8A2BE2.svg)](https://claude.com/code)

## What's New in v5.0.0

- **Lean Framework**: 3 core files in `.claude/` (~316 lines session-loaded)
- **-74% Context Reduction**: From 1,228 to 316 lines (7 core files consolidated into 3)
- **Simplified Core**: ROUTING.md, CAPABILITIES.md, COMMANDS.md, FLAGS.md absorbed into CORE.md
- **Trimmed Agents**: Redundant sections removed from all 7 Opus agents
- **MCP Integration**: Context7 (REQUIRED before implementation) + Sequential coordination
- **Development Tracks**: Quick, Standard, Enterprise workflows

## Features

- **15 Specialized Commands** - Complete workflow from design to deployment
- **7 Expert Opus Agents** - SwiftUI, Architecture, Performance, Testing, Swift, Security, DevOps with MCP integration
- **3 Core Framework Files** - Lean architecture with consolidated core
- **Smart Auto-Activation** - Keyword-based persona and agent routing
- **Context7 Required** - Always consult official documentation before implementation
- **Production-Ready** - Enterprise-grade code patterns with quality gates

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

## Architecture

```
.claude/                       # 3 core framework files (~316 lines)
├── CLAUDE.md                  # Entry point with references
├── CORE.md                    # Principles, rules, agents, flags, MCP
└── WORKFLOWS.md               # Development tracks, ADR templates

.claude-plugin/plugin.json     # Plugin configuration
commands/                      # 15 specialized commands
agents/                        # 7 Opus expert agents
hooks/                         # Smart hooks for best practices
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

| Agent | Domain | MCP Servers |
|-------|--------|-------------|
| **swift-specialist** | Generics, protocols, async/await, actors | Context7, Sequential |
| **swiftui-specialist** | Views, layouts, state, navigation | Context7, Sequential |
| **architecture-specialist** | MVVM, TCA, SwiftData, DI | Context7, Sequential |
| **performance-specialist** | Instruments, memory, rendering | Sequential, Context7 |
| **testing-specialist** | XCTest, UI testing, TDD | Sequential, Context7 |
| **security-specialist** | OWASP, Keychain, encryption, ATS | Sequential, Context7 |
| **devops-specialist** | CI/CD, Xcode Cloud, Fastlane | Sequential, Context7 |

### Development Tracks

| Track | Complexity | Workflow |
|-------|------------|----------|
| **Quick** | <0.3, <5 files | Plan → Implement |
| **Standard** | 0.3-0.7 | Context7 → Analyze → Plan → Implement → Test |
| **Enterprise** | >0.7, >20 files | Context7 → Full Analysis → ADR → Wave → Validate |

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

## Quality Gates

8-step validation cycle:
1. **Syntax** - Language parsers, Context7 validation
2. **Types** - Type compatibility, context-aware suggestions
3. **Lint** - Context7 rules, quality analysis
4. **Security** - Vulnerability assessment, OWASP compliance
5. **Tests** - Coverage ≥80% unit, ≥70% integration
6. **Performance** - Benchmarking, optimization
7. **Documentation** - Completeness, accuracy
8. **Integration** - Deployment validation

## Contributing

Contributions welcome:
1. Enhance commands or agents
2. Improve MCP server integration
3. Better documentation and examples
4. Add new patterns to agent specializations

## License

MIT License - see [LICENSE](LICENSE) file.

---

**Built with ❤️ for the iOS development community**

*Version 5.0.0 • Swift 6.2 • SwiftUI • SwiftData • 15 Commands • 7 Opus Agents • MCP Integration*
