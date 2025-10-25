---
allowed-tools: [Read, Grep, Glob, Bash, TodoWrite]
description: "Deep iOS code analysis with Instruments integration"
category: "Analysis & Investigation"
auto-persona: ["performance-specialist", "swift-specialist", "architecture-specialist"]
mcp-servers: ["context7"]
---

# /ios:analyze - iOS Code Analysis

## Purpose
Comprehensive iOS code analysis including performance, architecture, security, and quality metrics.

## Usage
```bash
/ios:analyze [target] [--focus <area>] [--export <path>]
```

## Arguments
- `[target]` - Files, directories, or project to analyze
- `--focus performance|security|architecture|quality` - Analysis focus
- `--instruments` - Include Instruments profiling
- `--export <path>` - Export analysis results

## Analysis Areas
- Performance bottlenecks
- Memory leaks and retain cycles
- Architecture violations
- Security vulnerabilities
- Code complexity metrics
- Technical debt assessment

## Examples
```bash
/ios:analyze . --focus security
/ios:analyze ProductList.swift --focus performance --instruments
```

---

**Delegates to**: performance-specialist, swift-specialist, architecture-specialist
