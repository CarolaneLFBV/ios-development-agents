---
name: ios-workflow
description: "Run the named iOS workflows analyze, brainstorm, cleanup, design, document, implement, improve, localize, migrate, optimize, publish, security, test, troubleshoot, or accessibility. Use for an explicit workflow or /ios:* request."
---

# iOS workflows

Choose the workflow explicitly requested by the user and read only its matching
file under `references/` (for example, [implement](references/implement.md) or
[analyze](references/analyze.md)). The other filenames match the workflow names in
this skill's description. If the workflow is ambiguous, infer it from the request
or clarify only when the distinction changes the action.

These references are portable instruction workflows. `/ios:*` names are Claude
commands, not native Codex slash commands. In Codex, use `$ios-workflow` with a
workflow name and the user's target. Treat `$ARGUMENTS` as that supplied target
and options. Flags describe intent; they are not shell arguments or model settings.

Read the relevant specialist guidance only when it adds useful domain knowledge:

| Task | Skill |
|---|---|
| Language/concurrency | [ios-swift](../ios-swift/SKILL.md) |
| Views/accessibility/localization | [ios-swiftui](../ios-swiftui/SKILL.md) |
| Architecture/persistence | [ios-architecture](../ios-architecture/SKILL.md) |
| Tests | [ios-testing](../ios-testing/SKILL.md) |
| Profiling | [ios-performance](../ios-performance/SKILL.md) |
| Security | [ios-security](../ios-security/SKILL.md) |
| Build/release | [ios-devops](../ios-devops/SKILL.md) |

Work directly by default. Use subagents only when explicitly requested; the user
can name a custom `*-specialist` agent if installed. Give delegated work a bounded
scope and consolidate its evidence; do not recursively fan out or assign overlapping
writes. Without subagent support, apply the same guidance in the current session.

Inspect the actual deployment target and toolchain. Use documentation or an
available MCP for uncertain APIs, and run checks relevant to the change. Respect
read-only/preview flags. Report concrete results and unrun checks; omit empty report
templates, unsupported quality scores, and invented metrics.
