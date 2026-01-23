---
name: memory
description: Instructions for maintaining and using the memory files in .claude/memory
user-invocable: false
---

# Claude Memory Management

This skill ensures that Claude maintains a persistent memory of the project state, decisions, and task progress.

## Memory Files

- **[.claude/memory/brief.md](file:///Users/patrikmichalicka/Desktop/projects/agents/rule-migration-agent/.claude/memory/brief.md)**: High-level project goal, purpose, and key responsibilities.
- **[.claude/memory/decisions.md](file:///Users/patrikmichalicka/Desktop/projects/agents/rule-migration-agent/.claude/memory/decisions.md)**: Log of locked-in technical and architectural decisions.
- **[.claude/memory/summaries/current.md](file:///Users/patrikmichalicka/Desktop/projects/agents/rule-migration-agent/.claude/memory/summaries/current.md)**: Concise summaries of recent tasks.

## Usage Guidelines

1. **Read on Start**: Always read these files at the beginning of a session to understand the project's current state and constraints.
2. **Update on Completion**: When a significant task is completed, update `summaries/current.md` with a concise factual summary.
3. **Log Decisions**: When an architectural or configuration decision is reached, log it in `decisions.md`.
4. **Maintain Parity**: If you modify these files in Claude, ensure the corresponding files in `.cursor/memory/` are also updated (and vice-versa).
