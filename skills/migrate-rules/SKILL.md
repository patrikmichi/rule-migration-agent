---
name: migrate-rules
description: Convert between Cursor rules and Claude Skills. Handles bidirectional conversion with proper command/rule distinction.
user-invocable: false
allowed-tools:
  - Read
  - Write
  - Glob
  - Task
  - Bash
---

# Rule Migration Agent

## Purpose

The rule-migration-agent handles bidirectional conversion between Cursor rules/commands and Claude Skills. It ensures rules and skills stay synchronized across both platforms.

## When to Use

- User asks to convert rules between Cursor and Claude formats
- User wants to migrate a project from one format to another
- User needs to sync rules and skills across both platforms
- User asks to generate AGENTS.md for a project with both formats

## Usage

The agent is installed as a Python package. Run via CLI:

```bash
rule-migration <project-path> [options]
```

Or directly:

```bash
python3 -m migrate <project-path> [options]
```

### Options

- `--cursor-to-claude` - Convert Cursor rules/commands to Claude Skills
- `--claude-to-cursor` - Convert Claude Skills to Cursor rules/commands
- `--both` - Sync both directions
- `--force` - Overwrite existing files without confirmation
- `--dry-run` - Show what would be converted without making changes

## Conversion Mapping

### Cursor to Claude
- `.cursor/commands/*.md` → `.claude/skills/<name>/SKILL.md` (user-invocable, `/slash-command`)
- `.cursor/rules/<name>/RULE.md` → `.claude/skills/<name>/SKILL.md` with `user-invocable: false` (background knowledge)
- `description:` → `description:` (enhanced with triggers)
- `globs:` → Included in description
- `alwaysApply:` → "always active" in description

### Claude to Cursor
- `.claude/skills/` with `user-invocable: true` or not set → `.cursor/commands/<name>.md` (slash command)
- `.claude/skills/` with `user-invocable: false` → `.cursor/rules/<name>/RULE.md` (background knowledge)
- `name:` → Rule/command identifier
- `description:` → `description:` (extracts globs if mentioned)

## AGENTS.md Generation

When both `.cursor/rules` and `.claude/skills` folders exist, the agent automatically creates/updates `AGENTS.md` in the project root.

## Documentation Sources

Always fetches latest documentation before conversions:
- Cursor Rules: `https://cursor.com/docs/context/rules`
- Claude Skills: `https://code.claude.com/docs/en/skills`
