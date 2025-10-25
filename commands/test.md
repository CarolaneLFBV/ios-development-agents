---
allowed-tools: [Read, Write, Edit, Bash, TodoWrite, Task]
description: "XCTest generation and test execution for iOS projects"
category: "Testing & Quality"
auto-persona: ["testing-specialist"]
mcp-servers: ["context7"]
---

# /ios:test - iOS Testing

## Purpose
Generate, run, and manage XCTest unit tests, UI tests, and snapshot tests for iOS applications.

## Usage
```bash
/ios:test [target] [--type <type>] [--coverage]
```

## Arguments
- `[target]` - Class, file, or test suite to run/generate
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
