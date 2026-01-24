---
allowed-tools: [Read, Write, Glob, Grep, TodoWrite, Task, WebSearch]
description: "Structured idea generation and solution exploration for iOS development"
argument-hint: "[topic] [--depth shallow|medium|deep] [--focus ui|architecture]"
wave-enabled: true
category: "Planning"
auto-persona: ["architecture-specialist", "swiftui-specialist", "swift-specialist"]
mcp-servers: ["context7", "sequential"]
---

# /ios:brainstorm - Idea Generation

Brainstorm `$ARGUMENTS` with structured ideas and solution exploration.

## Arguments

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--depth` | shallow\|medium\|deep | medium | Analysis depth |
| `--format` | list\|mindmap\|pros-cons\|matrix | list | Output format |
| `--focus` | ui\|architecture\|performance\|data | - | Primary focus area |
| `--constraints` | `<text>` | - | Project constraints |
| `--export` | `<path>` | - | Export results |

## Depth Levels

| Depth | Duration | Output |
|-------|----------|--------|
| `shallow` | ~5 min | Top 3-5 approaches, high-level trade-offs |
| `medium` | ~15 min | Detailed exploration, architecture options |
| `deep` | ~30 min | Comprehensive analysis, migration paths |

## Focus Areas

| Focus | Explores |
|-------|----------|
| `ui` | SwiftUI views, layouts, animations, gestures |
| `architecture` | MVVM, TCA, Clean Architecture, patterns |
| `performance` | Memory, rendering, concurrency, caching |
| `data` | SwiftData, persistence, sync, networking |

## Output Formats

### list (default)
```markdown
## Ideas for [Topic]
1. **Approach A** - Description
   - Pros: ...
   - Cons: ...
```

### pros-cons
```markdown
| Option | Pros | Cons | Effort |
|--------|------|------|--------|
| A | ... | ... | Low |
```

### matrix
```markdown
| Criteria | Weight | Opt A | Opt B |
|----------|--------|-------|-------|
| Maintainability | 30% | 8 | 9 |
```

## Examples

```bash
# Quick feature ideation
/ios:brainstorm "user onboarding flow"

# Deep architecture exploration
/ios:brainstorm "offline-first sync" --depth deep --focus data

# UI pattern exploration with constraints
/ios:brainstorm "dashboard layout" --focus ui --constraints "iPad support"

# Compare approaches with decision matrix
/ios:brainstorm "state management" --format matrix --focus architecture
```

## Workflow

1. **Understand** - Clarify topic and constraints
2. **Diverge** - Generate multiple approaches
3. **Analyze** - Evaluate trade-offs for iOS context
4. **Converge** - Recommend best options with rationale

## Output

```markdown
# Brainstorm: [Topic]
## Focus: ui | architecture | performance | data
## Depth: shallow | medium | deep
## Ideas: [Generated approaches]
## Recommendation: [Best option with rationale]
```
