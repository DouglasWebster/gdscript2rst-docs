.. _conf_py_file:

Appendix A - Sphinx conf.py file
================================

.. code:: python

    # Configuration file for the Sphinx documentation builder.
    #
    # For the full list of built-in configuration values, see the documentation:
    # https://www.sphinx-doc.org/en/master/usage/configuration.html

    # -- Project information -----------------------------------------------------
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

    project = 'A Document Project'
    copyright = '2022, The Author'
    author = 'The Author'
    version = '0.1'
    release = version

    # -- General configuration ---------------------------------------------------
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

    needs_sphinx = "5.0"

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


    smartquotes = False

    # Pygments (syntax highlighting) style to use
    pygments_style = "sphinx"
    highlight_language = "gdscript"


    # -- Options for HTML output -------------------------------------------------
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

    html_theme = 'sphinx_rtd_theme'

    html_theme_options = {
        # if we have a html_logo below, this shows /only/ the logo with no title text
        'logo_only': True,
        # Collapse navigation (False makes it tree-like)
        'collapse_navigation': False,
    }

    html_logo = 'images/logo.png'


    html_static_path = ['_static']

    def setup(app):
        app.add_css_file("css/custom.css")