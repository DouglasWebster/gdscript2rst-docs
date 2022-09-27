
Setting Up the Project Structure
================================

I like to have a separate document folder within my projects but for this primer I will assume that the document folder 
is stand alone and completely disconnected from any project folder.  This makes it easier to explain some of the 
concepts involved.

With a terminal window or cmd prompt open navigate to where you wish the root of your project to be then enter

``$ sphinx-quickstart``

This will offer you a set of options.  Accept the default options or provide answers where required.  A typical question
and response session would be:

.. code:: console

    $ sphinx-quickstart
    Welcome to the Sphinx 5.1.1 quickstart utility.

    Please enter values for the following settings (just press Enter to
    accept a default value, if one is given in brackets).

    Selected root path: .

    You have two options for placing the build directory for Sphinx output.
    Either, you use a directory "_build" within the root path, or you separate
    "source" and "build" directories within the root path.
    > Separate source and build directories (y/n) [n]: 

    The project name will occur in several places in the built documentation.
    > Project name: Godot API documentation
    > Author name(s): Doc Creator
    > Project release []: 0.0.1

    If the documents are to be written in a language other than English,
    you can select a language here by its language code. Sphinx will then
    translate text that it generates into that language.

    For a list of supported codes, see
    https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
    > Project language [en]: 

    Creating file /../demo_root/conf.py.
    Creating file /../demo_root/index.rst.
    Creating file /../demo_root/Makefile.
    Creating file /../demo_root/make.bat.

    Finished: An initial directory structure has been created.

    You should now populate your master file /Documentation/testSphinxSetup/index.rst 
    and create other documentation source files. Use the Makefile to build the 
    docs, like so:
    make builder
    where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

this would result in the following directory structure:

 .. code:: console

    demo_root
    ├── _build
    ├── _static
    ├── _templates
    ├── conf.py
    ├── index.rst
    ├── make.bat
    └── Makefile

.. warning:: Alternative structure **not** used in this tutorial

    If you reply Y(es) to the question ``> Separate source and build directories (y/n) [n]:`` then you
    will have a directory structure as follows:

    .. code:: console

        demo_root
        ├── build
        ├── make.bat
        ├── Makefile
        └── source
            ├── conf.py
            ├── index.rst
            ├── _static
            └── _templates

    Here the source for your documentation is moved into a subfolder of the main project.  