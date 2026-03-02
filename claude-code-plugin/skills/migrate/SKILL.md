---
name: migrate
description: Convert between Cursor rules and Claude Skills. Auto-detects direction, fetches latest docs, validates output, and handles conflicts.
disable-model-invocation: true
argument-hint: "[project-path] [--cursor-to-claude | --claude-to-cursor | --both] [--dry-run] [--auto-backup]"
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - WebFetch
  - Task
---

# Migrate Rules and Skills

Convert between Cursor rules (`.cursor/rules`) and Claude Skills (`.claude/skills`).

## Instructions

When the user runs `/migrate $ARGUMENTS`:

1. **Validate project path** - Use the first argument as project path (default: current directory)
2. **Detect formats** - Check for `.cursor/rules`, `.cursor/commands`, and `.claude/skills` directories
3. **Fetch latest docs** from:
   - `https://cursor.com/docs/context/rules` (Cursor rules format)
   - `https://code.claude.com/docs/en/skills` (Claude Skills format)
4. **Parse existing files** - Read all RULE.md, SKILL.md, and command .md files
5. **Convert** between formats with proper metadata mapping
6. **Validate** output meets format requirements
7. **Handle conflicts** - Show diffs, create backups, or ask for confirmation
8. **Generate AGENTS.md** if both formats exist
9. **Report summary** of what was converted

## Options

- `--cursor-to-claude` - Convert Cursor rules/commands to Claude Skills
- `--claude-to-cursor` - Convert Claude Skills to Cursor rules/commands
- `--both` - Sync both directions
- `--force` - Overwrite without confirmation
- `--dry-run` - Preview changes only
- `--auto-backup` - Create backup before overwriting
- `--check-sync` - Check sync status without converting

## Conversion Mapping

### Cursor to Claude
- `.cursor/commands/*.md` → `.claude/skills/<name>/SKILL.md` (user-invocable, `/slash-command`)
- `.cursor/rules/<name>/RULE.md` → `.claude/skills/<name>/SKILL.md` with `user-invocable: false` (background knowledge)
- `description:` maps to `description:` (enhanced with triggers)
- `globs:` included in description
- `alwaysApply:` becomes "always active" note in description

### Claude to Cursor
- `.claude/skills/` with `user-invocable: true` or not set → `.cursor/commands/<name>.md` (slash command)
- `.claude/skills/` with `user-invocable: false` → `.cursor/rules/<name>/RULE.md` (background knowledge)
- `name:` becomes rule/command identifier
- `description:` maps to `description:`

## Examples

```
/migrate                                          # auto-detect direction
/migrate ~/projects/my-app --cursor-to-claude     # one direction
/migrate ~/projects/my-app --both --auto-backup   # sync with backup
/migrate ~/projects/my-app --both --dry-run       # preview only
/migrate ~/projects/my-app --check-sync           # check status
```

## Notes

- Run `/setup` first if you haven't installed the agent
- Use `--dry-run` to preview changes safely
- The agent tracks state and skips unchanged files automatically
