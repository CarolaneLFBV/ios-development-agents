---
allowed-tools: [Read, Grep, Bash, TodoWrite]
description: "Advanced debugging workflows and crash analysis"
category: "Debugging & Troubleshooting"
auto-persona: ["swift-specialist", "performance-specialist"]
mcp-servers: ["context7"]
---

# /ios:debug - Advanced Debugging

## Purpose
Advanced iOS debugging including crash analysis, memory debugging, and issue reproduction.

## Usage
```bash
/ios:debug [issue] [--type <type>] [--reproduce]
```

## Arguments
- `[issue]` - Bug description or crash log
- `--type crash|hang|memory|ui` - Issue type
- `--reproduce` - Generate reproduction steps
- `--fix` - Suggest fixes

## Features
- Crash log analysis
- Memory leak detection
- UI debugging tips
- Breakpoint suggestions
- LLDB command generation

## Examples
```bash
/ios:debug "App crashes on login" --type crash
/ios:debug crash.log --reproduce --fix
```

---

**Delegates to**: swift-specialist, performance-specialist
