---
allowed-tools: [Read, Write, Edit, Bash, TodoWrite, Task]
description: "XCTest generation and test execution for iOS projects"
argument-hint: "[target] [--type unit|ui|snapshot] [--generate]"
wave-enabled: false
category: "Quality"
auto-persona: ["testing-specialist"]
mcp-servers: ["context7"]
---

# /ios:test - iOS Testing

Generate or run tests for `$ARGUMENTS`.

## Arguments

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--type` | unit\|ui\|snapshot\|performance\|all | unit | Test type |
| `--coverage` | - | - | Generate code coverage report |
| `--generate` | - | - | Generate tests for existing code |
| `--fix` | - | - | Fix failing tests |

## Test Types

| Type | Framework | Purpose |
|------|-----------|---------|
| `unit` | XCTest | ViewModels, Services, Logic |
| `ui` | XCUITest | User flows, interactions |
| `snapshot` | XCTest | Visual regression |
| `performance` | XCTest | Performance baselines |

## Test Patterns

```swift
// Unit Test
func testViewModel_LoadUsers_SetsLoadingState() async {
    // Given
    let viewModel = UserViewModel()

    // When
    let task = Task { await viewModel.loadUsers() }

    // Then
    XCTAssertTrue(viewModel.isLoading)
    await task.value
}

// SwiftData Test
let config = ModelConfiguration(isStoredInMemoryOnly: true)
let container = try ModelContainer(for: Task.self, configurations: config)
let context = ModelContext(container)
```

## Examples

```bash
/ios:test UserViewModel --generate --type unit
/ios:test LoginFlow --type ui
/ios:test . --coverage --type all
/ios:test . --fix
```

## Output

```markdown
# Test Results: [Target]
## Coverage: X%
## Tests: Passed | Failed | Skipped
## Generated: New test files
```
