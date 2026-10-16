# Minimal specialist example

A short agent and command illustrate the Claude format. This directory is a
prompt example, not a separately registered marketplace plugin.

- [Agent](agents/example-agent.md): focused description, inherited model and tools.
- [Command](commands/example-command.md): user arguments and a bounded workflow.

In the main framework, create canonical specialist instructions under
`skills/ios-<domain>/SKILL.md`, register the domain in `scripts/framework.py`, and
regenerate both client adapters. Register additional Claude agents/commands in
`.claude-plugin/marketplace.json`. Update validation and documentation when the
public catalog changes.

Codex skills use YAML `name` and `description` plus Markdown instructions. Current
Codex custom agents use TOML `name`, `description` and `developer_instructions`.
These are separate formats: renaming a Claude Markdown agent to TOML is insufficient.
See the [main README](../../README.md) for installation and checks.

Keep metadata small. Include guidance that affects decisions, preserve the app's
constraints, and avoid generic expertise catalogs or invented tool names. Use
subagents for explicit delegated work; simple tasks can stay in the main session.
