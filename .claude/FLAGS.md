# FLAGS.md - iOS Framework Flag System

## Planning & Analysis

| Flag | Purpose | Auto-Activation |
|------|---------|-----------------|
| `--think` | Module analysis (4K) | Import chains >5 files |
| `--think-hard` | System analysis (10K) | Cross-module >10 refs |
| `--ultrathink` | Critical analysis (32K) | Legacy modernization |
| `--plan` | Show execution plan | Manual only |
| `--validate` | Pre-operation validation | Risk >0.7 |

## iOS-Specific Flags

### Framework Flags
| Flag | Purpose | Default |
|------|---------|---------|
| `--framework swiftui\|uikit\|hybrid` | UI framework | swiftui |
| `--pattern mvvm\|tca\|clean` | Architecture | mvvm |
| `--swiftdata` | SwiftData integration | - |
| `--cloudkit` | CloudKit sync | - |
| `--ios <version>` | Min iOS version | 17 |

### Quality Flags
| Flag | Purpose |
|------|---------|
| `--with-tests` | Generate XCTests |
| `--accessibility` | Full a11y support |
| `--safe` | Conservative changes |
| `--preview` | Preview changes |

### Refactoring Flags
| Flag | Purpose |
|------|---------|
| `--to observable` | Migrate to @Observable |
| `--to async` | Migrate to async/await |
| `--to actor` | Migrate to actor |
| `--to swiftdata` | Migrate to SwiftData |

### Analysis Flags
| Flag | Purpose |
|------|---------|
| `--review` | Code review mode |
| `--checklist` | Review checklist |
| `--score` | Quality score (0-100) |
| `--pr` | PR review format |
| `--focus <area>` | Focus: security\|performance\|quality\|architecture |

### Debug Flags
| Flag | Purpose |
|------|---------|
| `--debug` | Debug mode |
| `--breakpoints` | Generate breakpoints |
| `--trace` | Detailed trace |
| `--type <type>` | Type: crash\|hang\|memory\|ui |

### Design Flags
| Flag | Purpose |
|------|---------|
| `--scope ui\|architecture\|system` | Design scope |
| `--modules` | Module breakdown |
| `--diagram` | Generate diagram |

## MCP Control

| Flag | Purpose | Auto-Activation |
|------|---------|-----------------|
| `--c7` | Force Context7 | All iOS commands |
| `--seq` | Force Sequential | --think flags, security |
| `--no-mcp` | Disable MCP | Manual only |

## Efficiency Flags

| Flag | Purpose | Auto-Activation |
|------|---------|-----------------|
| `--uc` | Ultra-compressed | Context >75% |
| `--answer-only` | Direct response | Manual only |
| `--safe-mode` | Max validation | Production, risk >85% |

## Wave Control

| Flag | Purpose |
|------|---------|
| `--wave-mode auto\|force\|off` | Wave orchestration |
| `--wave-strategy <strategy>` | progressive\|systematic\|adaptive\|enterprise |

## Agent Control

| Flag | Purpose |
|------|---------|
| `--agent <name>` | Force specific agent |
| `--agents <list>` | Multi-agent coordination |
| `--multi-agent <mode>` | auto\|parallel\|sequential\|hierarchical |

## Flag Precedence

1. Safety flags (`--safe-mode`) > optimization
2. Explicit flags > auto-activation
3. Thinking: `--ultrathink` > `--think-hard` > `--think`
4. `--no-mcp` overrides MCP flags
5. Scope: system > project > module > file
6. `--uc` auto-activates when context >75%

## Auto-Activation Patterns

```yaml
swiftui_development:
  triggers: [View, @State, NavigationStack]
  flags: [--framework swiftui, --c7]
  agents: [swiftui-specialist]

architecture_work:
  triggers: [@Model, ViewModel, repository]
  flags: [--pattern mvvm, --c7]
  agents: [architecture-specialist]

security_audit:
  triggers: [Keychain, auth, encryption]
  flags: [--focus security, --c7, --seq, --validate]
  agents: [security-specialist]

performance_optimization:
  triggers: [optimize, slow, memory, launch]
  flags: [--focus performance, --c7]
  agents: [performance-specialist]

complex_debugging:
  triggers: [crash, hang, memory leak]
  flags: [--think, --seq, --debug]
  agents: [swift-specialist, performance-specialist]
```
