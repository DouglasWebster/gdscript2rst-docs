Setting up the documentation folder
===================================

We first add the scripts needed for creating the documentation from the Godot project.  This is best
accomplished first as the git version of installing the scripts requires and empty directory 
(git can be very selfish at times!):

If you dont have git then download the repository from 
`gds2rst_scripts <https://github.com/DouglasWebster/gds2rst_scripts.git>`_
using the green **Code** button 
        
.. image:: /images/get_scripts_zip.png

then extract the contents to a subfolder of ``DesignPatterns`` named ``DesignPatternsDoc``.

Else:

.. tabs:: 

    .. tab:: Linux/macOS

        .. code:: shell-session

            [DesignPatternsProject]$ git clone --depth 1 -b main https://github.com/DouglasWebster/gds2rst_scripts.git DesignPatternsDoc
            [DesignPatternsProject]$ cd DesignPatternsDoc/

    .. tab:: Windows (cmd)

        .. code:: PowerShell

            [DesignPatternsProject]> git clone --depth 1 -b main https://github.com/DouglasWebster/gds2rst_scripts.git DesignPatternsDoc
            [DesignPatternsProject]> cd DesignPatternsDoc/


    .. tab:: Windows (ps)

        .. code:: PowerShell

            [DesignPatternsProject]ps git clone --depth 1 -b main https://github.com/DouglasWebster/gds2rst_scripts.git DesignPatternsDoc
            [DesignPatternsProject]ps cd DesignPatternsDoc/

.. admonition:: Changing into an IDE

    At this point I like to start  up VSCode and carry out all of the following in VSCode's terminal window.
    This is purely your choice but I find it helpful to have a separate interface for the documentation.

Within the ``DesignPatternsProject`` run the following commands to populate the documents folder with the
required document creation modules.

.. code:: shell-session

    [DesignPatternsDoc]$ python -m venv .venv
    [DesignPatternsDoc]$ source .venv/bin/activate
    (.venv) [DesignPatternsDoc]$ pip install sphinx sphinx-rtd-theme
    (.venv) [DesignPatternsDoc]$ pip install sphinx-notfound-page sphinx-tabs
    (.venv) [DesignPatternsDoc]$ pip install sphinx-notfound-page sphinx-tabs
    (.venv) [DesignPatternsDoc]$ pip install gdscript2rest godot-api-refs
    (.venv) [DesignPatternsDoc]$ pip install esbonio


Now run the following to create an initial Sphinx project:

.. code:: console

    (.venv) [DesignPatternsDoc]$ sphinx-quickstart 
    Welcome to the Sphinx 5.2.2 quickstart utility.

    Please enter values for the following settings (just press Enter to
    accept a default value, if one is given in brackets).

    Selected root path: .

    You have two options for placing the build directory for Sphinx output.
    Either, you use a directory "_build" within the root path, or you separate
    "source" and "build" directories within the root path.
    > Separate source and build directories (y/n) [n]: n

    The project name will occur in several places in the built documentation.
    > Project name: Design Patterns
    > Author name(s): A N Other
    > Project release []: 0.1.0

    If the documents are to be written in a language other than English,
    you can select a language here by its language code. Sphinx will then
    translate text that it generates into that language.

    For a list of supported codes, see
    https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
    > Project language [en]: 

    Creating file /DesignPatternsDoc/conf.py.
    Creating file /DesignPatternsDoc/index.rst.
    Creating file /DesignPatternsDoc/Makefile.
    Creating file /DesignPatternsDoc/make.bat.

    Finished: An initial directory structure has been created.

    You should now populate your master file /DesignPatternsDoc/index.rst and create other documentation
    source files. Use the Makefile to build the docs, like so:
    make builder
    where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

We also need a copy of the Godot API html addresses - The **gdscript2rest** module uses these to create
the links from your documentation to the Godot documentation.

Entering the following whilst in the ``DesignPatternsProject`` folder will create the link file
``godot_api_calls.json``:

.. code:: console

    (.venv) [DesignPatternsDoc]$ python -m godot_api_ref

The above default run of **godot_api_ref** will get the links for the Godot API stable release *at the time of 
your run*.  If you need a different version of the API see 
:doc:`/api_creation/create_godot_hyperlinks` for detailed instructions.

``DesignPatternsDoc`` should now have all the required elements and structure for creating your project
documentation and look something like this.

.. code:: console

    DesignPatternsProject
    └── DesignPatternsDoc
        ├── _build
        ├── _static
        ├── _templates
        ├── .venv
        ├── godot-scripts
        │   ├── Collector.gd
        │   ├── ReferenceCollectorCLI.gd
        │   └── ReferenceCollector.gd
        ├── generate_reference
        ├── generate_reference.bat
        ├── godot_api_calls.json
        ├── conf.py
        ├── index.rst
        ├── make.bat
        └── Makefile


