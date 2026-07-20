# Getting Started with the iOS Development Framework

Welcome! This guide gets you productive with the **iOS Development Framework** — a single Claude Code plugin (`ios`) providing **15 commands** and **7 Opus specialist agents** for Swift 6, SwiftUI, and SwiftData.

## Installation

```bash
# 1. Add the marketplace
/plugin marketplace add CarolaneLFBV/ios-development-agents

# 2. Install the plugin
/plugin install ios@ios-development

# 3. Verify
/help          # the /ios:* commands should now be listed
```

Optional but recommended: install the **Context7** MCP server so the agents can consult up-to-date Apple documentation before writing code.

```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp
```

The agents request the `mcp__context7__*` tools; without Context7 they fall back to their built-in patterns.

## Two ways to work

### 1. Run a command (`/ios:*`)

Commands orchestrate a workflow and delegate to the right specialist(s) automatically.

```bash
/ios:implement "user profile screen with avatar and edit button" --framework swiftui --pattern mvvm
/ios:analyze UserProfileView.swift --review --checklist --score
/ios:troubleshoot "EXC_BAD_ACCESS" --type crash --trace
```

### 2. Invoke a specialist directly

For a focused, single-domain task, ask for the agent by name — the main agent also delegates automatically based on each specialist's description.

```bash
"Use swiftui-specialist to build a profile card with avatar, name, bio and a follow button, with animations and accessibility labels."
"Use architecture-specialist to design SwiftData models for a recipe app (Recipe, Ingredient, Category) with relationships."
```

## The 15 commands

| Category | Commands |
|----------|----------|
| **Development** | `implement`, `design` |
| **Quality** | `improve`, `test`, `cleanup`, `security` |
| **Documentation** | `document` |
| **Migration** | `migrate`, `optimize` |
| **Analysis** | `analyze`, `troubleshoot` |
| **Delivery** | `accessibility`, `localize`, `publish` |
| **Planning** | `brainstorm` |

Every command accepts `$ARGUMENTS` (a target and/or flags). See each command's file in `commands/` for its flags, or run it with a natural-language description.

```bash
/ios:design "e-commerce app" --scope architecture --pattern mvvm --modules
/ios:improve ViewModel.swift --to observable
/ios:migrate coredata swiftdata --backup
/ios:security . --owasp --report
/ios:test UserViewModel --generate --type unit
/ios:accessibility LoginView.swift --level aa --fix
/ios:brainstorm "offline-first sync" --depth deep --focus data
```

## The 7 Opus agents

All agents run on **Opus** and query Context7 before writing non-trivial code. Commands route to them via the Task tool; you can also invoke them directly.

| Agent | Domain |
|-------|--------|
| **swift-specialist** | Swift 6, concurrency (async/await, actors), generics, protocols, memory/ownership, networking |
| **swiftui-specialist** | Views, layout, state, navigation, animations, view-level accessibility |
| **architecture-specialist** | MVVM, TCA, Clean, SwiftData, dependency injection, app structure |
| **performance-specialist** | Instruments profiling, memory, rendering, launch time |
| **testing-specialist** | Swift Testing, XCTest, UI/snapshot testing, TDD, mocking |
| **security-specialist** | OWASP, Keychain, auth/biometrics, encryption, ATS |
| **devops-specialist** | CI/CD, Xcode Cloud, GitHub Actions, Fastlane, signing, TestFlight |

Each specialist owns its domain and delegates out of scope (e.g. swiftui-specialist delegates Swift-language questions to swift-specialist). See `.claude/CORE.md` for the full delegation map.

### Choosing an agent

- Architecture / data modeling → **architecture-specialist**
- UI implementation → **swiftui-specialist**
- Language / concurrency → **swift-specialist**
- Slow or leaking code → **performance-specialist**
- Tests → **testing-specialist**
- Secrets, auth, crypto → **security-specialist**
- CI/CD, releases → **devops-specialist**

## Common workflows

### Build a new feature end-to-end

```bash
/ios:implement "task manager with SwiftData and CloudKit sync" --swiftdata --cloudkit --with-tests --accessibility
```

`implement` coordinates architecture → SwiftUI/Swift → testing → accessibility, each specialist consulting Context7.

### Review and harden existing code

```bash
/ios:analyze . --focus security       # fans out to the security-specialist
/ios:improve Views/ --focus performance --preview
/ios:security AuthService.swift --focus auth --fix
```

### Modernize / migrate

```bash
/ios:migrate uikit swiftui --strategy incremental
/ios:improve DataService.swift --to async
"Use swift-specialist to modernize this code to Swift 6 strict concurrency."
```

## Tips for best results

1. **Be specific.** ❌ "Create a profile view" → ✅ "Create a SwiftUI profile view with an 80pt circular avatar, headline-font name, 3-line bio, and a follow button with haptic feedback."
2. **State your constraints.** Target (iOS 17+), framework (SwiftUI/UIKit), pattern (MVVM/TCA), persistence, accessibility needs.
3. **Iterate.** Agents refine their output: "Use a spring animation with 0.6 response", "Add error handling for network failures", "Make this VoiceOver-friendly".
4. **Install Context7** so agents pull current Apple APIs instead of relying on memory.

## Next steps

- **Explore the framework**: read `.claude/CORE.md` (principles, agents, flags) and `.claude/WORKFLOWS.md` (development tracks, ADR templates).
- **Build your own plugin**: see [`examples/minimal-plugin/`](../examples/minimal-plugin/README.md) for an agent + command template in the real Claude Code format.
- **Main README**: [../README.md](../README.md).

---

**Ready to build great iOS apps with AI assistance!** 🚀
