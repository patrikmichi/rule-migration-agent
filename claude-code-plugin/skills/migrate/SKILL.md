---
name: migrate
user-invocable: true
description: "Command: migrate"
---

# Migrate Rules and Skills

Convert between Cursor rules (`.cursor/rules`) and Claude Skills (`.claude/skills`).

## Usage

```
/migrate [project-path] [options]
```

## What it does

- ✅ **Auto-detects direction** - Converts based on what exists in the project
- ✅ **Fetches latest docs** - Gets current format specifications
- ✅ **Validates output** - Ensures compliance with format requirements
- ✅ **Handles conflicts** - Shows diffs and manages file conflicts
- ✅ **Generates AGENTS.md** - Creates documentation when both formats exist

## Arguments

- `[project-path]` - Path to project/repo (defaults to current directory if omitted)

## Options

- `--cursor-to-claude` - Convert Cursor rules → Claude Skills
- `--claude-to-cursor` - Convert Claude Skills → Cursor rules
- `--both` - Convert both directions (sync)
- `--force` - Overwrite existing files without confirmation
- `--dry-run` - Preview changes without making them
- `--auto-backup` - Create backup before overwriting
- `--check-sync` - Check sync status without converting

## Examples

**Basic migration (auto-detect):**
```
/migrate
/migrate ~/projects/my-app
```

**Convert Cursor → Claude:**
```
/migrate ~/projects/my-app --cursor-to-claude
```

**Convert Claude → Cursor:**
```
/migrate ~/projects/my-app --claude-to-cursor
```

**Sync both directions:**
```
/migrate ~/projects/my-app --both
```

**Preview changes:**
```
/migrate ~/projects/my-app --both --dry-run
```

**Safe migration with backup:**
```
/migrate ~/projects/my-app --both --auto-backup
```

**Check sync status:**
```
/migrate ~/projects/my-app --check-sync
```

## What happens

1. **Validates project path** - Checks that the path exists and is safe
2. **Detects formats** - Finds `.cursor/rules` and `.claude/skills` directories
3. **Fetches documentation** - Downloads latest format specs from official sources
4. **Parses files** - Reads existing rules/skills
5. **Converts** - Transforms between formats with proper mapping
6. **Validates** - Checks output meets format requirements
7. **Handles conflicts** - Shows diffs, creates backups, or asks for confirmation
8. **Generates AGENTS.md** - Creates documentation if both formats exist
9. **Reports summary** - Shows what was converted, errors, warnings

## Output

- **Converted files** - New or updated rules/skills in target format
- **AGENTS.md** - Auto-generated when both formats exist
- **Backup files** - Created if `--auto-backup` is used
- **State files** - `.migration-state.json`, `.migration-history.json`

## Common Workflows

**First-time migration:**
```
/migrate ~/projects/my-app --cursor-to-claude
```

**Keep both formats in sync:**
```
/migrate ~/projects/my-app --both --auto-backup
```

**Preview before converting:**
```
/migrate ~/projects/my-app --both --dry-run
```

**Check if sync is needed:**
```
/migrate ~/projects/my-app --check-sync
```

## Related Commands

- `/setup` - Install and configure the agent first

## Notes

- Run `/setup` first if you haven't installed the agent
- Use `--dry-run` to preview changes safely
- Use `--auto-backup` for safe migrations
- The agent tracks state and skips unchanged files automatically

