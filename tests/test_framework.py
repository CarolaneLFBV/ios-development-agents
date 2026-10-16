import importlib.util
import contextlib
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]


def load_module(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


framework = load_module("framework", "scripts/framework.py")
hook = load_module("ios_hook", "hooks/ios_reminder_hook.py")


class BundleTests(unittest.TestCase):
    def test_distribution_works_without_local_documentation(self):
        with tempfile.TemporaryDirectory() as directory:
            snapshot = Path(directory) / "framework"
            snapshot.mkdir()
            for name in ("agents", "codex", "commands", "skills", "examples", ".claude-plugin", "hooks"):
                shutil.copytree(ROOT / name, snapshot / name,
                                ignore=shutil.ignore_patterns("__pycache__"))
            for name in ("README.md", "AGENTS.md", "CLAUDE.md", "LICENSE"):
                destination = snapshot / name
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / name, destination)
            project = Path(directory) / "iOS App"
            project.mkdir()
            output = io.StringIO()
            with patch.object(framework, "ROOT", snapshot), contextlib.redirect_stdout(output):
                framework.check()
                framework.budget()
                report = json.loads(output.getvalue().split("\n", 1)[1])
                self.assertEqual(report["groups"]["skills"]["files"], 10)
                self.assertNotIn("baseline_tokens", report["groups"]["agents"])
                framework.install(project, with_agents=True)
            self.assertFalse((snapshot / "docs").exists())
            self.assertEqual(len(list((project / ".agents/skills").glob("*/SKILL.md"))), 10)
            self.assertEqual(len(list((project / ".codex/agents").glob("*.toml"))), 8)

    def test_generated_bundle_matches_sources(self):
        framework.check()

    def test_evaluation_cases_have_distributable_inputs(self):
        catalog = json.loads((ROOT / "evals/cases.json").read_text())
        identifiers = set()
        for case in catalog["cases"]:
            with self.subTest(case=case["id"]):
                self.assertNotIn(case["id"], identifiers)
                identifiers.add(case["id"])
                fixture = (ROOT / case["fixture"]).resolve()
                self.assertTrue(fixture.is_relative_to(ROOT / "evals/fixtures"))
                self.assertTrue(fixture.is_file())
                self.assertTrue(case["prompt"])
                self.assertGreaterEqual(len(case["criteria"]), 3)
                for skill in case["skills"]:
                    self.assertTrue((ROOT / "skills" / skill / "SKILL.md").is_file())

    def test_agent_instructions_are_portable_and_synchronized(self):
        for domain in framework.COLORS:
            with self.subTest(domain=domain):
                source = ROOT / "skills" / f"ios-{domain}" / "SKILL.md"
                _, expected = framework.markdown(source)
                codex = tomllib.loads((ROOT / "codex/agents" / f"{domain}-specialist.toml").read_text())
                _, claude = framework.markdown(ROOT / "agents" / f"{domain}-specialist.md")
                # Restore source-relative links to compare the substantive prompts.
                native_body = codex["developer_instructions"].replace(f"../../.agents/skills/ios-{domain}/", "")
                claude_body = claude.replace(f"../skills/ios-{domain}/", "")
                self.assertTrue(native_body.endswith(expected))
                self.assertTrue(claude_body.endswith(expected))
                for target in re.findall(r"\]\(([^)]+)\)", claude):
                    if "://" not in target and not target.startswith("#"):
                        self.assertTrue((ROOT / "agents" / target).is_file(), target)

    def test_install_is_self_contained_and_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            instructions = project / "AGENTS.md"
            instructions.write_text("Existing project policy\n")
            framework.install(project, with_agents=True)
            first = {p.relative_to(project): p.read_bytes() for p in project.rglob("*") if p.is_file()}
            framework.install(project, with_agents=True)
            second = {p.relative_to(project): p.read_bytes() for p in project.rglob("*") if p.is_file()}
            self.assertEqual(first, second)
            self.assertEqual(instructions.read_text(), "Existing project policy\n")
            self.assertEqual(len(list((project / ".codex/agents").glob("*.toml"))), 8)
            self.assertEqual(len(list((project / ".agents/skills").glob("*/SKILL.md"))), 10)
            for name in framework.COMMANDS:
                self.assertTrue((project / ".agents/skills/ios-workflow/references" / f"{name}.md").is_file())
            # Installed packages resolve references without the source repository.
            for path in (project / ".agents/skills").rglob("*.md"):
                for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                    if "://" not in link and not link.startswith("#"):
                        self.assertTrue((path.parent / link).is_file(), f"Broken installed link: {link}")
            # A custom agent can find support files without this source checkout.
            for path in (project / ".codex/agents").glob("*.toml"):
                body = tomllib.loads(path.read_text())["developer_instructions"]
                for link in re.findall(r"\]\(([^)]+)\)", body):
                    if "://" not in link and not link.startswith("#"):
                        self.assertTrue((path.parent / link).is_file(), f"Broken agent support link: {link}")

    def test_skills_only_install_does_not_add_agent_configuration(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            framework.install(project)
            self.assertFalse((project / ".codex").exists())

    def test_conflict_is_detected_before_any_install_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            conflict = project / ".codex/agents/testing-specialist.toml"
            conflict.parent.mkdir(parents=True)
            conflict.write_text("User customizations\n")
            with self.assertRaisesRegex(ValueError, "Existing file differs"):
                framework.install(project, with_agents=True)
            self.assertEqual(conflict.read_text(), "User customizations\n")
            self.assertFalse((project / ".agents").exists())

    def test_symlink_parent_is_rejected_without_writing_outside_project(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            project, outside = base / "project", base / "outside"
            project.mkdir()
            outside.mkdir()
            (project / ".agents").symlink_to(outside, target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "symlink destination"):
                framework.install(project)
            self.assertEqual(list(outside.iterdir()), [])

    def test_non_directory_parent_is_rejected_before_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            (project / ".codex").write_text("Not a directory\n")
            with self.assertRaisesRegex(ValueError, "not a directory"):
                framework.install(project, with_agents=True)
            self.assertFalse((project / ".agents").exists())


class HookTests(unittest.TestCase):
    def test_logical_negation_and_inequality_are_quiet(self):
        self.assertEqual(hook.build_reminders("if !isLoading && count != 0 { run() }"), [])

    def test_strings_and_nested_comments_are_quiet(self):
        for source in (
            '// try! load()\nlet value = "hello!"',
            '/* try! a() /* as! Int */ foo! */ let okay = true',
            'let example = #"try! foo() and "nested quotes!""#',
            'let example = """\nfoo!\ntry! test()\n"""',
            'let example = "escaped \\" quote foo!"',
        ):
            with self.subTest(source=source):
                self.assertEqual(hook.build_reminders(source), [])

    def test_force_operations_are_detected(self):
        for source in ("let value = optional!", "try! work()", "let value = input as! Int", "make()!"):
            with self.subTest(source=source):
                self.assertEqual(len(hook.build_reminders(source)), 1)

    def test_existing_observation_and_small_eager_stacks_do_not_trigger_churn(self):
        source = "class State: ObservableObject {}\nVStack { ForEach(items) { Row($0) } }"
        self.assertEqual(hook.build_reminders(source), [])

    def test_credentials_in_defaults_are_reported(self):
        self.assertEqual(len(hook.build_reminders('UserDefaults.standard.set(token, forKey: "session")')), 1)

    def test_hook_protocol_is_nonblocking_and_swift_only(self):
        payload = {"tool_input": {"file_path": "View.swift", "new_string": "try! load()"}}
        run = subprocess.run([sys.executable, str(ROOT / "hooks/ios_reminder_hook.py")],
                             input=json.dumps(payload), text=True, capture_output=True, check=True)
        output = json.loads(run.stdout)["hookSpecificOutput"]
        self.assertEqual(output["hookEventName"], "PreToolUse")
        self.assertIn("additionalContext", output)
        self.assertNotIn("permissionDecision", output)
        payload["tool_input"]["file_path"] = "README.md"
        run = subprocess.run([sys.executable, str(ROOT / "hooks/ios_reminder_hook.py")],
                             input=json.dumps(payload), text=True, capture_output=True, check=True)
        self.assertEqual(run.stdout, "")

    def test_malformed_hook_payloads_stay_quiet(self):
        for payload in ("not-json", "[]", '{"tool_input": null}',
                        '{"tool_input": {"file_path": 1}}',
                        '{"tool_input": {"file_path": "A.swift", "content": [1]}}'):
            with self.subTest(payload=payload):
                run = subprocess.run([sys.executable, str(ROOT / "hooks/ios_reminder_hook.py")],
                                     input=payload, text=True, capture_output=True, check=True)
                self.assertEqual(run.stdout, "")
                self.assertEqual(run.stderr, "")


if __name__ == "__main__":
    unittest.main()
