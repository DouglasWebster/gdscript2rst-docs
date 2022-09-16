# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


#from ipaddress import collapse_addresses
import sphinx
import sphinx_rtd_theme
import sys
import os

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'gdscript2rst'
copyright = '2022, Douglas Webster'
author = 'Douglas Webster'
version = '0.1'
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

needs_sphinx = "1.3"

sys.path.append(os.path.abspath("_extensions"))

extensions = [
    'sphinx_rtd_theme',
    'sphinx_tabs.tabs',
    'sphinx.ext.extlinks'
]

extlinks = {
    'godot_class' :
     ('https://docs.godotengine.org/en/stable/classes/class_%s.html', '')
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# These imports should *not* be moved to the start of the file,
# they depend on the sys.path.append call registering "_extensions".
# GDScript syntax highlighting
from gdscript import GDScriptLexer
from sphinx.highlighting import lexers

lexers["gdscript"] = GDScriptLexer()


smartquotes = False

# Pygments (syntax highlighting) style to use
pygments_style = "sphinx"
highlight_language = "gdscript"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_logo = 'images/logo.png'

html_static_path = ['_static']

html_theme_options = {
    'collapse_navigation' : False
}

def setup(app):
    app.add_css_file("css/custom.css")
