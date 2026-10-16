# Extensions, widgets, Live Activities and App Intents

Identify the actual target, OS availability, entitlements and system execution
contract before implementing. App and extension code may execute in separate
processes with independent lifetimes; do not share an in-memory singleton or a live
ModelContext as cross-process state. Use supported shared containers/App Groups and
an explicit consistency strategy for the data store.

Widget timelines, reload requests, Live Activity updates and App Intent execution
have different budgets and delivery rules. Check current framework documentation;
an update request does not guarantee immediate display or unlimited work. Keep
snapshots bounded and current enough for their purpose, and protect sensitive
content on locked surfaces.

For App Intents, model actions and entity identifiers with clear parameter/query
contracts. Verify discovery, permissions, authentication and process requirements.
An action must not depend on a particular screen already being alive. Make repeated
invocations safe and support cancellation. Keep presentation in the UI layer and
business/data policy in the application's existing services.

Test the extension target and system entry point, not only a SwiftUI preview. Include
unavailable data, app termination, locked-device behavior where relevant and changes
made by another process. Report which checks require a real device or account.
[Apple App Intents](https://developer.apple.com/documentation/appintents),
[WidgetKit](https://developer.apple.com/documentation/widgetkit),
[ActivityKit](https://developer.apple.com/documentation/activitykit).
