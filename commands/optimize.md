---
allowed-tools: [Read, Edit, Bash, TodoWrite, Task]
description: "Performance optimization with Instruments profiling"
argument-hint: "[target] [--metric launch|render|memory|battery]"
wave-enabled: false
category: "Migration"
auto-persona: ["performance-specialist"]
mcp-servers: ["context7"]
---

# /ios:optimize - Performance Optimization

Optimize `$ARGUMENTS` using Instruments profiling and best practices.

## Arguments

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--metric` | launch\|render\|memory\|battery | render | Optimization metric |
| `--goal` | `<value>` | - | Performance goal (e.g., "launch<2s") |
| `--instruments` | - | - | Use Xcode Instruments |

## Optimization Areas

| Metric | Focus | Target |
|--------|-------|--------|
| `launch` | App startup time | <2s cold, <1s warm |
| `render` | SwiftUI rendering | 60fps, no hitches |
| `memory` | Memory usage | <100MB baseline |
| `battery` | Energy efficiency | Low CPU usage |

## Optimization Patterns

```swift
// List Performance
// Before:
VStack { ForEach(items) { ExpensiveView(item: $0) } }

// After:
LazyVStack(spacing: 8) {
    ForEach(items, id: \.id) { ItemView(item: $0).id($0.id) }
}

// Image Loading
// Before:
Image(uiImage: loadImage())

// After:
AsyncImage(url: imageURL) { phase in
    switch phase {
    case .success(let image): image.resizable()
    default: ProgressView()
    }
}
```

## Instruments Templates

| Template | Use Case |
|----------|----------|
| Time Profiler | CPU usage, hot paths |
| Allocations | Memory usage, leaks |
| SwiftUI | View body evaluation |
| Core Animation | Rendering performance |
| Energy Log | Battery consumption |

## Examples

```bash
/ios:optimize App --metric launch --goal "launch<1s"
/ios:optimize ProductList --metric render
/ios:optimize . --metric memory --instruments
/ios:optimize ImageLoader --metric battery
```

## Output

```markdown
# Optimization: [Target]
## Metric: launch | render | memory | battery
## Before: Current measurements
## After: Improved measurements
## Changes: Applied optimizations
## Instruments: Profile recommendations
```
