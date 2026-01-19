---
allowed-tools: [Read, Write, Edit, Glob, Grep, TodoWrite]
description: "Generate documentation (README, API docs, DocC, inline comments)"
argument-hint: "[target] [--type readme|api|docc|inline] [--export]"
---

# /ios:document - Documentation Generation

Generate documentation for `$ARGUMENTS`.

## Arguments
- `--type readme|api|docc|inline|changelog` - Documentation type (default: readme)
- `--format markdown|docc|html` - Output format
- `--export <path>` - Export documentation
- `--update` - Update existing documentation
- `--coverage` - Show documentation coverage report

## Documentation Types

### README (--type readme)
```markdown
# Project Name

> Brief description

## Features
- Feature 1
- Feature 2

## Requirements
- iOS 17.0+
- Xcode 15.0+

## Installation
[SPM/CocoaPods instructions]

## Usage
[Code examples]

## Architecture
[Brief overview]

## License
MIT
```

### API Documentation (--type api)
```swift
/// A view model managing user profile data.
///
/// Use `UserProfileViewModel` to load and update user information.
///
/// ## Topics
///
/// ### Loading Data
/// - ``loadUser()``
/// - ``isLoading``
///
/// ### User Information
/// - ``user``
/// - ``updateUser(_:)``
@Observable
class UserProfileViewModel {
    /// The currently loaded user, or `nil` if not loaded.
    var user: User?

    /// Indicates whether a loading operation is in progress.
    var isLoading = false

    /// Loads the current user's profile.
    ///
    /// - Throws: `NetworkError` if the request fails.
    func loadUser() async throws { }
}
```

### DocC Catalog (--type docc)
```
Documentation.docc/
├── Documentation.md          # Landing page
├── GettingStarted.md         # Tutorial
├── Articles/
│   ├── Architecture.md
│   └── BestPractices.md
├── Tutorials/
│   └── MeetMyApp.tutorial
└── Resources/
    └── images/
```

### Inline Comments (--type inline)
```swift
// MARK: - Properties

// MARK: - Lifecycle

// MARK: - Public Methods

// MARK: - Private Methods

// TODO: Implement caching
// FIXME: Handle edge case
// NOTE: This requires iOS 17+
```

### Changelog (--type changelog)
```markdown
# Changelog

## [1.2.0] - 2024-01-15
### Added
- User profile editing
- Dark mode support

### Changed
- Improved list performance

### Fixed
- Crash on empty state
```

## Coverage Report (--coverage)
```markdown
# Documentation Coverage

## Summary
- Total symbols: 150
- Documented: 120 (80%)
- Missing: 30

## Missing Documentation
| File | Symbol | Type |
|------|--------|------|
| UserService.swift | fetchUsers() | Method |
| ProfileView.swift | ProfileView | Struct |
```

## Examples
```bash
/ios:document . --type readme --export README.md
/ios:document Services/ --type api --update
/ios:document . --type docc --format docc
/ios:document UserViewModel.swift --type inline
/ios:document . --coverage
```

---

**Delegates to**: swift-specialist (API docs), architecture-specialist (architecture docs)
