---
name: Modernize Swift
description: Modernize Swift code to use Swift 6 language features (generics, protocols, property wrappers, etc.)
version: 1.0

required_parameters:
  - name: target
    type: string
    description: File or directory to modernize

optional_parameters:
  - name: focus
    type: array
    options: [generics, protocols, property-wrappers, error-handling, value-types, all]
    default: [all]
    description: Which Swift features to modernize
  - name: safety
    type: string
    options: [conservative, balanced, aggressive]
    default: balanced
    description: How aggressive to be with refactoring

execution:
  phases:
    - analysis
    - modernization
    - validation
---

# Modernize Swift Command

Modernizes Swift code to leverage modern Swift 6 language features.

## Phase 1: Code Analysis

### Objective
Analyze existing code for modernization opportunities.

### Execution
```
Use Task tool:
- subagent_type: "general-purpose"
- description: "Swift code modernization analysis"
- prompt: """
  Analyze Swift code for modernization opportunities:

  Target: {{target}}
  Focus areas: {{focus}}

  Identify opportunities for:

  1. Generics
     - Functions that could be generic
     - Types that could benefit from generics
     - Repeated code patterns

  2. Protocol-Oriented Design
     - Classes that should be protocols
     - Missing protocol extensions
     - Protocol composition opportunities

  3. Property Wrappers
     - Repetitive property patterns
     - Validation logic
     - Transformation logic

  4. Error Handling
     - Force unwrapping (!)
     - Forced try (try!)
     - Optional handling anti-patterns

  5. Value Semantics
     - Classes that should be structs
     - Missing copy-on-write optimizations
     - Reference type usage patterns

  6. Memory Management
     - Strong reference cycles
     - Missing weak/unowned
     - Closure capture issues

  Provide:
  - List of modernization opportunities
  - Priority (high/medium/low)
  - Risk level (safe/moderate/risky)
  - Estimated impact
  """
```

### Expected Output
- Modernization opportunities by category
- Priority and risk assessment
- Code locations with issues
- Estimated refactoring effort

### Success Criteria
- ✅ All code patterns identified
- ✅ Opportunities prioritized
- ✅ Risks assessed

---

## Phase 2: Code Modernization

### Objective
Apply modern Swift 6 language features to code.

### Execution
```
Use Task tool:
- subagent_type: "general-purpose"
- description: "Apply Swift modernization"
- prompt: """
  Modernize Swift code based on analysis:

  Analysis from Phase 1: {{PHASE1_ANALYSIS}}
  Safety mode: {{safety}}

  Apply modernization:

  1. Generics Refactoring
     ```swift
     // Before
     func addInt(_ a: Int, _ b: Int) -> Int { a + b }
     func addDouble(_ a: Double, _ b: Double) -> Double { a + b }

     // After
     func add<T: Numeric>(_ a: T, _ b: T) -> T { a + b }
     ```

  2. Protocol-Oriented Design
     ```swift
     // Before
     class DataFetcher {
         func fetchData() -> Data { ... }
     }

     // After
     protocol DataFetching {
         func fetchData() -> Data
     }
     class NetworkDataFetcher: DataFetching { ... }
     class MockDataFetcher: DataFetching { ... }
     ```

  3. Property Wrappers
     ```swift
     // Before
     var _email: String = ""
     var email: String {
         get { _email }
         set { _email = newValue.lowercased() }
     }

     // After
     @Lowercased var email: String = ""
     ```

  4. Error Handling
     ```swift
     // Before
     let user = try! decoder.decode(User.self, from: data)

     // After
     do {
         let user = try decoder.decode(User.self, from: data)
     } catch {
         // Handle error
     }
     ```

  5. Value Types
     ```swift
     // Before
     class Point {
         var x: Double
         var y: Double
     }

     // After
     struct Point {
         var x: Double
         var y: Double
     }
     ```

  For each refactoring:
  - Show before/after code
  - Explain benefits
  - Note any breaking changes
  - Provide migration path

  Apply changes based on safety level:
  - Conservative: Only safe refactorings
  - Balanced: Safe + moderate risk changes
  - Aggressive: All recommended changes
  """
```

### Expected Output
- Refactored code with modern Swift 6 features
- Before/after comparisons
- Explanation of changes
- Migration notes

### Success Criteria
- ✅ Code compiles after changes
- ✅ Modern patterns applied correctly
- ✅ No regressions introduced

---

## Phase 3: Validation

### Objective
Validate modernized code for correctness and improvements.

### Execution
```
Use Task tool:
- subagent_type: "general-purpose"
- description: "Validate Swift modernization"
- prompt: """
  Validate modernized Swift code:

  Original code: {{ORIGINAL_CODE}}
  Modernized code: {{PHASE2_CODE}}

  Check:

  1. Compilation
     - Code compiles without errors
     - No new warnings introduced
     - Swift 6 compatibility

  2. Type Safety
     - Generic constraints correct
     - Protocol conformance valid
     - Type inference working

  3. Memory Safety
     - No new retain cycles
     - Proper weak/unowned usage
     - Value semantics where intended

  4. Error Handling
     - No force unwraps (unless justified)
     - Proper error propagation
     - Result types used correctly

  5. Code Quality
     - More type-safe than before
     - Better code reuse
     - Clearer intent
     - Improved testability

  6. Performance
     - No performance regressions
     - Copy-on-write where needed
     - Efficient generic usage

  Provide:
  - Validation checklist ✅/❌
  - Improvements achieved
  - Any remaining issues
  - Code quality score improvement (+XX points)
  """
```

### Expected Output
- Validation report
- Quality improvements
- Remaining issues (if any)
- Before/after metrics

### Success Criteria
- ✅ All validations pass
- ✅ Code quality improved
- ✅ No regressions

---

## Final Deliverables

### Modernized Code
- All files updated with modern Swift 6 patterns
- Proper use of generics, protocols, property wrappers
- Improved error handling
- Better memory management

### Modernization Report
```markdown
# Swift Modernization Report

## Summary
- Files analyzed: X
- Modernization opportunities: Y
- Changes applied: Z

## Changes by Category

### Generics (X changes)
- [List of generic refactorings]

### Protocols (X changes)
- [List of protocol improvements]

### Property Wrappers (X changes)
- [List of wrapper additions]

### Error Handling (X changes)
- [List of error handling improvements]

### Value Types (X changes)
- [List of struct conversions]

## Code Quality Improvements
- Type safety: +XX%
- Code reuse: +XX%
- Test coverage: +XX%
- Cyclomatic complexity: -XX%

## Migration Notes
- [Any breaking changes]
- [Compatibility notes]
- [Recommended next steps]
```

---

## Usage Examples

### Modernize Entire Project
```bash
/swift-language:modernize-swift \
  --target Sources/ \
  --focus all \
  --safety balanced
```

### Focus on Generics and Protocols
```bash
/swift-language:modernize-swift \
  --target Sources/Services/ \
  --focus generics,protocols \
  --safety conservative
```

### Aggressive Refactoring
```bash
/swift-language:modernize-swift \
  --target LegacyCode/ \
  --focus all \
  --safety aggressive
```

---

## What Gets Created

- ✅ Modernized Swift 6 code
- ✅ Before/after comparisons
- ✅ Modernization report with metrics
- ✅ Migration guide
- ✅ Code quality improvements documented

---

This command brings your Swift codebase up to modern Swift 6 standards.
