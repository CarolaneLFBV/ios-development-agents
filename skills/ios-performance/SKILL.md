---
name: ios-performance
description: "Investigate measured or suspected iOS slowness, memory growth, rendering hitches, launch latency, or energy use. Use for profiling and optimization work."
---

# Performance

Identify the symptom and representative workload before changing code. Inspect
existing performance tests, device targets and budgets. Use current Apple
documentation for profiling APIs or tool availability; Context7 is optional.

- Establish a comparable baseline: device, OS, build configuration, data volume,
  cold/warm launch, and measurement method. Simulator timings alone do not prove
  device performance. Do not impose generic memory or launch-time thresholds.
- Match tools to the symptom: Time Profiler for CPU, Allocations/Leaks and memory
  graphs for lifetime issues, SwiftUI instruments for updates, signposts/MetricKit
  for app-specific timing and field evidence. Discover installed templates.
- Optimize demonstrated hot paths. Check main-actor CPU work, repeated fetching,
  unstable view IDs, image decoding, allocation growth and task lifetime.
  `async` does not guarantee background execution; verify isolation settings.
- Choose lazy containers from collection size and interaction requirements. View
  extraction is a composition technique, not a guarantee of fewer evaluations.
- Downsample images before decoding full resolution; bound caches and respond to
  memory pressure. An actor around `NSCache` does not by itself make UIKit values
  safe to transfer between actors. Check actual SDK sendability and consumers.
- Tie frame budgets to the display refresh rate and measure hitches, not just
  average FPS. Avoid trading away correctness, accessibility or battery for a score.

Apply scoped optimizations directly without recursive delegation, then compare
using the same workload. If profiling tools or devices are unavailable, label
suspected causes as hypotheses and provide concrete measurement steps. Never
report invented before/after figures or guarantee improvements from inspection.
