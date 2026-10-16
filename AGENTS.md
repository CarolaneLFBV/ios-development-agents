# Working on this framework

This repository distributes iOS instructions; it is not an iOS app. Do not assume
there is an Xcode project or run an iOS build to validate instruction-only changes.

- `skills/ios-*/SKILL.md` contains the seven canonical specialist prompts and the
  portable workflow router. Keep descriptions short and scopes distinct.
- `commands/*.md` contains the fifteen canonical workflows. Flags describe intent;
  do not imply that they configure model reasoning or invoke a real argument parser.
- `agents/*.md`, `codex/agents/*.toml`, and
  `skills/ios-workflow/references/*.md` are generated. Edit the corresponding
  source, then run `python3 scripts/framework.py generate`.
- `.claude-plugin/marketplace.json` preserves Claude plugin registration.
  `hooks/` is a Claude-only, non-blocking reminder, not a Swift parser or Codex hook.
- `scripts/framework.py install-codex` installs into an explicitly selected app
  project. Do not install globally or replace that project's instructions by default.

Keep runtime prompts self-contained and focused on decisions a capable model might
otherwise get wrong. Preserve project toolchains, deployment targets and architecture.
Use primary documentation for version-sensitive claims. Avoid mandatory MCP lookups,
recursive delegation, model pinning, arbitrary quality gates and copied API tutorials.

Python tooling requires Python 3.11+. After a substantive change, run:

```sh
python3 scripts/framework.py check
python3 -m unittest discover -s tests -v
```

`python3 scripts/framework.py budget` reports size without dependencies;
`budget --tokens` additionally requires tiktoken and may download its dictionary.
Treat tokenization as a proxy, not billed usage or evidence of model effectiveness.
Local audits and notes under `docs/` are ignored and optional; distributed tooling
must work without them. Do not commit or publish unless requested, and preserve
unrelated local edits.
