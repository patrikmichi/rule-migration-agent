# Configuration file for Sphinx documentation

import sys
from pathlib import Path

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

project = 'rule-migration-agent'
copyright = '2024'
author = 'rule-migration-agent contributors'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
