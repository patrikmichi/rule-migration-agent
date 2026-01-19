---
description: Install Python, dependencies, and configure the rule migration agent
---

# Setup Rule Migration Agent

Fully automated setup - installs Python (if needed), downloads/installs the Python tools, and configures the agent.

## Instructions

When the user runs `/setup`, follow these steps:

### Step 1: Check if Already Installed

First, check if the agent is already installed:

```bash
# Try to find migrate.py in common locations
which migrate.py
python3 -c "import migrate" 2>/dev/null
ls ~/.local/bin/migrate.py 2>/dev/null
ls ~/rule-migration-agent/migrate.py 2>/dev/null
```

If found, verify it works:
```bash
python3 [path-to-migrate.py] --help
```

If it works, report success and skip installation.

### Step 2: Try pip Install (if published to PyPI)

Attempt to install via pip:

```bash
pip install rule-migration-agent
# or
pip3 install rule-migration-agent
# or
python3 -m pip install rule-migration-agent
```

If successful:
- Verify installation: `python3 -m rule_migration_agent --help` or `migrate --help`
- Report success and location
- Skip to Step 4

If pip install fails (package not found), proceed to Step 3.

### Step 3: Install from GitHub

Clone and install from the GitHub repository:

```bash
# Determine installation location
INSTALL_DIR="$HOME/.local/share/rule-migration-agent"

# Clone the repository
git clone https://github.com/patrikmichi/rule-migration-agent.git "$INSTALL_DIR"

# Navigate to directory
cd "$INSTALL_DIR"

# Run the installation script
python3 install_agent.py
```

**Alternative if git is not available:**
```bash
# Download as ZIP
INSTALL_DIR="$HOME/.local/share/rule-migration-agent"
mkdir -p "$INSTALL_DIR"
cd "$INSTALL_DIR"
curl -L https://github.com/patrikmichi/rule-migration-agent/archive/refs/heads/main.zip -o repo.zip
unzip repo.zip
mv rule-migration-agent-main/* .
rm -rf rule-migration-agent-main repo.zip

# Run installation script
python3 install_agent.py
```

### Step 4: Verify Installation

After installation, verify it works:

```bash
# If installed via pip
python3 -m rule_migration_agent --help

# If installed from GitHub
python3 "$HOME/.local/share/rule-migration-agent/migrate.py" --help
```

### Step 5: Report Results

Show the user:
- ✅ Installation method used (pip or GitHub)
- ✅ Installation location
- ✅ Python version detected
- ✅ Dependencies installed
- ✅ How to use the agent:
  - Via plugin command: `/migrate [project-path]`
  - Via command line: `python3 [path]/migrate.py [project-path]`

## What the Setup Does

The setup process:
- ✅ Checks for Python 3.8+ (installs if missing on macOS/Linux)
- ✅ Installs dependencies from `requirements.txt`
- ✅ Verifies the installation works
- ✅ Creates default configuration (`.migration-config.yaml`)

## Installation Locations

The agent may be installed in:
- **pip install**: System Python site-packages or user site-packages
- **GitHub clone**: `~/.local/share/rule-migration-agent/` (default)
- **Custom location**: User-specified directory

## Troubleshooting

**If pip install fails:**
- The package may not be published to PyPI yet
- Fall back to GitHub installation (Step 3)

**If git clone fails:**
- Check internet connection
- Try downloading ZIP instead
- User may need to install git: `brew install git` (macOS) or `sudo apt-get install git` (Linux)

**If install_agent.py fails:**
- Check Python version: `python3 --version` (needs 3.8+)
- Check error messages for missing dependencies
- May need to install Python manually

**If migrate.py not found after installation:**
- Check installation location
- May need to add to PATH or use full path
- Verify files were copied correctly

## Next Steps After Setup

Once setup completes, users can:
1. **Use the plugin command**: `/migrate [project-path]`
2. **Use command line**: `python3 [path]/migrate.py [project-path]`
3. **Check sync status**: `/migrate [project-path] --check-sync`

## Notes

- The plugin provides the commands and skills (Markdown files)
- The Python tools are installed separately via this setup
- This keeps the plugin lightweight and follows best practices
- Updates to Python tools require re-running setup or `pip install --upgrade`
