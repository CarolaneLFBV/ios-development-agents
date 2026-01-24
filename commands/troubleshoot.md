---
allowed-tools: [Read, Grep, Glob, Bash, TodoWrite, Task]
description: "Diagnose and resolve iOS issues in code, builds, runtime, and system behavior"
argument-hint: "[issue] [--type crash|build|performance] [--debug]"
wave-enabled: false
category: "Analysis"
auto-persona: ["swift-specialist", "performance-specialist"]
mcp-servers: ["sequential"]
---

# /ios:troubleshoot - iOS Issue Diagnosis

Diagnose and resolve the issue from `$ARGUMENTS`.

## Arguments

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--type` | build\|crash\|performance\|runtime\|ui\|data\|deployment | runtime | Issue category |
| `--debug` | - | - | Interactive debugging mode |
| `--breakpoints` | - | - | Generate strategic breakpoints |
| `--trace` | - | - | Enable detailed investigation |
| `--xcode` | - | - | Include Xcode-specific diagnostics |
| `--instruments` | - | - | Include Instruments recommendations |
| `--fix` | - | - | Automatically apply safe fixes |

## Issue Categories

| Type | Common Issues |
|------|---------------|
| `build` | Compiler errors, dependencies, signing |
| `crash` | EXC_BAD_ACCESS, SIGABRT, OOM |
| `performance` | Slow rendering, memory leaks |
| `runtime` | Data not updating, state issues |
| `ui` | Layout, Safe Area, Dark mode |
| `data` | SwiftData sync, persistence |
| `deployment` | App rejection, entitlements |

## Common Fixes

```swift
// Force Unwrap Crash
// Before:
let user = users.first!
// After:
guard let user = users.first else { return }

// @Observable Not Updating
// Before:
class UserViewModel { var user: User? }
// After:
@Observable class UserViewModel { var user: User? }

// Memory Leak
// Before:
completion = { self.doSomething() }
// After:
completion = { [weak self] in self?.doSomething() }
```

## LLDB Commands

```lldb
po view.recursiveDescription()     # View hierarchy
thread backtrace all               # Thread analysis
watchpoint set variable myVar      # Value changes
expr -l Swift -- print(self)       # Swift expression
```

## Examples

```bash
/ios:troubleshoot "Build failed" --type build --xcode
/ios:troubleshoot "EXC_BAD_ACCESS" --type crash --trace
/ios:troubleshoot "List stutters" --type performance --instruments
/ios:troubleshoot "Data not updating" --type runtime --debug
/ios:troubleshoot "App rejected" --type deployment
```

## Output

```markdown
# Troubleshooting: [Issue]
## Classification: Type | Severity | Components
## Root Cause: [Explanation]
## Solution: [Fix with code]
## Prevention: [Recommendations]
## Verification: [Test steps]
```
