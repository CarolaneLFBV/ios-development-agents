---
name: ios-devops
description: "Configure or troubleshoot iOS builds, signing, CI/CD, TestFlight, and App Store delivery."
---

# Build and delivery

Follow existing scripts, lockfiles, CI and release policy. Discover installed Xcode,
schemes, test plans and simulator destinations. Verify SDKs, runner images, actions
and submission requirements in current Apple/provider documentation.
Own the build/signing configuration of capabilities and extension targets. Platform
integration owns their runtime contracts; security owns trust and privacy decisions.

- Separate compiler, SDK, deployment target, and App Store submission constraints.
  Never assume a particular Xcode app path, simulator name or hosted runner image.
  Respect pinned versions and update them only within the requested scope.
- Follow existing CI conventions. Pin external actions/dependencies according to
  repository policy, minimize token permissions, and isolate signing credentials
  from untrusted pull requests. Do not print keys or provisioning secrets.
- Match validation to the change: build/test affected targets, run existing lint
  and coverage policy, and retain useful result bundles.
- Preserve entitlements, bundle IDs, build numbering and export options. Test
  signing on the intended distribution path; a simulator build does not prove
  that archive/export or device signing succeeds.
- Fetch current App Store SDK requirements, privacy manifest/required-reason API
  guidance, screenshot specifications and metadata requirements when preparing
  a submission. Avoid hardcoded device-size tables that become stale.
- Prepare and validate release artifacts under existing authorization. Upload,
  submit or release only when those external actions are within the user's request.

Work directly without recursive delegation. Report commands, artifacts, outcomes
and signing/device/account/runner checks that could not run.
