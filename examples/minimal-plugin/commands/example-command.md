---
allowed-tools: [Read, Write, Edit, Glob, Grep, TodoWrite, Task]
description: "Example orchestration command showing a phased, multi-agent workflow"
argument-hint: "[task] [--complexity simple|medium|complex] [--no-tests]"
---

# /example-plugin:example-command - Template

Orchestrate a task described by `$ARGUMENTS`, coordinating specialists through phases.

> This is a **template**. It uses the real Claude Code command format:
> - Frontmatter: only `allowed-tools`, `description`, `argument-hint`, `model` are read by the harness.
> - Arguments arrive as `$ARGUMENTS` (full string) or `$1`, `$2`… (positional). There is no `{{var}}` templating.
> - To delegate, `Task` must be listed in `allowed-tools`, then spawn a subagent with the Task tool.

## Arguments

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--complexity` | simple\|medium\|complex | medium | Depth of analysis and implementation |
| `--no-tests` | - | - | Skip the testing phase |

## Delegation

Coordinate specialists via the Task tool. Run independent phases in parallel; sequence phases that depend on prior output.

1. **Analysis** → spawn **example-agent** to break down the task, propose an approach, and flag risks.
2. **Implementation** → spawn **example-agent** with the analysis to produce the code and docs.
3. **Testing** → unless `--no-tests`, spawn **example-agent** to write tests for the implementation.

Pass context between phases by including the previous phase's result text in the next Task prompt.

## Workflow

```yaml
1. analysis:
   - Parse the task from $ARGUMENTS
   - Delegate breakdown + plan + risks to example-agent
2. implementation:
   - Delegate code + documentation, grounded in the analysis
3. testing:            # skipped with --no-tests
   - Delegate unit tests + fixtures for the implementation
```

## Examples

```bash
/example-plugin:example-command "Create a caching helper" --complexity simple --no-tests
/example-plugin:example-command "Implement an offline sync engine" --complexity complex
```

## Output

```markdown
# Result: [Task]
## Analysis: Breakdown | Approach | Risks
## Implementation: Files created | Key decisions
## Tests: Coverage | Passing (unless --no-tests)
## Next Steps: Integration and verification
```
