# Framework conventions

Preserve the target project's toolchain, OS support, architecture and test style.
Newer APIs are choices gated by availability, not reasons for unrelated migrations.

Specialist mapping: `swift`, `swiftui`, `architecture`, `performance`, `testing`,
`security`, `devops`. Each has a portable `ios-*` skill and generated
`*-specialist` agents for Claude/Codex. UI accessibility and localization belong
to SwiftUI; persistence/migration design belongs to architecture.

Work directly by default. Use delegated specialists when the user requests them,
with bounded scopes and concise evidence. Avoid recursive delegation and overlapping
writes. Both clients inherit the parent's model selection; do not assume Opus or
a particular Codex model.

Consult official Swift/Apple/framework sources for uncertainty or version-sensitive
behavior. Context7 is optional; resolve library IDs and verify source relevance.
Do not assume `/apple/*` catalogs exist, repeat identical lookups, or treat a
documentation lookup as compiler validation.

Validation follows the change: relevant build/tests and the project's actual policies.
Profile measured performance problems; perform device/accessibility/signing checks
when applicable and available. Report unrun checks explicitly. There is no universal
80% coverage threshold, eight-gate ceremony or automatic compliance certification.

Workflow flags describe requested behavior. Depth labels are not model reasoning
settings. Preview/audit-only/dry-run overrides editing flags.
