# AGENTS.md

## Project Overview

Excalidraw is an open-source, collaborative virtual whiteboard for sketching hand-drawn-like diagrams. Built with React and TypeScript, it uses a custom Canvas 2D rendering engine and custom state management via `actionManager`.

## Tech Stack

- **Language**: TypeScript (strict mode)
- **UI**: React 19 (functional components, hooks only)
- **Build**: Vite
- **Testing**: Vitest + React Testing Library
- **Package Manager**: Yarn 1.x with workspaces
- **Linting**: ESLint + Prettier

## Project Structure

```
excalidraw-monorepo/
├── excalidraw-app/        # Vite-based web application
├── packages/
│   ├── excalidraw/        # Core library (@excalidraw/excalidraw)
│   │   ├── components/    # React UI components
│   │   ├── actions/       # State actions (actionManager)
│   │   ├── renderer/      # Canvas rendering pipeline
│   │   ├── scene/         # Scene management
│   │   └── types.ts       # Core type definitions (AppState)
│   ├── math/              # Math utilities (points, angles, vectors)
│   ├── element/           # Element types and operations
│   ├── common/            # Shared utilities
│   └── utils/             # General utilities
├── examples/              # Usage examples (Next.js, browser script)
└── dev-docs/              # Developer documentation
```

## Key Commands

- `yarn` — install dependencies
- `yarn start` — start dev server (excalidraw-app)
- `yarn build` — build the app
- `yarn test:app` — run Vitest tests
- `yarn test:typecheck` — TypeScript type checking
- `yarn test:code` — ESLint
- `yarn test:other` — Prettier check
- `yarn test:all` — run all checks
- `yarn fix` — auto-fix linting and formatting

## Architecture

- **State Management**: custom `actionManager` (NOT Redux/Zustand/MobX). State updates via `actionManager.dispatch()` only. State type: `AppState` in `packages/excalidraw/types.ts`.
- **Rendering**: Canvas 2D rendering via custom engine (NOT React DOM for drawing). Pipeline: Scene -> `renderScene()` -> canvas 2D context.
- **Monorepo**: Yarn workspaces with `@excalidraw/*` package aliases defined in `tsconfig.json`.

## Conventions

- Functional components with hooks only (no class components)
- Named exports only (no default exports)
- Props type: `{ComponentName}Props`
- Colocated tests: `ComponentName.test.tsx`
- TypeScript strict mode — no `any`, no `@ts-ignore`
- SCSS modules or CSS custom properties for styling
- kebab-case for utility files, PascalCase for components

## Skills

Available skills in this project (`agents/skills/`):

- **rules-governor** (`agents/skills/rules-governor/`) — Audits planned/current changes against AI governance and Cursor placement rules.
- **pr-file-router** (`agents/skills/pr-file-router/`) — Validates PR file placement for Cursor assets, with automation script at `agents/skills/pr-file-router/scripts/verify_cursor_layout.py`.
- **branch-safety** (`agents/skills/branch-safety/`) — Checks branch/remote safety for fork workflows before commit/push.

### Skills authoring notes

- Every skill must contain a valid `SKILL.md` with `name` and `description` frontmatter.
- Use `scripts/` for executable automation when a task is repeatable.
- Use `references/` for optional, on-demand docs that should not always load.
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
