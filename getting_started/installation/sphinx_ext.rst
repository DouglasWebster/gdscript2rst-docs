.. Install the Sphinx extensions as required.

Sphinx extensions
=================

In order for the documentation to have the same look and feel as the Godot official documentation
the following extensions should be installed.

.. _sphinx_rtd_theme_ins:

sphinx-rtd-theme
----------------

This is the theme used by Godot and a great many other projects.  The following is taken from the PyPi
repository and highlights why it is favoured.

    This `Sphinx <http://www.sphinx-doc.org/>`_ theme was designed to provide a great reader 
    experience for documentation users on both desktop and mobile devices. 
    This theme is used primarily on `Read the Docs <http://www.readthedocs.org/>`_ but 
    can work with any Sphinx project. You can find a working demo of the theme in the 
    `theme documentation <https://sphinx-rtd-theme.readthedocs.io/en/stable/>`_

This is installed by ``$ pip install sphinx-rtd-theme``

sphinx-notfound-page
--------------------

This extension creates a custom 404 page with absolute URL's hardcoded.  Documentation can be
found at `<https://sphinx-notfound-page.readthedocs.io/>`_ 

The extension is installed by ``$ pip install sphinx-notfound-page`` 

sphinx-tabs
-----------

This extension creates tabbed content in `Sphinx documentation <http://www.sphinx-doc.org/>`_.
Documentation can be found at `Sphinx Tabs <https://sphinx-tabs.readthedocs.io/en/latest/>`_

The extension is installed by ``$ pip install sphinx-tabs`` 

.. caution::
    
    see the :ref:`v_env_warning` warning regarding the use of virtual environments.
