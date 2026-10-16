---
name: ios-storekit
description: "Implement StoreKit purchases, verified entitlements, subscriptions, restores, and purchase tests."
---

# In-app purchases and subscriptions

Inspect supported OS versions, product types/IDs, the existing purchase provider,
entitlement ownership and any server integration. Preserve a working SDK/provider
unless replacement is requested. Check current Apple/provider API contracts.

- Handle success, pending, user cancellation and failures separately. Unlock content
  only from verified transaction/entitlement state, never a button response, local
  Boolean or unverified payload. Make product delivery idempotent.
- Observe transaction updates with explicit app/service ownership and cancellation,
  starting early enough to receive unfinished or external transactions. A listener
  tied only to a paywall's visibility misses app-lifetime events. Handle same-device
  purchase results as well as updates without double delivery.
- Call `finish()` after delivering content or enabling the service successfully.
  A failed delivery needs recovery, not premature acknowledgement.
- Reconcile current access on launch and relevant updates. Distinguish consumables,
  non-consumables, non-renewing and auto-renewable subscriptions. Current entitlements
  do not restore a consumable balance; non-renewing duration needs business policy.
- Respect revocation, upgrades and subscription states such as billing grace periods.
  A renewal being cancelled does not alone end access immediately. Do not reduce
  every entitlement decision to `expirationDate > now` or an auto-renew Boolean.
- Provide an appropriate user-initiated restore path; do not force store sync on
  every launch. Keep server notifications/credentials and authority explicit when
  subscription status is shared across platforms.

Use StoreKit configuration tests and sandbox/device checks as appropriate, including
pending completion, duplicate delivery, restart, restore, refund/revocation and
failed verification. Report which environment actually ran; local StoreKit tests
do not establish production/server behavior. Work directly without recursive delegation.

Read the matching Apple contracts when needed:
[entitlements](https://developer.apple.com/documentation/storekit/transaction/currententitlements),
[updates](https://developer.apple.com/documentation/storekit/transaction/updates),
[delivery acknowledgement](https://developer.apple.com/documentation/storekit/transaction/finish()).
