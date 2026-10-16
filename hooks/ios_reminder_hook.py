#!/usr/bin/env python3
"""iOS best-practices reminder hook.

Runs on PreToolUse for Edit/Write on Swift files. Never blocks — it only
surfaces gentle reminders as additional context when it spots common
iOS anti-patterns in the content being written.
"""

import json
import re
import sys

STRING_START = re.compile(r'(#+)?("""|")')


def code_mask(content: str) -> str:
    """Mask common Swift strings/comments; this is a heuristic, not a parser.

    Interpolated expressions and regex literals are not analyzed as Swift syntax.
    Preserve positions/newlines so masking cannot join unrelated tokens.
    """
    result = list(content)
    i = 0
    while i < len(content):
        start = i
        if content.startswith("//", i):
            end = content.find("\n", i)
            i = len(content) if end < 0 else end
        elif content.startswith("/*", i):
            depth = 1
            i += 2
            while i < len(content) and depth:
                if content.startswith("/*", i):
                    depth += 1
                    i += 2
                elif content.startswith("*/", i):
                    depth -= 1
                    i += 2
                else:
                    i += 1
        else:
            match = STRING_START.match(content, i)
            if not match:
                i += 1
                continue
            hashes = match.group(1) or ""
            delimiter = match.group(2) + hashes
            escape = "\\" + hashes
            i += len(match.group())
            while i < len(content):
                if content.startswith(escape, i):
                    i += len(escape) + 1
                elif content.startswith(delimiter, i):
                    i += len(delimiter)
                    break
                else:
                    i += 1
        for index in range(start, min(i, len(content))):
            if result[index] != "\n":
                result[index] = " "
    return "".join(result)


def build_reminders(content: str) -> list[str]:
    code = code_mask(content)
    reminders = []
    if re.search(r'(?<=[\w)\]])!(?!=)|\b(?:try|as)\s*!', code):
        reminders.append("Check force unwrap / try! / as!: justify the invariant or handle failure while preserving useful errors.")
    if "DispatchQueue.main" in code and re.search(r'\b(?:async|await)\b', code):
        reminders.append("Check actor isolation around DispatchQueue.main; use @MainActor where appropriate for the existing API.")
    if re.search(r'UserDefaults[^\n]*(token|password|secret|apiKey|api_key)', code, re.IGNORECASE):
        reminders.append("Store credentials in Keychain with an appropriate access policy, not UserDefaults.")
    return reminders


def main():
    try:
        input_data = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, ValueError):
        return  # nothing to do; stay silent and non-blocking

    if not isinstance(input_data, dict):
        return
    tool_input = input_data.get("tool_input", {})
    if not isinstance(tool_input, dict):
        return
    file_path = tool_input.get("file_path", "")
    if not isinstance(file_path, str) or not file_path.endswith(".swift"):
        return

    content = tool_input.get("content") or tool_input.get("new_string") or ""
    if not isinstance(content, str):
        return
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
