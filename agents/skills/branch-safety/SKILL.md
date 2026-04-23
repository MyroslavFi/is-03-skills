---
name: branch-safety
description: Enforces safe git branch and remote verification before commit or push operations. Use when the user asks about forks, remotes, branch tracking, or push safety checks.
---

# Branch Safety

## Instructions

1. Before commit/push guidance, check:
   - `git status -sb`
   - `git remote -v`
   - current branch tracking target
2. Confirm push destination is the intended remote, especially fork workflows:
   - `origin` should point to user fork when contributing upstream
   - `upstream` should point to original repository
3. Recommend explicit push commands:
   - `git push origin <branch>`
4. Highlight risky states:
   - detached HEAD
   - wrong remote mapping
   - no upstream tracking branch
5. Return a short actionable checklist users can run before every push.

## Output Format

- `Current state`: branch + remote summary
- `Risks`: bullet list
- `Safe commands`: exact commands for user to run
