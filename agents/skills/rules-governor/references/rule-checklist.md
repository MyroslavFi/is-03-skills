# Rule Compliance Checklist

Use this checklist during rule/command governance reviews.

## Placement

- `.mdc` files belong in `.cursor/rules/`
- `.md` command prompts belong in `.cursor/commands/`
- AI operating guide belongs in `AGENTS.md`

## Rule Quality

- Front-matter includes `description`
- If scoped, front-matter includes `globs`
- `alwaysApply` is explicitly set
- Rule body contains actionable instructions
- Rule body includes `How to verify` when appropriate

## Command Quality

- Command prompt is task-focused and unambiguous
- Uses `$ARGUMENTS` when user input is needed
- Output expectations are explicit
- Does not conflict with repository policies
