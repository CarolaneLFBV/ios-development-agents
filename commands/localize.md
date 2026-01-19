---
allowed-tools: [Read, Write, Edit, Bash, TodoWrite]
description: "i18n/l10n implementation and string extraction"
argument-hint: "[target] [--languages en,fr,es] [--extract]"
---

# /ios:localize - Localization & i18n

Localize `$ARGUMENTS` with string extraction and translation management.

## Arguments
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
