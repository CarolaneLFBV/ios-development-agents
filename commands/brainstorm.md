---
allowed-tools: [Read, Write, Glob, Grep, TodoWrite, Task, WebSearch]
description: "Structured idea generation and solution exploration for iOS development"
category: "Planning & Ideation"
auto-persona: ["architecture-specialist", "swiftui-specialist", "swift-specialist"]
mcp-servers: ["context7"]
---

# /ios:brainstorm - Idea Generation

## Purpose
Generate structured ideas, explore solutions, and evaluate architectural approaches for iOS features and applications.

## Usage
```bash
/ios:brainstorm [topic] [--depth <level>] [--format <format>] [--focus <area>]
```

## Arguments
- `[topic]` - Feature, problem, or concept to brainstorm
- `--depth shallow|medium|deep` - Analysis depth (default: medium)
- `--format list|mindmap|pros-cons|matrix` - Output format
- `--focus ui|architecture|performance|data` - Primary focus area
- `--constraints <text>` - Project constraints to consider
- `--export <path>` - Export results to file

## Depth Levels

### Shallow (~5 min)
- Quick ideation
- Top 3-5 approaches
- High-level trade-offs

### Medium (~15 min)
- Detailed exploration
- Architecture options
- SwiftUI patterns
- Code structure suggestions

### Deep (~30 min)
- Comprehensive analysis
- Multiple architecture comparisons
- Performance considerations
- Testing strategies
- Migration paths

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
2. **Approach B** - Description
```

### pros-cons
```markdown
## Option Analysis
| Option | Pros | Cons | Effort |
|--------|------|------|--------|
| A | ... | ... | Low |
```

### matrix
```markdown
## Decision Matrix
| Criteria | Weight | Opt A | Opt B | Opt C |
|----------|--------|-------|-------|-------|
| Maintainability | 30% | 8 | 9 | 7 |
```

## Examples

```bash
# Quick feature ideation
/ios:brainstorm "user onboarding flow"

# Deep architecture exploration
/ios:brainstorm "offline-first sync" --depth deep --focus data

# UI pattern exploration with constraints
/ios:brainstorm "dashboard layout" --focus ui --constraints "iPad support, accessibility"

# Compare approaches with decision matrix
/ios:brainstorm "state management" --format matrix --focus architecture
```

## Workflow

1. **Understand** - Clarify topic and constraints
2. **Diverge** - Generate multiple approaches
3. **Analyze** - Evaluate trade-offs for iOS context
4. **Converge** - Recommend best options with rationale

---

**Delegates to**: architecture-specialist (patterns), swiftui-specialist (UI), swift-specialist (implementation)
