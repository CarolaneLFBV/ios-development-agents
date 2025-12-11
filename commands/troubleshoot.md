---
allowed-tools: [Read, Grep, Glob, Bash, TodoWrite, Task]
description: "Diagnose and resolve iOS issues in code, builds, runtime, and system behavior"
category: "Debugging & Troubleshooting"
auto-persona: ["swift-specialist", "performance-specialist", "architecture-specialist"]
mcp-servers: ["context7"]
---

# /ios:troubleshoot - iOS Issue Diagnosis and Resolution

## Purpose
Systematically diagnose and resolve iOS development issues including Xcode build errors, runtime crashes, performance problems, SwiftUI rendering issues, SwiftData sync problems, and deployment failures.

## Usage
```bash
/ios:troubleshoot [issue] [--type <type>] [--trace] [--fix] [--<flags>]
```

## Arguments
- `[issue]` - Description of the problem, error message, or crash log
- `--type build|crash|performance|runtime|ui|data|deployment` - Issue category
- `--trace` - Enable detailed tracing and investigation logging
- `--fix` - Automatically apply fixes when safe
- `--safe` - Only apply low-risk, reversible fixes
- `--xcode` - Include Xcode-specific diagnostics
- `--instruments` - Include Instruments profiling recommendations
- `--device <simulator|device>` - Target environment for diagnostics

## Auto-Activation Patterns

### Agents
- **swift-specialist**: Swift language errors, compilation issues, type mismatches
  - Keywords: compiler error, type mismatch, protocol conformance, generic constraint
  - Errors: *.swift build failures, syntax errors, semantic issues

- **performance-specialist**: Performance and memory issues
  - Keywords: slow, memory leak, high CPU, battery drain, frame drop
  - Issues: UI stuttering, excessive memory, thermal throttling

- **architecture-specialist**: Architecture and design pattern issues
  - Keywords: retain cycle, data flow, dependency, circular reference
  - Issues: State management problems, data inconsistency

### MCP Servers
- **context7**: Apple documentation, error resolution guides, platform-specific solutions

## Issue Categories

### 1. Build Issues (--type build)

```bash
/ios:troubleshoot "Build failed with Swift compiler error" --type build --xcode
```

**Common Build Issues**:
- Swift compiler errors
- Missing dependencies
- Code signing failures
- Provisioning profile issues
- Framework linking errors
- Module resolution failures
- Swift version mismatches

**Diagnostic Steps**:
```
1. Analyze build log for root error
2. Identify dependency graph issues
3. Check Swift version compatibility
4. Validate code signing configuration
5. Verify framework search paths
6. Test clean build
```

**Example - Module Not Found**:
```
Error: No such module 'SwiftData'
```

**Resolution**:
```swift
// 1. Verify iOS deployment target (iOS 17.0+ for SwiftData)
// In Xcode: Target > General > Minimum Deployments

// 2. Check import statement
import SwiftData  // Requires iOS 17.0+

// 3. Verify framework is linked
// Target > General > Frameworks, Libraries, and Embedded Content
```

### 2. Crash Issues (--type crash)

```bash
/ios:troubleshoot "EXC_BAD_ACCESS crash on launch" --type crash --trace
```

**Common Crash Types**:
- EXC_BAD_ACCESS (memory access violation)
- SIGABRT (assertion failure)
- EXC_CRASH (unhandled exception)
- Watchdog timeout (main thread blocked)
- Out of memory crashes

**Diagnostic Steps**:
```
1. Parse crash log and symbolicate
2. Identify crash location and stack trace
3. Analyze memory state at crash time
4. Check for threading issues
5. Review recent code changes
6. Reproduce in debugger
```

**Example - Force Unwrap Crash**:
```
Fatal error: Unexpectedly found nil while unwrapping an Optional value
```

**Resolution**:
```swift
// Before (dangerous):
let user = users.first!

// After (safe):
guard let user = users.first else {
    // Handle missing user appropriately
    return
}

// Or with optional binding:
if let user = users.first {
    processUser(user)
}

// Or with nil coalescing:
let user = users.first ?? User.placeholder
```

### 3. Performance Issues (--type performance)

```bash
/ios:troubleshoot "App stutters when scrolling list" --type performance --instruments
```

**Common Performance Issues**:
- UI stuttering (frame drops)
- Slow launch time
- High memory usage
- Battery drain
- Network latency
- CPU spikes

**Diagnostic Steps**:
```
1. Profile with Time Profiler
2. Check main thread utilization
3. Analyze memory allocations
4. Review network calls
5. Identify expensive view updates
6. Check background task impact
```

**Example - List Scrolling Stutter**:
```swift
// Before (causes frame drops):
ScrollView {
    VStack {
        ForEach(items) { item in
            ExpensiveItemView(item: item)
        }
    }
}

// After (smooth scrolling):
ScrollView {
    LazyVStack(spacing: 8) {
        ForEach(items, id: \.id) { item in
            ItemView(item: item)
                .id(item.id)
        }
    }
}
```

**Instruments Recommendations**:
```
- Time Profiler: CPU usage analysis
- Allocations: Memory tracking
- Leaks: Memory leak detection
- Core Animation: Rendering performance
- Network: API call analysis
```

### 4. Runtime Issues (--type runtime)

```bash
/ios:troubleshoot "Data not updating in view" --type runtime --trace
```

**Common Runtime Issues**:
- State not updating views
- @Observable not triggering updates
- Async/await deadlocks
- Task cancellation issues
- Actor isolation problems

**Diagnostic Steps**:
```
1. Verify state management setup
2. Check property wrapper usage
3. Analyze async call chain
4. Identify threading issues
5. Review actor boundaries
6. Test with debugger breakpoints
```

**Example - @Observable Not Updating**:
```swift
// Before (incorrect):
class UserViewModel {  // Missing @Observable
    var user: User?
}

// After (correct):
@Observable
class UserViewModel {
    var user: User?  // Changes now tracked automatically
}
```

**Example - Main Actor Issues**:
```swift
// Before (crashes on background update):
class ViewModel {
    var data: [Item] = []

    func loadData() async {
        data = await fetchItems()  // May not be on main thread
    }
}

// After (safe main actor update):
@MainActor
@Observable
class ViewModel {
    var data: [Item] = []

    func loadData() async {
        data = await fetchItems()  // Guaranteed main thread
    }
}
```

### 5. UI Issues (--type ui)

```bash
/ios:troubleshoot "View not appearing correctly on iPad" --type ui
```

**Common UI Issues**:
- Layout constraint conflicts
- Safe Area violations
- Dark mode inconsistencies
- Dynamic Type problems
- Orientation issues
- Device-specific layout bugs

**Diagnostic Steps**:
```
1. Review view hierarchy in debugger
2. Check constraint satisfaction
3. Test all device sizes
4. Verify Dark Mode support
5. Test Dynamic Type sizes
6. Check Safe Area handling
```

**Example - Safe Area Issues**:
```swift
// Before (content hidden under notch):
VStack {
    ContentView()
}

// After (respects Safe Area):
VStack {
    ContentView()
}
.safeAreaInset(edge: .top) {
    Color.clear.frame(height: 0)
}
// Or use:
.ignoresSafeArea(.keyboard, edges: .bottom)
```

**Example - Constraint Conflict**:
```swift
// Debug constraint issues:
// In LLDB: po view.constraints
// Or enable: UIViewAlertForUnsatisfiableConstraints breakpoint

// Fix conflicting constraints:
view.setContentHuggingPriority(.defaultHigh, for: .vertical)
view.setContentCompressionResistancePriority(.required, for: .horizontal)
```

### 6. Data Issues (--type data)

```bash
/ios:troubleshoot "SwiftData not syncing with CloudKit" --type data --trace
```

**Common Data Issues**:
- SwiftData save failures
- CloudKit sync issues
- Migration failures
- Relationship inconsistencies
- Query performance problems

**Diagnostic Steps**:
```
1. Check ModelContainer configuration
2. Verify CloudKit entitlements
3. Review @Model definitions
4. Test save/fetch operations
5. Check migration requirements
6. Analyze sync logs
```

**Example - SwiftData Save Failure**:
```swift
// Before (silent failure):
func saveItem(_ item: Item) {
    modelContext.insert(item)
}

// After (proper error handling):
func saveItem(_ item: Item) throws {
    modelContext.insert(item)

    do {
        try modelContext.save()
    } catch {
        // Handle specific SwiftData errors
        if let swiftDataError = error as? SwiftDataError {
            switch swiftDataError {
            case .fetchFailed:
                throw DataServiceError.fetchFailed
            case .saveFailed:
                throw DataServiceError.saveFailed
            default:
                throw error
            }
        }
        throw error
    }
}
```

**Example - CloudKit Sync Debug**:
```swift
// Enable CloudKit logging:
// Add to scheme: -com.apple.CoreData.CloudKitDebug 1

// Check CloudKit entitlements:
// 1. Signing & Capabilities > iCloud
// 2. Enable CloudKit checkbox
// 3. Select container

// Configure for CloudKit:
let schema = Schema([Item.self])
let config = ModelConfiguration(
    cloudKitDatabase: .automatic
)
let container = try ModelContainer(
    for: schema,
    configurations: [config]
)
```

### 7. Deployment Issues (--type deployment)

```bash
/ios:troubleshoot "App rejected for missing privacy manifest" --type deployment
```

**Common Deployment Issues**:
- App Store rejection
- Code signing problems
- Missing privacy manifests
- Entitlement mismatches
- Archive failures
- TestFlight issues

**Diagnostic Steps**:
```
1. Review App Store rejection reason
2. Check privacy manifest completeness
3. Verify entitlements configuration
4. Test archive process
5. Validate app binary
6. Review App Store guidelines compliance
```

**Example - Privacy Manifest Missing**:
```xml
<!-- PrivacyInfo.xcprivacy -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>NSPrivacyTracking</key>
    <false/>
    <key>NSPrivacyTrackingDomains</key>
    <array/>
    <key>NSPrivacyCollectedDataTypes</key>
    <array/>
    <key>NSPrivacyAccessedAPITypes</key>
    <array>
        <dict>
            <key>NSPrivacyAccessedAPIType</key>
            <string>NSPrivacyAccessedAPICategoryUserDefaults</string>
            <key>NSPrivacyAccessedAPITypeReasons</key>
            <array>
                <string>CA92.1</string>
            </array>
        </dict>
    </array>
</dict>
</plist>
```

## Execution Workflow

### Phase 1: Issue Analysis
```
1. Parse issue description and error messages
2. Categorize issue type (build/crash/performance/etc.)
3. Identify affected components and files
4. Gather relevant logs and stack traces
5. Establish reproduction steps if possible
```

### Phase 2: Root Cause Investigation
```
1. Analyze error patterns and correlations
2. Search codebase for related issues
3. Check recent changes (git diff)
4. Review dependency versions
5. Cross-reference with known issues
6. Consult Apple documentation via Context7
```

### Phase 3: Solution Development
```
1. Identify potential fixes
2. Assess fix risk level
3. Develop implementation plan
4. Create test verification steps
5. Document workarounds if needed
```

### Phase 4: Fix Application (if --fix)
```
1. Apply safest fix first
2. Verify fix resolves issue
3. Run related tests
4. Check for regressions
5. Document changes made
```

### Phase 5: Validation & Prevention
```
1. Confirm issue resolution
2. Add tests to prevent recurrence
3. Update documentation
4. Recommend architectural improvements
5. Suggest monitoring additions
```

## Examples

### Build Error Investigation
```bash
/ios:troubleshoot "Cannot find type 'ModelContext' in scope" --type build --fix
```

### Crash Analysis
```bash
/ios:troubleshoot crash.log --type crash --trace
```

### Performance Deep Dive
```bash
/ios:troubleshoot "List view drops to 30fps when loading images" --type performance --instruments
```

### SwiftUI State Issue
```bash
/ios:troubleshoot "@State variable not updating view" --type runtime --trace
```

### CloudKit Sync Problem
```bash
/ios:troubleshoot "Changes not syncing between devices" --type data --trace
```

### App Store Rejection
```bash
/ios:troubleshoot "Rejected: Guideline 2.1 - App Completeness" --type deployment
```

## Output Structure

```markdown
# Troubleshooting Report: [Issue Summary]

## Issue Classification
- **Type**: Build | Crash | Performance | Runtime | UI | Data | Deployment
- **Severity**: Critical | High | Medium | Low
- **Affected Components**: [List of files/modules]
- **iOS Version**: [Affected versions]
- **Device Types**: [Affected devices]

## Root Cause Analysis
[Detailed explanation of what's causing the issue]

## Investigation Steps Taken
1. [Step 1 with findings]
2. [Step 2 with findings]
3. [Step 3 with findings]

## Solution

### Recommended Fix
[Primary solution with code examples]

### Alternative Approaches
[Other possible solutions if applicable]

### Workaround (if immediate fix not possible)
[Temporary workaround steps]

## Applied Changes (if --fix)
- [File 1]: [Change description]
- [File 2]: [Change description]

## Prevention Recommendations
1. [Recommendation to prevent recurrence]
2. [Additional best practice]
3. [Monitoring suggestion]

## Verification Steps
1. [How to verify the fix]
2. [Tests to run]
3. [Manual verification steps]

## Related Resources
- [Apple Documentation links]
- [Relevant WWDC sessions]
- [Stack Overflow discussions]
```

## Common iOS Troubleshooting Patterns

### Swift 6.2 Concurrency Issues
```swift
// Problem: Data race warning
// Solution: Proper actor isolation

// Before:
class DataManager {
    var cache: [String: Data] = [:]
}

// After:
actor DataManager {
    var cache: [String: Data] = [:]

    func getData(for key: String) -> Data? {
        cache[key]
    }

    func setData(_ data: Data, for key: String) {
        cache[key] = data
    }
}
```

### SwiftUI View Update Issues
```swift
// Problem: View not updating when model changes
// Solution: Ensure proper @Observable usage

// Before:
struct ContentView: View {
    var viewModel: ViewModel  // Not observed

    var body: some View {
        Text(viewModel.title)
    }
}

// After:
struct ContentView: View {
    @State private var viewModel = ViewModel()

    var body: some View {
        Text(viewModel.title)
    }
}
```

### Memory Leak Detection
```swift
// Problem: Memory leak from strong reference cycle
// Solution: Use weak or unowned references

// Before (leak):
class ViewController {
    var completion: (() -> Void)?

    func setupCompletion() {
        completion = {
            self.doSomething()  // Strong capture
        }
    }
}

// After (no leak):
class ViewController {
    var completion: (() -> Void)?

    func setupCompletion() {
        completion = { [weak self] in
            self?.doSomething()  // Weak capture
        }
    }
}
```

## LLDB Debug Commands Reference

```lldb
# View hierarchy debugging
po view.recursiveDescription()

# SwiftUI view inspection
po _printHierarchy()

# Memory graph
command script import lldb.macosx.heap

# Check constraints
po view.constraints
po view.hasAmbiguousLayout

# Thread analysis
thread backtrace all

# Watchpoints for value changes
watchpoint set variable myVariable
```

## Xcode Debug Techniques

### Enable Zombie Objects
```
Product > Scheme > Edit Scheme > Diagnostics > Zombie Objects
```

### Memory Graph Debugger
```
Debug Navigator > Memory Graph (cube icon)
```

### View Debugger
```
Debug > View Debugging > Capture View Hierarchy
```

### Network Debugging
```
Product > Scheme > Edit Scheme > Arguments
Add: -com.apple.URLSessionDebugLogging 1
```

## Related Commands
- `/ios:debug` - Advanced debugging workflows
- `/ios:analyze` - Deep code analysis
- `/ios:optimize` - Performance optimization
- `/ios:review` - Code review for potential issues

---

**Delegates to**: swift-specialist (language issues), performance-specialist (performance/memory), architecture-specialist (design problems)
