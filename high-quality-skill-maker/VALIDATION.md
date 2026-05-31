# Validation Guide

This package has three validation paths with different environment assumptions.

## 1. Repo-local validator

Use the repo-local validator for deterministic MVP checks without third-party dependencies:

```bash
python3 high-quality-skill-maker/scripts/validate_structure.py high-quality-skill-maker
```

If you are not in a Codex environment, you only need to run the repo-local validator.

It checks:

- Required MVP files exist.
- `SKILL.md` starts with frontmatter.
- Frontmatter includes `name` and `description`.
- Frontmatter follows the same basic constraints as the system `quick_validate.py`: allowed keys, hyphen-case name, and description length/character limits.
- `SKILL.md` contains `create`, `review`, `optimize` and `cold-start`, `usable`, `pro`, `release`.
- Trigger eval cases contain at least 20 cases and include at least 3 cases each for `trigger/create`, `trigger/review`, `trigger/optimize`, `no_trigger`, and `clarify`.
- Trigger modes are only `create`, `review`, `optimize`, or `null`, with mode required for `trigger` and forbidden for `no_trigger` / `clarify`.
- Selection eval cases contain at least 8 cases and use failure modes from `references/failure-patterns.md`.
- Eval case ids are unique within each eval file.

## 2. System skill-creator quick validation

`run_system_quick_validate.py` depends on `/opt/codex/skills/.system/skill-creator/scripts/quick_validate.py` existing.
If that path does not exist, the current environment does not support the system validator; this is not an error in this Skill.

When the system validator is available, it can be run directly:

```bash
python3 /opt/codex/skills/.system/skill-creator/scripts/quick_validate.py high-quality-skill-maker
```

The system validator imports `yaml`, which is provided by the `PyYAML` package. If it fails with:

```text
ModuleNotFoundError: No module named 'yaml'
```

install the development dependency first:

```bash
python3 -m pip install -r high-quality-skill-maker/requirements-dev.txt
```

Then rerun the system validator.

## 3. Offline wrapper for Codex environments

Use the offline wrapper only when the system `quick_validate.py` exists but the environment lacks PyYAML and cannot install dependencies. It runs the same system validator but injects a tiny YAML parser that supports this Skill's simple frontmatter:

```bash
python3 high-quality-skill-maker/scripts/run_system_quick_validate.py high-quality-skill-maker
```

## Recommended local validation sequence

```bash
python3 high-quality-skill-maker/scripts/validate_structure.py high-quality-skill-maker
python3 -m json.tool high-quality-skill-maker/evals/trigger-cases.json >/tmp/trigger-cases.formatted.json
python3 -m json.tool high-quality-skill-maker/evals/selection-cases.json >/tmp/selection-cases.formatted.json
python3 -m py_compile high-quality-skill-maker/scripts/*.py
```
