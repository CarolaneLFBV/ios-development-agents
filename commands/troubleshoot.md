---
allowed-tools: [Read, Grep, Glob, Bash, TodoWrite, Task]
description: "Diagnose and resolve iOS issues in code, builds, runtime, and system behavior"
category: "Debugging & Troubleshooting"
auto-persona: ["swift-specialist", "performance-specialist", "architecture-specialist"]
mcp-servers: ["context7"]
---

# /ios:troubleshoot - iOS Issue Diagnosis

## Usage
```bash
/ios:troubleshoot [issue] [--type <type>] [--trace] [--fix] [--<flags>]
```

## Arguments
- `[issue]` - Problem description, error message, or crash log
- `--type build|crash|performance|runtime|ui|data|deployment` - Issue category
- `--trace` - Enable detailed investigation logging
- `--fix` - Automatically apply safe fixes
- `--xcode` - Include Xcode-specific diagnostics
- `--instruments` - Include Instruments profiling recommendations

## Issue Categories

### Build Issues (--type build)
```bash
/ios:troubleshoot "Build failed" --type build --xcode
```
**Common**: Swift compiler errors, missing dependencies, code signing, framework linking

```swift
// Module Not Found Resolution
// 1. Verify iOS deployment target (iOS 17.0+ for SwiftData)
// 2. Check import statement
import SwiftData  // Requires iOS 17.0+
// 3. Link framework in Target > General > Frameworks
```

### Crash Issues (--type crash)
```bash
/ios:troubleshoot "EXC_BAD_ACCESS" --type crash --trace
```
**Common**: EXC_BAD_ACCESS, SIGABRT, watchdog timeout, OOM

```swift
// Force Unwrap Crash Fix
// Before:
let user = users.first!

// After:
guard let user = users.first else { return }
```

### Performance Issues (--type performance)
```bash
/ios:troubleshoot "List stutters" --type performance --instruments
```

```swift
// List Scrolling Fix
// Before (frame drops):
VStack { ForEach(items) { ExpensiveView(item: $0) } }

// After (smooth):
LazyVStack(spacing: 8) {
    ForEach(items, id: \.id) { ItemView(item: $0).id($0.id) }
}
```

### Runtime Issues (--type runtime)
```bash
/ios:troubleshoot "Data not updating" --type runtime --trace
```

```swift
// @Observable Not Updating Fix
// Before:
class UserViewModel { var user: User? }

// After:
@Observable
class UserViewModel { var user: User? }

// Main Actor Issues Fix
@MainActor @Observable
class ViewModel {
    var data: [Item] = []
    func loadData() async { data = await fetchItems() }
}
```

### UI Issues (--type ui)
```bash
/ios:troubleshoot "View not appearing" --type ui
```
**Common**: Layout constraints, Safe Area violations, Dark mode, Dynamic Type

```swift
// Safe Area Fix
.safeAreaInset(edge: .top) { Color.clear.frame(height: 0) }
.ignoresSafeArea(.keyboard, edges: .bottom)
```

### Data Issues (--type data)
```bash
/ios:troubleshoot "SwiftData not syncing" --type data --trace
```

```swift
// SwiftData Save Fix
func saveItem(_ item: Item) throws {
    modelContext.insert(item)
    do { try modelContext.save() }
    catch { throw DataServiceError.saveFailed }
}

// CloudKit Setup
let config = ModelConfiguration(cloudKitDatabase: .automatic)
let container = try ModelContainer(for: schema, configurations: [config])
```

### Deployment Issues (--type deployment)
```bash
/ios:troubleshoot "App rejected" --type deployment
```
**Common**: Code signing, privacy manifests, entitlements

## Execution Workflow

### Phase 1: Analysis
1. Parse issue and categorize type
2. Identify affected components
3. Gather logs and stack traces

### Phase 2: Investigation
1. Analyze error patterns
2. Search codebase for related issues
3. Check recent changes (git diff)
4. Consult Apple documentation

### Phase 3: Resolution
1. Identify potential fixes
2. Apply safest fix first
3. Verify resolution
4. Document changes

## Common Patterns

### Concurrency Issues
```swift
// Data Race Fix
// Before:
class DataManager { var cache: [String: Data] = [:] }

// After:
actor DataManager {
    var cache: [String: Data] = [:]
    func getData(for key: String) -> Data? { cache[key] }
}
```

### Memory Leaks
```swift
// Strong Reference Cycle Fix
// Before:
completion = { self.doSomething() }

// After:
completion = { [weak self] in self?.doSomething() }
```

### View Update Issues
```swift
// Before:
struct ContentView: View {
    var viewModel: ViewModel  // Not observed
}

// After:
struct ContentView: View {
    @State private var viewModel = ViewModel()
}
```

## LLDB Commands
```lldb
po view.recursiveDescription()     # View hierarchy
po _printHierarchy()               # SwiftUI inspection
po view.constraints                # Check constraints
thread backtrace all               # Thread analysis
watchpoint set variable myVar      # Value changes
```

## Xcode Debug Tips
- **Zombie Objects**: Scheme > Diagnostics > Zombie Objects
- **Memory Graph**: Debug Navigator > Memory Graph (cube icon)
- **View Debugger**: Debug > View Debugging > Capture View Hierarchy
- **Network**: Add `-com.apple.URLSessionDebugLogging 1` to scheme

## Output Structure
```markdown
# Troubleshooting: [Issue]
## Classification: Type | Severity | Components | iOS Version
## Root Cause: [Explanation]
## Solution: [Fix with code]
## Prevention: [Recommendations]
## Verification: [Test steps]
```

---

**Delegates to**: swift-specialist (language), performance-specialist (perf/memory), architecture-specialist (design)
