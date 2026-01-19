# Test Suite

Comprehensive test suite for rule-migration-agent.

## Running Tests

### Run all tests:
```bash
python tests/run_tests.py
```

### Run specific test module:
```bash
python -m unittest tests.test_utils
python -m unittest tests.test_parsers
python -m unittest tests.test_converters
python -m unittest tests.test_validation
```

### Run with verbose output:
```bash
python -m unittest discover tests -v
```

## Test Coverage

- **test_utils.py**: Tests for utility functions (normalization, validation, caching, exceptions)
- **test_parsers.py**: Tests for file parsing (Cursor rules, Claude Skills)
- **test_converters.py**: Tests for conversion functions
- **test_validation.py**: Tests for validation functions

## Adding New Tests

1. Create a new test file: `tests/test_<module>.py`
2. Follow the existing test structure
3. Use `unittest.TestCase` as base class
4. Add descriptive test method names starting with `test_`

## Test Requirements

Tests use the standard library `unittest` module. No additional dependencies required for basic tests.
