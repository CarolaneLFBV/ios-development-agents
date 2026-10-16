# Application data and network policy

Inspect persistence, API contracts, account boundaries and existing service ownership.
Define the source of truth, freshness needs and offline behavior before adding a
repository, cache or sync layer. Architecture owns these policies; Swift owns
language/URLSession mechanics, security credential trust, and platform OS execution.

- Define cache keys, validators, expiry and account scoping. Prevent one account's
  data leaking into another session; clear or partition caches on logout as needed.
- Model pagination identity and ordering, cancellation and stale responses. A request
  for an earlier filter/page must not overwrite a newer state. Deduplicate items and
  define behavior when cursor validity or the backing dataset changes.
- Retry only eligible failures with bounded attempts, backoff/jitter and an overall
  deadline. Honor server retry guidance. Replaying a write needs an idempotency
  contract or reconciliation; do not retry every request on every error.
- Coordinate credential refresh so concurrent unauthorized responses do not trigger
  a refresh storm. Retry eligible requests within a bound; preserve useful errors
  and stop or cancel work when the account/session changes.
- Offline writes need stable operation IDs, durable ordering, conflict policy and
  recovery after relaunch. Define server/local authority and deletion/tombstone
  behavior; eventual sync is not immediate consistency.
- A connectivity hint does not prove an endpoint is reachable. URLSession's
  `waitsForConnectivity` covers connection establishment, not every dropped connection.

Use deterministic transport/clock/store doubles to verify retry budgets, duplicate
writes, reordered responses, account changes and conflicting remote edits. Test
schema upgrades with representative old stores. Keep live models in their storage
isolation domain; cross boundaries with identifiers or suitable snapshots.
[URLSession connectivity policy](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/waitsforconnectivity),
[SwiftData sync contracts](https://developer.apple.com/documentation/swiftdata/syncing-model-data-across-a-persons-devices).
