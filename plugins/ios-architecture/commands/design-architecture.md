---
name: Design Architecture
description: Design complete iOS app architecture using MVVM, TCA, or Clean Architecture patterns
version: 1.0

required_parameters:
  - name: app-description
    type: string
    description: Brief description of the app and its main features

optional_parameters:
  - name: pattern
    type: string
    options: [mvvm, tca, clean, auto]
    default: auto
    description: Architecture pattern to use (auto = intelligent selection)
  - name: complexity
    type: string
    options: [simple, medium, complex]
    default: medium
  - name: platforms
    type: array
    description: Target platforms (ios, macos, watchos)
    default: [ios]

execution:
  phases:
    - analysis
    - architecture_design
    - validation
---

# Design Architecture Command

Creates complete iOS application architecture design based on requirements and complexity.

## Phase 1: Requirements Analysis

### Objective
Analyze app requirements to determine optimal architecture pattern.

### Execution
```
Use Task tool:
- subagent_type: "general-purpose"
- description: "Architecture requirements analysis"
- prompt: """
  Analyze this iOS app for architecture design:

  App: {{app-description}}
  Target platforms: {{platforms}}
  Specified complexity: {{complexity}}

  Provide:
  1. Feature breakdown
  2. Complexity assessment (state management, data flow, side effects)
  3. Architecture pattern recommendation with rationale
  4. Key architectural challenges
  5. Scalability considerations

  Consider:
  - Number of screens/features
  - State management complexity
  - Data persistence needs
  - Network operations
  - Business logic complexity
  """
```

### Expected Output
- Feature list with complexity scores
- Architecture pattern recommendation
- Key challenges identified
- Technical constraints

### Success Criteria
- ✅ Clear understanding of requirements
- ✅ Pattern recommendation justified
- ✅ Complexity accurately assessed

---

## Phase 2: Architecture Design

### Objective
Design complete architecture using recommended pattern.

### Execution
```
Use Task tool:
- subagent_type: "general-purpose"
- description: "iOS architecture design"
- prompt: """
  Design iOS architecture for: {{app-description}}

  Context from Phase 1: {{PHASE1_ANALYSIS}}
  Pattern: {{pattern}} (or use Phase 1 recommendation if auto)
  Platforms: {{platforms}}

  Create complete architecture design:

  1. Layer Structure
     - Define all architectural layers
     - Specify responsibilities of each layer
     - Document dependencies between layers

  2. Component Organization
     - Directory structure
     - Module organization
     - File naming conventions

  3. Data Flow
     - How data moves through layers
     - State management approach
     - Event handling patterns

  4. Dependency Injection
     - DI strategy (constructor injection, container, etc.)
     - How dependencies are resolved
     - Protocol abstractions needed

  5. Key Components
     - ViewModels/Reducers design
     - Repository/Service interfaces
     - Use cases (if applicable)
     - Data models structure

  6. Testing Strategy
     - What to test at each layer
     - Mock/stub strategy
     - Test organization

  Provide concrete code examples for each component type.
  """
```

### Expected Output
- Complete layer structure diagram
- Directory organization
- Data flow documentation
- Component designs with code examples
- DI strategy
- Testing approach

### Success Criteria
- ✅ All layers clearly defined
- ✅ Dependencies flow correctly
- ✅ Testability designed in
- ✅ Code examples provided

---

## Phase 3: Architecture Validation

### Objective
Validate architecture design for common issues and best practices.

### Execution
```
Use Task tool:
- subagent_type: "general-purpose"
- description: "Architecture validation"
- prompt: """
  Validate this architecture design:

  Architecture from Phase 2: {{PHASE2_ARCHITECTURE}}

  Check for:

  1. Separation of Concerns
     - Are responsibilities clearly separated?
     - Any layer violations?
     - God objects or massive classes?

  2. Dependency Flow
     - Dependencies flow in correct direction?
     - No circular dependencies?
     - Inner layers independent?

  3. Testability
     - Components easily testable?
     - Proper abstractions for mocking?
     - Clear testing strategy?

  4. Scalability
     - Can handle growth in features?
     - Easy to add new components?
     - Performance considerations addressed?

  5. Common Pitfalls
     - Framework in domain layer?
     - Tight coupling between layers?
     - Missing abstractions?
     - Over-engineering?

  6. Best Practices
     - Follows iOS community standards?
     - Modern Swift patterns used?
     - Clear naming conventions?

  Provide:
  - Validation checklist with ✅/❌
  - Issues found with severity (critical/warning/suggestion)
  - Recommended improvements
  - Final architecture quality score (0-100)
  """
```

### Expected Output
- Validation checklist
- Issues identified with severity
- Improvement recommendations
- Architecture quality score

### Success Criteria
- ✅ No critical issues
- ✅ Score above 85/100
- ✅ All best practices followed

---

## Final Deliverables

### Architecture Document
```markdown
# {{App Name}} Architecture

## Overview
[Pattern used and why]

## Layer Structure
[Complete layer diagram]

## Directory Organization
```
AppName/
├── Domain/
├── Data/
├── Presentation/
└── Infrastructure/
```

## Components
[Key component designs]

## Data Flow
[How data moves through app]

## Dependency Injection
[DI strategy and setup]

## Testing Strategy
[How to test this architecture]

## Trade-offs
[What was gained/lost with this design]
```

### Code Examples
- ViewModel/Reducer example
- Repository interface example
- Use case example (if applicable)
- View example with architecture integration

### Validation Report
- Architecture score: XX/100
- Issues found: X critical, X warnings
- Recommendations: [list]

---

## Usage Examples

### Simple CRUD App
```bash
/ios-architecture:design-architecture \
  --app-description "Task manager with local storage" \
  --pattern mvvm \
  --complexity simple
```

### Complex Social App
```bash
/ios-architecture:design-architecture \
  --app-description "Social media app with real-time messaging, feeds, and stories" \
  --pattern tca \
  --complexity complex \
  --platforms ios,watchos
```

### Auto-Pattern Selection
```bash
/ios-architecture:design-architecture \
  --app-description "Recipe app with meal planning and grocery lists" \
  --pattern auto
```

---

## What Gets Created

- ✅ Complete architecture design document
- ✅ Layer structure and organization
- ✅ Component designs with code examples
- ✅ Data flow documentation
- ✅ Testing strategy
- ✅ Validation report with score
- ✅ Implementation guidelines

---

This command creates production-ready architecture designs tailored to your specific app needs.
