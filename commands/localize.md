---
allowed-tools: [Read, Write, Edit, Bash, TodoWrite]
description: "i18n/l10n implementation and string extraction"
category: "Localization & i18n"
auto-persona: ["swiftui-specialist"]
mcp-servers: ["context7"]
---

# /ios:localize - Localization & i18n

## Purpose
Implement internationalization and localization for iOS apps including string extraction and translation management.

## Usage
```bash
/ios:localize [target] [--languages <langs>] [--extract]
```

## Arguments
- `[target]` - Files or screens to localize
- `--languages <langs>` - Target languages (e.g., "en,fr,es,de")
- `--extract` - Extract localizable strings
- `--generate` - Generate .strings files

## Features
- String extraction from code
- .strings file generation
- Plural rules and formatting
- Right-to-left (RTL) support
- Date/number formatting
- Testing localization

## Examples
```bash
/ios:localize . --extract --languages "en,fr,es"
/ios:localize LoginView.swift --generate
```

---

**Delegates to**: swiftui-specialist
