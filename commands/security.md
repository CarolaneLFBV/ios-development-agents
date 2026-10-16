---
description: "Security audit (OWASP, Keychain, ATS, data protection, authentication)"
argument-hint: "[target] [--focus auth|storage|network] [--owasp]"
---

# /ios:security

Audit `$ARGUMENTS` using security specialist expertise. Report by default; work
directly unless delegation is explicitly requested.

- `--focus auth|storage|network|crypto|all` selects scope (default: all).
- `--fix` applies scoped fixes with behavior validation.
- `--report` includes evidence and mitigations.
- `--owasp` maps findings to the current Mobile Top 10 edition and relevant MASVS controls.
- `--compliance` identifies technical privacy/compliance questions requiring further review; it does not certify compliance.

Check assets, threat boundaries, Keychain access policies, credential lifecycle,
ATS/trust, cryptographic key/nonce handling and sensitive logs. Use current Apple
and OWASP sources for security details. Pinning needs a justified threat model and
rotation strategy rather than a blanket requirement.

The Mobile Top 10 2024 uses M9 for insecure storage, M5 for communication and M10
for cryptography; do not reuse the 2016 numbering. Verify the current edition.

Return severity-ranked findings with location, preconditions, impact, mitigation
and verification. Redact sensitive values. State static/runtime coverage and gaps.
