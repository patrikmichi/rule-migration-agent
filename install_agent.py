#!/usr/bin/env python3
"""
Automated setup script for rule-migration-agent

Checks for Python, installs dependencies, and verifies installation.
"""

import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path

# Colors for output
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

def print_success(msg):
    print(f"{GREEN}✅ {msg}{RESET}")

def print_warning(msg):
    print(f"{YELLOW}⚠️  {msg}{RESET}")

def print_error(msg):
    print(f"{RED}❌ {msg}{RESET}")

def print_info(msg):
    print(f"{BLUE}ℹ️  {msg}{RESET}")

def print_step(msg):
    print(f"\n{BOLD}{BLUE}→ {msg}{RESET}")


def check_python():
    """Check if Python 3.8+ is installed."""
    print_step("Checking Python installation...")
    
    # Try python3 first, then python
    python_cmd = None
    for cmd in ['python3', 'python']:
        try:
            result = subprocess.run(
                [cmd, '--version'],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                version_str = result.stdout.strip()
                # Extract version number
                version_parts = version_str.split()[1].split('.')
                major = int(version_parts[0])
                minor = int(version_parts[1])
                
                if major >= 3 and minor >= 8:
                    print_success(f"Python {major}.{minor} found: {cmd}")
                    return cmd, f"{major}.{minor}"
                else:
                    print_warning(f"Python {major}.{minor} found but need 3.8+")
                    python_cmd = cmd  # Keep for potential upgrade
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue
    
    return None, None


def install_python_macos():
    """Attempt to install Python on macOS using Homebrew."""
    print_step("Attempting to install Python on macOS...")
    
    # Check if Homebrew is installed
    try:
        result = subprocess.run(['which', 'brew'], capture_output=True, timeout=5)
        if result.returncode != 0:
            print_warning("Homebrew not found. Cannot auto-install Python.")
            print_info("Install Homebrew: /bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
            return False
    except Exception:
        return False
    
    print_info("Homebrew found. Installing Python 3...")
    try:
        result = subprocess.run(
            ['brew', 'install', 'python3'],
            timeout=300  # 5 minutes timeout
        )
        if result.returncode == 0:
            print_success("Python installed successfully!")
            return True
        else:
            print_error("Failed to install Python via Homebrew")
            return False
    except subprocess.TimeoutExpired:
        print_error("Installation timed out")
        return False
    except Exception as e:
        print_error(f"Installation failed: {e}")
        return False


def install_python_linux():
    """Attempt to install Python on Linux."""
    print_step("Attempting to install Python on Linux...")
    
    # Detect package manager
    package_managers = {
        'apt': ['sudo', 'apt-get', 'update', '&&', 'sudo', 'apt-get', 'install', '-y', 'python3', 'python3-pip'],
        'yum': ['sudo', 'yum', 'install', '-y', 'python3', 'python3-pip'],
        'dnf': ['sudo', 'dnf', 'install', '-y', 'python3', 'python3-pip'],
        'pacman': ['sudo', 'pacman', '-S', '--noconfirm', 'python', 'python-pip'],
    }
    
    for pm, cmd in package_managers.items():
        if shutil.which(pm):
            print_info(f"Using {pm} to install Python...")
            print_warning("This requires sudo permissions. You may be prompted for your password.")
            
            # For apt-get, we need to handle the update separately
            if pm == 'apt':
                try:
                    subprocess.run(['sudo', 'apt-get', 'update'], check=True, timeout=60)
                    subprocess.run(['sudo', 'apt-get', 'install', '-y', 'python3', 'python3-pip'], check=True, timeout=300)
                except Exception as e:
                    print_error(f"Installation failed: {e}")
                    return False
            else:
                try:
                    # For other package managers
                    install_cmd = [c for c in cmd if c != '&&']
                    subprocess.run(install_cmd, check=True, timeout=300)
                except Exception as e:
                    print_error(f"Installation failed: {e}")
                    return False
            
            print_success("Python installed successfully!")
            return True
    
    print_warning("Could not detect package manager. Please install Python manually.")
    return False


def install_python_windows():
    """Provide instructions for installing Python on Windows."""
    print_step("Python installation for Windows")
    print_warning("Automatic Python installation is not available on Windows.")
    print_info("Please install Python manually:")
    print("  1. Download from: https://www.python.org/downloads/")
    print("  2. Run the installer")
    print("  3. Make sure to check 'Add Python to PATH'")
    print("  4. Restart your terminal after installation")
    return False


def try_install_python():
    """Attempt to install Python based on the operating system."""
    system = platform.system()
    
    if system == 'Darwin':  # macOS
        return install_python_macos()
    elif system == 'Linux':
        return install_python_linux()
    elif system == 'Windows':
        return install_python_windows()
    else:
        print_warning(f"Unsupported operating system: {system}")
        return False


def install_dependencies(python_cmd):
    """Install Python dependencies."""
    print_step("Installing dependencies...")
    
    script_dir = Path(__file__).parent
    requirements_file = script_dir / 'requirements.txt'
    
    if not requirements_file.exists():
        print_error(f"requirements.txt not found at {requirements_file}")
        return False
    
    try:
        # Try pip3 first, then pip
        pip_cmd = 'pip3' if python_cmd == 'python3' else 'pip'
        
        # Use python -m pip for better reliability
        result = subprocess.run(
            [python_cmd, '-m', 'pip', 'install', '-r', str(requirements_file)],
            capture_output=True,
            text=True,
            timeout=300
        )
        
        if result.returncode == 0:
            print_success("Dependencies installed successfully!")
            return True
        else:
            print_error(f"Failed to install dependencies: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print_error("Installation timed out")
        return False
    except Exception as e:
        print_error(f"Installation failed: {e}")
        return False


def verify_installation(python_cmd):
    """Verify the agent installation."""
    print_step("Verifying installation...")
    
    script_dir = Path(__file__).parent
    migrate_script = script_dir / 'migrate.py'
    
    if not migrate_script.exists():
        print_error(f"migrate.py not found at {migrate_script}")
        return False
    
    try:
        result = subprocess.run(
            [python_cmd, str(migrate_script), '--help'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            print_success("Agent is working correctly!")
            return True
        else:
            print_error("Agent verification failed")
            return False
    except Exception as e:
        print_error(f"Verification failed: {e}")
        return False


def create_config_template():
    """Create a default configuration file if it doesn't exist."""
    print_step("Checking configuration...")
    
    script_dir = Path(__file__).parent
    config_file = script_dir / '.migration-config.yaml'
    
    if config_file.exists():
        print_info("Configuration file already exists")
        return True
    
    # Create default config
    default_config = """preferences:
  auto_backup: true
  show_diffs: false
  skip_unchanged: true
  conflict_resolution: "ask"

validation:
  strict: false
  auto_fix: false
"""
    
    try:
        config_file.write_text(default_config, encoding='utf-8')
        print_success("Created default configuration file")
        return True
    except Exception as e:
        print_warning(f"Could not create config file: {e}")
        return False


def main():
    """Main setup function."""
    print(f"\n{BOLD}{BLUE}{'='*60}{RESET}")
    print(f"{BOLD}{BLUE}Rule Migration Agent - Automated Setup{RESET}")
    print(f"{BOLD}{BLUE}{'='*60}{RESET}\n")
    
    # Step 1: Check Python
    python_cmd, version = check_python()
    
    if not python_cmd:
        print_warning("Python 3.8+ not found")
        print_info("Attempting to install Python automatically...")
        
        if not try_install_python():
            print_error("\n❌ Could not install Python automatically.")
            print_info("\nPlease install Python manually:")
            print("  - macOS: brew install python3")
            print("  - Linux: sudo apt-get install python3 python3-pip")
            print("  - Windows: https://www.python.org/downloads/")
            print("\nAfter installing, run this setup script again.")
            sys.exit(1)
        
        # Re-check Python after installation
        python_cmd, version = check_python()
        if not python_cmd:
            print_error("Python still not found after installation. Please restart your terminal and try again.")
            sys.exit(1)
    
    # Step 2: Install dependencies
    if not install_dependencies(python_cmd):
        print_error("Failed to install dependencies")
        sys.exit(1)
    
    # Step 3: Verify installation
    if not verify_installation(python_cmd):
        print_error("Installation verification failed")
        sys.exit(1)
    
    # Step 4: Create config
    create_config_template()
    
    # Success!
    print(f"\n{BOLD}{GREEN}{'='*60}{RESET}")
    print(f"{BOLD}{GREEN}✅ Setup completed successfully!{RESET}")
    print(f"{BOLD}{GREEN}{'='*60}{RESET}\n")
    
    print_info("You can now use the agent:")
    print(f"  {python_cmd} migrate.py <project-path> --both")
    print("\nOr use the slash commands:")
    print("  /migrate [project-path]")
    print("\n")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Setup cancelled by user{RESET}")
        sys.exit(1)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        sys.exit(1)
