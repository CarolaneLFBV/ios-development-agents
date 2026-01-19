#!/usr/bin/env python3
"""iOS development best practices reminder hook."""

import json
import sys
import os

def main():
    try:
        input_data = json.loads(sys.stdin.read())
        tool_input = input_data.get("tool_input", {})
        file_path = tool_input.get("file_path", "")

        # Only check Swift files
        if not file_path.endswith(".swift"):
            print(json.dumps({"decision": "approve"}))
            return

        content = tool_input.get("content", "") or tool_input.get("new_string", "")

        reminders = []

        # Check for common iOS anti-patterns
        if "ObservableObject" in content and "@Observable" not in content:
            reminders.append("Consider using @Observable (iOS 17+) instead of ObservableObject")

        if "force unwrap" in content.lower() or content.count("!") > 5:
            reminders.append("Avoid force unwrapping - use guard let or if let")

        if "DispatchQueue.main" in content and "async" in content:
            reminders.append("Consider @MainActor instead of DispatchQueue.main in async contexts")

        if "VStack {" in content and "ForEach" in content and "LazyVStack" not in content:
            reminders.append("Consider LazyVStack for better performance with ForEach")

        if reminders:
            reminder_text = "iOS Best Practices:\n" + "\n".join(f"- {r}" for r in reminders)
            print(json.dumps({
                "decision": "approve",
                "message": reminder_text
            }))
        else:
            print(json.dumps({"decision": "approve"}))

    except Exception as e:
        print(json.dumps({"decision": "approve"}), file=sys.stderr)

if __name__ == "__main__":
    main()
