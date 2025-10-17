---
name: ios-dev:concurrency
description: Add Swift Concurrency (async/await, actors, @MainActor) to existing code or design new concurrent systems
version: 1.0

required_parameters:
  - name: target
    type: string
    description: File or module to add concurrency to

optional_parameters:
  - name: pattern
    type: string
    options: [async-await, actors, main-actor, task-groups, all]
    default: all
    description: Which concurrency patterns to implement
  - name: migration
    type: boolean
    default: false
    description: Migrate from callbacks/GCD to async/await

execution:
  phases:
    - analysis
    - implementation
    - validation
---

# Implement Concurrency Command

Adds modern Swift Concurrency patterns to code or designs new concurrent systems.

## Phase 1: Concurrency Analysis

### Objective
Analyze code for concurrency needs and opportunities.

### Execution
```
Use Task tool:
- subagent_type: "general-purpose"
- description: "Swift concurrency analysis"
- prompt: """
  Analyze code for concurrency implementation:

  Target: {{target}}
  Patterns: {{pattern}}
  Migration mode: {{migration}}

  Identify:

  1. Async/Await Opportunities
     - Synchronous blocking calls
     - Callback-based APIs
     - Completion handlers
     - Long-running operations

  2. Actor Needs
     - Shared mutable state
     - Race condition risks
     - Classes that should be actors
     - Data race prevention needs

  3. @MainActor Requirements
     - UI updates
     - Main thread requirements
     - View model properties
     - UI-bound operations

  4. Task Management
     - Parallel operations
     - Child task opportunities
     - Cancellation needs
     - Task group use cases

  5. Existing Issues
     - Thread safety problems
     - Data races
     - Deadlock risks
     - Race conditions

  Provide:
  - Concurrency opportunities by type
  - Safety issues identified
  - Recommended patterns
  - Migration complexity (if applicable)
  - Implementation priority
  """
```

### Expected Output
- Concurrency opportunities categorized
- Safety issues and risks
- Pattern recommendations
- Implementation roadmap

### Success Criteria
- ✅ All concurrency needs identified
- ✅ Patterns recommended
- ✅ Risks assessed

---

## Phase 2: Concurrency Implementation

### Objective
Implement async/await, actors, and task management.

### Execution
```
Use Task tool:
- subagent_type: "general-purpose"
- description: "Implement Swift concurrency"
- prompt: """
  Implement concurrency patterns:

  Analysis from Phase 1: {{PHASE1_ANALYSIS}}
  Target patterns: {{pattern}}

  1. async/await Implementation
     ```swift
     // Before: Callback
     func fetchUser(completion: @escaping (Result<User, Error>) -> Void) {
         URLSession.shared.dataTask(with: url) { data, _, error in
             // ...
             completion(.success(user))
         }.resume()
     }

     // After: async/await
     func fetchUser() async throws -> User {
         let (data, _) = try await URLSession.shared.data(from: url)
         return try JSONDecoder().decode(User.self, from: data)
     }
     ```

  2. Actor Isolation
     ```swift
     // Before: Class with potential races
     class Cache {
         private var storage: [String: Data] = [:]

         func get(_ key: String) -> Data? {
             storage[key] // Data race risk!
         }
     }

     // After: Actor with automatic isolation
     actor Cache {
         private var storage: [String: Data] = [:]

         func get(_ key: String) -> Data? {
             storage[key] // Thread-safe!
         }
     }
     ```

  3. @MainActor for UI
     ```swift
     // Before: Manual dispatch
     class ViewModel {
         var items: [Item] = []

         func load() {
             fetchItems { items in
                 DispatchQueue.main.async {
                     self.items = items
                 }
             }
         }
     }

     // After: @MainActor
     @MainActor
     class ViewModel {
         var items: [Item] = []

         func load() async {
             items = await fetchItems()
             // Already on main thread
         }
     }
     ```

  4. Task Groups for Parallelism
     ```swift
     // Before: Sequential
     let user = await fetchUser()
     let posts = await fetchPosts()
     let stats = await fetchStats()

     // After: Parallel with async let
     async let user = fetchUser()
     async let posts = fetchPosts()
     async let stats = fetchStats()
     let result = try await (user, posts, stats)
     ```

  5. Cancellation Handling
     ```swift
     func processLarge() async throws {
         for item in largeCollection {
             try Task.checkCancellation()
             await process(item)
         }
     }
     ```

  For each implementation:
  - Show complete before/after code
  - Explain thread safety improvements
  - Document cancellation behavior
  - Note any breaking changes
  - Provide migration path

  Apply all recommended patterns from Phase 1.
  """
```

### Expected Output
- Fully concurrent code
- Actor-based thread safety
- Proper @MainActor usage
- Task management implemented
- Migration guide (if applicable)

### Success Criteria
- ✅ All concurrency patterns implemented
- ✅ Thread-safe by design
- ✅ Proper error handling
- ✅ Cancellation supported

---

## Phase 3: Concurrency Validation

### Objective
Validate concurrent code for correctness and safety.

### Execution
```
Use Task tool:
- subagent_type: "general-purpose"
- description: "Validate concurrency implementation"
- prompt: """
  Validate concurrent code:

  Original code: {{ORIGINAL_CODE}}
  Concurrent code: {{PHASE2_CODE}}

  Validate:

  1. Thread Safety
     - No data races
     - Proper actor isolation
     - Sendable conformance correct
     - No shared mutable state issues

  2. Main Thread Safety
     - UI updates on @MainActor
     - No main thread blocking
     - Proper MainActor.run usage
     - UI state properly isolated

  3. Task Management
     - Proper structured concurrency
     - Tasks properly awaited
     - Cancellation handled correctly
     - No task leaks

  4. Error Handling
     - Errors properly propagated
     - Try/await used correctly
     - Throwing functions marked
     - Error recovery in place

  5. Performance
     - Parallelism where appropriate
     - No unnecessary serialization
     - Efficient task usage
     - No performance regressions

  6. Concurrency Correctness
     - No deadlocks
     - No race conditions
     - Proper suspension points
     - Reentrancy considered

  Run Swift 6 strict concurrency checks:
  - Enable -strict-concurrency=complete
  - Check for data race warnings
  - Verify Sendable conformance
  - Validate actor isolation

  Provide:
  - Validation checklist ✅/❌
  - Thread safety improvements
  - Performance metrics
  - Remaining issues
  - Concurrency safety score
  """
```

### Expected Output
- Validation report
- Thread safety confirmation
- Performance benchmarks
- Remaining issues (if any)

### Success Criteria
- ✅ All validations pass
- ✅ Swift 6 strict concurrency enabled
- ✅ No data race warnings
- ✅ Performance acceptable

---

## Final Deliverables

### Concurrent Code
```swift
// Example output

// Thread-safe cache with actor
actor ImageCache {
    private var storage: [URL: UIImage] = [:]

    func get(_ url: URL) -> UIImage? {
        storage[url]
    }

    func set(_ url: URL, image: UIImage) {
        storage[url] = image
    }
}

// Main thread view model
@MainActor
class ImageListViewModel {
    private let cache = ImageCache()
    var images: [UIImage] = []

    func loadImages(urls: [URL]) async {
        await withTaskGroup(of: (URL, UIImage?).self) { group in
            for url in urls {
                group.addTask { [cache] in
                    if let cached = await cache.get(url) {
                        return (url, cached)
                    }

                    let image = try? await downloadImage(url)
                    if let image = image {
                        await cache.set(url, image: image)
                    }
                    return (url, image)
                }
            }

            for await (_, image) in group {
                if let image = image {
                    images.append(image)
                }
            }
        }
    }
}
```

### Concurrency Report
```markdown
# Concurrency Implementation Report

## Summary
- Files modified: X
- Patterns implemented: Y
- Safety improvements: Z

## Implementations

### async/await (X conversions)
- Callback → async/await: Y functions
- GCD → async/await: Z functions
- Completion handlers removed: W

### Actors (X actors created)
- Thread-safe state isolation: Y classes → actors
- Race conditions eliminated: Z
- Data race prevention: 100%

### @MainActor (X annotations added)
- UI-safe view models: Y
- Main thread guarantees: Z locations
- Main thread blocking eliminated: W cases

### Task Management
- Parallel operations: X task groups
- Structured concurrency: Y scopes
- Cancellation support: Z operations

## Safety Improvements
- Data races eliminated: 100%
- Thread safety: +100%
- Race conditions fixed: X
- Deadlock risks removed: Y

## Performance Impact
- Parallel execution: +XX% faster
- Efficient task usage: -XX% overhead
- Cancellation responsiveness: +XX%

## Migration Notes
- Breaking changes: [list]
- Deployment target: iOS 13+
- Swift version: 5.5+
```

---

## Usage Examples

### Migrate Callbacks to async/await
```bash
/swift-concurrency:implement-concurrency \
  --target Sources/Services/ \
  --pattern async-await \
  --migration true
```

### Add Actors for Thread Safety
```bash
/swift-concurrency:implement-concurrency \
  --target Sources/Cache/ \
  --pattern actors
```

### Complete Concurrency Implementation
```bash
/swift-concurrency:implement-concurrency \
  --target Sources/ \
  --pattern all
```

---

## What Gets Created

- ✅ Modern async/await code
- ✅ Thread-safe actors
- ✅ Main thread safety with @MainActor
- ✅ Efficient task management
- ✅ Proper cancellation handling
- ✅ Concurrency validation report
- ✅ Migration guide

---

This command brings your code up to Swift 6 concurrency standards with complete thread safety.
