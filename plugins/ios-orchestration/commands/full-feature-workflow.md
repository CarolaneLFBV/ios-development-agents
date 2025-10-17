---
name: ios-dev:orchestration
description: End-to-end iOS feature implementation from architecture to deployment. Orchestrates multiple specialized agents through 8 phases for production-quality features.
version: 1.0

required_parameters:
  - name: feature
    type: string
    description: Feature description (e.g., "User profile with photo upload")
  - name: platform
    type: string
    options: [ios, ipados, watchos, macos, multi-platform]
  - name: complexity
    type: string
    options: [simple, medium, complex]

optional_parameters:
  - name: ui-framework
    type: string
    options: [swiftui, uikit, hybrid]
    default: swiftui
  - name: persistence
    type: string
    options: [swiftdata, coredata, none]
    default: swiftdata
  - name: cloud-sync
    type: boolean
    default: false
  - name: testing-strategy
    type: string
    options: [unit-only, integration, full-coverage]
    default: integration
  - name: deployment
    type: boolean
    default: false

execution:
  phases:
    - architecture_design
    - data_model_implementation
    - ui_implementation
    - business_logic_integration
    - testing_comprehensive
    - performance_optimization
    - accessibility_review
    - deployment_preparation
---

# iOS Full Feature Workflow - Complete Implementation

Complete orchestration for implementing a production-ready iOS feature from conception to deployment.

## Phase 1: Architecture Design 🏗️

### Objective
Design the feature architecture, module structure, and data flow.

### Execution
```
Use Task tool:
- subagent_type: "ios-architect"
- prompt: """
  Design architecture for iOS feature: {{feature}}

  Requirements:
  - Platform: {{platform}}
  - Complexity: {{complexity}}
  - UI Framework: {{ui-framework}}
  - Persistence: {{persistence}}
  - Cloud Sync: {{cloud-sync}}

  Provide comprehensive architecture including:
  1. Architecture pattern recommendation (MVVM/TCA/Clean)
  2. Module structure with file organization
  3. Key protocols and types
  4. Data flow diagram
  5. Technology stack justification
  6. Dependency injection strategy

  Output format: Markdown document with code examples
  """
```

### Expected Output
- Architecture document (.md)
- Module structure diagram
- Protocol definitions
- Technology decisions with rationale

### Success Criteria
- ✅ Clear separation of concerns (Presentation/Domain/Data)
- ✅ Testable architecture with dependency injection
- ✅ Scalable design for future growth
- ✅ Compliance with Apple HIG

---

## Phase 2: Data Model Implementation 💾

### Objective
Implement SwiftData models, relationships, and persistence layer based on architecture.

### Execution
```
Use Task tool:
- subagent_type: "swiftdata-architect"
- prompt: """
  Implement data models for feature: {{feature}}

  Architecture context from Phase 1:
  {{PASS_PHASE1_ARCHITECTURE}}

  Requirements:
  - Persistence type: {{persistence}}
  - Cloud Sync: {{cloud-sync}}
  - Platform: {{platform}}

  Provide complete data layer:
  1. @Model definitions with proper relationships
  2. ModelContainer configuration
  3. Repository protocol and implementation
  4. Query examples for common operations
  5. Migration plan for schema versioning
  6. CloudKit integration setup (if enabled)
  7. Unit tests for models and repositories

  Ensure:
  - Proper relationship delete rules
  - Strategic indexing for performance
  - CloudKit-ready design (optional relationships)
  """
```

### Expected Output
- Model files (.swift) with @Model macro
- ModelContainer configuration
- Repository protocol + implementation
- Query helpers and FetchDescriptors
- Migration strategy document
- Unit tests for data layer

### Success Criteria
- ✅ Relationships correctly modeled with appropriate delete rules
- ✅ Repository pattern implemented for testability
- ✅ CloudKit-ready (if cloud sync enabled)
- ✅ Query performance optimized with indexes
- ✅ Unit tests passing (80%+ coverage)

---

## Phase 3: UI Implementation 🎨

### Objective
Build SwiftUI views, view composition, and user interface following design.

### Execution
```
Use Task tool:
- subagent_type: "swiftui-specialist"
- prompt: """
  Implement user interface for feature: {{feature}}

  Context from previous phases:
  - Architecture: {{PHASE1_ARCHITECTURE}}
  - Data models: {{PHASE2_MODELS}}

  Requirements:
  - UI Framework: {{ui-framework}}
  - Platform: {{platform}}
  - Design system: Use native SwiftUI components

  Create complete UI implementation:
  1. Main view hierarchy (max 100 lines per view)
  2. Composed subviews for reusability
  3. ViewModels with @Observable (Swift 6)
  4. Custom view modifiers for consistent styling
  5. Animations and transitions
  6. Preview providers for all states
  7. Basic accessibility labels

  Best practices:
  - View composition (no massive views)
  - Proper state management (@State, @Binding, @Environment)
  - Responsive layout for all device sizes
  - Loading/error states
  """
```

### Expected Output
- View files (.swift) with SwiftUI code
- ViewModel files with @Observable
- Custom view modifiers
- Preview providers for all states
- Supporting view components

### Success Criteria
- ✅ View composition (all views < 100 lines)
- ✅ Proper state management with @Observable
- ✅ Responsive layout tested on multiple sizes
- ✅ Previews for all UI states (default, loading, error)
- ✅ Animations smooth and purposeful

---

## Phase 4: Business Logic Integration ⚙️

### Objective
Connect UI, data layer, and implement use cases / business logic.

### Execution
```
Use Task tool:
- subagent_type: "ios-architect"
- prompt: """
  Integrate business logic for feature: {{feature}}

  Context from previous phases:
  - Architecture: {{PHASE1}}
  - Data layer: {{PHASE2}}
  - UI layer: {{PHASE3}}

  Implement integration layer:
  1. Use case classes (business operations)
  2. Connect ViewModels to repositories
  3. Dependency injection container setup
  4. Error handling strategy
  5. Async/await data flow
  6. Networking layer (if needed)
  7. Background task management
  8. State synchronization

  Ensure:
  - Clean separation: UI ↔ Domain ↔ Data
  - Proper Swift Concurrency usage (async/await, actors)
  - Comprehensive error handling
  - Testable use cases
  """
```

### Expected Output
- Use case implementations
- Repository implementations connected
- Dependency injection setup
- Error types and handling
- Integration code

### Success Criteria
- ✅ Clean architecture boundaries maintained
- ✅ Async/await patterns used correctly
- ✅ Proper error handling throughout
- ✅ Testable use cases with protocols
- ✅ No tight coupling between layers

---

## Phase 5: Testing Comprehensive 🧪

### Objective
Implement unit, integration, and UI tests based on testing strategy.

### Execution
```
Use Task tool:
- subagent_type: "xctest-specialist"
- prompt: """
  Create comprehensive test suite for feature: {{feature}}

  Testing Strategy: {{testing-strategy}}

  Context:
  - Complete implementation from Phases 1-4

  Implement testing suite:
  1. Unit tests for ViewModels and Use Cases (80%+ coverage)
  2. Integration tests for Repository + SwiftData (70%+ coverage)
  3. UI tests for critical user flows (main paths only)
  4. Mock implementations for external dependencies
  5. Test fixtures and sample data
  6. Performance tests for critical operations

  Coverage targets:
  - Unit tests: 80%+
  - Integration tests: 70%+
  - UI tests: Critical paths only

  Test scenarios:
  - Happy path
  - Error handling
  - Edge cases
  - Concurrent operations
  """
```

### Expected Output
- XCTest suites (Unit/Integration/UI)
- Mock objects and test doubles
- Test fixtures and sample data
- Test documentation
- Coverage report

### Success Criteria
- ✅ All use cases unit tested (80%+ coverage)
- ✅ ViewModel logic fully covered
- ✅ Integration with persistence tested
- ✅ Critical UI flows automated
- ✅ All tests passing ✅

---

## Phase 6: Performance Optimization ⚡

### Objective
Profile app performance and optimize bottlenecks.

### Execution
```
Use Task tool:
- subagent_type: "instruments-expert"
- prompt: """
  Performance optimization for feature: {{feature}}

  Context:
  - Complete implementation from Phases 1-5

  Profile and optimize:
  1. Time Profiler: Identify hot code paths
  2. Allocations: Check memory usage patterns
  3. Leaks: Detect retain cycles
  4. SwiftUI: View update optimization
  5. Network: API call efficiency (if applicable)
  6. Battery: Impact on battery life
  7. Thermal state: CPU usage under load

  Provide:
  - Instruments profiling results
  - Identified bottlenecks with metrics
  - Optimization recommendations
  - Implemented optimizations
  - Before/after performance metrics

  Performance targets:
  - App launch: < 400ms to first screen
  - View rendering: < 16ms (60fps)
  - Memory footprint: Reasonable for device
  - No retain cycles detected
  """
```

### Expected Output
- Instruments profiling results
- Bottleneck analysis
- Optimization implementations
- Performance metrics (before/after)
- Recommendations document

### Success Criteria
- ✅ Launch time < 400ms
- ✅ 60fps rendering (< 16ms per frame)
- ✅ Memory usage optimized
- ✅ No retain cycles detected
- ✅ Battery impact minimal

---

## Phase 7: Accessibility Review ♿

### Objective
Ensure full accessibility compliance (VoiceOver, Dynamic Type, etc.)

### Execution
```
Use Task tool:
- subagent_type: "accessibility-expert"
- prompt: """
  Accessibility audit and enhancement for feature: {{feature}}

  Context:
  - UI implementation from Phase 3

  Review and enhance accessibility:
  1. VoiceOver labels and hints for all interactive elements
  2. Dynamic Type support (test at all text sizes)
  3. High contrast mode compliance
  4. Reduce Motion respect (animations)
  5. Keyboard navigation (iPad/Mac)
  6. Color contrast ratios (WCAG AA minimum)
  7. Focus management and order

  Deliverables:
  - Accessibility labels and hints added
  - Dynamic Type testing results
  - VoiceOver testing guide
  - Accessibility compliance checklist
  - Code changes for accessibility

  Compliance target: WCAG 2.1 AA minimum
  """
```

### Expected Output
- Accessibility labels/hints added to code
- Dynamic Type testing results
- VoiceOver testing guide
- Accessibility documentation
- Compliance checklist

### Success Criteria
- ✅ All interactive elements have proper labels
- ✅ Dynamic Type scales correctly (tested XS to XXXL)
- ✅ VoiceOver navigation is logical
- ✅ High contrast mode supported
- ✅ WCAG 2.1 AA compliant

---

## Phase 8: Deployment Preparation 🚀

### Condition
Only execute if `{{deployment}} == true`

### Objective
Prepare feature for TestFlight beta and App Store submission.

### Execution
```
Use Task tool:
- subagent_type: "app-store-expert"
- prompt: """
  Deployment preparation for feature: {{feature}}

  Context:
  - Complete, tested, optimized feature

  Prepare for deployment:
  1. App Store screenshots (all device sizes)
  2. Feature description and marketing copy
  3. What's New text for release notes
  4. TestFlight beta testing plan
  5. Phased rollout strategy (5% → 50% → 100%)
  6. App Store Connect configuration checklist
  7. App Review guidelines compliance check

  Deliverables:
  - Screenshot suite for all devices
  - App Store copy (title, description, keywords)
  - Release notes
  - TestFlight distribution plan
  - Deployment checklist
  - Risk mitigation plan
  """
```

### Expected Output
- Screenshot suite (iPhone/iPad all sizes)
- App Store copy and metadata
- Release notes / What's New
- TestFlight beta plan
- Deployment checklist
- Risk assessment

### Success Criteria
- ✅ Screenshots for all required device sizes
- ✅ Compelling feature description
- ✅ Beta testing plan defined
- ✅ Phased rollout configured
- ✅ App Review guidelines compliant
- ✅ Ready for submission

---

## Final Deliverables

### Code Structure
```
Feature/
├── Domain/
│   ├── Models/              # Phase 2
│   ├── UseCases/            # Phase 4
│   └── Repositories/        # Phase 2 (protocols)
├── Data/
│   ├── SwiftData/           # Phase 2
│   └── Repositories/        # Phase 4 (implementations)
├── Presentation/
│   ├── Views/               # Phase 3
│   ├── ViewModels/          # Phase 3
│   └── Components/          # Phase 3
└── Tests/
    ├── Unit/                # Phase 5
    ├── Integration/         # Phase 5
    └── UI/                  # Phase 5
```

### Documentation
- Architecture Decision Record (ADR)
- API documentation
- Testing guide
- Deployment checklist
- Performance benchmarks
- Accessibility compliance report

### Quality Metrics
- Code coverage: 75%+
- Performance: All targets met
- Accessibility: WCAG 2.1 AA compliant
- App Store ready: ✅

---

## Usage Examples

### Example 1: Simple Feature
```bash
/ios-orchestration:full-feature-workflow \
  --feature "Settings screen with dark mode toggle" \
  --platform ios \
  --complexity simple \
  --testing-strategy unit-only
```

### Example 2: Complex Multi-Platform Feature
```bash
/ios-orchestration:full-feature-workflow \
  --feature "Social media sharing with image filters" \
  --platform multi-platform \
  --complexity complex \
  --ui-framework swiftui \
  --persistence swiftdata \
  --cloud-sync true \
  --testing-strategy full-coverage \
  --deployment true
```

### Example 3: Watch Complication
```bash
/ios-orchestration:full-feature-workflow \
  --feature "Fitness tracker complication" \
  --platform watchos \
  --complexity medium \
  --persistence swiftdata \
  --testing-strategy integration
```

---

## Workflow Customization

### Skip Phases
```bash
--skip-phases "performance_optimization,deployment_preparation"
```

### Custom Agent Selection
```bash
--architecture-agent custom-ios-architect
--ui-agent uikit-specialist
```

### Parallel Execution
Some phases can potentially run in parallel:
- Phase 2 (Data) + Phase 3 (UI) after Phase 1 completes
- Phase 6 (Performance) + Phase 7 (Accessibility) can run concurrently

---

This workflow ensures production-quality iOS feature implementation following Apple's best practices and modern Swift 6 patterns.
