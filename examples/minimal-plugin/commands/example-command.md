---
description: "Review a callback-to-async conversion without changing source code"
argument-hint: "[target]"
---

# /example-plugin:example-command

Review `$ARGUMENTS` for continuation correctness, task cancellation and actor
isolation. Read affected callers and existing tests. Work directly; if the user
explicitly requests delegation, use `example-agent` with a bounded target and
consolidate its evidence.

Return actionable findings with file/line, triggering path, consequence and a
regression-test suggestion. Do not edit code or claim tests passed unless executed.
