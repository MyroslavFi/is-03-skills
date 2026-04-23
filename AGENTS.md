# AGENTS.md

## Purpose

Repository-level instructions for coding agents working in this project.

## Skills

Project skills are stored in `agents/skills/` and should be used when their trigger conditions match the user request.

### `rules-governor`

- Location: `agents/skills/rules-governor/`
- Use for: rule compliance reviews, Cursor file placement checks, and governance validation.
- Includes on-demand reference docs in `references/rule-checklist.md`.

### `pr-file-router`

- Location: `agents/skills/pr-file-router/`
- Use for: verifying PR file placement for Cursor rule and command assets.
- Includes executable automation in `scripts/verify_cursor_layout.py`.

### `branch-safety`

- Location: `agents/skills/branch-safety/`
- Use for: fork/remote safety checks before commits and pushes.
- Focuses on branch tracking, remote mapping, and safe push commands.

## Maintenance

- Keep each skill directory self-contained with a valid `SKILL.md`.
- Use lowercase hyphenated skill names.
- Add scripts only when they automate a repeatable task.
- Add references when detailed docs are useful but not always required.
