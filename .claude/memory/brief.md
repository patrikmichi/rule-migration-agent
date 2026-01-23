# Rule Migration Agent: Project Brief

> Convert between Cursor rules and Claude Skills

## Purpose

Convert rule formats between different AI coding assistants. Support migration from Cursor to Claude and vice versa.

## Key Responsibilities

- Convert Cursor rules → Claude Skills
- Convert Claude Skills → Cursor rules
- Generate AGENTS.md documentation
- Batch conversion support

## Supported Formats

| Source | Target |
|--------|--------|
| `.cursor/rules/` | `.claude/skills/` |
| `.claude/skills/` | `.cursor/rules/` |

## Output

- Converted rules/skills in target format
- AGENTS.md when both formats exist
- Migration state tracking

---

_Last updated: 2026-01-22_
