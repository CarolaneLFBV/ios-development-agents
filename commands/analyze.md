---
allowed-tools: [Read, Grep, Glob, Bash, TodoWrite, Task]
description: "Analyze iOS code for quality, performance, security, and review"
argument-hint: "[target] [--focus performance|security] [--review] [--score]"
wave-enabled: true
category: "Analysis"
auto-persona: ["swift-specialist", "architecture-specialist", "performance-specialist", "security-specialist"]
mcp-servers: ["context7"]
---

# /ios:analyze - iOS Code Analysis & Review

Analyze `$ARGUMENTS` for performance, architecture, security, quality, and code review.

## Arguments

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--focus` | performance\|security\|architecture\|quality | quality | Analysis focus |
| `--review` | - | - | Code review mode |
| `--checklist` | - | - | Generate review checklist |
| `--score` | - | - | Include quality score (0-100) |
| `--pr` | - | - | PR review format |
| `--instruments` | - | - | Include Instruments recommendations |
| `--export` | `<path>` | - | Export results |

## Analysis Modes

| Mode | Output |
|------|--------|
| Default | Deep analysis with findings |
| `--review` | Code review with suggestions |
| `--checklist` | Structured checklist output |
| `--score` | Numeric quality assessment |
| `--pr` | PR approve/request changes format |

## Review Checklist (--checklist)

### Swift Best Practices
- [ ] Uses `@Observable` over `ObservableObject`
- [ ] Proper error handling (no force unwraps)
- [ ] Memory management (weak/unowned)
- [ ] Async/await over completion handlers

### SwiftUI Patterns
- [ ] `LazyVStack` for lists
- [ ] Proper state management
- [ ] Small, focused views
- [ ] Modern navigation APIs

### Architecture
- [ ] Single responsibility
- [ ] Protocol-based abstractions
- [ ] Dependency injection

### Security
- [ ] Keychain for sensitive data
- [ ] No hardcoded secrets
- [ ] Input validation

## Quality Score (--score)

```markdown
# Quality Score: 85/100
| Category | Score | Details |
|----------|-------|---------|
| Architecture | 90 | Clean separation |
| Performance | 80 | Minor optimizations |
| Security | 85 | Good practices |
| Maintainability | 85 | Clear code |
```

## Examples

```bash
/ios:analyze . --focus security --export report.md
/ios:analyze ProductList.swift --focus performance --instruments
/ios:analyze . --review --checklist --score
/ios:analyze feature-branch --review --pr
/ios:analyze Services/ --focus architecture
```

## Output

```markdown
# Analysis: [Target]
## Summary: Files | Issues | Severity
## Findings: File | Issue | Severity | Category
## Quality Score: [If --score]
## Action Items: Prioritized fixes
```
