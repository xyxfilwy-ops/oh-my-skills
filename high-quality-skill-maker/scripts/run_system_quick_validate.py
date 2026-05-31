#!/usr/bin/env python3
"""Run the system skill-creator quick_validate.py with an offline YAML fallback.

The upstream validator imports `yaml` from PyYAML. Some sandboxed environments do not
have PyYAML installed and cannot download it. This wrapper uses PyYAML when present;
otherwise it registers a tiny YAML module that supports the simple scalar frontmatter
used by Codex skills (`key: value` pairs), then runs the upstream validator unchanged.
"""

from __future__ import annotations

import importlib.util
import runpy
import sys
import types
from pathlib import Path

QUICK_VALIDATE = Path("/opt/codex/skills/.system/skill-creator/scripts/quick_validate.py")


class MinimalYAMLError(Exception):
    """Fallback exception type compatible with yaml.YAMLError."""


def minimal_safe_load(text: str) -> dict[str, str]:
    """Parse simple YAML frontmatter containing scalar `key: value` lines."""
    data: dict[str, str] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise MinimalYAMLError(f"Unsupported YAML line: {raw_line}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip("'\"")
        if not key:
            raise MinimalYAMLError(f"Empty YAML key: {raw_line}")
        data[key] = value
    return data


def ensure_yaml_module() -> None:
    """Use PyYAML when installed; otherwise provide the minimal API quick_validate needs."""
    if importlib.util.find_spec("yaml") is not None:
        return

    module = types.ModuleType("yaml")
    module.safe_load = minimal_safe_load  # type: ignore[attr-defined]
    module.YAMLError = MinimalYAMLError  # type: ignore[attr-defined]
    sys.modules["yaml"] = module


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python run_system_quick_validate.py <skill_directory>")
        raise SystemExit(1)
    if not QUICK_VALIDATE.exists():
        print(f"System quick_validate.py not found: {QUICK_VALIDATE}")
        raise SystemExit(1)

    ensure_yaml_module()
    skill_directory = sys.argv[1]
    sys.argv = [str(QUICK_VALIDATE), skill_directory]
    runpy.run_path(str(QUICK_VALIDATE), run_name="__main__")


if __name__ == "__main__":
    main()
