Setting Up Sphinx Environment
=============================

In order generate Sphinx documentation Sphinx and a number of associated python modules have to be installed.  As these are
python modules there is no difference in the installation procedure and the prompt displayed will be for a *bash* script 
(for Windows read ``>`` for ``$``).

.. note:: These instructions will assume a Python virtual environment.  
    
    They also show the Linux/macOS  
    prompt format - this will make no difference to the commands.

Install Sphinx
--------------


To install Sphinx run the following command:

.. code:: console

    (.venv) $ pip install sphinx

If you enter the following command:

.. code:: console

    (.venv) $ pip list
    Package                       Version
    ----------------------------- ---------
    alabaster                     0.7.12
        .
        .
        .
    Sphinx                        5.1.1
    sphinxcontrib-applehelp       1.0.2
    sphinxcontrib-devhelp         1.0.2
    sphinxcontrib-htmlhelp        2.0.0
    sphinxcontrib-jsmath          1.0.1
    sphinxcontrib-qthelp          1.0.3
    sphinxcontrib-serializinghtml 1.1.5
    urllib3                       1.26.12

You will get a list of approx 23 additional modules that are required to run a basic version of Sphinx.  

.. note:: 

    It is because Sphinx can install a large number of modules that may be of use only to the current project
    that I recommend creating a virtual environment - these modules won't pollute your global environment.


The Sphinx command line tools should now be available.  You can do a basic check by running the following command:

.. code:: console

    (.venv) $ sphinx-build --version
    sphinx-build 5.1.1

If you see a similar output then Sphinx should have been installed correctly.

Install additional modules
--------------------------

In order for your documentation to look like Godot's additional Sphinx modules have to be installed.  Sphinx comes pre-loaded with
several themes; a theme being the settings controlling the documentations overall look and feel.  One of the main disadvantages of
the in built themes is that only two of them are optimized for mobile layout.  Godot uses ReadTheDocs theme
which is optimised for mobile layout.

The read-the-docs theme is installed by the following command:

.. code:: console

    (.venv) $ pip install sphinx-rtd-theme

Two other modules that may be used should be installed at this point.  These are sphinx-notfound-page and sphinx-tabs.  The first
allows you to specify the response to trying to access a non-existant page instead of getting the dreaded 404 message.  The other
allows tabbed output for the webpage version of the documentation.

These can be installed with one command:

.. code:: console

    (.venv) $ pip install sphinx-notfound-page sphinx-tabs

.. warning:: 

    You may receive an error message when you install the above packages.  Essentially one of the packages installs
    a docutils version => 18.0 and the sphinx-rtd-theme requires a version of docutils < 18.0.  I have found no problem with
    leaving the docutils at the higher version level.






