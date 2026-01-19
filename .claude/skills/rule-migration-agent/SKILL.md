---
name: rule-migration-agent
description: "Instructions for the rule-migration-agent that converts between Cursor rules and Claude Skills. Use when editing files matching `agents/rule-migration-agent/**/*`, `**/.cursor/rules/**/*`, `**/.claude/skills/**/*`."
---

# Rule Migration Agent

## Purpose

The rule-migration-agent handles bidirectional conversion between Cursor rules (`.cursor/rules`) and Claude Skills (`.claude/skills`). It ensures rules and skills stay synchronized across both platforms.

## When to Use

- User asks to convert rules between Cursor and Claude formats
- User wants to migrate a project from one format to another
- User needs to sync rules and skills across both platforms
- User asks to generate AGENTS.md for a project with both formats

## Agent Location

**Location:** `agents/rule-migration-agent/`

**Script:** `agents/rule-migration-agent/migrate.py`

**Instructions:** `agents/rule-migration-agent/instructions.md`

## Usage

### Basic Usage

The agent takes a project/repo path and automatically detects what to convert:

```bash
python agents/rule-migration-agent/migrate.py <project-path>
```

### Specific Conversions

**Convert Cursor rules to Claude Skills:**
```bash
python agents/rule-migration-agent/migrate.py <project-path> --cursor-to-claude
```

**Convert Claude Skills to Cursor rules:**
```bash
python agents/rule-migration-agent/migrate.py <project-path> --claude-to-cursor
```

**Convert both directions:**
```bash
python agents/rule-migration-agent/migrate.py <project-path> --both
```

### Options

- `--force` - Overwrite existing files without confirmation
- `--dry-run` - Show what would be converted without making changes
- `--skip-existing` - Skip files that already exist

## Key Features

1. **Always fetches latest documentation** from:
   - `https://cursor.com/docs/context/rules` (Cursor rules format)
   - `https://code.claude.com/docs/en/skills` (Claude Skills format)

2. **Automatic detection:**
   - If both `.cursor/rules` and `.claude/skills` exist → converts both directions
   - If only one exists → converts to the other format
   - Automatically generates `AGENTS.md` when both folders are present

3. **Format conversion:**
   - Cursor `RULE.md` files (in rule folders) → Claude `SKILL.md` files (in skill folders)
   - Claude `SKILL.md` files (in skill folders) → Cursor `RULE.md` files (in rule folders)
   - Preserves content, examples, and structure
   - Maps metadata fields appropriately

## Conversion Mapping

### Cursor → Claude
- Rule filename → Skill directory name (normalized)
- `description:` → `description:` (enhanced with triggers)
- `globs:` → Included in description
- `alwaysApply:` → "always active" in description
- Rule body → Skill instructions

### Claude → Cursor
- Skill directory name → Rule filename
- `name:` → Rule identifier
- `description:` → `description:` (extracts globs if mentioned)
- Skill instructions → Rule body

## AGENTS.md Generation

When both `.cursor/rules` and `.claude/skills` folders exist, the agent automatically creates/updates `AGENTS.md` in the project root with:
- Instructions for Cursor agent
- Instructions for Claude agent
- Shared guidelines
- Migration instructions

## Workflow

1. **User specifies project path**
   - Agent validates path exists
   - Checks for `.cursor/rules` and `.claude/skills` folders

2. **Fetch latest documentation**
   - Downloads Cursor Rules docs
   - Downloads Claude Skills docs
   - Uses cached version if fetch fails

3. **Detect conversion direction**
   - Auto-detect based on what exists
   - Or use explicit flags (`--cursor-to-claude`, `--claude-to-cursor`, `--both`)

4. **Parse existing files**
   - Read Cursor rules (`RULE.md` files in rule folders)
   - Read Claude Skills (`SKILL.md` files in skill folders)

5. **Convert and validate**
   - Convert to target format
   - Validate output meets format requirements
   - Handle conflicts (skip, overwrite, or ask)

6. **Generate AGENTS.md** (if both folders exist)
   - Create/update `AGENTS.md` with instructions for both agents

7. **Report summary**
   - Show what was converted
   - List created/updated files
   - Report any errors or warnings

## Examples

**User says:** "Convert rules in feedbot project to Claude Skills"
**Action:** Run `python agents/rule-migration-agent/migrate.py feedbot --cursor-to-claude`

**User says:** "Migrate this project from Claude to Cursor"
**Action:** Run `python agents/rule-migration-agent/migrate.py <project-path> --claude-to-cursor`

**User says:** "Sync rules and skills in this repo"
**Action:** Run `python agents/rule-migration-agent/migrate.py <project-path> --both`

**User says:** "Generate AGENTS.md for this project"
**Action:** Check if both folders exist, then run migration with `--both` to trigger AGENTS.md generation

## Error Handling

- **Documentation fetch fails:** Continue with known format specs, warn user
- **Parse errors:** Report which file failed, skip and continue
- **Validation errors:** List all failures, suggest fixes
- **File conflicts:** Show diff, ask for confirmation (unless `--force`)

## Related Files

- `agents/rule-migration-agent/instructions.md` - Complete agent instructions
- `agents/rule-migration-agent/migrate.py` - Migration script
- `agents/rule-migration-agent/requirements.txt` - Python dependencies
