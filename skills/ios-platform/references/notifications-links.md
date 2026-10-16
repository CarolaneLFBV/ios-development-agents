# Notifications and incoming links

Read existing app/scene handlers, navigation state and authorization flow. Configure
notification delegates before dependent events arrive. Separate permission prompts,
APNs registration and current notification settings; denial and later settings
changes need explicit behavior.

Notification responses, remote pushes and incoming URLs may reach a cold app or an
inactive scene. Parse them into validated domain events, retain only the minimum
pending route, then navigate when the relevant scene and authentication state are
ready. Deduplicate events and check authorization for the destination. Treat URL
paths, query values and push payloads as untrusted input; allowlist routes and avoid
forwarding arbitrary URLs or privileged actions.

For silent pushes, check capabilities and the server's current APNs headers/payload
requirements. Delivery is not guaranteed and is unsuitable for exact periodic work.
Complete handlers promptly, once, and preserve cancellation/expiration behavior.
Do not assume an APNs device token is stable or include it in diagnostics.

Test cold/warm start, foreground delivery, denied permission, duplicate events,
expired authentication and malformed links. Simulator injection verifies local
handling; real remote delivery requires the intended environment and device.
[Apple notification handling](https://developer.apple.com/documentation/usernotifications/handling-notifications-and-notification-related-actions),
[background push delivery](https://developer.apple.com/documentation/usernotifications/pushing-background-updates-to-your-app).
