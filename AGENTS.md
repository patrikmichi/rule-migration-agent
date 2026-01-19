# AGENTS

## Cursor Agent

- **Rules:** `.cursor/rules/` - Folder-based format with `RULE.md` files
- **Commands:** `.cursor/commands/` - Slash command definitions (`.md` files)
- Format: Rules use YAML frontmatter with `description`, `globs`, `alwaysApply`
- Used by Cursor for context attachments based on file patterns, manual invocations, etc.

## Claude Agent

- **Skills:** `.claude/skills/` - Each Skill is a folder with `SKILL.md` file
- **Commands:** `.claude/commands/` - Slash command definitions (`.md` files)
- Required fields: `name`, `description` (in SKILL.md frontmatter)
- Optional fields: `allowed-tools`, `model`, etc.
- Description is used to trigger skill usage; instructions in markdown content

## Shared Guidelines

- Ensure rule/skill names are consistent and descriptive
- Keep Skill frontmatter descriptions aligned with Cursor rule descriptions
- Examples should be preserved across formats where relevant
- Where behavior differs (e.g. automatic vs explicit invocation), clarify in instructions
- Commands are shared between both agents - keep them in sync

## Migration

To migrate between formats, use the rule-migration-agent:
- Cursor → Claude: Converts `.cursor/rules/*/RULE.md` to `.claude/skills/*/SKILL.md`
- Claude → Cursor: Converts `.claude/skills/*/SKILL.md` to `.cursor/rules/*/RULE.md`
- Commands: Automatically synced to both `.cursor/commands/` and `.claude/commands/` when both agents are present
