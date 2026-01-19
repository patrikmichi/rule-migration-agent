# Changelog

## [Unreleased] - Enhancement Plan

### Planned Enhancements

#### High Priority
- [ ] Fix folder-based format output (create `rule-name/RULE.md` instead of `.mdc`)
- [ ] Improve documentation fetching (fix SSL, add HTML parsing)
- [ ] Add comprehensive validation (schema checking, field validation)
- [ ] Implement diff viewing before overwriting

#### Medium Priority
- [ ] Add progress indicators for large migrations
- [ ] Better reference handling (`@file` references)
- [ ] Configuration file support (`.migration-config.yaml`)
- [ ] Improved error recovery (continue after errors)

#### Low Priority
- [ ] Batch processing multiple projects
- [ ] Remote rules support (GitHub import)
- [ ] Comprehensive testing suite
- [ ] Advanced CLI features (interactive mode, JSON output)

### Recent Changes

#### Fixed
- ✅ Convert to folder-based format (`rule-name/RULE.md`) instead of `.mdc` files
- ✅ Updated rule references to use folder-based format
- ✅ Improved YAML escaping in descriptions

#### Added
- ✅ Support for INDEX.md files
- ✅ Automatic command syncing when both formats exist
- ✅ Enhanced AGENTS.md generation
