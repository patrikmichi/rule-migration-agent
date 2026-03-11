# Rule Migration Agent — Agent Reference

Bidirectional converter between Cursor rules/commands and Claude Skills. See `CLAUDE.md` for commands and constraints.

## Project Structure

```
rule-migration-agent/
├── migrate.py          — Entry point; handles CLI flags and dispatches to converters
├── converters.py       — Core conversion logic (cursor_rule_to_claude_skill, claude_skill_to_cursor_rule)
├── parsers.py          — File parsing: YAML frontmatter, .mdc files, RULE.md, SKILL.md
├── validation.py       — Format validation for both Cursor and Claude formats
├── config.py           — Configuration and defaults
├── memory.py           — State management and SHA256 hash tracking
├── memory_commands.py  — Rollback and history commands
├── utils.py            — Shared utilities
├── install_agent.py    — Installation from source
├── pyproject.toml      — Package metadata (version 1.2.1)
├── requirements.txt    — PyYAML, requests, beautifulsoup4, tqdm, rich
├── tests/              — 39 tests
├── skills/             — Claude skills bundled with the agent
├── claude-code-plugin/ — Claude Code plugin distribution
├── docs/               — Additional documentation
├── instructions.md     — Full conversion rules, field mapping, and workflow
└── agent.md            — Agent definition and frontmatter
```

## Format Reference

### Cursor Format

| Path | Type | Frontmatter fields |
|------|------|--------------------|
| `.cursor/rules/<name>/RULE.md` or `.mdc` | Auto-attached by file pattern | `description`, `globs`, `alwaysApply` |
| `.cursor/commands/<name>.md` | User-invocable slash commands | `description` |

### Claude Format

| Path | Type | Frontmatter fields |
|------|------|--------------------|
| `.claude/skills/<name>/SKILL.md` | Auto-triggered (non-invocable) | `name`, `description`, `user-invocable: false` |
| `.claude/skills/<name>/SKILL.md` | User-invocable slash commands | `name`, `description` (`user-invocable` defaults to `true`) |

`allowed-tools` and `model` are optional Claude frontmatter fields preserved on round-trip.

## Conversion Mapping

### Cursor → Claude

| Source | Target | `user-invocable` |
|--------|--------|-----------------|
| `.cursor/rules/` (RULE.md or .mdc files) | `.claude/skills/` | `false` |
| `.cursor/commands/*.md` | `.claude/skills/` | `true` (default — field omitted) |
| Legacy `.claude/commands/*.md` | `.claude/skills/` (originals deleted) | `true` |

### Claude → Cursor

| Source | Target |
|--------|--------|
| `.claude/skills/` with `user-invocable: false` | `.cursor/rules/<name>/RULE.md` |
| `.claude/skills/` with `user-invocable: true` or unset | `.cursor/commands/<name>.md` |

Path references are rewritten during conversion (`.cursor/rules/` ↔ `.claude/skills/`).

## Key Commands

| Command | What it does |
|---------|--------------|
| `python3 migrate.py <path>` | Auto-detect direction and convert |
| `python3 migrate.py <path> --cursor-to-claude` | Rules → non-invocable skills; commands → invocable skills |
| `python3 migrate.py <path> --claude-to-cursor` | Non-invocable skills → rules; invocable skills → commands |
| `python3 migrate.py <path> --both` | Bidirectional sync |
| `python3 migrate.py <path> --dry-run` | Preview changes without writing |
| `python3 migrate.py <path> --rollback op-001` | Roll back a specific operation by ID |
| `python3 migrate.py ~/projects/* --batch --both` | Batch across multiple projects |
| `python3 -m pytest tests/ -v` | Run all 39 tests |

## State Files

| File | Location | Contents |
|------|----------|---------|
| `state.json` | `<project>/.rule-migration/state.json` | SHA256 hashes (drives `skip_unchanged`) |
| `history.json` | `<project>/.rule-migration/history.json` | Audit log with rollback operation IDs |
| Global stats | `~/.config/rule-migration-agent/` | Aggregated run statistics |
| Doc cache | `~/.cache/rule-migration-agent/docs/` | Cached documentation (24h TTL) |

## Detailed References

| Topic | Where to look |
|-------|---------------|
| Full conversion rules and field mapping | `instructions.md` |
| Conversion logic | `converters.py` |
| File parsing | `parsers.py` |
| Format validation | `validation.py` |
| State and rollback | `memory.py`, `memory_commands.py` |
| Agent definition (frontmatter) | `agent.md` |
| Package metadata and version | `pyproject.toml` |
| Claude Code plugin | `claude-code-plugin/` |
