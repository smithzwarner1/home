project = 'Trézor hardwaré® Wallet'
copyright = '2025'
author = 'Trézor®'

# Add essential extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx'
]

templates_path = ['_templates']
exclude_patterns = []

# Theme configuration
html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_title = "Trézor hardwaré® Wallet | Starting Up Your Device — Trézor®"
html_theme_options = {
    "navigation_with_keys": True,
    "announcement": "⚡️ New: Enhanced security features available!",
    "light_logo": "Trézor-logo-light.png",
    "dark_logo": "Trézor-logo-dark.png",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/Trézor",
            "html": "",
            "class": "fa-brands fa-github",
        },
    ],
}

# SEO Improvements
html_meta = {
    "description": "Trézor hardwaré wallet keeps your crypto safe from hackers. Easy to use, ultra-secure, and perfect for long-term holders protecting Bitcoin and altcoins.",
    "keywords": "Trézor hardwaré wallet",
    "robots": "index, follow",
    "viewport": "width=device-width, initial-scale=1.0",
}

# Language settings
language = 'en'
locale_dirs = ['locale/']
gettext_compact = False
