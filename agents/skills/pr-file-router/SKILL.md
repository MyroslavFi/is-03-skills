---
name: pr-file-router
description: Validates pull request file placement for Cursor assets and reports misplaced files. Use when preparing a PR, checking changed files, or enforcing .cursor/rules and .cursor/commands organization.
---

# PR File Router

## Instructions

1. Collect changed paths from git status/diff.
2. Run the validator script to detect misplaced Cursor assets:
   - `python agents/skills/pr-file-router/scripts/verify_cursor_layout.py <path>...`
3. Interpret results:
   - Exit code `0`: layout valid.
   - Exit code `1`: at least one placement violation found.
4. Share violations with exact move recommendations.
5. Re-run validation after proposed fixes.

## Utility Script

- Script: `scripts/verify_cursor_layout.py`
- Purpose: detect `.mdc` files outside `.cursor/rules/` and command markdown outside `.cursor/commands/`

## Output Format

- `Status`: PASS/FAIL
- `Violations`: list of failing paths
- `Next actions`: exact path corrections
