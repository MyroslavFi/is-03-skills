#!/usr/bin/env python3
"""Validate Cursor file placement rules for provided paths."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


def is_command_markdown(path: Path) -> bool:
    if path.suffix != ".md":
        return False
    parts = path.as_posix().split("/")
    if ".cursor" in parts and "rules" in parts:
        return False
    return True


def validate_path(path: Path) -> list[str]:
    violations: list[str] = []
    posix = path.as_posix()

    if path.suffix == ".mdc" and not posix.startswith(".cursor/rules/"):
        violations.append(
            f"{posix}: .mdc files must be in .cursor/rules/"
        )

    if is_command_markdown(path) and ".cursor" in path.parts:
        if not posix.startswith(".cursor/commands/"):
            violations.append(
                f"{posix}: Cursor command markdown must be in .cursor/commands/"
            )

    return violations


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Cursor rules/commands file placement."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="Repository-relative file paths to validate",
    )
    args = parser.parse_args()

    violations: list[str] = []
    for raw in args.paths:
        path = Path(raw)
        violations.extend(validate_path(path))

    if violations:
        print("FAIL: placement violations found")
        for violation in violations:
            print(f"- {violation}")
        return 1

    print("PASS: all provided paths match Cursor placement rules")
    return 0


if __name__ == "__main__":
    sys.exit(main())
