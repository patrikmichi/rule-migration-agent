# Setup Rule Migration Agent

Fully automated setup - installs Python (if needed), dependencies, and configures the agent.

## Usage

```
/setup-agent
```

## AI Instructions

When the user runs `/setup-agent`, you should:

1. **Locate the agent directory** - Find `agents/rule-migration-agent/` in the current project
2. **Run the setup script** - Execute `python3 agents/rule-migration-agent/setup.py` (or `python setup.py` on Windows)
3. **Handle any errors** - If Python is not found, the script will attempt to install it automatically
4. **Report results** - Show the user what was installed and configured

The setup script (`setup.py`) will automatically:
- Check for Python 3.8+
- Install Python if missing (macOS/Linux)
- Install all dependencies
- Verify the installation
- Create default configuration

**Example execution:**
```bash
cd agents/rule-migration-agent
python3 setup.py
```

Or if the agent is in a different location, adjust the path accordingly.

## What it does

- ✅ **Checks Python installation** - Verifies Python 3.8+ is available
- ✅ **Auto-installs Python** - Installs Python automatically if missing (macOS/Linux)
- ✅ **Installs dependencies** - Installs required packages from `requirements.txt`
- ✅ **Verifies installation** - Tests that the agent works correctly
- ✅ **Creates configuration** - Sets up `.migration-config.yaml` with defaults
- ✅ **Shows next steps** - Provides instructions for first migration

## How it works

When you run `/setup-agent`, the AI will:

1. **Locate the agent directory** - Finds `agents/rule-migration-agent/` in your project
2. **Run automated setup script** - Executes `setup.py` which:
   - Checks for Python 3.8+
   - Attempts to install Python if missing (macOS via Homebrew, Linux via package manager)
   - Installs all dependencies automatically
   - Verifies the installation works
   - Creates default configuration
3. **Reports status** - Shows what was installed and configured

## Automatic Python Installation

The setup script will attempt to install Python automatically:

- **macOS**: Uses Homebrew (`brew install python3`) if available
- **Linux**: Uses system package manager (apt/yum/dnf/pacman) with sudo
- **Windows**: Provides download link and instructions (manual install required)

**Note**: Automatic installation may require:
- Admin/sudo permissions (Linux)
- Homebrew installed (macOS)
- User confirmation for password prompts

## What happens

1. **Checks Python version** - Verifies Python 3.8 or higher is installed
2. **Auto-installs Python** - If missing, attempts installation based on OS
3. **Locates agent directory** - Finds `agents/rule-migration-agent/` in your project
4. **Installs dependencies** - Runs `pip install -r requirements.txt`
5. **Verifies installation** - Tests the agent with `--help` command
6. **Creates config template** - Generates `.migration-config.yaml` with defaults
7. **Shows status** - Displays installation status and next steps

## Configuration

After setup, you can customize behavior via `.migration-config.yaml`:

```yaml
preferences:
  auto_backup: true
  show_diffs: false
  skip_unchanged: true
  conflict_resolution: "ask"

validation:
  strict: false
  auto_fix: false
```

## Examples

- `/setup-agent` - Run full automated setup

## Next Steps

After running `/setup-agent`:

1. **Migrate your first project:**
   ```
   /migrate [project-path]
   ```

2. **Or use the agent directly:**
   ```bash
   python3 agents/rule-migration-agent/migrate.py [project-path] --both
   ```

3. **Check sync status:**
   ```
   /migrate [project-path] --check-sync
   ```

## Troubleshooting

**"Python installation failed"**
- **macOS**: Install Homebrew first: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- **Linux**: Ensure you have sudo permissions
- **Windows**: Download and install from [python.org](https://www.python.org/downloads/)

**"pip install failed"**
- Try: `python3 -m pip install -r requirements.txt`
- Or: `pip3 install -r requirements.txt`
- Check your internet connection

**"Agent directory not found"**
- Make sure `agents/rule-migration-agent/` exists in your project
- Or clone the agent to that location first

**"Permission denied" (Linux)**
- The setup may need sudo for Python installation
- You'll be prompted for your password

## Related Commands

- `/migrate` - Run migration between Cursor rules and Claude Skills

## Notes

- The agent is installed locally in your project (not globally)
- Dependencies are installed in your current Python environment
- For virtual environments, activate it before running `/setup-agent`
- Automatic Python installation works best on macOS (with Homebrew) and Linux (with package manager)

## Manual Setup (if automated setup fails)

If automatic setup fails, you can set up manually:

```bash
# 1. Install Python 3.8+ (if not installed)
# macOS: brew install python3
# Linux: sudo apt-get install python3 python3-pip

# 2. Navigate to agent directory
cd agents/rule-migration-agent

# 3. Install dependencies
pip install -r requirements.txt

# 4. Verify
python3 migrate.py --help
```
