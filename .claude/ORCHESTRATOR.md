# ORCHESTRATOR.md - iOS Framework Orchestration System

Intelligent routing and coordination system for iOS development workflows.

## Overview

The iOS Framework Orchestrator automatically routes requests to the optimal combination of agents, commands, and workflows based on context analysis.

## Architecture

```
User Request
    ↓
Intent Detection
    ↓
Agent Selection ← MCP Integration
    ↓
Command Routing
    ↓
Execution & Validation
    ↓
Quality Gates
    ↓
Results & Recommendations
```

## Agent System

### 5 Specialized Agents

1. **swiftui-specialist** - SwiftUI views, state, navigation, animations
2. **swift-specialist** - Swift 6.2 language features, protocols, generics
3. **architecture-specialist** - MVVM, TCA, Clean Architecture, SwiftData
4. **performance-specialist** - Performance optimization, Instruments profiling
5. **testing-specialist** - XCTest, UI testing, TDD workflows

### Auto-Activation Matrix

```yaml
swiftui-specialist:
  keywords: [SwiftUI, View, navigation, @State, layout]
  files: ["*.swift" with SwiftUI imports]
  commands: [implement, design, improve, refactor]

swift-specialist:
  keywords: [protocol, generic, InlineArray, async, @Observable]
  files: ["*.swift"]
  commands: [implement, improve, refactor, migrate]

architecture-specialist:
  keywords: [MVVM, TCA, SwiftData, @Model, repository]
  files: [ViewModels, Models, Repositories]
  commands: [implement, design, refactor, analyze]

performance-specialist:
  keywords: [performance, optimize, slow, memory, Instruments]
  files: [All Swift files]
  commands: [optimize, analyze, improve]

testing-specialist:
  keywords: [test, XCTest, coverage, mock]
  files: ["*Tests.swift"]
  commands: [test, implement --with-tests]
```

## Command Routing

### Decision Tree

```
Request Analysis
├─ Feature Implementation? → /ios:implement
├─ Code Enhancement? → /ios:improve
├─ Pattern Change? → /ios:refactor
├─ Code Review? → /ios:review
├─ UI Design? → /ios:design
├─ Testing? → /ios:test
├─ Migration? → /ios:migrate
├─ Analysis? → /ios:analyze
├─ Performance? → /ios:optimize
├─ Accessibility? → /ios:accessibility
├─ Publishing? → /ios:publish
├─ Debugging? → /ios:debug
└─ i18n/l10n? → /ios:localize
```

### Context-Based Routing

```yaml
"implement login with SwiftUI":
  command: /ios:implement
  args: LoginView --framework swiftui --pattern mvvm
  agents: [swiftui-specialist, architecture-specialist]

"optimize app launch time":
  command: /ios:optimize
  args: App --metric launch
  agents: [performance-specialist]

"migrate to SwiftData":
  command: /ios:migrate
  args: coredata swiftdata
  agents: [architecture-specialist, swift-specialist]

"add accessibility to profile":
  command: /ios:accessibility
  args: ProfileView --level aa --fix
  agents: [swiftui-specialist]
```

## MCP Server Integration

### Context7 Integration
- **Purpose**: Apple documentation, HIG guidelines, framework patterns
- **Usage**: All commands for Apple best practices
- **Activation**: Automatic for all iOS-specific queries

### Coordination Patterns

```yaml
implement_feature:
  1. Context7: Fetch Apple guidelines
  2. swiftui-specialist: Generate views
  3. architecture-specialist: Apply patterns
  4. testing-specialist: Generate tests (if --with-tests)

optimize_performance:
  1. performance-specialist: Profile with Instruments
  2. Context7: Fetch optimization patterns
  3. swift-specialist: Apply language optimizations
  4. Validation: Measure improvements

migrate_framework:
  1. architecture-specialist: Analyze current structure
  2. Context7: Fetch migration guides
  3. swift-specialist: Apply language changes
  4. swiftui-specialist: Migrate views
  5. testing-specialist: Update tests
```

## Quality Gates

### 8-Step Validation Cycle

1. **Syntax** - Swift compiler validation
2. **Type Safety** - Type checking and inference
3. **Code Quality** - SwiftLint, code standards
4. **Security** - Vulnerability scanning, data protection
5. **Testing** - XCTest execution, coverage ≥80%
6. **Performance** - Performance benchmarks, memory profiling
7. **Accessibility** - VoiceOver, Dynamic Type, WCAG compliance
8. **Integration** - Build validation, compatibility checks

### Quality Metrics

```yaml
code_quality:
  swift_lint: pass
  complexity: low|medium|high
  maintainability_index: 0-100

performance:
  launch_time: <2s
  memory_usage: <100MB baseline
  frame_rate: 60fps

accessibility:
  voiceover_labels: 100%
  dynamic_type: supported
  color_contrast: WCAG AA

testing:
  unit_coverage: ≥80%
  ui_coverage: ≥60%
  critical_paths: 100%
```

## Workflow Patterns

### Standard Feature Implementation

```bash
/ios:implement UserProfile --pattern mvvm --swiftdata --with-tests --accessibility
```

**Orchestration**:
1. **Analysis Phase**
   - Parse requirements
   - Detect frameworks (SwiftUI + SwiftData)
   - Identify pattern (MVVM)

2. **Agent Activation**
   - swiftui-specialist (views)
   - architecture-specialist (MVVM + SwiftData)
   - swift-specialist (language features)
   - testing-specialist (tests)

3. **Implementation Phase**
   - Generate SwiftData models
   - Create MVVM ViewModels
   - Build SwiftUI views
   - Generate XCTests
   - Add accessibility

4. **Validation Phase**
   - Quality gates (all 8 steps)
   - Test execution
   - Accessibility audit

5. **Documentation**
   - Implementation summary
   - Integration steps
   - Testing instructions

### Performance Optimization Workflow

```bash
/ios:optimize App --metric launch --goal "launch<1s"
```

**Orchestration**:
1. Profile with Instruments (performance-specialist)
2. Identify bottlenecks
3. Apply optimizations (swift-specialist, swiftui-specialist)
4. Re-profile and validate
5. Document improvements

### Migration Workflow

```bash
/ios:migrate uikit swiftui --strategy incremental
```

**Orchestration**:
1. Analyze current UIKit code (architecture-specialist)
2. Generate migration plan
3. Convert views incrementally (swiftui-specialist)
4. Update tests (testing-specialist)
5. Validate functionality
6. Document changes

## Agent Coordination

### Parallel Execution
When tasks are independent:
```yaml
implement_full_feature:
  parallel:
    - swiftui-specialist: Generate views
    - architecture-specialist: Design data layer
    - testing-specialist: Prepare test infrastructure
  sequential:
    - Integrate components
    - Run quality gates
```

### Sequential Execution
When dependencies exist:
```yaml
refactor_to_tca:
  sequential:
    1. architecture-specialist: Analyze current architecture
    2. architecture-specialist: Design TCA structure
    3. swift-specialist: Implement reducers
    4. swiftui-specialist: Update views
    5. testing-specialist: Update tests
```

### Hierarchical Coordination
For complex multi-phase tasks:
```yaml
app_redesign:
  coordinator: architecture-specialist
  phases:
    - design: swiftui-specialist
    - implementation: [swiftui, architecture, swift]
    - testing: testing-specialist
    - optimization: performance-specialist
```

## Best Practices

### Orchestration Principles
1. **Single Responsibility**: Each agent handles one domain
2. **Clear Delegation**: Explicit handoffs between agents
3. **Quality First**: All changes pass quality gates
4. **Context Preservation**: Maintain context across agent switches
5. **User-Centric**: Focus on user needs and Apple HIG

### Performance Optimization
- Cache Context7 lookups
- Batch similar operations
- Parallel agent execution when possible
- Intelligent context switching

### Error Handling
- Graceful degradation
- Clear error messages
- Suggested fixes
- Automatic rollback on failures

## Metrics & Monitoring

### Orchestration Metrics
- Agent activation accuracy: >90%
- Command routing accuracy: >95%
- Quality gate pass rate: >80%
- User satisfaction: High

### Performance Metrics
- Average command execution: <30s
- Agent switch overhead: <2s
- Context retention: >95%
- MCP response time: <1s

---

**Key Insight**: The orchestrator learns from patterns and improves routing decisions based on successful outcomes.
