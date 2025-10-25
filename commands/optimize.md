---
allowed-tools: [Read, Edit, Bash, TodoWrite, Task]
description: "Performance optimization with Instruments profiling"
category: "Performance & Optimization"
auto-persona: ["performance-specialist"]
mcp-servers: ["context7"]
---

# /ios:optimize - Performance Optimization

## Purpose
Profile and optimize iOS app performance using Instruments and best practices.

## Usage
```bash
/ios:optimize [target] [--metric <metric>] [--goal <goal>]
```

## Arguments
- `[target]` - Component to optimize
- `--metric launch|render|memory|battery` - Optimization metric
- `--goal <value>` - Performance goal (e.g., "launch<2s")
- `--instruments` - Use Xcode Instruments

## Optimization Areas
- App launch time
- SwiftUI rendering performance
- Memory usage and leaks
- Battery consumption
- Network efficiency
- Image optimization

## Examples
```bash
/ios:optimize App --metric launch --goal "launch<1s"
/ios:optimize ProductList --metric render
/ios:optimize . --metric memory --instruments
```

---

**Delegates to**: performance-specialist
