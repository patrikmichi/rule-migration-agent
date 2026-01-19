---
description: Convert between Cursor rules and Claude Skills
argument-hint: [--cursor-to-claude|--claude-to-cursor|--both]
---
# Migrate Rules and Skills

Convert between Cursor rules (`.cursor/rules/`) and Claude Skills (`.claude/skills/`).

## Instructions

When the user runs this command, you should execute the Python migration tool. Follow these steps:

### Step 1: Find the Installed Migration Tool

Locate the `migrate.py` script. Try these locations in order:

1. **Check if installed via pip:**
   ```bash
   python3 -m rule_migration_agent --help 2>/dev/null
   which migrate.py
   ```

2. **Check common installation locations:**
   ```bash
   ls ~/.local/share/rule-migration-agent/migrate.py 2>/dev/null
   ls ~/rule-migration-agent/migrate.py 2>/dev/null
   ls ./rule-migration-agent/migrate.py 2>/dev/null
   ls ./migrate.py 2>/dev/null
   ```

3. **If not found, prompt user to run `/setup` first**

### Step 2: Determine Project Path

- If user provided a path: use `$ARGUMENTS` or `$1` as the project path
- If no path provided: use current directory (`.`)

### Step 3: Parse Arguments

Extract any flags from the command:
- `--cursor-to-claude`: Convert Cursor → Claude
- `--claude-to-cursor`: Convert Claude → Cursor  
- `--both`: Sync both directions
- `--dry-run`: Preview changes
- `--force`: Overwrite without confirmation
- Other flags: pass through to migrate.py

### Step 4: Execute the Migration

Run the Python script with the determined path and arguments:

```bash
# If installed via pip
python3 -m rule_migration_agent [project-path] [flags]

# If installed from GitHub
python3 ~/.local/share/rule-migration-agent/migrate.py [project-path] [flags]

# If found in current directory
python3 [path-to-migrate.py] [project-path] [flags]
```

### Step 5: Report Results

- Show the output from the migration script
- List converted files
- Show any errors or warnings
- Suggest next steps if needed

## What the Migration Tool Does

The `migrate.py` script automatically:
- Detects existing formats (`.cursor/rules/` or `.claude/skills/`)
- Converts between formats based on arguments or auto-detection
- Validates output to ensure compliance
- Handles conflicts and shows diffs
- Tracks state to skip unchanged files

## If Tool Not Found

If `migrate.py` cannot be found:
1. **Prompt user to run setup first:**
   ```
   The migration tool is not installed. Please run:
   /setup
   ```
2. **Or provide manual installation instructions**

## Format Reference

### Cursor Rule Format (.mdc)
```markdown
---
description: What this rule does
globs: ["**/*.ts", "**/*.tsx"]
alwaysApply: false
---

# Rule Title

Rule content and instructions...
```

### Claude Skill Format (.md)
```markdown
---
description: What this skill does
globs: "**/*.ts", "**/*.tsx"
---

# Skill Title

Skill content and instructions...
```

## Key Differences
- Cursor uses `.mdc` extension, Claude uses `.md`
- Cursor globs is an array, Claude globs is comma-separated string
- Cursor has `alwaysApply`, Claude doesn't use it
