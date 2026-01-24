---
allowed-tools: [Read, Grep, Glob, Edit, TodoWrite, Task]
description: "Improve iOS code quality, performance, and maintainability"
argument-hint: "[target] [--focus performance|accessibility] [--to observable]"
wave-enabled: true
category: "Quality"
auto-persona: ["swift-specialist", "swiftui-specialist", "performance-specialist", "architecture-specialist"]
mcp-servers: ["context7"]
---

# /ios:improve - iOS Code Improvement

Improve code from `$ARGUMENTS` for quality, performance, and maintainability.

## Arguments

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--focus` | performance\|accessibility\|architecture\|quality | quality | Improvement focus |
| `--to` | observable\|swiftdata\|async\|actor | - | Refactor to modern pattern |
| `--safe` | - | - | Apply only safe, low-risk improvements |
| `--preview` | - | - | Show improvements without applying |
| `--iterative` | - | - | Apply improvements in multiple passes |

## Refactoring Patterns (--to)

| Pattern | From | To |
|---------|------|-----|
| `--to observable` | ObservableObject | @Observable |
| `--to async` | Completion handlers | async/await |
| `--to actor` | NSLock/DispatchQueue | actor |
| `--to swiftdata` | CoreData | SwiftData |

## Focus Areas

| Focus | Improvements |
|-------|-------------|
| `performance` | LazyVStack, image optimization, memory |
| `accessibility` | VoiceOver labels, Dynamic Type, contrast |
| `architecture` | Protocol abstractions, DI, separation |
| `quality` | Naming, SOLID, error handling |

## Examples

```bash
# Quality improvements
/ios:improve Views/ --focus quality --safe --preview

# Performance optimization
/ios:improve ProductListView.swift --focus performance --iterative

# Refactoring
/ios:improve ViewModel.swift --to observable
/ios:improve DataService.swift --to async
/ios:improve Cache.swift --to actor
```

## Output

```markdown
# Improvements: [Target]
## Summary: Files analyzed | Issues found | Applied | Risk level
## Changes Made: File | Issue | Solution | Impact
## Performance Impact: Before → After metrics
## Next Steps: Tests, profiling, verification
```
