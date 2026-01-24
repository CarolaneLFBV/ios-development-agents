---
allowed-tools: [Read, Write, Edit, Glob, TodoWrite, Task]
description: "Design UI/UX and system architecture with Apple HIG compliance"
argument-hint: "[component] [--scope ui|architecture|system] [--pattern mvvm]"
wave-enabled: true
category: "Development"
auto-persona: ["swiftui-specialist", "architecture-specialist"]
mcp-servers: ["context7"]
---

# /ios:design - UI/UX & Architecture Design

Design `$ARGUMENTS` following Apple Human Interface Guidelines and iOS architecture best practices.

## Arguments

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--scope` | ui\|architecture\|system | ui | Design scope |
| `--style` | minimal\|bold\|professional | minimal | UI design style |
| `--platform` | ios\|ipados\|macos\|visionos | ios | Target platform |
| `--pattern` | mvvm\|tca\|clean\|viper | mvvm | Architecture pattern |
| `--modules` | - | - | Modular architecture design |
| `--diagram` | - | - | Generate architecture diagrams |
| `--dark-mode` | - | - | Include dark mode design |

## Scopes

### UI (--scope ui)
- Apple HIG compliance
- Typography: SF Pro, Dynamic Type
- Colors: System colors, semantic colors
- Spacing: 8pt grid system
- Safe Area handling

### Architecture (--scope architecture)
- MVVM, TCA, Clean Architecture patterns
- Protocol-based abstractions
- Dependency injection
- Repository pattern

### System (--scope system)
- Full system design (UI + Architecture)
- Modular architecture
- Dependency management
- Data flow

## Examples

```bash
# UI/UX Design
/ios:design "user profile screen" --scope ui --style minimal

# Architecture Design
/ios:design "e-commerce app" --scope architecture --pattern mvvm --modules

# System Design
/ios:design "banking app" --scope system --pattern clean --diagram
```

## Output

```markdown
# Design: [Component/System]
## Overview: Purpose and scope
## Architecture Diagram: [If --diagram]
## Components: Detailed breakdown
## Patterns: Applied patterns with rationale
## Implementation Plan: Prioritized steps
```
