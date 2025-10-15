# iOS Development Agents

> Ultra-granular AI agents for iOS development with Swift 6.2, SwiftUI, and SwiftData

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Swift 6.2](https://img.shields.io/badge/Swift-6.2-orange.svg)](https://swift.org)
[![SwiftUI](https://img.shields.io/badge/SwiftUI-Latest-blue.svg)](https://developer.apple.com/swiftui/)
[![SwiftData](https://img.shields.io/badge/SwiftData-Latest-green.svg)](https://developer.apple.com/swiftdata/)
[![Claude Code](https://img.shields.io/badge/Claude-Code-8A2BE2.svg)](https://claude.com/code)

## 🌟 Features

- 🎯 **7 Core Plugins** - Ultra-granular "1 plugin = 1 job" architecture
- 🚀 **Swift 6.2 Support** - Latest language features (InlineArray, nonisolated async, Observations)
- 📱 **SwiftUI & SwiftData** - Modern declarative UI and persistence
- ⚡ **Token Efficient** - 75-90% token savings vs monolithic systems
- 🎨 **Expert Agents** - Deep domain expertise for each specialized area
- 🔮 **27 Plugins Roadmap** - Complete Apple ecosystem coverage planned
- 🧩 **Composable** - Mix and match plugins for your needs
- 📚 **Production-Ready** - Enterprise-grade code and architecture

## 📦 Installation

### Add Marketplace

```bash
/plugin marketplace add CarolaneLFBV/ios-development-agents
```

### Install Plugins

```bash
# Install specific plugins
/plugin install ios-architecture@ios-development
/plugin install swift-language@ios-development
/plugin install swift-concurrency@ios-development

# Or install all 7 core plugins
/plugin install ios-architecture swift-language swift-concurrency swiftui-views swiftui-state swiftdata-models ios-orchestration@ios-development
```

## 🚀 Quick Start

### Create a SwiftUI View

```bash
"Use view-composer to create a user profile card with avatar, name, and bio. Include smooth animations and proper layout."
```

### Design App Architecture

```bash
"Use ios-architect to design a habit tracking app with SwiftData persistence. Provide complete architecture with MVVM pattern."
```

### Implement Swift 6.2 Features

```bash
"Use swift-specialist to refactor this array to use InlineArray for better performance"
"Use concurrency-expert to add async/await with nonisolated async methods"
```

### Complete Feature Workflow

```bash
"Use ios-orchestrator to coordinate building a todo list feature with SwiftUI views, SwiftData models, and proper state management"
```

## 📚 Available Plugins (Phase 1 - v1.0.0)

### Architecture & Language (3 plugins)

| Plugin | Agent | Description |
|--------|-------|-------------|
| **ios-architecture** | `ios-architect` | iOS architecture patterns specialist (MVVM, TCA, Clean Architecture ONLY) |
| **swift-language** | `swift-specialist` | Swift 6.2 language features (generics, protocols, property wrappers, InlineArray, integer generic parameters) |
| **swift-concurrency** | `concurrency-expert` | Swift 6.2 Concurrency (async/await, actors, @MainActor, nonisolated async, Observations framework) |

### SwiftUI (2 plugins)

| Plugin | Agent | Description |
|--------|-------|-------------|
| **swiftui-views** | `view-composer` | SwiftUI view composition specialist (layout, custom views, ViewBuilder ONLY) |
| **swiftui-state** | `state-architect` | SwiftUI state management (@State, @Observable, @Binding ONLY) |

### Data (1 plugin)

| Plugin | Agent | Description |
|--------|-------|-------------|
| **swiftdata-models** | `model-architect` | SwiftData model architect (@Model, relationships, attributes ONLY) |

### Orchestration (1 plugin)

| Plugin | Agent | Description |
|--------|-------|-------------|
| **ios-orchestration** | `ios-orchestrator` | Multi-agent workflow coordination for complex features |

## 🗺️ Roadmap (27 Plugins Planned)

### Phase 2 - Priority 2 (7 plugins)
- **swiftui-animations** - Animations and transitions
- **swiftdata-queries** - Query and FetchDescriptor
- **swiftdata-migrations** - Schema migrations
- **cloudkit-sync** - CloudKit integration
- **swiftui-custom-modifiers** - ViewModifiers
- **project-structure** - Project organization
- **dependency-management** - SPM and packages

### Phase 3 - Priority 3 (6 plugins)
- **widgets-extensions** - WidgetKit
- **healthkit-integration** - HealthKit APIs
- **mapkit-location** - MapKit and CoreLocation
- **storekit-iap** - In-app purchases
- **arkit-augmented** - ARKit
- **passkit-wallet** - Wallet integration

### Phase 4 - Priority 4 (7 plugins)
- **ios-testing** - XCTest
- **ios-performance** - Instruments profiling
- **ios-accessibility** - Accessibility
- **ios-security** - Security audit
- **watchos-development** - watchOS
- **macos-development** - macOS/AppKit
- **visionos-development** - visionOS

### Phase 5 - Priority 5 (7 plugins)
- **mvvm-architecture** - MVVM implementation
- **tca-architecture** - TCA implementation
- **clean-architecture** - Clean arch implementation
- **app-store-deployment** - App Store submission
- **fastlane-automation** - Fastlane CI/CD
- **xcode-cloud** - Xcode Cloud
- **uikit-development** - UIKit legacy

## 🎯 Usage Examples

### Example 1: Swift 6.2 Language Features

```bash
"Use swift-specialist to refactor my fixed-size sprite array to use InlineArray for better performance"
```

**Output**: Complete InlineArray implementation with compile-time size verification and optimal memory layout.

### Example 2: Concurrency with Swift 6.2

```bash
"Use concurrency-expert to add async/await support using nonisolated async methods and the Observations framework"
```

**Output**: Modern concurrency implementation with Swift 6.2 features, proper actor isolation, and streaming state changes.

### Example 3: SwiftUI View Composition

```bash
"Use view-composer to create a user profile card with avatar, name, and bio using proper layout techniques"
```

**Output**: Complete SwiftUI view with ViewBuilder, custom layouts, and proper composition patterns.

### Example 4: SwiftData Models

```bash
"Use model-architect to design data models for a recipe app with categories, ingredients, and cooking steps"
```

**Output**: Complete @Model definitions, relationships, ModelContainer setup, and best practices.

### Example 5: Complete Feature Orchestration

```bash
"Use ios-orchestrator to coordinate building a todo list feature with architecture, views, state management, and data models"
```

**Output**: Complete multi-agent workflow coordinating ios-architect, view-composer, state-architect, and model-architect for end-to-end feature implementation.

## 🏗️ Architecture Philosophy

This system follows a **ultra-granular, "1 plugin = 1 job"** architecture inspired by [wshobson/agents](https://github.com/wshobson/agents):

### Ultra-Granular Plugin System
- **1 Plugin = 1 Job**: Each plugin has a single, well-defined responsibility
- **Clear Boundaries**: Explicit documentation of what each plugin does and doesn't do
- **Token Efficient**: 75-90% token savings vs monolithic systems
- **Composable**: Mix and match only the plugins you need
- **Maintainable**: Independent versioning and isolated evolution

### Expert Agents
- **Deep Specialization**: Each agent is an expert in one specific domain
- **Delegation Matrix**: Agents know when to delegate to other specialists
- **Production-Quality**: Enterprise-grade code and architecture patterns
- **Swift 6.2 Native**: Built for the latest Swift language features

### Multi-Agent Orchestration
- **Coordinated Workflows**: ios-orchestrator coordinates multiple specialists
- **Context Preservation**: Context flows seamlessly between agents
- **Quality Focus**: Each agent enforces domain-specific best practices
- **Scalable**: Easy to add new specialized agents

## 🤝 Contributing

Contributions welcome! This is a modular system where you can:

1. **Improve Existing Agents** - Enhance the 7 core agents with better examples
2. **Add Phase 2-5 Plugins** - Help implement the 27 catalogued plugins
3. **Create New Plugins** - Propose new specialized domains
4. **Enhance Documentation** - Improve examples and guides

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by [wshobson/agents](https://github.com/wshobson/agents) ultra-granular architecture
- Built for the [Claude Code](https://docs.claude.com/claude-code) ecosystem
- Designed for Swift 6.2 and modern Apple platforms

## 🔗 Links

- [Repository](https://github.com/CarolaneLFBV/ios-development-agents)
- [Issues](https://github.com/CarolaneLFBV/ios-development-agents/issues)
- [Claude Code Docs](https://docs.claude.com/claude-code)
- [Plugin Marketplaces](https://docs.claude.com/en/docs/claude-code/plugin-marketplaces)

---

**Built with ❤️ for the iOS development community**

*Version 1.0.0 • Swift 6.2 • SwiftUI • SwiftData • 7 Ultra-Granular Plugins*
