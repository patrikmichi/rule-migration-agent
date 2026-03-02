---
name: update
description: Update the rule-migration-agent to the latest version from PyPI or GitHub.
disable-model-invocation: true
allowed-tools:
  - Bash
  - Read
---

# Update Rule Migration Agent

Update the rule-migration-agent Python package to the latest version.

## Instructions

When the user runs `/update`:

1. **Check current version** - Run `rule-migration --version` or `pip show rule-migration-agent`
2. **Update the package** - Try pip upgrade first, then fall back to GitHub
3. **Verify the update** - Confirm the new version is installed
4. **Report results** - Show old version → new version

## Update Steps

### Method 1: pip upgrade (preferred)

```bash
pip install --upgrade rule-migration-agent
```

If that fails:

```bash
pip3 install --upgrade rule-migration-agent
```

Or:

```bash
python3 -m pip install --upgrade rule-migration-agent
```

### Method 2: From GitHub (latest main)

```bash
pip install --upgrade git+https://github.com/patrikmichi/rule-migration-agent.git
```

### Method 3: Clone and reinstall

```bash
git clone https://github.com/patrikmichi/rule-migration-agent.git /tmp/rule-migration-agent
cd /tmp/rule-migration-agent && pip install --upgrade .
```

## Verify Update

```bash
pip show rule-migration-agent | grep Version
rule-migration --help
```

## Notes

- Run `/setup` first if the package is not yet installed
- Use `/update` anytime to get the latest conversion logic, bug fixes, and format support
