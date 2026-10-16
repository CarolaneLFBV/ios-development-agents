---
description: "Audit or improve iOS authentication, storage, network trust, and crypto."
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

Name the OWASP edition used and keep findings consistent with that taxonomy.

Return severity-ranked findings with location, preconditions, impact, mitigation
and verification. Redact sensitive values. State static/runtime coverage and gaps.
