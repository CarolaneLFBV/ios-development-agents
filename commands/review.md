---
allowed-tools: [Read, Grep, Glob, TodoWrite]
description: "Comprehensive iOS code review with Apple guidelines compliance"
category: "Quality & Analysis"
auto-persona: ["swift-specialist", "architecture-specialist", "testing-specialist"]
mcp-servers: ["context7"]
---

# /ios:review - iOS Code Review

## Purpose
Comprehensive code review for iOS projects checking Apple Human Interface Guidelines, Swift API Design Guidelines, performance, security, and accessibility.

## Usage
```bash
/ios:review [target] [--focus <area>] [--format <format>]
```

## Arguments
- `[target]` - Files, PR, or commit to review
- `--focus security|performance|quality|architecture|accessibility` - Review focus
- `--format report|checklist|metrics` - Output format
- `--export <path>` - Export review results

## Review Checklist

### Code Quality (0-100)
- [ ] Swift API Design Guidelines compliance
- [ ] Proper error handling
- [ ] No force unwrapping
- [ ] Meaningful naming conventions
- [ ] Appropriate comments and documentation

### Architecture (0-100)
- [ ] Clear separation of concerns
- [ ] SOLID principles applied
- [ ] Proper dependency injection
- [ ] Testable design
- [ ] Appropriate design patterns

### Performance (0-100)
- [ ] Efficient algorithms
- [ ] Proper memory management
- [ ] No strong reference cycles
- [ ] LazyVStack for long lists
- [ ] Optimized image loading

### Security (0-100)
- [ ] No hardcoded secrets
- [ ] Proper authentication
- [ ] Secure data storage (Keychain)
- [ ] Input validation
- [ ] HTTPS enforcement

### Accessibility (0-100)
- [ ] VoiceOver labels
- [ ] Dynamic Type support
- [ ] Keyboard navigation
- [ ] Color contrast WCAG compliance
- [ ] Accessibility identifiers

## Output Example

```markdown
# Code Review: UserAuthentication

## Overall Score: 78/100

### ✅ Strengths
- Clean MVVM architecture
- Comprehensive error handling
- Good test coverage (85%)

### ⚠️ Issues Found

#### High Priority
1. **Security**: API keys hardcoded in AuthService.swift:45
   - Risk: Critical
   - Recommendation: Move to Keychain or environment variables

2. **Performance**: Force loading all users in UserListView.swift:23
   - Risk: High
   - Recommendation: Use lazy loading with pagination

#### Medium Priority
3. **Accessibility**: Missing VoiceOver labels on LoginView buttons
   - Risk: Medium
   - Recommendation: Add .accessibilityLabel() modifiers

### 📊 Metrics
- Files reviewed: 12
- Lines of code: 1,250
- Test coverage: 85%
- Technical debt: 3.5 hours

### 🎯 Action Items
1. Fix security issues (2 hours)
2. Implement pagination (3 hours)
3. Add accessibility labels (1 hour)
```

---

**Delegates to**: All specialists for comprehensive review
