# iOS Development Framework

Eight iOS specialties, a StoreKit skill and fifteen workflows for **Claude Code and Codex**.
Swift, SwiftUI/UIKit UI, architecture/persistence, platform integration, testing,
performance, security and delivery.

Version **6.1.0** keeps specialist knowledge in portable skills and generates
client-specific agents from the same source. Models inherit the parent session;
Context7 and delegated agents are optional. The framework follows the target
project's actual compiler, SDK, deployment target and architecture.

## Codex

Requires Python 3.11+ for the installer and a current local Codex client with
[skills support](https://learn.chatgpt.com/docs/build-skills).
From a checkout of this repository:

```sh
python3 scripts/framework.py install-codex --project "/path/to/ios-app"
```

This copies ten skill packages into the app's `.agents/skills/`. It preserves
existing project instructions/configuration and refuses conflicting files before
writing. Identical installations are safe to repeat. To update a customized or
older installation, compare the conflicting files before replacing them.

In that app's Codex session:

```text
$ios-swiftui Build an accessible profile screen using this project's patterns.
$ios-swift Fix the actor-isolation errors in UserService.swift.
$ios-platform Review background refresh cancellation and notification routing.
$ios-storekit Fix entitlement restoration after subscription renewal.
$ios-workflow analyze Sources/ --focus security
$ios-workflow migrate coredata swiftdata --strategy incremental --backup
```

Skills can also activate automatically from a matching request. For optional
custom delegated agents, install with `--with-agents`:

```sh
python3 scripts/framework.py install-codex --project "/path/to/ios-app" --with-agents
```

This also copies eight standalone agent TOML files into `.codex/agents/` for current
Codex releases. Ask explicitly to use a specialist or parallel agents. Without this
option, the skills work directly in the main session. `/ios:*` names are Claude
commands; they are not registered Codex slash commands.

## Claude Code

```text
/plugin marketplace add CarolaneLFBV/ios-development-agents
/plugin install ios@ios-development

/ios:implement "profile screen with editable avatar" --with-tests
/ios:analyze Sources/ --review
/ios:test UserService --generate
```

For local development, start Claude Code from the repository with
`claude --plugin-dir .`. Plugin agents remain named `swift-specialist`,
`swiftui-specialist`, `architecture-specialist`, `performance-specialist`,
`testing-specialist`, `security-specialist`, `devops-specialist`, and `platform-specialist`.
Commands work directly unless delegation is requested; Claude may also select an
agent from its description. The existing advisory Swift hook is Claude-only.

## Shared repository instructions

`AGENTS.md` is the single source for maintaining this repository. Codex reads it
as project guidance. Claude Code can read it directly from v2.1.277, depending on
its Project instructions setting and other `CLAUDE.md`/`CLAUDE.local.md` files.
The root `CLAUDE.md` contains only `@AGENTS.md` for sessions that need the import;
there are no separate legacy core/workflow instruction files under `.claude/`.
These repository instructions are not installed into an app by the Codex installer.
[Codex instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md),
[Claude instruction loading](https://code.claude.com/docs/en/memory#agents-md).

## Workflows

| Purpose | Names |
|---|---|
| Build/design | `implement`, `design` |
| Quality | `analyze`, `improve`, `test`, `cleanup`, `security` |
| Investigate | `troubleshoot`, `optimize` |
| Maintain | `document`, `migrate`, `localize`, `accessibility` |
| Deliver/plan | `publish`, `brainstorm` |

Options express workflow intent, not a compiled CLI parser or model reasoning
settings. Preview/audit-only/dry-run modes preserve source. Read-only analysis and
release preparation do not post reviews, upload builds or submit releases.

## Specialty boundaries

The UI role owns SwiftUI/UIKit screens and their bridges. Platform integration owns
lifecycle, background scheduling, notifications, incoming links and extensions.
Architecture owns offline data, cache/retry policy and synchronization. Swift owns
language and URLSession mechanics, security trust/privacy decisions, and DevOps
builds/signing. Purchases and entitlements use `ios-storekit`; release preparation
remains a delivery workflow. Existing roles are retained with these explicit boundaries.

UIKit, data/network and platform references load only for matching work. Generated
agents rebase support links to their installed location; keep the corresponding
skill packages alongside the agents when distributing them.

## Maintenance

| Source | Generated distribution |
|---|---|
| `skills/ios-*/SKILL.md` | `agents/*.md`, `codex/agents/*.toml` |
| `commands/*.md` | `skills/ios-workflow/references/*.md` |
| `skills/*/references/*.md` | Support files copied with the skill packages |

```sh
python3 scripts/framework.py generate
python3 scripts/framework.py check
python3 -m unittest discover -s tests -v
python3 scripts/framework.py budget
```

Generation, validation and installation use the Python standard library. Optional
`budget --tokens` uses tiktoken's `o200k_base` as a text-size proxy and can download
its dictionary on first use. It does not measure billed tokens or task effectiveness.

Audit comparisons use `docs/audit-baseline.json` when it is available locally;
without it, the budget command reports current sizes. Local audits and notes in
`docs/` are ignored and are not required to install or validate the framework.

`evals/cases.json` contains review tasks and observable criteria with small fixtures.
Run each prompt in an isolated copy using its listed skills. Compare framework
versions with the same model, settings, inputs and tools; record actual findings,
executed checks, wall time and reported token usage under local `docs/`. Use
pass/fail/not-run per criterion and repeat cases before drawing conclusions.
Fixture tests and catalog validation alone do not measure model quality.

See the [minimal example](examples/minimal-plugin/README.md).
MIT: [LICENSE](LICENSE).
