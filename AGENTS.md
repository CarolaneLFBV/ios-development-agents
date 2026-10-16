# Maintaining the iOS framework

This repository distributes prompts and tooling, not an iOS application.
Shared repository instructions live here; `CLAUDE.md` is only a compatibility import.

- Edit canonical skills in `skills/*/SKILL.md`, their conditional `references/`,
  or workflows in `commands/*.md`.
- `agents/*.md`, `codex/agents/*.toml` and `skills/ios-workflow/references/*.md`
  are generated. After source edits, run `python3 scripts/framework.py generate`.
- Register catalog changes in `scripts/framework.py` and
  `.claude-plugin/marketplace.json`. Keep descriptions brief and roles distinct.
- Preserve the target app's architecture, toolchain and OS support. Verify uncertain
  API behavior in primary documentation or the installed SDK. Avoid generic
  tutorials, mandatory MCP lookups, model pinning and automatic delegation.
- Keep runtime prompts self-contained; load detailed references only for matching
  work. Preserve parent permissions and the user's requested scope.
- `install-codex` installs only into an explicitly selected project. Never replace
  that app's instructions or install globally by default. `hooks/` is Claude-only.

Python tooling requires 3.11+. Validate substantive changes with:

```sh
python3 scripts/framework.py check
python3 -m unittest discover -s tests -v
```

`budget` reports current sizes; `budget --tokens` optionally uses tiktoken as a
text-size proxy. `evals/` contains intentionally imperfect review fixtures and
behavioral criteria; catalog validation does not prove model effectiveness.

Keep audits/results under ignored `docs/`; tooling must work without it. Preserve
unrelated local edits. Commit or publish only when requested.
