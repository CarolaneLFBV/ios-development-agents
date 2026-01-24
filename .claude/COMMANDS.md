# COMMANDS.md - iOS Framework Command Reference

## Command Matrix (15 Commands)

| Command | Category | Wave | Primary Agents | MCP |
|---------|----------|------|----------------|-----|
| `/ios:implement` | Development | ✅ | swiftui, architecture, swift | c7 |
| `/ios:design` | Development | ✅ | swiftui, architecture | c7 |
| `/ios:improve` | Quality | ✅ | varies by focus | c7 |
| `/ios:test` | Quality | - | testing | c7 |
| `/ios:cleanup` | Quality | - | swift, architecture | c7 |
| `/ios:security` | Quality | - | security | c7, seq |
| `/ios:document` | Documentation | - | architecture | c7 |
| `/ios:migrate` | Migration | ✅ | architecture, swift | c7 |
| `/ios:optimize` | Migration | - | performance | c7 |
| `/ios:analyze` | Analysis | ✅ | varies by focus | c7 |
| `/ios:troubleshoot` | Analysis | - | swift, performance | seq |
| `/ios:accessibility` | Delivery | - | swiftui | c7 |
| `/ios:localize` | Delivery | - | swiftui | c7 |
| `/ios:publish` | Delivery | - | devops | c7 |
| `/ios:brainstorm` | Planning | ✅ | architecture, swift | c7, seq |

## Categories

- **Development** (2): implement, design
- **Quality** (4): improve, test, cleanup, security
- **Documentation** (1): document
- **Migration** (2): migrate, optimize
- **Analysis** (2): analyze, troubleshoot
- **Delivery** (3): accessibility, localize, publish
- **Planning** (1): brainstorm

## Command Details

### /ios:implement
**Wave-enabled** | **Agents**: swiftui, architecture, swift

```yaml
args:
  --framework: swiftui|uikit|hybrid (default: swiftui)
  --pattern: mvvm|tca|clean (default: mvvm)
  --swiftdata: Include SwiftData
  --cloudkit: Enable CloudKit
  --with-tests: Generate XCTests
  --accessibility: Full a11y support

workflow:
  1. Parse feature, detect context
  2. Context7: Apple patterns
  3. Generate Views, ViewModels, Models
  4. Apply architecture pattern
  5. Generate tests if requested
  6. Validate quality gates
```

### /ios:design
**Wave-enabled** | **Agents**: swiftui, architecture

```yaml
args:
  --scope: ui|architecture|system
  --pattern: mvvm|tca|clean
  --modules: Module breakdown
  --diagram: Generate diagram
  --style: minimal|bold|professional

scopes:
  ui: Apple HIG, SwiftUI components
  architecture: System design, patterns
  system: Full system design (ui + architecture)
```

### /ios:improve
**Wave-enabled** | **Agents**: varies by focus

```yaml
args:
  --focus: performance|accessibility|architecture|quality
  --to: observable|async|actor|swiftdata
  --safe: Conservative changes
  --preview: Preview changes

refactoring:
  --to observable: ObservableObject → @Observable
  --to async: Completion handlers → async/await
  --to actor: Thread-unsafe → actor
  --to swiftdata: CoreData → SwiftData
```

### /ios:test
**Agents**: testing

```yaml
args:
  --type: unit|ui|snapshot|performance|all
  --coverage: Coverage report
  --generate: Generate tests
  --fix: Fix failing tests
```

### /ios:cleanup
**Agents**: swift, architecture

```yaml
args:
  --scope: file|module|project
  --dry-run: Preview only
  --report: Generate report

detects:
  - Unused imports
  - Dead code
  - Unreachable code
  - Unused assets
```

### /ios:security
**Agents**: security | **MCP**: c7, sequential

```yaml
args:
  --owasp: OWASP checklist
  --keychain: Keychain audit
  --biometric: Biometric review
  --report: Generate report

checks:
  - Data storage (Keychain vs UserDefaults)
  - Network security (ATS, certificate pinning)
  - Authentication flows
  - Encryption usage
```

### /ios:document
**Agents**: architecture

```yaml
args:
  --type: readme|api|docc|inline
  --update: Update existing
  --export: Export path
```

### /ios:migrate
**Wave-enabled** | **Agents**: architecture, swift, swiftui

```yaml
args:
  --strategy: incremental|complete|hybrid
  --validate: Validate migration
  --backup: Backup first
  --adr: Create ADR

migrations:
  uikit → swiftui
  coredata → swiftdata
  observableobject → observable
  completion → async
  swift5 → swift6
```

### /ios:optimize
**Agents**: performance

```yaml
args:
  --metric: launch|render|memory|battery
  --goal: Performance target
  --instruments: Use Instruments
```

### /ios:analyze
**Wave-enabled** | **Agents**: varies by focus

```yaml
args:
  --focus: security|performance|quality|architecture
  --review: Code review mode
  --checklist: Review checklist
  --score: Quality score (0-100)
  --pr: PR review format
  --export: Export path

modes:
  default: Deep analysis
  --review: Code review with suggestions
  --checklist: Structured checklist output
  --score: Numeric quality assessment
```

### /ios:troubleshoot
**Agents**: swift, performance | **MCP**: sequential

```yaml
args:
  --type: crash|hang|memory|ui
  --debug: Debug mode
  --breakpoints: Generate breakpoints
  --trace: Detailed trace
  --reproduce: Reproduction steps
```

### /ios:accessibility
**Agents**: swiftui

```yaml
args:
  --level: a|aa|aaa (WCAG level)
  --fix: Auto-fix issues
  --audit-only: Audit without changes

checks:
  - VoiceOver labels
  - Dynamic Type
  - Color contrast
  - Keyboard navigation
```

### /ios:localize
**Agents**: swiftui

```yaml
args:
  --languages: Target languages
  --extract: Extract strings
  --generate: Generate .strings
```

### /ios:publish
**Agents**: devops

```yaml
args:
  --validate: Validate build
  --screenshots: Generate screenshots
  --metadata: Prepare metadata
```

### /ios:brainstorm
**Wave-enabled** | **Agents**: architecture, swift

```yaml
args:
  --format: json|markdown|mindmap
  --depth: shallow|deep|comprehensive
  --export: Export path
```

## Workflow Examples

### Feature Implementation
```bash
/ios:implement UserProfile --pattern mvvm --swiftdata --with-tests
```

### Code Review
```bash
/ios:analyze UserView.swift --review --checklist --score
```

### Migration
```bash
/ios:migrate uikit swiftui --strategy incremental --backup
```

### Security Audit
```bash
/ios:security . --owasp --report
```
