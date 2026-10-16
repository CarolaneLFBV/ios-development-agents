---
name: ios-workflow
description: "Run an explicitly requested /ios:* workflow in Codex, such as implement, analyze, migrate, test, or publish."
---

# iOS workflows

Read only the requested `references/<workflow>.md`, such as
[implement](references/implement.md) or [analyze](references/analyze.md).
Available workflows: accessibility, analyze, brainstorm, cleanup, design, document,
implement, improve, localize, migrate, optimize, publish, security, test, troubleshoot.

These references are portable instruction workflows. `/ios:*` names are Claude
commands, not native Codex slash commands. In Codex, use `$ios-workflow` with a
workflow name and the user's target. Treat `$ARGUMENTS` as that supplied target
and options. Flags describe intent; they are not shell arguments or model settings.

Read the relevant specialist guidance only when it adds useful domain knowledge:

| Task | Skill |
|---|---|
| Language/concurrency | [ios-swift](../ios-swift/SKILL.md) |
| SwiftUI/UIKit UI, accessibility, localization | [ios-swiftui](../ios-swiftui/SKILL.md) |
| Architecture/persistence | [ios-architecture](../ios-architecture/SKILL.md) |
| Lifecycle/background/notifications/extensions | [ios-platform](../ios-platform/SKILL.md) |
| Purchases/subscription entitlements | [ios-storekit](../ios-storekit/SKILL.md) |
| Tests | [ios-testing](../ios-testing/SKILL.md) |
| Profiling | [ios-performance](../ios-performance/SKILL.md) |
| Security | [ios-security](../ios-security/SKILL.md) |
| Build/release | [ios-devops](../ios-devops/SKILL.md) |

Work directly; delegate only on explicit request, using a bounded scope and
consolidated evidence. Avoid recursive delegation and overlapping writes. Apply the
same guidance locally when custom agents or subagent support are unavailable.

Inspect the actual deployment target and toolchain. Use documentation or an
available MCP for uncertain APIs, and run checks relevant to the change. Respect
read-only/preview flags. Report concrete results and unrun checks; omit empty report
templates, unsupported quality scores, and invented metrics.
