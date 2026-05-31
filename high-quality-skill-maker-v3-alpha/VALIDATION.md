# Validation Guide

This package has two validation paths.

## 1. Built-in MVP validator

Use the repo-local validator for deterministic MVP checks without third-party dependencies:

```bash
python3 high-quality-skill-maker-v3-alpha/scripts/validate_structure.py high-quality-skill-maker-v3-alpha
```

It checks:

- Required MVP files exist.
- `SKILL.md` starts with frontmatter.
- Frontmatter includes `name` and `description`.
- Frontmatter follows the same basic constraints as the system `quick_validate.py`: allowed keys, hyphen-case name, and description length/character limits.
- `SKILL.md` contains `create`, `review`, `optimize` and `cold-start`, `usable`, `pro`, `release`.
- Trigger and selection eval JSON files are valid and contain required fields.

## 2. System skill-creator quick validation

The system validator at `/opt/codex/skills/.system/skill-creator/scripts/quick_validate.py` imports `yaml`, which is provided by the `PyYAML` package. If it fails with:

```text
ModuleNotFoundError: No module named 'yaml'
```

install the development dependency first:

```bash
python3 -m pip install -r high-quality-skill-maker-v3-alpha/requirements-dev.txt
```

Then run:

```bash
python3 /opt/codex/skills/.system/skill-creator/scripts/quick_validate.py high-quality-skill-maker-v3-alpha
```

If package installation is blocked by the environment, use the offline wrapper instead. It runs the same system validator but injects a tiny YAML parser that supports this Skill's simple frontmatter:

```bash
python3 high-quality-skill-maker-v3-alpha/scripts/run_system_quick_validate.py high-quality-skill-maker-v3-alpha
```

## Recommended local validation sequence

```bash
python3 high-quality-skill-maker-v3-alpha/scripts/validate_structure.py high-quality-skill-maker-v3-alpha
python3 -m json.tool high-quality-skill-maker-v3-alpha/evals/trigger-cases.json >/tmp/trigger-cases.formatted.json
python3 -m json.tool high-quality-skill-maker-v3-alpha/evals/selection-cases.json >/tmp/selection-cases.formatted.json
python3 -m py_compile high-quality-skill-maker-v3-alpha/scripts/validate_structure.py
python3 high-quality-skill-maker-v3-alpha/scripts/run_system_quick_validate.py high-quality-skill-maker-v3-alpha
```
