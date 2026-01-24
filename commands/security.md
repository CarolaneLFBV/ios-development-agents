---
allowed-tools: [Read, Grep, Glob, Edit, TodoWrite, Task]
description: "Security audit (OWASP, Keychain, ATS, data protection, authentication)"
argument-hint: "[target] [--focus auth|storage|network] [--owasp]"
wave-enabled: false
category: "Quality"
auto-persona: ["security-specialist"]
mcp-servers: ["context7", "sequential"]
---

# /ios:security - Security Audit

Audit security for `$ARGUMENTS`.

## Arguments

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--focus` | auth\|storage\|network\|crypto\|all | all | Security focus |
| `--fix` | - | - | Auto-fix safe security issues |
| `--report` | - | - | Generate detailed security report |
| `--owasp` | - | - | Check against OWASP Mobile Top 10 |
| `--compliance` | - | - | Check GDPR, HIPAA hints |

## Security Areas

| Focus | Checks |
|-------|--------|
| `auth` | Biometric, token storage, session mgmt |
| `storage` | Keychain usage, no secrets in code |
| `network` | ATS, certificate pinning, HTTPS |
| `crypto` | Modern algorithms, secure random |

## OWASP Mobile Top 10

1. M1 - Improper Platform Usage
2. M2 - Insecure Data Storage
3. M3 - Insecure Communication
4. M4 - Insecure Authentication
5. M5 - Insufficient Cryptography
6. M6 - Insecure Authorization
7. M7 - Client Code Quality
8. M8 - Code Tampering
9. M9 - Reverse Engineering
10. M10 - Extraneous Functionality

## Common Fixes

```swift
// ❌ BAD: UserDefaults for sensitive data
UserDefaults.standard.set(token, forKey: "authToken")

// ✅ GOOD: Keychain
try KeychainManager.save(token, for: "authToken")
```

## Examples

```bash
/ios:security . --owasp --report
/ios:security AuthService.swift --focus auth --fix
/ios:security . --focus storage --compliance
/ios:security NetworkLayer/ --focus network
```

## Output

```markdown
# Security Audit: [Target]
## Risk Level: Critical | High | Medium | Low
## Findings: [Count by severity]
## Vulnerabilities: ID | Severity | Category | Location | Fix
## Recommendations: [Prioritized list]
```
