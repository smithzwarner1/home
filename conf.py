import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Trezor Suite Documentation'
copyright = '2025, Trezor'
author = 'Trezor Team'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Enable both Markdown and reStructuredText
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}