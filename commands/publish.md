---
allowed-tools: [Read, Write, Bash, TodoWrite]
description: "App Store submission preparation and validation"
category: "Deployment & Publishing"
auto-persona: ["architecture-specialist"]
mcp-servers: ["context7"]
---

# /ios:publish - App Store Publishing

## Purpose
Prepare iOS app for App Store submission including validation, screenshots, and metadata.

## Usage
```bash
/ios:publish [--validate] [--screenshots] [--metadata]
```

## Arguments
- `--validate` - Validate build for submission
- `--screenshots` - Generate App Store screenshots
- `--metadata` - Prepare App Store metadata
- `--export` - Export IPA for submission

## Checklist
- [ ] App Store guidelines compliance
- [ ] Privacy policy and data usage
- [ ] App icons and screenshots
- [ ] App description and keywords
- [ ] Version number and build
- [ ] Testing on TestFlight

## Examples
```bash
/ios:publish --validate
/ios:publish --screenshots --metadata
```

---

**Delegates to**: architecture-specialist
