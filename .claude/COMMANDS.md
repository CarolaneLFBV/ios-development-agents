# COMMANDS.md - iOS Framework Command Reference

Complete command catalog for the iOS Development Framework.

## Command Overview

**13 specialized commands** organized by category for comprehensive iOS development workflows.

## Command Categories

### Development & Implementation
- **/ios:implement** - Feature implementation with SwiftUI/UIKit
- **/ios:refactor** - Code refactoring to modern patterns

### Quality & Enhancement
- **/ios:improve** - Code quality, performance, and maintainability improvements
- **/ios:review** - Comprehensive code review
- **/ios:optimize** - Performance optimization with Instruments

### Design & Architecture
- **/ios:design** - UI/UX design with Apple HIG compliance

### Testing & Quality Assurance
- **/ios:test** - XCTest generation and execution

### Analysis & Investigation
- **/ios:analyze** - Deep code analysis
- **/ios:debug** - Advanced debugging workflows

### Migration & Transformation
- **/ios:migrate** - Framework and version migrations

### Accessibility & Compliance
- **/ios:accessibility** - Accessibility audit and implementation

### Deployment & Publishing
- **/ios:publish** - App Store submission preparation

### Localization
- **/ios:localize** - i18n/l10n implementation

---

## Detailed Command Reference

### /ios:implement
**Purpose**: Implement iOS features with modern patterns
**Agents**: swiftui-specialist, architecture-specialist, swift-specialist
**Flags**:
- `--framework swiftui|uikit` - UI framework
- `--pattern mvvm|tca|clean` - Architecture pattern
- `--swiftdata` - Include SwiftData
- `--with-tests` - Generate tests
- `--accessibility` - Accessibility support

**Examples**:
```bash
/ios:implement LoginView --framework swiftui --pattern mvvm
/ios:implement TaskManager --swiftdata --with-tests
/ios:implement UserAuth --pattern tca --accessibility
```

---

### /ios:improve
**Purpose**: Improve code quality and performance
**Agents**: swiftui-specialist, performance-specialist, swift-specialist
**Flags**:
- `--focus performance|accessibility|architecture|quality`
- `--type swift-modern|swiftui|swiftdata`
- `--safe` - Safe improvements only
- `--preview` - Preview changes

**Examples**:
```bash
/ios:improve ContentView.swift --focus performance
/ios:improve . --type swift-modern --safe
/ios:improve Services/ --focus architecture
```

---

### /ios:review
**Purpose**: Comprehensive code review
**Agents**: All specialists
**Flags**:
- `--focus security|performance|quality|architecture`
- `--format report|checklist|metrics`
- `--export <path>` - Export results

**Examples**:
```bash
/ios:review UserAuth/ --focus security
/ios:review . --format report --export review.md
```

---

### /ios:refactor
**Purpose**: Refactor to modern patterns
**Agents**: architecture-specialist, swift-specialist
**Flags**:
- `--pattern mvvm|tca|clean` - Target pattern
- `--to observable|swiftdata|async` - Specific refactoring
- `--safe` - Conservative refactoring

**Examples**:
```bash
/ios:refactor UserViewModel.swift --to observable
/ios:refactor Models/ --to swiftdata
/ios:refactor NetworkService.swift --to async
```

---

### /ios:design
**Purpose**: UI/UX design with Apple HIG
**Agents**: swiftui-specialist, architecture-specialist
**Flags**:
- `--style minimal|bold|playful|professional`
- `--platform ios|ipados|macos`
- `--dark-mode` - Dark mode design

**Examples**:
```bash
/ios:design OnboardingFlow --style minimal
/ios:design Dashboard --platform ipados --dark-mode
```

---

### /ios:test
**Purpose**: Testing and quality assurance
**Agents**: testing-specialist
**Flags**:
- `--type unit|ui|snapshot|performance|all`
- `--coverage` - Coverage report
- `--generate` - Generate tests
- `--fix` - Fix failing tests

**Examples**:
```bash
/ios:test UserViewModel --generate --type unit
/ios:test LoginFlow --type ui
/ios:test . --coverage --type all
```

---

### /ios:migrate
**Purpose**: Framework and version migrations
**Agents**: swift-specialist, swiftui-specialist, architecture-specialist
**Flags**:
- `--strategy incremental|complete|hybrid`
- `--validate` - Validate migration
- `--backup` - Backup before migration

**Examples**:
```bash
/ios:migrate uikit swiftui --strategy incremental
/ios:migrate coredata swiftdata --backup
/ios:migrate swift5 swift6 --validate
```

---

### /ios:analyze
**Purpose**: Deep code analysis
**Agents**: performance-specialist, architecture-specialist
**Flags**:
- `--focus performance|security|architecture|quality`
- `--instruments` - Instruments profiling
- `--export <path>` - Export results

**Examples**:
```bash
/ios:analyze . --focus security
/ios:analyze ProductList.swift --focus performance --instruments
```

---

### /ios:optimize
**Purpose**: Performance optimization
**Agents**: performance-specialist
**Flags**:
- `--metric launch|render|memory|battery`
- `--goal <value>` - Performance goal
- `--instruments` - Use Instruments

**Examples**:
```bash
/ios:optimize App --metric launch --goal "launch<1s"
/ios:optimize ProductList --metric render
/ios:optimize . --metric memory --instruments
```

---

### /ios:accessibility
**Purpose**: Accessibility compliance
**Agents**: swiftui-specialist
**Flags**:
- `--level a|aa|aaa` - WCAG level
- `--fix` - Auto-fix issues
- `--audit-only` - Audit without changes

**Examples**:
```bash
/ios:accessibility LoginView.swift --level aa --fix
/ios:accessibility . --audit-only
```

---

### /ios:publish
**Purpose**: App Store publishing
**Agents**: architecture-specialist
**Flags**:
- `--validate` - Validate build
- `--screenshots` - Generate screenshots
- `--metadata` - Prepare metadata

**Examples**:
```bash
/ios:publish --validate
/ios:publish --screenshots --metadata
```

---

### /ios:debug
**Purpose**: Advanced debugging
**Agents**: swift-specialist, performance-specialist
**Flags**:
- `--type crash|hang|memory|ui`
- `--reproduce` - Reproduction steps
- `--fix` - Suggest fixes

**Examples**:
```bash
/ios:debug "App crashes on login" --type crash
/ios:debug crash.log --reproduce --fix
```

---

### /ios:localize
**Purpose**: i18n/l10n implementation
**Agents**: swiftui-specialist
**Flags**:
- `--languages <langs>` - Target languages
- `--extract` - Extract strings
- `--generate` - Generate .strings files

**Examples**:
```bash
/ios:localize . --extract --languages "en,fr,es"
/ios:localize LoginView.swift --generate
```

---

## Command Workflows

### Full Feature Implementation
```bash
1. /ios:design UserProfile --style professional
2. /ios:implement UserProfile --pattern mvvm --swiftdata --with-tests
3. /ios:accessibility UserProfile --level aa --fix
4. /ios:test UserProfile --type all --coverage
5. /ios:review UserProfile
```

### Performance Optimization Workflow
```bash
1. /ios:analyze App --focus performance --instruments
2. /ios:optimize App --metric launch --goal "launch<1s"
3. /ios:test App --type performance
```

### Migration Workflow
```bash
1. /ios:analyze . --focus architecture
2. /ios:migrate uikit swiftui --strategy incremental --backup
3. /ios:test . --type all
4. /ios:review . --focus quality
```

---

## Auto-Activation Matrix

| Command | Primary Agent | Secondary Agents | MCP Servers |
|---------|---------------|------------------|-------------|
| implement | swiftui-specialist | architecture, swift | context7 |
| improve | Varies by focus | performance, swift | context7 |
| review | All agents | - | context7 |
| refactor | architecture | swift, swiftui | context7 |
| design | swiftui | architecture | context7 |
| test | testing | - | context7 |
| migrate | Varies by migration | All relevant | context7 |
| analyze | performance | architecture | context7 |
| optimize | performance | - | context7 |
| accessibility | swiftui | - | context7 |
| publish | architecture | - | context7 |
| debug | swift | performance | context7 |
| localize | swiftui | - | context7 |

---

## Best Practices

### Command Selection
- Use **/ios:implement** for new features
- Use **/ios:improve** for enhancements
- Use **/ios:refactor** for pattern changes
- Use **/ios:optimize** for performance issues

### Flag Usage
- Always use `--safe` for production code
- Use `--preview` to review changes
- Include `--with-tests` for critical features
- Use `--accessibility` for user-facing features

### Workflow Integration
- Run /ios:review before merging
- Use /ios:test for CI/CD
- Apply /ios:accessibility for compliance
- Use /ios:debug for troubleshooting

---

For detailed command documentation, see individual command files in `commands/` directory.
