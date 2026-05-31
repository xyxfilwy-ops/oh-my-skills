#!/usr/bin/env python3
"""Lightweight structure validation for high-quality-skill-maker-v3-alpha."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REQUIRED_PATHS = [
    "SKILL.md",
    "bootstrap-prompt.md",
    "references/experience-pack-guide.md",
    "references/utility-rubric.md",
    "references/failure-patterns.md",
    "evals/trigger-cases.json",
    "evals/selection-cases.json",
    "logs/optimization-log.md",
    "logs/rejected-edits.md",
    "scripts/validate_structure.py",
]

REQUIRED_MODES = ["create", "review", "optimize"]
REQUIRED_LEVELS = ["cold-start", "usable", "pro", "release"]
REQUIRED_TRIGGER_EXPECTED = {"trigger", "no_trigger", "clarify"}
ALLOWED_FRONTMATTER_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}
MAX_SKILL_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path} is not valid JSON: {exc}")


def parse_frontmatter(skill_text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", skill_text, re.DOTALL)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")

    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            fail(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip("'\"")
    return values


def validate_frontmatter(values: dict[str, str]) -> None:
    unexpected = set(values) - ALLOWED_FRONTMATTER_KEYS
    if unexpected:
        allowed = ", ".join(sorted(ALLOWED_FRONTMATTER_KEYS))
        fail(f"Unexpected SKILL.md frontmatter key(s): {', '.join(sorted(unexpected))}. Allowed: {allowed}")

    for key in ["name", "description"]:
        if not values.get(key):
            fail(f"SKILL.md frontmatter missing {key}")

    name = values["name"].strip()
    if not re.fullmatch(r"[a-z0-9-]+", name):
        fail("SKILL.md frontmatter name must be hyphen-case: lowercase letters, digits, and hyphens only")
    if name.startswith("-") or name.endswith("-") or "--" in name:
        fail("SKILL.md frontmatter name cannot start/end with hyphen or contain consecutive hyphens")
    if len(name) > MAX_SKILL_NAME_LENGTH:
        fail(f"SKILL.md frontmatter name is too long: {len(name)} > {MAX_SKILL_NAME_LENGTH}")

    description = values["description"].strip()
    if "<" in description or ">" in description:
        fail("SKILL.md frontmatter description cannot contain angle brackets")
    if len(description) > MAX_DESCRIPTION_LENGTH:
        fail(f"SKILL.md frontmatter description is too long: {len(description)} > {MAX_DESCRIPTION_LENGTH}")


def validate_trigger_cases(data: object) -> None:
    if not isinstance(data, dict) or not isinstance(data.get("cases"), list):
        fail("trigger-cases.json must contain a cases array")
    seen: set[str] = set()
    for case in data["cases"]:
        if not isinstance(case, dict):
            fail("Each trigger case must be an object")
        for key in ["id", "input", "expected", "reason"]:
            if not case.get(key):
                fail(f"Trigger case missing {key}: {case}")
        expected = case["expected"]
        if expected not in REQUIRED_TRIGGER_EXPECTED:
            fail(f"Invalid trigger expected value: {expected}")
        seen.add(expected)
    missing = REQUIRED_TRIGGER_EXPECTED - seen
    if missing:
        fail(f"trigger-cases.json missing expected categories: {sorted(missing)}")


def validate_selection_cases(data: object) -> None:
    if not isinstance(data, dict) or not isinstance(data.get("cases"), list):
        fail("selection-cases.json must contain a cases array")
    for case in data["cases"]:
        if not isinstance(case, dict):
            fail("Each selection case must be an object")
        for key in [
            "id",
            "input",
            "current_problem",
            "expected_behavior",
            "scoring_dimensions",
            "pass_condition",
        ]:
            if key not in case or case[key] in (None, "", []):
                fail(f"Selection case missing {key}: {case}")
        if not isinstance(case["scoring_dimensions"], list):
            fail(f"Selection case scoring_dimensions must be a list: {case}")


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    root = root.resolve()

    for relative in REQUIRED_PATHS:
        path = root / relative
        if not path.exists():
            fail(f"Missing required path: {relative}")

    skill_text = (root / "SKILL.md").read_text(encoding="utf-8")
    validate_frontmatter(parse_frontmatter(skill_text))

    for mode in REQUIRED_MODES:
        if mode not in skill_text:
            fail(f"SKILL.md missing mode: {mode}")

    for level in REQUIRED_LEVELS:
        if level not in skill_text:
            fail(f"SKILL.md missing version level: {level}")

    validate_trigger_cases(load_json(root / "evals/trigger-cases.json"))
    validate_selection_cases(load_json(root / "evals/selection-cases.json"))

    print(f"PASS: {root} structure is valid")


if __name__ == "__main__":
    main()
