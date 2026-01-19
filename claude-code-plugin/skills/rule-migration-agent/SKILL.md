---
name: rule-migration-agent
description: Instructions for converting between Cursor rules and Claude Skills
globs: "**/.cursor/rules/**/*", "**/.claude/skills/**/*"
---
# Rule Migration Agent

When editing files matching `.cursor/rules/` or `.claude/skills/`, follow these conversion guidelines:

## Cursor Rule Format (.cursor/rules/*.mdc)

```markdown
---
description: Brief description of what this rule does
globs: ["**/*.ts", "**/*.tsx"]
alwaysApply: false
---

# Rule Title

Content with instructions for the AI...
```

## Claude Skill Format (.claude/skills/*.md)

```markdown
---
description: Brief description of what this skill does
globs: "**/*.ts", "**/*.tsx"
---

# Skill Title

Content with instructions for the AI...
```

## Conversion Rules

### Cursor → Claude
1. Change extension from `.mdc` to `.md`
2. Convert `globs` array to comma-separated string
3. Remove `alwaysApply` field (not used in Claude)
4. Keep description and content as-is

### Claude → Cursor
1. Change extension from `.md` to `.mdc`
2. Convert `globs` string to array format
3. Add `alwaysApply: false` if needed
4. Keep description and content as-is

## Tips
- Both formats use YAML frontmatter
- The `globs` field determines when the rule/skill activates
- Content should be clear instructions for the AI assistant
