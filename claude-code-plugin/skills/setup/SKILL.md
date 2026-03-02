---
name: setup
description: Install Python, dependencies, and configure the rule migration agent. Use when setting up the agent for the first time.
disable-model-invocation: true
allowed-tools:
  - Bash
  - Read
  - Glob
---

# Setup Rule Migration Agent

Install the rule-migration-agent Python package and all its dependencies.

## Instructions

When the user runs `/setup`:

1. **Check Python** - Verify Python 3.8+ is available
2. **Install the package** - Try pip first, then fall back to GitHub clone
3. **Verify installation** - Run `rule-migration` or `migrate-rules` to confirm
4. **Report results** - Show what was installed

## Installation Steps

Run these commands in order. Stop at the first successful installation method.

### Method 1: pip install (preferred)

```bash
pip install rule-migration-agent
```

If that fails, try:

```bash
pip3 install rule-migration-agent
```

Or:

```bash
python3 -m pip install rule-migration-agent
```

### Method 2: GitHub clone (fallback)

```bash
git clone https://github.com/patrikmichi/rule-migration-agent.git /tmp/rule-migration-agent
cd /tmp/rule-migration-agent && pip install .
```

### Method 3: Direct from GitHub

```bash
pip install git+https://github.com/patrikmichi/rule-migration-agent.git
```

## Verify Installation

After installing, verify it works:

```bash
rule-migration --help
```

Or:

```bash
python3 -m migrate --help
```

## If Python Is Missing

Install Python first:
- **macOS**: `brew install python3`
- **Linux**: `sudo apt-get install python3 python3-pip`
- **Windows**: Download from https://www.python.org/downloads/

## What Gets Installed

- `rule-migration` and `migrate-rules` CLI commands
- Python packages: PyYAML, requests, beautifulsoup4, tqdm, rich
- Migration scripts: migrate.py, converters.py, parsers.py, validation.py, utils.py, memory.py, config.py

## Next Steps

After setup, run `/migrate [project-path]` to migrate your first project.
