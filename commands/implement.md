---
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, TodoWrite, Task]
description: "iOS feature implementation with SwiftUI/UIKit and architectural patterns"
argument-hint: "[feature] [--framework swiftui|uikit] [--pattern mvvm|tca]"
---

# /ios:implement - iOS Feature Implementation

Implement iOS features using `$ARGUMENTS` as the feature description.

## Delegation

Coordinate specialists via the Task tool (each queries context7 before writing):
1. **architecture-specialist** → structure, @Observable ViewModels, SwiftData models, DI
2. **swiftui-specialist** → views, navigation, state
3. **swift-specialist** → concurrency, generics, networking
4. **testing-specialist** → if `--with-tests`
5. **swiftui-specialist** → accessibility pass if `--accessibility`

Run independent specialists in parallel; sequence steps that depend on prior output.

## Arguments

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--framework` | swiftui\|uikit\|hybrid | swiftui | UI framework |
| `--pattern` | mvvm\|tca\|clean | mvvm | Architecture pattern |
| `--swiftdata` | - | - | Include SwiftData integration |
| `--cloudkit` | - | - | Enable CloudKit synchronization |
| `--with-tests` | - | - | Generate XCTest unit tests |
| `--accessibility` | - | - | Comprehensive accessibility support |

## Workflow

```yaml
1. requirements:
   - Parse feature description
   - Detect technology context
   - Assess complexity

2. context7:
   - Query Apple patterns
   - Get framework best practices

3. implementation:
   - Generate SwiftUI views or UIKit
   - Implement @Observable ViewModels
   - Create SwiftData models if needed
   - Apply architectural pattern

4. validation:
   - Generate XCTests if requested
   - Check accessibility compliance
   - Verify iOS version compatibility
```

## Examples

```bash
# SwiftUI + MVVM
/ios:implement UserProfileView --framework swiftui --pattern mvvm

# SwiftData Feature
/ios:implement TaskManager --swiftdata --pattern mvvm --with-tests

# Full-featured
/ios:implement UserAuth --pattern tca --accessibility --with-tests
```

## Output

```markdown
# Implementation: [Feature]
## Summary: Framework | Pattern | iOS Version | Complexity
## Files Created: Views, ViewModels, Models, Tests
## Accessibility: VoiceOver ✅ | Dynamic Type ✅
## Next Steps: Integration, testing, verification
```
