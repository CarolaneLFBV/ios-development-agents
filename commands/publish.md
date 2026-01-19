---
allowed-tools: [Read, Write, Bash, TodoWrite]
description: "App Store submission preparation and validation"
argument-hint: "[--validate] [--screenshots] [--metadata]"
---

# /ios:publish - App Store Publishing

Prepare app for App Store submission: `$ARGUMENTS`.

## Arguments
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
