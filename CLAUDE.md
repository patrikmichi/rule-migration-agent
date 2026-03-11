# CLAUDE.md — Rule Migration Agent

## What

Bidirectional converter between Cursor rules/commands and Claude Skills. Available as a PyPI package, Claude Code plugin, and standalone script. Version 1.2.1. See [AGENTS.md](./AGENTS.md) for agent reference.

## How

```bash
pip install rule-migration-agent              # Install from PyPI
python3 install_agent.py                      # Or install from source
python3 migrate.py <project-path>             # Auto-detect direction
python3 migrate.py <path> --cursor-to-claude  # Explicit direction
python3 migrate.py <path> --dry-run           # Preview only
python3 migrate.py <path> --rollback op-001   # Rollback by operation ID
python3 migrate.py ~/projects/* --batch --both # Batch across projects
python3 -m pytest tests/ -v                   # Run 39 tests
```

Requirements: `PyYAML`, `requests`, `beautifulsoup4`, `tqdm`, `rich`

## Key Files

- `instructions.md` — full conversion rules, field mapping, and workflow
- `migrate.py` — main entry point
- `converters.py` — conversion logic
- `parsers.py` — file parsing (YAML frontmatter, .mdc, RULE.md, SKILL.md)
- `validation.py` — format validation
- `install_agent.py` — installation from source

## Key Constraints

- Auto-detection with both formats present converts BOTH directions — use explicit flags when in doubt
- Legacy `.claude/commands/*.md` files are migrated to skills and originals deleted
- `skip_unchanged=true` by default — only re-converts changed files
- `dist/` contains a 1.0.0 wheel but `pyproject.toml` is 1.2.1 — always build fresh

## Gotchas

State files written per-project: `.rule-migration/state.json` (SHA256 hashes) and `.rule-migration/history.json` (rollback IDs). Global stats at `~/.config/rule-migration-agent/`; doc cache at `~/.cache/rule-migration-agent/docs/` (24h TTL).

## Status: active
