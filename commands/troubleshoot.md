---
description: "Diagnose and resolve iOS issues in code, builds, runtime, and system behavior"
argument-hint: "[issue] [--type crash|build|performance] [--debug]"
---

# /ios:troubleshoot

Diagnose `$ARGUMENTS`. Reproduce or capture evidence before asserting a root cause.
Report by default; apply fixes when `--fix` or the user's request authorizes them.
Work directly unless specialist delegation is explicitly requested.

- `--type build|crash|performance|runtime|ui|data|deployment` narrows scope (default: runtime).
- `--debug` / `--breakpoints` / `--trace` request appropriate debugger/capture steps.
- `--xcode` includes Xcode-specific diagnostics.
- `--instruments` requests profiling steps or available captures.
- `--fix` applies scoped fixes followed by relevant verification.

Use Swift expertise for language/runtime diagnostics, SwiftUI for UI/state,
architecture for persistence, performance for profiling, and DevOps for CI/signing.
Build errors can have different owners; classify from actual diagnostics.

Inspect logs, affected inputs, toolchain and recent changes. Do not rewrite state
management, add weak captures everywhere, reset stores or clear caches as a generic
fix. Preserve user data while narrowing the cause.

Return evidence, confirmed cause or ranked hypotheses, corrections and verification.
