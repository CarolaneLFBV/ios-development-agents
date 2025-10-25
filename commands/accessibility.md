---
allowed-tools: [Read, Edit, TodoWrite]
description: "Comprehensive accessibility audit and implementation (VoiceOver, Dynamic Type, etc.)"
category: "Accessibility & Compliance"
auto-persona: ["swiftui-specialist"]
mcp-servers: ["context7"]
---

# /ios:accessibility - Accessibility Compliance

## Purpose
Comprehensive accessibility audit and implementation for iOS apps including VoiceOver, Dynamic Type, and WCAG compliance.

## Usage
```bash
/ios:accessibility [target] [--level <level>] [--fix]
```

## Arguments
- `[target]` - Views or screens to audit
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
