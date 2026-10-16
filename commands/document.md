---
description: "Generate documentation (README, API docs, DocC, inline comments)"
argument-hint: "[target] [--type readme|api|docc|inline] [--export]"
---

# /ios:document

Document the actual code or project specified by `$ARGUMENTS`. Read source,
configuration and existing documentation; preserve its style. Work directly
unless specialist delegation is explicitly requested.

- `--type readme|api|docc|inline|changelog` selects output (default: readme).
- `--format markdown|docc|html` selects format (default: markdown).
- `--export <path>` sets the destination.
- `--update` updates existing documentation rather than creating a competing version.
- `--coverage` reports documentation coverage only when a tool or defined counting method supports it.

Explain public contracts, useful examples, setup and non-obvious decisions. Check
that documented flags, APIs and commands exist. Do not add comments that restate
obvious code or changelog claims without history evidence. For DocC, validate
symbol links and compile the affected catalog when supported by the project.

Return the files changed and relevant validation; flag examples that could not run.
