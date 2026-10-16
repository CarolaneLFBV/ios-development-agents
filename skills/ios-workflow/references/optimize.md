<!-- Generated from commands/ by scripts/framework.py. -->

# /ios:optimize

Investigate and optimize `$ARGUMENTS` with performance specialist expertise.
Work directly unless delegation is explicitly requested.

- `--metric launch|render|memory|battery` selects the metric (default: render).
- `--goal <value>` provides the user's explicit target and unit.
- `--instruments` requests profiling using available Instruments tooling.

Capture a comparable baseline with workload, device, OS, build mode and method.
Discover installed profiling templates. Find a demonstrated bottleneck, make a
scoped change, then compare the same workload and check correctness. If tools or
devices are unavailable, distinguish hypotheses from measurements and describe
concrete capture steps.

Use workload-specific budgets and verify SDK/isolation contracts in changed paths.

Report measured before/after results only when collected, plus changes, tradeoffs
and remaining checks. Stop when the requested performance problem is resolved.
