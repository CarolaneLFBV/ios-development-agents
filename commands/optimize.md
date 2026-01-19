---
allowed-tools: [Read, Edit, Bash, TodoWrite, Task]
description: "Performance optimization with Instruments profiling"
argument-hint: "[target] [--metric launch|render|memory|battery]"
---

# /ios:optimize - Performance Optimization

Optimize `$ARGUMENTS` using Instruments profiling and best practices.

## Arguments
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
