<!-- Generated from commands/ by scripts/framework.py. -->

# /ios:analyze

Review `$ARGUMENTS` without changing source code. Inspect the requested files,
working diff or branch and relevant callers; ground findings in concrete behavior.
Work directly unless the user explicitly requests parallel specialists.

- `--focus performance|security|architecture|quality` selects the domain (default: quality).
- `--review` emphasizes regressions and actionable findings.
- `--checklist` includes a short checklist specific to the reviewed code.
- `--score` includes a clearly labeled subjective score with its rubric, not a measured quality gate.
- `--pr` formats a review recommendation; it does not post or approve a PR.
- `--instruments` adds concrete profiling steps for performance hypotheses.
- `--export <path>` saves the report to that path.

Use the relevant specialist expertise. Check deployment/toolchain compatibility,
isolation, error paths, state identity and security where relevant. Prioritize
behavioral risks over stylistic preferences.

Report findings by severity with file/line, trigger, impact and suggested correction.
State when there are no actionable findings and disclose validation gaps.
