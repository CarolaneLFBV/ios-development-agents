# iOS Development Framework

Seven iOS specialties and fifteen workflows for **Claude Code and Codex**.
Swift, SwiftUI, architecture/persistence, testing, performance, security and delivery.

Version **6.0.0** keeps specialist knowledge in portable skills and generates
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

This copies eight skill packages into the app's `.agents/skills/`. It preserves
existing project instructions/configuration and refuses conflicting files before
writing. Identical installations are safe to repeat. To update a customized or
older installation, compare the conflicting files before replacing them.

In that app's Codex session:

```text
$ios-swiftui Build an accessible profile screen using this project's patterns.
$ios-swift Fix the actor-isolation errors in UserService.swift.
$ios-workflow analyze Sources/ --focus security
$ios-workflow migrate coredata swiftdata --strategy incremental --backup
```

Skills can also activate automatically from a matching request. For optional
custom delegated agents, install with `--with-agents`:

```sh
python3 scripts/framework.py install-codex --project "/path/to/ios-app" --with-agents
```

This also copies seven standalone agent TOML files into `.codex/agents/` for current
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
`testing-specialist`, `security-specialist`, and `devops-specialist`.
Commands work directly unless delegation is requested; Claude may also select an
agent from its description. The existing advisory Swift hook is Claude-only.

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

## Maintenance

| Source | Generated distribution |
|---|---|
| `skills/ios-*/SKILL.md` | `agents/*.md`, `codex/agents/*.toml` |
| `commands/*.md` | `skills/ios-workflow/references/*.md` |

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

See the [minimal example](examples/minimal-plugin/README.md).
MIT: [LICENSE](LICENSE).
