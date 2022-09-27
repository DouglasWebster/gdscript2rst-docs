Document Project Setup
======================


The previous sections dealt with creating the reStructuredText files.  On their own these files do not 
constitute a usable document; all they consist of are the details of your APIs marked up so that they
can be incorporated into a meaningful document - in this case an html document created with 
`Sphinx <https://www.sphinx-doc.org/en/master/index.html>`_.

This section deals creating the folder with a virtual environment.  Creating a Sphinx layout in that folder.
Setting up `Sphinx <https://www.sphinx-doc.org/en/master/index.html>`_ so that the 
documentation has the look of the Godot Documentation (which itself is based on the 
`sphinx-rtd-theme <https://sphinx-rtd-theme.readthedocs.io/en/stable/>`_).  And finally adding the script
files to enable the automatic creation of the Godot project APIs within the folder. 

.. note:: Obviously this is a very opinionated setup that may not be to everyone's
    liking.  If not then there are numerous `Sphinx themes <https://sphinx-themes.org/>`_ available for you to
    use with this primer so your documentation to your liking.  However, parts of the ``conf.py`` file 
    configuration section will not be applicable. 

It is assumed that you have `Sphinx <https://www.sphinx-doc.org/en/master/index.html>`_ installed if not 
then see :ref:`Installing sphinx <sphinx_install>`


.. toctree::
    :maxdepth: 1

    make_virt_env
    install_modules
    set_up_structure
    ide_choice
    conf_sphinx/index
    add_gd2rst_items
    
    
