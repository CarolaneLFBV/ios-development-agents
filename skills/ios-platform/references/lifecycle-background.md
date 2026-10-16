# Lifecycle and background execution

Inspect app-wide versus scene-scoped ownership. Multiple scenes can be active at
different times; a single global foreground flag is often insufficient. Persist
recoverable state before suspension and reconstruct it after process termination.

Choose the contract from the job:

- Short foreground work that needs time to finish: an appropriate UIKit background
  task assertion, with expiration handling and a balanced end call.
- Deferrable refresh or processing: the supported BackgroundTasks request type,
  registered early with matching task IDs and required capabilities.
- File upload/download across suspension: a background URLSession where supported,
  with delegate reconnection and completion handling after relaunch.

Scheduling expresses eligibility; the OS decides execution time. Do not use a timer,
an endless Task or a desired start date to promise a fixed background interval.
Select newer task types only after checking SDK, OS and platform support.

Retain the work's cancellation handle. Connect expiration to cancellation and cleanup;
report completion once, including failure/cancellation paths. Keep completion and
expiration races on a defined isolation domain. Save resumable progress and make
retries safe after the process dies.

Verify foreground/background transitions, expiration during work, partial progress
and relaunch. Distinguish debugger-triggered delivery from real scheduling.
[Apple background strategies](https://developer.apple.com/documentation/backgroundtasks/choosing-background-strategies-for-your-app).
