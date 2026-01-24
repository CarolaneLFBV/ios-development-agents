---
allowed-tools: [Read, Write, Bash, TodoWrite]
description: "App Store submission preparation and validation"
argument-hint: "[--validate] [--screenshots] [--metadata]"
wave-enabled: false
category: "Delivery"
auto-persona: ["devops-specialist"]
mcp-servers: ["context7"]
---

# /ios:publish - App Store Publishing

Prepare app for App Store submission: `$ARGUMENTS`.

## Arguments

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--validate` | - | - | Validate build for submission |
| `--screenshots` | - | - | Generate App Store screenshots |
| `--metadata` | - | - | Prepare App Store metadata |
| `--export` | - | - | Export IPA for submission |

## Pre-Submission Checklist

### App Store Guidelines
- [ ] Content guidelines compliance
- [ ] Privacy policy URL
- [ ] Data collection disclosure
- [ ] Age rating accurate

### Technical Requirements
- [ ] App icons (all sizes)
- [ ] Launch screen
- [ ] iOS version compatibility
- [ ] Device compatibility

### Metadata
- [ ] App description
- [ ] Keywords (100 chars)
- [ ] Screenshots (all device sizes)
- [ ] Preview video (optional)

### Testing
- [ ] TestFlight testing complete
- [ ] Crash-free rate acceptable
- [ ] Performance validated

## Screenshot Sizes

| Device | Size |
|--------|------|
| iPhone 6.7" | 1290 x 2796 |
| iPhone 6.5" | 1284 x 2778 |
| iPhone 5.5" | 1242 x 2208 |
| iPad Pro 12.9" | 2048 x 2732 |

## Examples

```bash
/ios:publish --validate
/ios:publish --screenshots --metadata
/ios:publish --export
```

## Output

```markdown
# Publishing: [App Name]
## Validation: Pass/Fail
## Screenshots: Generated devices
## Metadata: Completeness status
## Next Steps: Submission actions
```
