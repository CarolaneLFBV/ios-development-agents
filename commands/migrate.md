---
allowed-tools: [Read, Edit, Write, TodoWrite, Task]
description: "Migration paths for iOS (UIKit→SwiftUI, CoreData→SwiftData, Swift 5→6)"
argument-hint: "[source] [target] [--strategy incremental|complete]"
wave-enabled: true
category: "Migration"
auto-persona: ["architecture-specialist", "swift-specialist", "swiftui-specialist"]
mcp-servers: ["context7"]
---

# /ios:migrate - iOS Migration

Migrate `$ARGUMENTS` between frameworks, patterns, and Swift versions.

## Arguments

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--strategy` | incremental\|complete\|hybrid | incremental | Migration strategy |
| `--validate` | - | - | Validate migration |
| `--backup` | - | - | Create backup before migration |
| `--adr` | - | - | Create Architecture Decision Record |

## Migration Paths

| From | To | Strategy |
|------|-----|----------|
| UIKit | SwiftUI | incremental recommended |
| CoreData | SwiftData | complete recommended |
| ObservableObject | @Observable | complete |
| Completion handlers | async/await | incremental |
| Swift 5.x | Swift 6 | validate first |
| MVC | MVVM/TCA | incremental |

## Strategies

| Strategy | Use When |
|----------|----------|
| `incremental` | Large codebase, risk mitigation |
| `complete` | Small scope, full replacement |
| `hybrid` | Mixed usage during transition |

## Migration Workflow

```yaml
1. analysis:
   - Assess current implementation
   - Identify dependencies
   - Estimate effort

2. planning:
   - Create migration plan
   - Define milestones
   - Set up feature flags if needed

3. execution:
   - Migrate in phases
   - Maintain backward compatibility
   - Update tests

4. validation:
   - Run full test suite
   - Performance comparison
   - User acceptance
```

## Examples

```bash
/ios:migrate uikit swiftui --strategy incremental
/ios:migrate coredata swiftdata --backup
/ios:migrate swift5 swift6 --validate
/ios:migrate observableobject observable --strategy complete
```

## Output

```markdown
# Migration: [Source] → [Target]
## Strategy: incremental | complete | hybrid
## Files Affected: X files
## Changes: Before → After
## Validation: Tests | Performance | Compatibility
## ADR: [If --adr]
```
