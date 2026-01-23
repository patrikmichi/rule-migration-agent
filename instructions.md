# Rule Migration Agent Plugin Instructions

This is a Claude Code plugin that provides commands and instructions for converting between Cursor rules and Claude Skills.

## Plugin Overview

This plugin extends Claude Code with:
- **Commands**: `/migrate` and `/setup` for rule migration workflows
- **Instructions**: Detailed guidance on converting between Cursor rules and Claude Skills formats
- **Python Tools**: Migration scripts that handle bidirectional conversion
- **Persistent Memory**: Shared context tracking across platforms (`brief.md`, `decisions.md`)

## Plugin Commands

- `/migrate [project-path] [options]` - Convert between Cursor rules and Claude Skills
- `/setup` - Install and configure the agent (Python, dependencies, configuration)

**Important**: This plugin provides commands and skills (Markdown files). The Python tools are installed separately via the `/setup` command, which:
1. Tries to install via pip (if published to PyPI)
2. Falls back to cloning from GitHub: https://github.com/patrikmichi/rule-migration-agent
3. Runs the setup script to install dependencies

When users invoke `/migrate`, locate and execute the installed `migrate.py` script from the installation location.

## Purpose

The Rule Migration Agent handles bidirectional conversion between Cursor rules (`.cursor/rules`) and Claude Skills (`.claude/skills`). It ensures rules and skills stay synchronized across both platforms, fetches the latest documentation to maintain compliance, and automatically generates `AGENTS.md` when both formats are present.

## Responsibilities

1. **Fetch latest documentation** from official sources before any conversion
2. **Convert Cursor rules → Claude Skills** (`.cursor/rules/*.mdc` → `.claude/skills/*/SKILL.md`)
3. **Convert Claude Skills → Cursor rules** (`.claude/skills/*/SKILL.md` → `.cursor/rules/*.mdc`)
4. **Maintain Persistent Memory** Sync `brief.md` and `decisions.md` between platforms
5. **Generate AGENTS.md** when both `.cursor/rules` and `.claude/skills` folders exist
6. **Validate conversions** to ensure compliance with latest format specifications
7. **Handle legacy migration** Transform `.claude/commands/` to skills with `user-invocable: true`
8. **Handle conflicts** and preserve existing content when appropriate

## Documentation Sources

**ALWAYS fetch latest documentation before conversions:**

1. **Cursor Rules Documentation:**
   - URL: `https://cursor.com/docs/context/rules`
   - Used for: Understanding Cursor rule format, frontmatter fields, globs, alwaysApply, rule types

2. **Claude Skills Documentation:**
   - URL: `https://code.claude.com/docs/en/skills`
   - Used for: Understanding SKILL.md format, required fields (name, description), optional fields (allowed-tools, model), naming constraints

**Fetch these docs at the start of every migration operation to ensure compliance with latest specifications.**

## Conversion Workflows

### Cursor Rules → Claude Skills

**Input:** `.cursor/rules/*.mdc` or `.cursor/rules/*/RULE.md` files

**Output:** `.claude/skills/<skill-name>/SKILL.md` files

**Mapping:**
- **Rule filename/folder name** → Skill directory name + `name:` in frontmatter (normalize to lowercase, hyphens)
- **`description:` frontmatter** → `description:` in SKILL.md (enhance with trigger terms for Claude)
- **`globs:` patterns** → Include in description: "Use when editing files matching `glob XYZ`"
- **`alwaysApply: true`** → Include "always active" or broad triggers in description
- **Rule body content** → Instructions section in SKILL.md (preserve structure, examples, references)
- **`@filename` references** → Preserve or include content in Skill instructions

**Process:**
1. Fetch latest Claude Skills documentation
2. Scan `.cursor/rules/` for `.mdc` files and rule folders
3. Parse frontmatter (YAML) and body content
4. Normalize skill name (lowercase, hyphens, no reserved words)
5. Create `.claude/skills/<skill-name>/` directory
6. Generate `SKILL.md` with:
   - YAML frontmatter: `name:`, `description:` (required)
   - Optional fields if applicable: `allowed-tools`, `model`, etc.
   - Markdown body with instructions, examples, best practices
7. Validate: Check name constraints, description length (<1024 chars), valid YAML

### Claude Skills → Cursor Rules

**Input:** `.claude/skills/*/SKILL.md` files

**Output:** `.cursor/rules/*.mdc` files

**Mapping:**
- **Skill directory name** → Rule filename (`.mdc` extension)
- **`name:` frontmatter** → Rule identifier
- **`description:` frontmatter** → `description:` in rule frontmatter
- **Description triggers/patterns** → Extract `globs:` patterns if file patterns mentioned
- **Skill instructions** → Rule body content (preserve structure)
- **Examples** → Include in rule body

**Process:**
1. Fetch latest Cursor Rules documentation
2. Scan `.claude/skills/` for Skill directories
3. Read `SKILL.md` from each directory
4. Parse YAML frontmatter and instructions
5. Extract metadata:
   - `description:` → rule description
   - Analyze description for file patterns → `globs:` array
   - Determine `alwaysApply:` based on description (if mentions "always" or broad triggers)
6. Generate `.mdc` file in `.cursor/rules/` with:
   - YAML frontmatter: `description:`, `globs:` (if applicable), `alwaysApply:`
   - Markdown body with instructions and examples
7. Validate: Check frontmatter format, valid YAML

## Unified Memory System

The agent maintains shared state across both platforms to ensure context continuity.

### Memory Structure
- **`.cursor/memory/`** & **`.claude/memory/`**: Mirror directories for project state
- **`brief.md`**: Project-level goals and high-level responsibilities (Synced)
- **`decisions.md`**: Log of architectural and technical decisions (Synced)
- **`summaries/current.md`**: Brief factual summaries of recent work (Local only)

### Sync Logic
- When running `/migrate` or `migrate.py`, the agent detects changes in `brief.md` or `decisions.md`.
- Changes from the most recently modified platform are synced to the other.
- The `MigrationStateManager` tracks file hashes to ensure accurate synchronization.

## AGENTS.md Generation

**When both folders exist:**
- `.cursor/rules/` folder exists AND
- `.claude/skills/` folder exists

**Action:** Create or update `AGENTS.md` in project root

**Content Structure:**
```markdown
# AGENTS

## Cursor Agent

- Lives in `.cursor/rules/`
- Format: `.mdc` files with YAML frontmatter
- Metadata: `description`, `globs`, `alwaysApply`
- Used by Cursor for context attachments based on file patterns, manual invocations, etc.

## Claude Agent

- Lives in `.claude/skills/`
- Format: Each Skill is a folder with `SKILL.md` file
- Required fields: `name`, `description` (in SKILL.md frontmatter)
- Optional fields: `allowed-tools`, `model`, etc.
- Description is used to trigger skill usage; instructions in markdown content

## Shared Guidelines

- Ensure rule/skill names are consistent and descriptive
- Keep Skill frontmatter descriptions aligned with Cursor rule descriptions
- Examples should be preserved across formats where relevant
- Where behavior differs (e.g. automatic vs explicit invocation), clarify in instructions

## Migration

To migrate between formats, use the rule-migration-agent:
- Cursor → Claude: Converts `.cursor/rules/*.mdc` to `.claude/skills/*/SKILL.md`
- Claude → Cursor: Converts `.claude/skills/*/SKILL.md` to `.cursor/rules/*.mdc`
```

## Usage

### Plugin Commands

Users can invoke the plugin via slash commands:
- `/migrate [project-path] [options]` - Run migration
- `/setup` - Set up the agent

### Command Format

When executing migrations, run the Python script from the plugin directory:

```bash
python migrate.py <project-path> [options]
```

Or if the plugin is installed in a different location, adjust the path accordingly.

**Options:**
- `--cursor-to-claude` - Convert Cursor rules to Claude Skills
- `--claude-to-cursor` - Convert Claude Skills to Cursor rules
- `--both` - Convert both directions (default if both folders exist)
- `--force` - Overwrite existing files without confirmation
- `--dry-run` - Show what would be converted without making changes
- `--skip-existing` - Skip files that already exist

### Examples

**Convert Cursor rules to Claude Skills:**
```bash
python agents/rule-migration-agent/migrate.py /path/to/project --cursor-to-claude
```

**Convert Claude Skills to Cursor rules:**
```bash
python agents/rule-migration-agent/migrate.py /path/to/project --claude-to-cursor
```

**Auto-detect and convert both (if both folders exist):**
```bash
python agents/rule-migration-agent/migrate.py /path/to/project --both
```

**Dry run to preview changes:**
```bash
python agents/rule-migration-agent/migrate.py /path/to/project --both --dry-run
```

## File Format Specifications

### Cursor Rule Format (.mdc)

```markdown
---
description: "Rule description"
globs: ["pattern/**/*", "**/*.ts"]
alwaysApply: false
---

# Rule Title

Rule content here...
```

**Frontmatter fields:**
- `description:` (string) - Required
- `globs:` (array of strings) - Optional, file patterns
- `alwaysApply:` (boolean) - Optional, default false

### Claude Skill Format (SKILL.md)

```markdown
---
name: skill-name
description: "Skill description that explains what it does and when to use it"
allowed-tools: []  # Optional
model: claude-3-5-sonnet-20241022  # Optional
---

# Skill Title

Skill instructions here...
```

**Frontmatter fields:**
- `name:` (string) - Required, lowercase, hyphens, no reserved words
- `description:` (string) - Required, <1024 chars, should include trigger terms
- `allowed-tools:` (array) - Optional
- `model:` (string) - Optional

## Validation Rules

### Cursor Rules
- ✅ Valid YAML frontmatter
- ✅ `description:` field present
- ✅ Valid Markdown body
- ✅ `globs:` is array if present
- ✅ `alwaysApply:` is boolean if present

### Claude Skills
- ✅ Valid YAML frontmatter
- ✅ `name:` field present and valid (lowercase, hyphens, no reserved words)
- ✅ `description:` field present and <1024 characters
- ✅ Valid Markdown body
- ✅ Skill directory name matches `name:` field

## Conflict Resolution

**When converting and target already exists:**

1. **If `--force` flag:** Overwrite existing file
2. **If `--skip-existing` flag:** Skip and report
3. **Otherwise:** 
   - Show diff between existing and new
   - Ask user for confirmation
   - Optionally create backup before overwriting

**When both formats exist for same rule/skill:**

- Detect by matching `description:` or normalized name
- Warn user about potential duplicates
- Suggest merging or keeping both with different names

## Error Handling

### Documentation Fetch Failures
- If docs can't be fetched, use cached/known format specs
- Warn user that conversion may not be fully compliant with latest format
- Continue with conversion using known specifications

### Parsing Errors
- Report which file failed to parse
- Show error details
- Skip problematic files and continue with others
- Suggest fixes if possible

### Validation Errors
- List all validation failures
- Suggest corrections
- Optionally auto-fix common issues (with user confirmation)

## Best Practices

1. **Always fetch latest docs** before conversion
2. **Preserve content structure** - maintain examples, code blocks, references
3. **Normalize names consistently** - use same normalization for both directions
4. **Enhance descriptions** - add trigger terms for Claude Skills when converting from Cursor
5. **Validate after conversion** - check output files meet format requirements
6. **Create backups** - optionally backup existing files before overwriting
7. **Report changes** - show summary of what was converted, created, updated

## Related Documentation

- Cursor Rules: https://cursor.com/docs/context/rules
- Claude Skills: https://code.claude.com/docs/en/skills
- `.cursor/rules/rule-migration-agent.mdc` - Cursor rule for this agent
