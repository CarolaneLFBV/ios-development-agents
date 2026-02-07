# WORKFLOWS.md - Development Tracks & Templates

## Development Tracks

### Quick Track (complexity <0.3, <5 files)

```yaml
workflow: Plan -> Implement
context7: optional
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
wave: auto-activated (complexity >= 0.7, files > 20)
```

## Wave Strategies

```yaml
progressive:  Plan -> Small changes -> Validate -> Repeat
systematic:   Analyze all -> Categorize -> Prioritize -> Execute
adaptive:     Assess -> Adjust scope -> Execute -> Reassess
enterprise:   Full analysis -> ADR -> Multi-agent -> Validate
```

## Story File Template

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

## ADR Template

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

### Negative
- [Tradeoff 1]

### Risks
- [Risk 1 with mitigation]

## Alternatives Considered
1. [Alternative 1]: Rejected because...
```

### Common iOS ADRs

| ADR | Decision |
|-----|----------|
| ADR-001 | Architecture: MVVM vs TCA vs Clean |
| ADR-002 | Persistence: SwiftData vs CoreData |
| ADR-003 | Navigation: NavigationStack vs Coordinator |
| ADR-004 | DI: Protocol-based vs Container |
| ADR-005 | Networking: URLSession vs Alamofire |

## Quality Checklists

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

### Definition of Done
- [ ] Feature implemented and tested
- [ ] Code reviewed
- [ ] Accessibility validated
- [ ] Performance profiled
- [ ] Security checked
