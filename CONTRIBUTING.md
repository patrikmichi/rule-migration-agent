# Contributing to Rule Migration Agent

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/patrikmichi/rule-migration-agent.git
   cd rule-migration-agent
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Setup

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install development dependencies** (if any):
   ```bash
   pip install -r requirements-dev.txt  # If exists
   ```

## Code Style

- Follow **PEP 8** Python style guide
- Use **type hints** where appropriate
- Write **docstrings** for all functions and classes
- Keep functions focused and small
- Add comments for complex logic

## Testing

Run the test suite before submitting:

```bash
python3 tests/run_tests.py
```

Or run individual test files:

```bash
python3 -m pytest tests/test_converters.py
python3 -m pytest tests/test_parsers.py
python3 -m pytest tests/test_validation.py
python3 -m pytest tests/test_utils.py
```

## Making Changes

### Before You Start

- Check existing [issues](https://github.com/patrikmichi/rule-migration-agent/issues) to see if your feature/bug is already being worked on
- For major changes, open an issue first to discuss the approach

### Commit Messages

Use clear, descriptive commit messages:

```
feat: Add support for custom validation rules
fix: Handle empty globs array in frontmatter
docs: Update installation instructions for Windows
refactor: Simplify conversion logic
test: Add tests for edge cases in name normalization
```

### Pull Request Process

1. **Update documentation** if you've changed functionality
2. **Add tests** for new features or bug fixes
3. **Run tests** to ensure everything passes
4. **Update CHANGELOG.md** with your changes
5. **Submit PR** with a clear description

## Claude Code Plugin (for maintainers)

The Claude Code plugin is in `claude-code-plugin/`. The repo root has `.claude-plugin/marketplace.json` with `"source": "./claude-code-plugin"` so the marketplace loads that folder.

**Layout:**
- `.claude-plugin/marketplace.json` — marketplace manifest (must stay at repo root for `/plugin marketplace add owner/repo`)
- `claude-code-plugin/.claude-plugin/plugin.json` — plugin manifest
- `claude-code-plugin/commands/` — `/migrate`, `/setup`
- `claude-code-plugin/skills/` — skill for rule/skill files

When changing the plugin: update `plugin.json` version, keep `source` in `marketplace.json` as `./claude-code-plugin`, and ensure `install_agent.py` is used in `commands/setup.md` (the `/setup` command).

## Areas for Contribution

### High Priority

- **Bug fixes** - Check issues labeled `bug`
- **Documentation** - Improve README, add examples
- **Tests** - Increase test coverage
- **Validation** - Enhance format validation

### Feature Ideas

- Support for additional rule/skill formats
- Better error messages and recovery
- Performance optimizations
- UI improvements (CLI enhancements)

## Code Review

All submissions require review. We use GitHub pull requests for this purpose.

**Review Checklist:**
- [ ] Code follows style guidelines
- [ ] Tests pass
- [ ] Documentation updated
- [ ] CHANGELOG updated
- [ ] No breaking changes (or clearly documented)

## Questions?

- Open an issue for questions or discussions
- Check existing documentation first
- Be respectful and constructive in all interactions

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🎉
