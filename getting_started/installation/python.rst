.. instructions for installing the python environment

Python
======

Installing python is beyond the scope of this document.  If you need to install python and are unsure
how to do it then the following taken from the Python website should be followed.

.. admonition:: `BeginnersGuide <https://www.python.org/about/gettingstarted/>`_ 

    Installing Python is generally easy, and nowadays many Linux and UNIX 
    distributions include a recent Python. Even some Windows computers 
    (notably those from HP) now come with Python already installed. 
    If you do need to install Python and aren't confident about the task 
    you can find a few notes on the 
    `BeginnersGuide/Download <http://wiki.python.org/moin/BeginnersGuide/Download>`_ 
    wiki page, but installation is unremarkable on most platforms.

.. _pip_install:

Pip
===

Pip is the package management system used throughout this guide.  It is not unusual for it 
to be installed when python is installed but if not then the installation and usage instructions can
be found at https://pip.pypa.io/en/stable/

.. note::

    Pip is not the only package manager for python, two good alternatives I have used in the 
    past being `Conda <https://conda.pydata.org/>`_ and `Poetry <https://python-poetry.org/>`_. 

Virtual environments
====================

.. admonition:: From the python docs
    
    A virtual environment is a Python environment such that the Python interpreter, 
    libraries and scripts installed into it are isolated from those installed in other
    virtual environments, and (by default) any libraries installed in a “system” Python, 
    i.e., one which is installed as part of your operating system.

Many tools for managing Python development maintain virtual environments as a mater of course, for
example the two mentioned above `Conda <https://conda.io/>`_ and `Poetry <https://python-poetry.org/>`_.
These however may be overkill for the needs of a Godot game developer who is only using Python to
document her code.  In this case Python can be invoked to create a virtual environment for itself.

The following steps are all that is needed:

    * Open a terminal window (linux/macOS) or cmd prompt (windows)
    * Change into the directory where your project is to be created.
    * enter the following command

        ``python -m venv <your-environment-name>``

this will create a new director called whatever you chose for your-environment-name and
populate it with the minimum required to start a python project - usually `pip` and
`setuptools`.

However, if you enter  ``pip list`` at this point you will probably see the complete listing
of the `system` python environment as your new virtual environment hasn't been activated.

    * to activate your new environment type

        .. line-block:: 
            ``source  <your-environment-name>/bin/activate`` (linux/mac)
            ``<your-environment-name>/Scripts/activate.bat`` (windows CMD prompt)
            ``<your-environment-name>/Scripts/Activate.ps1`` (windows Powershell)  

If you now enter ``pip list`` you should see a minimal listing containing `pip` and `setuptools`

    * to leave a virtual environment simply run:
        
        ``deactivate``

An in depth discussion regarding the rationale for using virtual environments as well as more
detailed instructions can be found at `Installing packages using pip and virtual environments 
<https://packaging.python.org/en/latest/guides/
installing-using-pip-and-virtual-environments/#creating-a-virtual-environment>`_

