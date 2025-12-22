---
allowed-tools: [Read, Grep, Glob, Edit, Bash, TodoWrite, Task]
description: "Clean up iOS code, find dead code, unused resources, and technical debt"
category: "Quality & Enhancement"
auto-persona: ["swift-specialist", "architecture-specialist"]
mcp-servers: ["context7"]
---

# /ios:cleanup - iOS Code Cleanup

## Purpose
Systematic code cleanup: dead code detection, unused resources, deprecated APIs, and technical debt reduction.

## Usage
```bash
/ios:cleanup [target] [--type <type>] [--fix] [--report]
```

## Arguments
- `[target]` - Files, directories, or project to clean
- `--type dead-code|imports|resources|deprecated|all` - Cleanup type (default: all)
- `--fix` - Automatically remove detected issues
- `--report` - Generate detailed cleanup report
- `--dry-run` - Show what would be cleaned without applying
- `--aggressive` - Include low-confidence detections

## Cleanup Types

### Dead Code (--type dead-code)
```swift
// Detects:
private func unusedHelper() { }     // Never called
let unusedConstant = "value"        // Never read
class OrphanedType { }              // Never instantiated
protocol UnimplementedProtocol { }  // No conformances
```

### Unused Imports (--type imports)
```swift
// Before:
import Foundation
import UIKit        // Not used - SwiftUI only
import Combine      // Not used
import SwiftUI

// After:
import Foundation
import SwiftUI
```

### Unused Resources (--type resources)
```bash
# Detects unused:
Assets.xcassets/UnusedIcon.imageset
Localizable.strings keys
Storyboard/XIB files (if SwiftUI project)
Unused font files
```

### Deprecated APIs (--type deprecated)
```swift
// Before:
UIApplication.shared.keyWindow                    // Deprecated
NotificationCenter.default.addObserver(self, ...) // Legacy pattern
DispatchQueue.main.async { self.updateUI() }      // In async context

// After:
UIApplication.shared.connectedScenes...           // Modern API
NotificationCenter.default.publisher(for:)        // Combine
await MainActor.run { updateUI() }                // Structured concurrency
```

## Detection Patterns

### Code Analysis
| Pattern | Detection | Risk |
|---------|-----------|------|
| Private unused methods | Grep + call analysis | Safe |
| Unused local variables | Scope analysis | Safe |
| Orphaned types | Reference counting | Medium |
| Commented code blocks | Regex pattern | Safe |
| TODO/FIXME markers | Comment scanning | Info |

### Resource Analysis
| Resource | Detection | Risk |
|----------|-----------|------|
| Images | Asset catalog + string search | Medium |
| Strings | Localization key search | Medium |
| Fonts | Info.plist + usage scan | Safe |
| Storyboards | Code reference check | High |

## Examples
```bash
# Full project cleanup scan
/ios:cleanup . --report

# Fix unused imports only
/ios:cleanup Sources/ --type imports --fix

# Dead code detection with dry run
/ios:cleanup . --type dead-code --dry-run

# Aggressive cleanup with report
/ios:cleanup . --aggressive --fix --report

# Resource cleanup
/ios:cleanup . --type resources --report
```

## Output Structure
```markdown
# Cleanup Report: [Target]

## Summary
- Dead code: X occurrences
- Unused imports: X files
- Unused resources: X assets
- Deprecated APIs: X usages

## Dead Code
| File | Line | Type | Confidence | Status |
|------|------|------|------------|--------|

## Unused Imports
| File | Import | Reason |

## Resources
| Resource | Type | Last Modified |

## Deprecated APIs
| File | Line | Current | Replacement |

## Actions Taken / Recommended
```

## Safety Levels
- **Safe**: Unused imports, commented code, unused local vars
- **Medium**: Private unused methods, orphaned internal types
- **High**: Public API removal, resource deletion, protocol removal

## Integration
```bash
# Pre-commit cleanup
/ios:cleanup . --type imports --fix

# CI/CD integration
/ios:cleanup . --report --export cleanup-report.md

# Before refactoring
/ios:cleanup ModuleName/ --dry-run
```

---

**Delegates to**: swift-specialist (code analysis), architecture-specialist (dependency analysis)
