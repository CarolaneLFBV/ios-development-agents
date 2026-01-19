---
allowed-tools: [Read, Grep, Glob, Edit, TodoWrite, Task]
description: "Security audit (OWASP, Keychain, ATS, data protection, authentication)"
argument-hint: "[target] [--focus auth|storage|network|all] [--fix]"
---

# /ios:security - Security Audit

Audit security for `$ARGUMENTS`.

## Arguments
- `--focus auth|storage|network|crypto|all` - Security focus area
- `--fix` - Auto-fix safe security issues
- `--report` - Generate detailed security report
- `--owasp` - Check against OWASP Mobile Top 10
- `--compliance` - Check compliance (GDPR, HIPAA hints)

## Security Checklist

### Authentication (--focus auth)
- [ ] Biometric authentication (Face ID/Touch ID)
- [ ] Secure token storage (Keychain)
- [ ] Session management
- [ ] Password policies
- [ ] Multi-factor authentication

### Data Storage (--focus storage)
- [ ] Keychain for sensitive data
- [ ] No secrets in code/plist
- [ ] Data Protection API usage
- [ ] Secure file attributes
- [ ] Core Data/SwiftData encryption

### Network Security (--focus network)
- [ ] App Transport Security (ATS)
- [ ] Certificate pinning
- [ ] No HTTP (HTTPS only)
- [ ] API key protection
- [ ] Request/response validation

### Cryptography (--focus crypto)
- [ ] Modern algorithms (AES-256, SHA-256+)
- [ ] Secure random generation
- [ ] Key derivation (PBKDF2, Argon2)
- [ ] No hardcoded keys

## Common Vulnerabilities

### Insecure Storage
```swift
// ❌ BAD: UserDefaults for sensitive data
UserDefaults.standard.set(token, forKey: "authToken")

// ✅ GOOD: Keychain
try KeychainManager.save(token, for: "authToken")
```

### Hardcoded Secrets
```swift
// ❌ BAD: Hardcoded API key
let apiKey = "sk-1234567890abcdef"

// ✅ GOOD: Environment or Keychain
let apiKey = ProcessInfo.processInfo.environment["API_KEY"]
// Or: Configuration.plist (excluded from git)
```

### Missing ATS
```xml
<!-- ❌ BAD: Disabling ATS -->
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>

<!-- ✅ GOOD: Exception only for specific domain -->
<key>NSExceptionDomains</key>
<dict>
    <key>legacy-api.example.com</key>
    <dict>
        <key>NSExceptionAllowsInsecureHTTPLoads</key>
        <true/>
    </dict>
</dict>
```

### Insecure Biometrics
```swift
// ❌ BAD: No fallback handling
let context = LAContext()
context.evaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, ...)

// ✅ GOOD: Proper error handling + Keychain integration
context.evaluatePolicy(.deviceOwnerAuthentication, ...) // Includes passcode fallback
// Store auth state in Keychain with biometric protection
```

## OWASP Mobile Top 10 (--owasp)
1. **M1** - Improper Platform Usage
2. **M2** - Insecure Data Storage
3. **M3** - Insecure Communication
4. **M4** - Insecure Authentication
5. **M5** - Insufficient Cryptography
6. **M6** - Insecure Authorization
7. **M7** - Client Code Quality
8. **M8** - Code Tampering
9. **M9** - Reverse Engineering
10. **M10** - Extraneous Functionality

## Keychain Best Practices
```swift
// Keychain wrapper
actor KeychainManager {
    static func save(_ data: Data, for key: String, biometric: Bool = false) throws {
        var query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrAccount as String: key,
            kSecValueData as String: data
        ]
        if biometric {
            let access = SecAccessControlCreateWithFlags(nil, kSecAttrAccessibleWhenUnlockedThisDeviceOnly,
                .biometryCurrentSet, nil)
            query[kSecAttrAccessControl as String] = access
        }
        SecItemAdd(query as CFDictionary, nil)
    }
}
```

## Output Structure
```markdown
# Security Audit: [Target]
## Risk Level: Critical | High | Medium | Low
## Findings: [Count by severity]
## Vulnerabilities:
| ID | Severity | Category | Location | Description | Fix |
## Recommendations: [Prioritized list]
## Compliance: [Status]
```

## Examples
```bash
/ios:security . --owasp --report
/ios:security AuthService.swift --focus auth --fix
/ios:security . --focus storage --compliance
/ios:security NetworkLayer/ --focus network
```

---

**Delegates to**: security-specialist (audit), swift-specialist (crypto patterns)
