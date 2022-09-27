Setting up conf.py
==================

Setting up ``conf.py`` to give the look and feel of the Godot Documentation is fairly complex so I will
just go over the important parts.  A full :ref:`conf.py <conf_py_file>` file is available in the appendix 
and can be copied over to give you the correct set up.  Just remember to change the Project information
section to your requirements.

Basic changes
-------------

Changing the theme
^^^^^^^^^^^^^^^^^^

The first thing is to change the theme this is done by setting

.. code:: 

    html_theme = 'sphinx_rtd_theme'

This will give it the general appearance of the Godot help files and your preview should change to match.

Enabling external links
^^^^^^^^^^^^^^^^^^^^^^^

After this we can set up Sphinx so that the documentation can link to external web pages.  This is
accomplished by:

1. Adding an extension to the extensions array:
   
   .. code:: 

        extensions = [
            "sphinx.ext.extlinks"       # to generate external links
        ]

2. Setting up the godot_class to point to the correct location (the %s is a placeholder which will be
   replaced by the appropriate Godot class name):
   
   .. code:: python

        extlinks = {            
            'godot_class' : 
                ('https://docs.godotengine.org/en/stable/classes/class_%s.html', '')
        }

Finalising the look and feel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The above will give the basic functionality and if all you are creating is a basic document then that may
well be sufficient.  There are still differences between this and the Godot look and feel.  In order to more
closely approach the Godot look then a custom .css file has to be installed and Sphinx instructed to 
make use of it.

You can find an up to date copy of the .css file required at `Godot cusom.css 
<https://github.com/godotengine/godot-docs/blob/stable/_static/css/custom.css>`_.  A copy of this file at the time of writing is in
:ref:`custom_css`

Create a new folder in the ``_static`` folder called ``css`` and store the ``custom.css`` file in there. Then
alter ``conf.py`` to include:


.. code:: python

    # These paths are either relative to html_static_path
    # or fully qualified paths (eg. https://...)
    html_css_files = [
        "css/custom.css",
    ]

Additional enhancements
-----------------------

Correctly highlighting GDScript code snippets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to see any gdscript code snippets highlighted correctly then they have to be shown in a
``..code:: gdscript`` block and will display like this:

.. code:: gdscript
    
    # The model of the battery used in the
    # simulation.
    #
    # .. warning:: This mode isn't at all accurate
    #  and should not be used for any practicle
    #  projects.

    class_name BatteryEntity
    extends Node2D

    ## Total amount of power the battery is able to hold
    export var max_storage := 1000.0

    ## Actual amount of power currently in the battery
    var stored_power := 0.0 setget _set_stored_power

    onready var receiver := $PowerReceiver
    onready var source := $PowerSource
    onready var indicator := $Indicator


    func _set_stored_power(value: float) -> void:
        stored_power = value

An undefined lexing style ``..code::`` block will not highlight correctly and display like this:

.. code:: python
    
    # The model of the battery used in the
    # simulation.
    #
    # .. warning:: This mode isn't at all accurate
    #  and should not be used for any practicle
    #  projects.

    class_name BatteryEntity
    extends Node2D

    ## Total amount of power the battery is able to hold
    export var max_storage := 1000.0

    ## Actual amount of power currently in the battery
    var stored_power := 0.0 setget _set_stored_power

    onready var receiver := $PowerReceiver
    onready var source := $PowerSource
    onready var indicator := $Indicator


    func _set_stored_power(value: float) -> void:
        stored_power = value



If you want your code snippets to default to the gdscript lexer then add the following to the ``conf.py``
file:

.. code:: python
    
    # Pygments (syntax highlighting) style to use
    pygments_style = "sphinx"
    highlight_language = "gdscript"

Adding a logo
^^^^^^^^^^^^^

You can have a logo for the document that displays at the top of the sidebar.  For my documents I
normally create an ``images`` folder and store all any images required in the document there.  Suppose you
have an image in this folder called ``logo.png`` then you can select this as the logo with:

.. code:: python

    html_logo = 'images/logo.png'

Advanced options
----------------

There are many more options available for fine tuning the look and feel of your document but the above
will give you a look not dissimilar to the Godot documentation.  If you want to see the full range of
options available then check out the `Sphinx configuration 
<https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output>`_  documentation, 
the `sphinx-rtd-theme <https://sphinx-rtd-theme.readthedocs.io/en/stable/>`_  documentation and the `Godot
Document <https://github.com/godotengine/godot-docs>`_ source.
