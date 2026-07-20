#!/usr/bin/env python3
"""iOS best-practices reminder hook.

Runs on PreToolUse for Edit/Write on Swift files. Never blocks — it only
surfaces gentle reminders as additional context when it spots common
iOS anti-patterns in the content being written.
"""

import json
import re
import sys


def build_reminders(content: str) -> list[str]:
    reminders = []

    # Legacy observation model
    if "ObservableObject" in content and "@Observable" not in content:
        reminders.append("Prefer @Observable (iOS 17+) over ObservableObject.")

    # Force unwraps / force try / force cast — ignore `!=` and `!` in strings/comments
    code = re.sub(r'"(?:\\.|[^"\\])*"', '""', content)   # blank out string literals
    code = re.sub(r'//.*', '', code)                      # drop line comments
    force_unwraps = len(re.findall(r'(?<![!=<>/*])!(?!=)', code))
    if force_unwraps > 0 or re.search(r'\btry!\s', code) or re.search(r'\bas!\s', code):
        reminders.append("Avoid force unwrap / try! / as! — use guard let, if let, or try?.")

    # Manual main-thread hops inside async code
    if "DispatchQueue.main" in content and ("async " in content or "await " in content):
        reminders.append("Prefer @MainActor over DispatchQueue.main in async contexts.")

    # Non-lazy stacks driving ForEach
    if re.search(r'\b[VH]Stack\s*[({]', content) and "ForEach" in content \
            and "Lazy" not in content and "List" not in content:
        reminders.append("Consider LazyVStack/LazyHStack for long ForEach content.")

    # Secrets in UserDefaults
    if re.search(r'UserDefaults[^\n]*(token|password|secret|apiKey|api_key)', content, re.IGNORECASE):
        reminders.append("Store secrets in the Keychain, not UserDefaults.")

    return reminders


def main():
    try:
        input_data = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, ValueError):
        return  # nothing to do; stay silent and non-blocking

    tool_input = input_data.get("tool_input", {})
    file_path = tool_input.get("file_path", "")
    if not file_path.endswith(".swift"):
        return

    content = tool_input.get("content") or tool_input.get("new_string") or ""
    reminders = build_reminders(content)
    if not reminders:
        return

    context = "iOS best practices — consider:\n" + "\n".join(f"- {r}" for r in reminders)
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "additionalContext": context,
        }
    }))


if __name__ == "__main__":
    main()
