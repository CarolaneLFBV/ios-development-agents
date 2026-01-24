---
allowed-tools: [Read, Write, Edit, Bash, TodoWrite]
description: "i18n/l10n implementation and string extraction"
argument-hint: "[target] [--languages en,fr,es] [--extract]"
wave-enabled: false
category: "Delivery"
auto-persona: ["swiftui-specialist"]
mcp-servers: ["context7"]
---

# /ios:localize - Localization & i18n

Localize `$ARGUMENTS` with string extraction and translation management.

## Arguments

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--languages` | `<langs>` | en | Target languages (comma-separated) |
| `--extract` | - | - | Extract localizable strings |
| `--generate` | - | - | Generate .strings files |

## Features

| Feature | Description |
|---------|-------------|
| String Extraction | Find hardcoded strings in code |
| .strings Generation | Create localization files |
| Plural Rules | Handle plural forms correctly |
| RTL Support | Right-to-left layout support |
| Date/Number | Locale-aware formatting |

## Localization Patterns

```swift
// Basic String
Text("Hello, World!")
// Becomes:
Text("greeting_hello", bundle: .main)

// String with Variable
Text("Welcome, \(username)")
// Becomes:
Text("greeting_welcome \(username)")

// Plural
// Localizable.stringsdict for proper pluralization
```

## .strings Format

```
/* Greeting shown on home screen */
"greeting_hello" = "Hello, World!";

/* Welcome message with username */
"greeting_welcome %@" = "Welcome, %@!";
```

## Examples

```bash
/ios:localize . --extract --languages "en,fr,es"
/ios:localize LoginView.swift --generate
/ios:localize . --languages "en,de,ja,zh"
```

## Output

```markdown
# Localization: [Target]
## Languages: List of target languages
## Extracted Strings: Count
## Generated Files: .strings, .stringsdict
## RTL Support: Status
```
