# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

> **Framework Entry Point**: See `.claude/CLAUDE.md` for the complete iOS framework reference.

## Project Overview

**iOS Development Framework v4.0.0** for Claude Code with 15 commands, 7 Opus agents with MCP integration, and BMAD workflows.

**Version**: v4.0.0
**Plugin Name**: `ios`
**Repository**: CarolaneLFBV/ios-development-agents

## Quick Reference

| Component | Count | Location |
|-----------|-------|----------|
| Core Files | 7 | `.claude/` |
| Commands | 15 | `commands/` |
| Agents | 7 | `agents/` |
| Hooks | 1 | `hooks/` |

## Architecture

```
.claude/                       # 7 core framework files
├── CLAUDE.md                  # Entry point with references
├── CORE.md                    # Principles, rules, symbols
├── ROUTING.md                 # Detection engine, orchestration
├── CAPABILITIES.md            # 7 agents + MCP coordination
├── COMMANDS.md                # 15 command matrix
├── FLAGS.md                   # iOS-specific flags
└── WORKFLOWS.md               # Development tracks, BMAD, ADR

.claude-plugin/plugin.json     # Plugin configuration
commands/                      # 15 specialized commands
├── implement.md               # Feature implementation
├── design.md                  # UI/UX + Architecture
├── improve.md                 # Quality + Refactoring
├── test.md                    # Testing
├── cleanup.md                 # Dead code detection
├── security.md                # Security audit
├── document.md                # Documentation
├── migrate.md                 # Framework migration
├── optimize.md                # Performance
├── analyze.md                 # Analysis + Review
├── troubleshoot.md            # Diagnosis + Debug
├── accessibility.md           # Accessibility audit
├── localize.md                # i18n/l10n
├── publish.md                 # App Store
└── brainstorm.md              # Idea generation

agents/                        # 7 Opus agents (with integrated patterns)
├── swift-specialist.md        # Swift language & concurrency
├── swiftui-specialist.md      # Views, state, navigation
├── architecture-specialist.md # MVVM, TCA, SwiftData
├── performance-specialist.md  # Profiling, memory
├── testing-specialist.md      # XCTest, TDD
├── security-specialist.md     # OWASP, Keychain
└── devops-specialist.md       # CI/CD, Fastlane

hooks/                         # Smart hooks
├── hooks.json                 # Hook configuration
└── ios_reminder_hook.py       # Best practices reminder
```

## 7 Opus Agents

| Agent | Domain | MCP Servers |
|-------|--------|-------------|
| swift-specialist | Generics, protocols, async/await, actors | Context7, Sequential |
| swiftui-specialist | Views, layouts, state, navigation | Context7, Sequential |
| architecture-specialist | MVVM, TCA, SwiftData, DI | Context7, Sequential |
| performance-specialist | Instruments, memory, rendering | Sequential, Context7 |
| testing-specialist | XCTest, UI testing, TDD | Sequential, Context7 |
| security-specialist | OWASP, Keychain, encryption | Sequential, Context7 |
| devops-specialist | CI/CD, Xcode Cloud, Fastlane | Sequential, Context7 |

## 15 Commands

| Category | Commands |
|----------|----------|
| Development | `implement`, `design` |
| Quality | `improve`, `test`, `cleanup`, `security` |
| Documentation | `document` |
| Migration | `migrate`, `optimize` |
| Analysis | `analyze`, `troubleshoot` |
| Delivery | `accessibility`, `localize`, `publish` |
| Planning | `brainstorm` |

## Development Tracks

| Track | Complexity | Workflow |
|-------|------------|----------|
| Quick | <0.3 | Plan → Implement |
| Standard | 0.3-0.7 | Context7 → Analyze → Plan → Implement → Test |
| Enterprise | >0.7 | Context7 → Analysis → ADR → Wave → Validate |

## Quick Start

```bash
# Feature implementation
/ios:implement "user profile view"

# Code review
/ios:analyze UserProfileView.swift --review --checklist

# Debugging
/ios:troubleshoot "crash on launch" --type crash --debug

# Architecture design
/ios:design "e-commerce app" --scope architecture --pattern mvvm

# Refactoring
/ios:improve ViewModel.swift --to observable

# Security audit
/ios:security . --owasp --report
```

## Key Flags

| Flag | Description |
|------|-------------|
| `--think` | Multi-file analysis (~4K tokens) |
| `--think-hard` | Deep analysis (~10K tokens) |
| `--focus` | Scope: ui\|architecture\|performance\|security |
| `--pattern` | Architecture: mvvm\|tca\|clean |
| `--to` | Refactor target: observable\|async\|actor\|swiftdata |
| `--review` | Code review mode |
| `--debug` | Debug mode with breakpoints |

## MCP Integration

- **Context7**: REQUIRED before implementation - Apple/Swift patterns
- **Sequential**: Complex analysis, multi-step reasoning

## Quality Standards

- All agents use Opus model with MCP integration
- Context7 check REQUIRED before writing code
- Clear domain boundaries between agents
- 8-step quality gates validation
- Wave orchestration for complexity ≥0.7
