---
name: rules-governor
description: Audits planned or existing changes against repository AI governance files and rule placement policies. Use when the user asks to verify rule compliance, organize Cursor files, or review whether files are in correct .cursor folders.
---

# Rules Governor

## Instructions

1. Read repository policy files first:
   - `AGENTS.md`
   - `.cursor/rules/README.md` (if present)
   - `.cursor/rules/*.mdc` and `.cursor/commands/*.md` as needed
2. Classify each relevant file into one bucket:
   - Cursor rule (`.mdc`) -> `.cursor/rules/`
   - Cursor command (`.md`) -> `.cursor/commands/`
   - Other repository documentation -> root/docs location
3. Report issues as concrete violations with exact file paths.
4. Provide minimal fixes, ordered by impact.
5. If no violations exist, explicitly state that placement/compliance is valid.

## Output Format

- `Violations`: bullet list with path and reason
- `Suggested fixes`: bullet list with exact move/create action
- `Result`: `PASS` or `FAIL`

## Additional Resources

- For detailed compliance criteria, read [references/rule-checklist.md](references/rule-checklist.md)
