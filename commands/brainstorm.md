---
description: "Compare implementation options and tradeoffs for an iOS feature."
argument-hint: "[topic] [--depth shallow|medium|deep] [--focus ui|architecture]"
---

# /ios:brainstorm

Explore `$ARGUMENTS` without editing source code. Identify the user's constraints,
existing implementation and the decision to make. Work directly unless the user
explicitly requests parallel exploration.

- `--depth shallow|medium|deep` controls breadth/detail (default: medium), not a time guarantee or reasoning setting.
- `--format list|mindmap|pros-cons|matrix` selects presentation (default: list).
- `--focus ui|architecture|performance|data` narrows expertise.
- `--constraints <text>` adds explicit constraints.
- `--export <path>` saves the result.

Compare a few viable options, including preserving the current design when
reasonable. Explain tradeoffs, effort, compatibility and unknowns. Consult current
primary documentation when recommendations depend on API or platform availability.
For matrices, disclose subjective criteria and weights.

Return a recommendation with rationale and the next concrete experiment or
implementation step. Do not create ADRs, story files or diagrams unless requested
or needed to communicate the decision.
