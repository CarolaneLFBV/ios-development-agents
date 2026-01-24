# ROUTING.md - iOS Framework Routing System

## Detection Engine

### Complexity Scoring

```yaml
simple:     # <0.3
  indicators: single file, basic CRUD, <3 steps
  token_budget: 5K
  track: quick

moderate:   # 0.3-0.7
  indicators: multi-file, analysis, 3-10 steps
  token_budget: 15K
  track: standard

complex:    # >0.7
  indicators: system-wide, architecture, >10 steps
  token_budget: 30K+
  track: enterprise
```

### Domain Detection

```yaml
swiftui:
  keywords: [View, @State, @Binding, NavigationStack, LazyVStack]
  files: ["*View.swift", "*.swift with SwiftUI import"]
  agents: [swiftui-specialist]

swift:
  keywords: [protocol, generic, async, await, actor, @Observable]
  files: ["*.swift"]
  agents: [swift-specialist]

architecture:
  keywords: [MVVM, TCA, SwiftData, @Model, repository, clean]
  files: ["*ViewModel.swift", "*Repository.swift", "*Model.swift"]
  agents: [architecture-specialist]

performance:
  keywords: [optimize, slow, memory, Instruments, launch, render]
  files: ["*.swift"]
  agents: [performance-specialist]

testing:
  keywords: [test, XCTest, coverage, mock, stub]
  files: ["*Tests.swift", "*Spec.swift"]
  agents: [testing-specialist]

security:
  keywords: [Keychain, auth, encryption, OWASP, ATS, biometric]
  files: ["*Auth*.swift", "*Security*.swift", "*Keychain*.swift"]
  agents: [security-specialist]

devops:
  keywords: [CI/CD, Xcode Cloud, Fastlane, deploy, archive]
  files: ["*.yml", "Fastfile", "*.xcconfig"]
  agents: [devops-specialist]
```

## Command Routing

```
Request Analysis
├─ Feature Implementation? → /ios:implement
├─ UI/Architecture Design? → /ios:design
├─ Code Enhancement? → /ios:improve
├─ Testing? → /ios:test
├─ Dead Code? → /ios:cleanup
├─ Security Audit? → /ios:security
├─ Documentation? → /ios:document
├─ Migration? → /ios:migrate
├─ Performance? → /ios:optimize
├─ Analysis/Review? → /ios:analyze
├─ Debugging? → /ios:troubleshoot
├─ Accessibility? → /ios:accessibility
├─ Localization? → /ios:localize
├─ Publishing? → /ios:publish
└─ Ideation? → /ios:brainstorm
```

## Wave Orchestration

### Activation Triggers

```yaml
auto_activation:
  conditions:
    - complexity >= 0.7
    - files > 20
    - operation_types > 2
  commands: [implement, design, improve, analyze, migrate, brainstorm]
```

### Wave Strategies

```yaml
progressive:   # Incremental enhancement
  use_case: "Iterative improvements"
  pattern: "Plan → Small changes → Validate → Repeat"

systematic:    # Methodical analysis
  use_case: "Comprehensive review"
  pattern: "Analyze all → Categorize → Prioritize → Execute"

adaptive:      # Dynamic configuration
  use_case: "Varying complexity"
  pattern: "Assess → Adjust scope → Execute → Reassess"

enterprise:    # Large-scale
  use_case: ">100 files, >0.7 complexity"
  pattern: "Full analysis → ADR → Multi-agent → Validate"
```

## Resource Management

```yaml
green:    0-60%   # Full operations
yellow:  60-75%   # Optimize, suggest --uc
orange:  75-85%   # Defer non-critical
red:     85-95%   # Force efficiency
critical: 95%+    # Essential only
```

## Auto-Activation Matrix

| Pattern | Command | Agents | MCP |
|---------|---------|--------|-----|
| "implement login" | /ios:implement | swiftui, architecture | context7 |
| "optimize launch" | /ios:optimize | performance | context7 |
| "migrate swiftdata" | /ios:migrate | architecture, swift | context7 |
| "security audit" | /ios:security | security | context7, sequential |
| "review code" | /ios:analyze --review | all | context7 |
| "debug crash" | /ios:troubleshoot | swift, performance | sequential |

## Quality Gates Integration

All operations apply 8-step validation:
1. Syntax → 2. Types → 3. Lint → 4. Security → 5. Tests → 6. Performance → 7. Accessibility → 8. Integration
