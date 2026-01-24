---
allowed-tools: [Read, Edit, TodoWrite]
description: "Comprehensive accessibility audit and implementation (VoiceOver, Dynamic Type, etc.)"
argument-hint: "[target] [--level a|aa|aaa] [--fix]"
wave-enabled: false
category: "Delivery"
auto-persona: ["swiftui-specialist"]
mcp-servers: ["context7"]
---

# /ios:accessibility - Accessibility Compliance

Audit accessibility for `$ARGUMENTS` including VoiceOver, Dynamic Type, and WCAG compliance.

## Arguments

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--level` | a\|aa\|aaa | aa | WCAG compliance level |
| `--fix` | - | - | Auto-fix accessibility issues |
| `--audit-only` | - | - | Audit without changes |

## Accessibility Areas

| Area | Checks |
|------|--------|
| VoiceOver | Labels, hints, traits, grouping |
| Dynamic Type | Font scaling, layout adaptation |
| Color Contrast | WCAG ratios, semantic colors |
| Keyboard | Focus management, shortcuts |
| Motion | Reduced motion support |

## Common Fixes

```swift
// Missing Label
// Before:
Button(action: save) { Image(systemName: "checkmark") }

// After:
Button(action: save) { Image(systemName: "checkmark") }
    .accessibilityLabel("Save profile")
    .accessibilityHint("Saves your profile changes")

// Fixed Font Size
// Before:
Text("Title").font(.system(size: 24))

// After:
Text("Title").font(.title)

// Color Contrast
// Before:
Text("Important").foregroundColor(.gray)

// After:
Text("Important").foregroundStyle(.primary)
```

## WCAG Levels

| Level | Requirements |
|-------|-------------|
| A | Minimum accessibility |
| AA | Standard (recommended) |
| AAA | Enhanced accessibility |

## Examples

```bash
/ios:accessibility LoginView.swift --level aa --fix
/ios:accessibility . --audit-only
/ios:accessibility ProfileScreen.swift --level aaa
```

## Output

```markdown
# Accessibility Audit: [Target]
## Compliance Level: A | AA | AAA
## VoiceOver: Issues found | Fixed
## Dynamic Type: Support status
## Color Contrast: Pass/Fail ratio
## Recommendations: Prioritized fixes
```
