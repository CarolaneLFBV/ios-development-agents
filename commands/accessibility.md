---
allowed-tools: [Read, Edit, TodoWrite]
description: "Comprehensive accessibility audit and implementation (VoiceOver, Dynamic Type, etc.)"
argument-hint: "[target] [--level a|aa|aaa] [--fix]"
---

# /ios:accessibility - Accessibility Compliance

Audit accessibility for `$ARGUMENTS` including VoiceOver, Dynamic Type, and WCAG compliance.

## Arguments
- `--level a|aa|aaa` - WCAG compliance level
- `--fix` - Auto-fix accessibility issues
- `--audit-only` - Audit without changes

## Features
- VoiceOver label generation
- Dynamic Type support
- Keyboard navigation
- Color contrast checking
- Accessibility identifier generation
- WCAG 2.1 compliance

## Examples
```bash
/ios:accessibility LoginView.swift --level aa --fix
/ios:accessibility . --audit-only
```

---

**Delegates to**: swiftui-specialist
