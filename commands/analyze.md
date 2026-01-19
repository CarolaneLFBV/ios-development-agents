---
allowed-tools: [Read, Grep, Glob, Bash, TodoWrite, Task]
description: "Analyze iOS code for quality, performance, security, and review"
argument-hint: "[target] [--focus performance|security|architecture] [--review]"
---

# /ios:analyze - iOS Code Analysis & Review

Analyze `$ARGUMENTS` for performance, architecture, security, quality, and code review.

## Arguments
- `--focus performance|security|architecture|quality` - Analysis focus
- `--instruments` - Include Instruments profiling recommendations
- `--export <path>` - Export analysis results
- `--review` - Code review mode with actionable feedback
- `--checklist` - Generate review checklist
- `--score` - Include quality scores (0-100)
- `--pr` - PR review format with approve/request changes

## Analysis Modes

### Standard Analysis
```bash
/ios:analyze . --focus security
/ios:analyze ProductList.swift --focus performance --instruments
```

### Code Review (--review)
```bash
/ios:analyze PR#123 --review --pr
/ios:analyze UserService.swift --review --checklist
```

## Analysis Areas

### Performance Analysis
- Algorithmic complexity (O notation)
- Memory allocations and leaks
- Render performance (60fps target)
- Network efficiency
- Battery impact

### Security Analysis
- OWASP Mobile Top 10 compliance
- Data protection assessment
- Authentication/authorization
- Input validation
- Keychain usage

### Architecture Analysis
- SOLID principles adherence
- Dependency management
- Layer separation
- Protocol usage
- Testability assessment

### Quality Analysis
- Code complexity metrics
- Documentation coverage
- Test coverage
- Technical debt estimation
- Naming conventions

## Code Review Checklist (--checklist)

### Swift Best Practices
- [ ] Uses `@Observable` over `ObservableObject`
- [ ] Proper error handling (no force unwraps)
- [ ] Memory management (weak/unowned where needed)
- [ ] Async/await over completion handlers
- [ ] Actor usage for shared mutable state

### SwiftUI Patterns
- [ ] `LazyVStack`/`LazyHStack` for lists
- [ ] Proper `@State`/`@Binding` usage
- [ ] View composition (small, focused views)
- [ ] Environment objects at appropriate level
- [ ] Navigation using modern APIs

### Architecture
- [ ] Single responsibility per type
- [ ] Protocol-based abstractions
- [ ] Dependency injection
- [ ] Separation of concerns
- [ ] Testable design

### Security
- [ ] Keychain for sensitive data
- [ ] No hardcoded secrets
- [ ] Input validation
- [ ] Secure networking (HTTPS)
- [ ] Proper authentication handling

## Quality Scoring (--score)

```markdown
# Quality Score: 85/100

## Breakdown
| Category | Score | Details |
|----------|-------|---------|
| Architecture | 90 | Clean separation, good protocols |
| Performance | 80 | Minor optimization opportunities |
| Security | 85 | Keychain usage, needs input validation |
| Maintainability | 85 | Good naming, some complex methods |
| Test Coverage | 80 | 80% coverage, missing edge cases |
```

## PR Review Format (--pr)

```markdown
## Code Review: PR #123

### Summary
✅ **Approve** / ⚠️ **Request Changes** / 💬 **Comment**

### Strengths
- Clean architecture with proper separation
- Good test coverage for happy paths

### Required Changes
1. **Security**: Use Keychain instead of UserDefaults for tokens
2. **Memory**: Add `[weak self]` in completion handler

### Suggestions
- Consider using `LazyVStack` for better scroll performance
- Extract magic numbers to constants

### Files Reviewed
- `UserService.swift` - ⚠️ Security concern
- `ProfileView.swift` - ✅ Looks good
- `AuthManager.swift` - 💬 Minor suggestions
```

## Output Structure

```markdown
# Analysis: [Target]
## Summary: Files | Issues | Severity breakdown
## Findings:
| File | Issue | Severity | Category | Recommendation |
## Metrics:
| Metric | Value | Target | Status |
## Action Items: Prioritized fixes
## Quality Score: [If --score]
```

## Examples
```bash
/ios:analyze . --focus security --export security-report.md
/ios:analyze ProductList.swift --focus performance --instruments
/ios:analyze . --review --checklist --score
/ios:analyze feature-branch --review --pr
/ios:analyze Services/ --focus architecture
```

---

**Delegates to**: performance-specialist (perf), swift-specialist (quality), architecture-specialist (arch), security-specialist (security)
