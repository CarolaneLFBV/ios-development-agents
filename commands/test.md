---
allowed-tools: [Read, Write, Edit, Bash, TodoWrite, Task]
description: "XCTest generation and test execution for iOS projects"
argument-hint: "[target] [--type unit|ui|snapshot] [--generate]"
---

# /ios:test - iOS Testing

Generate or run tests for `$ARGUMENTS`.

## Arguments
- `--type unit|ui|snapshot|performance|all` - Test type
- `--coverage` - Generate code coverage report
- `--generate` - Generate tests for existing code
- `--fix` - Fix failing tests

## Features
- XCTest unit test generation
- XCUITest UI automation
- Snapshot testing support
- Performance testing
- Test coverage analysis
- Async/await test patterns

## Examples
```bash
/ios:test UserViewModel --generate --type unit
/ios:test LoginFlow --type ui
/ios:test --coverage --type all
```

---

**Delegates to**: testing-specialist
