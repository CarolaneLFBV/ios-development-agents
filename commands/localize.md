---
description: "Extract and maintain localized iOS strings and catalog variations."
argument-hint: "[target] [--languages en,fr,es] [--extract]"
---

# /ios:localize

Localize `$ARGUMENTS` using the project's current resource strategy. Work directly
with SwiftUI/localization expertise unless delegation is explicitly requested.

- `--languages <comma-separated locales>` selects target locales (default: en).
- `--extract` identifies/extracts localizable strings using supported project tooling.
- `--generate` creates or updates resources in the existing format; prefer String Catalogs for modern projects without an established format.

Preserve stable keys and existing translations. Account for interpolation types,
plural variations, translator comments, accessibility text and locale-aware
number/date formatting. SwiftUI `Text` literals may already be localized; do not
blindly turn them into opaque keys or concatenate translated fragments.

Use `.xcstrings`, `.strings` and `.stringsdict` according to target tooling.
Treat proposed machine translations as needing language review. Verify catalog
validity, missing entries and affected builds where tools are available; inspect
RTL, long strings and accessibility sizes when relevant.

Report locales/resources changed, untranslated entries and checks actually run.
