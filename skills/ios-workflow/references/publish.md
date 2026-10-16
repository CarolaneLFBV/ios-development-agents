<!-- Generated from commands/ by scripts/framework.py. -->

# /ios:publish

Prepare `$ARGUMENTS` for App Store delivery with DevOps expertise. Work directly
unless delegation is explicitly requested. Preparation/validation does not itself
request upload, submission or release; perform those actions when explicitly in scope.

- `--validate` checks the intended build/distribution configuration.
- `--screenshots` prepares screenshots for currently required device/display groups.
- `--metadata` prepares App Store metadata.
- `--export` exports an archive/IPA when signing and tooling are available.

Read current Apple submission requirements, screenshot specifications, privacy
manifest/required-reason API guidance and metadata constraints. Inspect the app's
bundle IDs, entitlements, SDK, deployment target, version/build numbers and export
configuration. Do not assume Xcode paths, simulator names or stale screenshot tables.

Validate only what can actually be checked. A simulator build does not validate
signing/export, a privacy manifest does not establish policy compliance, and source
review does not prove TestFlight testing occurred.

Return prepared artifacts, completed checks and concrete remaining submission steps.
