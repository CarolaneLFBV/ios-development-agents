---
allowed-tools: [Read, Write, Edit, Glob, TodoWrite, Task]
description: "UI/UX design with Apple Human Interface Guidelines compliance"
category: "Design & Architecture"
auto-persona: ["swiftui-specialist", "architecture-specialist"]
mcp-servers: ["context7"]
---

# /ios:design - UI/UX Design

## Purpose
Design iOS interfaces following Apple Human Interface Guidelines with SwiftUI best practices.

## Usage
```bash
/ios:design [component] [--style <style>] [--platform <platform>]
```

## Arguments
- `[component]` - UI component or screen to design
- `--style minimal|bold|playful|professional` - Design style
- `--platform ios|ipados|macos|watchos` - Target platform
- `--dark-mode` - Include dark mode design
- `--accessibility` - Comprehensive accessibility support

## Features
- Apple HIG compliance
- Safe Area handling
- Dynamic Type support
- Dark Mode variants
- Accessibility-first design
- Component library integration

---

**Delegates to**: swiftui-specialist (UI), architecture-specialist (structure)
