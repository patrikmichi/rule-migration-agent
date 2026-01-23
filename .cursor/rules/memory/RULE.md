---
description: Instructions for maintaining and using the memory files in .cursor/memory
globs:
- .cursor/memory/**/*
---

# Cursor Memory Management

This rule ensures that Cursor maintains a persistent memory of the project state, decisions, and task progress, matching the capabilities of the Claude agent.

## Memory Files

- **[.cursor/memory/brief.md](file:///Users/patrikmichalicka/Desktop/projects/agents/rule-migration-agent/.cursor/memory/brief.md)**: High-level project goal, purpose, and key responsibilities.
- **[.cursor/memory/decisions.md](file:///Users/patrikmichalicka/Desktop/projects/agents/rule-migration-agent/.cursor/memory/decisions.md)**: Log of locked-in technical and architectural decisions.
- **[.cursor/memory/summaries/current.md](file:///Users/patrikmichalicka/Desktop/projects/agents/rule-migration-agent/.cursor/memory/summaries/current.md)**: Concise summaries of recent tasks.

## Usage Guidelines

1. **Read on Start**: Always read these files at the beginning of a session to understand the project's current state and constraints.
2. **Update on Completion**: When a significant task is completed, update `summaries/current.md` with a concise factual summary.
3. **Log Decisions**: When an architectural or configuration decision is reached, log it in `decisions.md`.
4. **Maintain Parity**: If you modify these files in Cursor, ensure the corresponding files in `.claude/memory/` are also updated (and vice-versa).
