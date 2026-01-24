# WORKFLOWS.md - iOS Framework Workflows & BMAD

## Development Tracks

### Quick Track (complexity <0.3, <5 files)

```yaml
workflow: Plan → Implement
skip: deep analysis, ADR, facilitation
context7: optional
duration: minutes
```

### Standard Track (complexity 0.3-0.7)

```yaml
workflow:
  1. Context7 Check (REQUIRED)
  2. Analyze existing patterns
  3. Plan implementation
  4. Implement with tests
  5. Validate quality gates

adr: if architecture decision needed
facilitation: enabled
context7: REQUIRED before implementation
```

### Enterprise Track (complexity >0.7, >20 files)

```yaml
workflow:
  1. Context7 Check (REQUIRED + cache)
  2. Full codebase analysis
  3. ADR for architecture decisions
  4. Wave orchestration
  5. Multi-agent implementation
  6. Comprehensive validation
  7. Documentation

adr: REQUIRED
facilitation: full discovery
multi-agent: enabled
documentation: comprehensive
```

## Story File Pattern

```markdown
# Story: [Feature Name]

## Context
- Target: iOS 17+
- Patterns: MVVM, @Observable
- Dependencies: SwiftData, CloudKit (optional)

## Tasks
1. [ ] Create Model with @Model
2. [ ] Create ViewModel with @Observable
3. [ ] Create SwiftUI View
4. [ ] Add unit tests
5. [ ] Add accessibility

## Acceptance Criteria
- [ ] All tests pass (coverage >=80%)
- [ ] VoiceOver support complete
- [ ] Dynamic Type support
- [ ] Performance validated

## ADR References
- ADR-001: Architecture pattern choice
```

## ADR Pattern (Architecture Decision Records)

```markdown
# ADR-[NUMBER]: [Title]

## Status
Proposed | Accepted | Deprecated | Superseded by ADR-XXX

## Context
[Problem description and forces at play]

## Decision
[The change we're proposing or have agreed to]

## Consequences

### Positive
- [Benefit 1]
- [Benefit 2]

### Negative
- [Tradeoff 1]
- [Tradeoff 2]

### Risks
- [Risk 1 with mitigation]

## Alternatives Considered
1. [Alternative 1]: Rejected because...
2. [Alternative 2]: Rejected because...
```

### Common iOS ADRs

| ADR | Decision |
|-----|----------|
| ADR-001 | Architecture: MVVM vs TCA vs Clean |
| ADR-002 | Persistence: SwiftData vs CoreData |
| ADR-003 | Navigation: NavigationStack vs Coordinator |
| ADR-004 | DI: Protocol-based vs Container |
| ADR-005 | Networking: URLSession vs Alamofire |

## Context7 Integration (OBLIGATOIRE)

### Workflow

```yaml
context7_workflow:
  1. detect: Framework being used (SwiftUI, SwiftData, etc.)
  2. query: resolve-library-id → get patterns
  3. apply: Use official patterns, not outdated
  4. cache: Store successful patterns for reuse

auto_trigger:
  - SwiftUI views → Apple HIG patterns
  - SwiftData → @Model, relationships patterns
  - async/await → modern concurrency patterns
  - XCTest → testing best practices
```

### Library Resolution

```swift
// SwiftUI patterns
resolve-library-id("apple/swiftui")
query-docs(topic: "NavigationStack best practices")

// SwiftData patterns
resolve-library-id("apple/swiftdata")
query-docs(topic: "@Model relationships")

// TCA patterns
resolve-library-id("pointfreeco/swift-composable-architecture")
query-docs(topic: "Reducer composition")
```

## Facilitation Mode

### Purpose
Guided questions before solutions to ensure understanding.

### Activation
- Standard track: enabled
- Enterprise track: full discovery
- Quick track: disabled

### Process

```yaml
discovery_questions:
  1. "What problem are we solving?"
  2. "Who are the users?"
  3. "What are the constraints?"
  4. "What patterns exist in the codebase?"
  5. "What's the success criteria?"

only_after_clarity:
  - Propose solutions
  - Write code
  - Make architecture decisions
```

## Standard Workflows

### Feature Implementation

```bash
# Quick
/ios:implement LoginView

# Standard
/ios:implement UserDashboard --pattern mvvm --swiftdata --with-tests

# Enterprise
/ios:implement ECommerceCheckout --pattern tca --swiftdata --cloudkit --with-tests --accessibility
```

### Code Review

```bash
# Quick review
/ios:analyze UserView.swift --review

# Full review with checklist
/ios:analyze . --review --checklist --score

# PR review
/ios:analyze PR#123 --review --pr
```

### Migration

```bash
# Single file
/ios:migrate UserViewModel.swift --to observable

# Full migration
/ios:migrate uikit swiftui --strategy incremental --backup

# Enterprise migration
/ios:migrate coredata swiftdata --strategy systematic --validate --adr
```

### Security Audit

```bash
# Quick audit
/ios:security AuthService.swift

# Full audit
/ios:security . --owasp --report

# Enterprise audit
/ios:security . --owasp --keychain --biometric --report --adr
```

## Quality Checklist

### Pre-Implementation
- [ ] Context7 consulted for patterns
- [ ] Existing patterns identified
- [ ] ADR created if needed
- [ ] Story file created

### Post-Implementation
- [ ] All 8 quality gates pass
- [ ] Tests coverage >=80%
- [ ] Accessibility validated
- [ ] Documentation updated
- [ ] Story file updated

### Definition of Done
- [ ] Feature implemented
- [ ] Tests written and passing
- [ ] Code reviewed
- [ ] Accessibility validated
- [ ] Documentation updated
- [ ] Performance profiled
- [ ] Security checked
