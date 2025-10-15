---
name: Implement State
description: Implement SwiftUI state management (@State, @Observable, @Binding, @Environment)
version: 1.0

required_parameters:
  - name: target
    type: string
    description: View or module to add state management to

optional_parameters:
  - name: pattern
    type: string
    options: [state, observable, binding, environment, auto]
    default: auto
  - name: migrate
    type: boolean
    default: false
    description: Migrate ObservableObject to @Observable

execution:
  phases:
    - analysis
    - implementation
---

# Implement State Command

Adds proper state management to SwiftUI views.

## Phase 1: State Analysis

### Execution
```
Use Task tool:
- Analyze current state management
- Identify state ownership patterns
- Recommend optimal state pattern
- Plan data flow architecture
```

---

## Phase 2: Implementation

### Execution
```
Use Task tool:
- Implement recommended state pattern
- Add @State for local state
- Create @Observable classes for shared state
- Add @Binding for two-way flow
- Setup @Environment for DI
- Migrate ObservableObject if {{migrate}}
```

---

## Usage Examples

### Add State to View
```bash
/swiftui-state:implement-state \
  --target ProfileView \
  --pattern observable
```

### Migrate to @Observable
```bash
/swiftui-state:implement-state \
  --target ViewModels/ \
  --migrate true
```

---

Creates: Modern state management with proper data flow.
