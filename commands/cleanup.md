---
allowed-tools: [Read, Grep, Glob, Edit, Bash, TodoWrite, Task]
description: "Clean up iOS code, find dead code, unused resources, and technical debt"
argument-hint: "[target] [--type dead-code|imports|resources] [--fix]"
---

# /ios:cleanup - iOS Code Cleanup

Clean up `$ARGUMENTS`: dead code detection, unused resources, deprecated APIs.

## Delegation

Spawn the **swift-specialist** (dead code, unused language constructs) and, for structural cleanup, the **architecture-specialist** via the Task tool. Consolidate their reports before applying with `--fix`.

## Arguments

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--type` | dead-code\|imports\|resources\|deprecated\|all | all | Cleanup type |
| `--fix` | - | - | Automatically remove detected issues |
| `--report` | - | - | Generate detailed cleanup report |
| `--dry-run` | - | - | Show what would be cleaned |
| `--aggressive` | - | - | Include low-confidence detections |

## Detection Types

| Type | Detects | Risk |
|------|---------|------|
| `dead-code` | Unused methods, vars, types | Medium |
| `imports` | Unused import statements | Safe |
| `resources` | Unused assets, strings | Medium |
| `deprecated` | Deprecated API usage | Medium |

## Safety Levels

- **Safe**: Formatting, naming, comments, unused imports
- **Medium**: Private unused methods, orphaned internal types
- **High**: Public API removal, resource deletion

## Examples

```bash
# Full project cleanup scan
/ios:cleanup . --report

# Fix unused imports only
/ios:cleanup Sources/ --type imports --fix

# Dead code detection with dry run
/ios:cleanup . --type dead-code --dry-run

# Resource cleanup
/ios:cleanup . --type resources --report
```

## Output

```markdown
# Cleanup Report: [Target]
## Summary: Dead code | Unused imports | Resources | Deprecated
## Dead Code: File | Line | Type | Confidence
## Unused Imports: File | Import | Reason
## Actions Taken / Recommended
```
