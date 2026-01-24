---
allowed-tools: [Read, Write, Edit, Glob, Grep, TodoWrite]
description: "Generate documentation (README, API docs, DocC, inline comments)"
argument-hint: "[target] [--type readme|api|docc|inline] [--export]"
wave-enabled: false
category: "Documentation"
auto-persona: ["architecture-specialist"]
mcp-servers: ["context7"]
---

# /ios:document - Documentation Generation

Generate documentation for `$ARGUMENTS`.

## Arguments

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--type` | readme\|api\|docc\|inline\|changelog | readme | Documentation type |
| `--format` | markdown\|docc\|html | markdown | Output format |
| `--export` | `<path>` | - | Export documentation |
| `--update` | - | - | Update existing documentation |
| `--coverage` | - | - | Show documentation coverage |

## Documentation Types

| Type | Output | Description |
|------|--------|-------------|
| `readme` | README.md | Project documentation |
| `api` | Inline comments | Swift API documentation |
| `docc` | Documentation.docc | DocC catalog |
| `inline` | MARK comments | Code organization |
| `changelog` | CHANGELOG.md | Version history |

## API Documentation Format

```swift
/// A view model managing user profile data.
///
/// Use `UserProfileViewModel` to load and update user information.
///
/// ## Topics
/// ### Loading Data
/// - ``loadUser()``
@Observable
class UserProfileViewModel {
    /// The currently loaded user.
    var user: User?

    /// Loads the current user's profile.
    /// - Throws: `NetworkError` if the request fails.
    func loadUser() async throws { }
}
```

## Examples

```bash
/ios:document . --type readme --export README.md
/ios:document Services/ --type api --update
/ios:document . --type docc --format docc
/ios:document UserViewModel.swift --type inline
/ios:document . --coverage
```

## Output

```markdown
# Documentation: [Target]
## Type: readme | api | docc
## Files: Generated | Updated
## Coverage: X% documented
```
