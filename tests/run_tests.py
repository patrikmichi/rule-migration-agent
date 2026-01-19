#!/usr/bin/env python3
"""
Test runner for rule-migration-agent test suite.
"""

import unittest
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

def run_tests():
    """Run all tests."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Discover and add all test modules
    test_dir = Path(__file__).parent
    tests = loader.discover(str(test_dir), pattern='test_*.py')
    suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(run_tests())
