---
name: Design Models
description: Design SwiftData @Model classes with relationships and proper schema
version: 1.0

required_parameters:
  - name: domain
    type: string
    description: Domain to model (e.g., "Task management", "E-commerce")

optional_parameters:
  - name: entities
    type: array
    description: Entity names (e.g., [User, Post, Comment])
  - name: relationships
    type: boolean
    default: true

execution:
  phases:
    - design
    - implementation
---

# Design Models Command

Creates complete SwiftData model schema with relationships.

## Phase 1: Schema Design

### Execution
```
Use Task tool:
- Analyze domain requirements
- Identify entities and relationships
- Design @Model classes
- Define delete rules
- Plan attributes and indexes
```

---

## Phase 2: Implementation

### Execution
```
Use Task tool:
- Create @Model classes
- Implement relationships
- Add @Attribute modifiers
- Setup ModelContainer
- Generate sample data
```

---

## Usage Example

```bash
/swiftdata-models:design-models \
  --domain "Recipe app" \
  --entities Recipe,Ingredient,Category
```

---

Creates: Complete SwiftData schema with models, relationships, and container setup.
