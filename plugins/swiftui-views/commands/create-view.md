---
name: Create View
description: Create SwiftUI view with proper composition, layout, and reusability
version: 1.0

required_parameters:
  - name: view-name
    type: string
    description: Name of the view to create

optional_parameters:
  - name: layout
    type: string
    options: [vstack, hstack, zstack, grid, scroll, auto]
    default: auto
  - name: complexity
    type: string
    options: [simple, moderate, complex]
    default: moderate
  - name: preview
    type: boolean
    default: true

execution:
  phases:
    - design
    - implementation
---

# Create View Command

Creates production-ready SwiftUI view with proper composition and layout.

## Phase 1: View Design

### Execution
```
Use Task tool to design view structure:
- Analyze view requirements
- Choose optimal layout ({{layout}} or auto-select)
- Break down into subviews (<100 lines each)
- Define view modifiers
- Plan preview configurations
```

---

## Phase 2: Implementation

### Execution
```
Use Task tool to implement:
- Create main view with chosen layout
- Extract subviews as computed properties
- Apply custom view modifiers
- Create PreviewProvider with configurations (if {{preview}})
- Document view parameters
```

---

## Usage Examples

### Simple View
```bash
/swiftui-views:create-view \
  --view-name ProfileCard \
  --layout vstack \
  --complexity simple
```

### Complex Grid View
```bash
/swiftui-views:create-view \
  --view-name PhotoGallery \
  --layout grid \
  --complexity complex
```

---

Creates: Complete SwiftUI view with composition, layout, modifiers, and previews.
