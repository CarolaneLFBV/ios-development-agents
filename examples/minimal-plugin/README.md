# Minimal iOS Plugin Template

This is a minimal working example showing how to create your own iOS development plugin for the Claude Code agent system.

## Structure

```
minimal-plugin/
├── agents/
│   └── example-agent.md         # Agent definition
├── commands/
│   └── example-command.md       # Command definition (optional)
└── README.md                    # This file
```

## Agent Template

See `agents/example-agent.md` for a complete agent definition with:

- **Frontmatter metadata** - Name, description, model, tools
- **Expertise definition** - Core expertise areas
- **Best practices** - Coding standards and patterns
- **Output format** - Expected deliverables
- **Behavioral traits** - How the agent thinks and responds

## Command Template

See `commands/example-command.md` for an orchestration command with:

- **Parameter definitions** - Required and optional parameters
- **Phase-based execution** - Multi-phase workflow
- **Multi-agent coordination** - Using Task tool for sub-agents
- **Usage examples** - How to invoke the command

## Creating Your Own Plugin

### Step 1: Define Your Agent

Create `agents/your-agent.md`:

```markdown
---
name: your-agent
description: Brief description of what this agent does and when to use it. Use PROACTIVELY for specific scenarios.
model: sonnet  # or opus for complex reasoning, haiku for simple tasks
tools: read, write, edit, bash, grep, glob
---

# Your Agent Name

You are an expert in [domain].

## Core Expertise

[Define what the agent knows]

## Best Practices

[Coding standards, patterns, anti-patterns]

## Output Format

[What the agent should deliver]

---

Use this expertise to [purpose].
```

### Step 2: Create a Command (Optional)

If you need orchestration, create `commands/your-command.md`:

```markdown
---
name: Your Command Name
description: What this command orchestrates
version: 1.0

required_parameters:
  - name: param1
    type: string
    description: Parameter description

optional_parameters:
  - name: param2
    type: boolean
    default: false

execution:
  phases:
    - phase_one
    - phase_two
---

# Your Command

## Phase 1: Description

### Execution
\`\`\`
Use Task tool:
- subagent_type: "your-agent"
- prompt: """
  Instructions for the agent using {{param1}}
  """
\`\`\`

## Phase 2: Description

[Continue with more phases]
```

### Step 3: Add to Marketplace

Edit `.claude-plugin/marketplace.json` and add your plugin:

```json
{
  "name": "your-plugin-name",
  "source": "./plugins/your-plugin-name",
  "description": "What your plugin does",
  "version": "1.0.0",
  "category": "development",
  "keywords": ["ios", "your", "keywords"],
  "author": "Your Name",
  "license": "MIT"
}
```

### Step 4: Test Your Plugin

```bash
# Install locally
/plugin marketplace add file:///path/to/your/repo

# Install your plugin
/plugin install your-plugin-name

# Test your agent
"Use your-agent to [do something]"

# Test your command (if you created one)
/your-plugin-name:your-command --param1 "value"
```

## Tips for Creating Great Agents

### 1. Be Specific in Descriptions
```markdown
❌ description: Expert iOS developer
✅ description: Expert SwiftUI animator specializing in keyframe animations, matched geometry effects, and Core Animation integration. Use PROACTIVELY when creating complex animations.
```

### 2. Choose the Right Model
- **haiku**: Simple, fast tasks (formatting, basic code generation)
- **sonnet**: Standard development tasks (most agents)
- **opus**: Complex reasoning (architecture, system design)

### 3. Define Clear Expertise Areas
Break down what the agent knows into specific sections

### 4. Include Code Examples
Show both good and bad patterns with ✅/❌ markers

### 5. Specify Output Format
Tell the agent exactly what deliverables you expect

### 6. Add Behavioral Traits
Define how the agent should think and communicate

## Real-World Plugin Ideas

### iOS Development
- **swift-6-modernization** - Migrate code to Swift 6
- **combine-to-async** - Convert Combine to async/await
- **uikit-to-swiftui** - Migrate UIKit to SwiftUI
- **accessibility-audit** - Comprehensive a11y review

### Platform-Specific
- **watchos-complications** - Watch face complications
- **app-clips** - App Clip development
- **shortcuts-integration** - Siri Shortcuts
- **spotlight-search** - Core Spotlight integration

### Quality & Testing
- **snapshot-testing** - Snapshot test generation
- **performance-benchmarks** - Performance testing
- **security-hardening** - Security best practices
- **code-review-ios** - iOS-specific code review

## Publishing Your Plugin

1. **Create GitHub Repository**
   ```bash
   git init
   git add .
   git commit -m "Initial plugin release"
   git remote add origin https://github.com/you/your-plugin
   git push -u origin main
   ```

2. **Tag Version**
   ```bash
   git tag v1.0.0
   git push --tags
   ```

3. **Share with Community**
   ```bash
   # Users can now install:
   /plugin marketplace add you/your-plugin
   /plugin install your-plugin-name
   ```

## Resources

- [Claude Code Documentation](https://docs.claude.com/claude-code)
- [iOS Development Agents Main Repo](../../README.md)
- [wshobson/agents](https://github.com/wshobson/agents) - Inspiration

---

Happy plugin building! 🚀
