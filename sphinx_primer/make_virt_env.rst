Create project root and virtual environment
===========================================

The first thing to do is to create a folder that will be the root folder for your project.  I will
create mine with the name ``demo_root`` and use this in instructions so that the file paths are less
ambiguous.

As mentioned in the Installation section I highly recommend the use of a virtual environment and populating
this with the required modules.  This is achieved by; 

In the root folder of your project (``demo_root`` in this case) enter:

.. tabs::

    .. tab:: Linux/MacOS

        .. code:: console
                  
            demo_root $ python -m venv .venv
        
        .. note:: 
            I like to use ``.venv`` for the environment name as it is a hidden folder and doesn't *pollute* the folder tree.  
            You are, as always, free to choose whatever name you like.

            Also, I use ``$ py -m venv .venv --upgrade-deps`` so that the virtual environment is fully up to date when
            it is created.

        The new virtual is then activated with

        .. code:: console
                  
            demo_root $ source .venv/bin/activate

        Most terminals should now show something like

        .. code:: console
                  
           (.venv) demo_root $

        The ``(.venv)`` indicating that your are now in a virtual environment called **.venv**

        If it doesn't then you can check that you are using the virtual environment by entering:

        .. code:: console

            $ which python

        You should see something like

        .. code:: console

           demo_root $ ../.venv/bin/python

        which shows that you are using the python interpreter in your virtual environment.

    .. tab:: Windows (cmd prompt)

        .. code:: console
                  
            C:\..\demo_root>py -m venv .venv
        
        .. note:: 
            I like to use ``.venv`` for the environment name as it is a hidden folder and doesn't *pollute* the folder tree.  
            You are, as always, free to choose whatever name you like.

            Also, I use ``$ py -m venv .venv --upgrade-deps`` so that the virtual environment is fully up to date when
            it is created.

        The new virtual is then activated with

        .. code:: console
                  
            C:\..\demo_root>.venv\Scripts\activate.bat

        Most terminals should now show something like

        .. code:: console
                  
           (.venv) C:\..\demo_root>

        The ``(.venv)`` indicating that your are now in a virtual environment called **.venv**

        If it doesn't then you can check that you are using the virtual environment by entering:

        .. code:: console

            (.venv) C:\..\demo_root> where python

        You should see a line like this in the output

        .. code:: text

            C:\..\demo_root> .venv\Scripts\python.exe

        which shows that you are using the python interpreter in your virtual environment.

    .. tab:: Windows (PowerShell)

        .. code:: console
                    
            PS C:\..\demo_root> py -m venv .venv
        
        .. note:: 
            I like to use ``.venv`` for the environment name as it is a hidden folder and doesn't *pollute* the folder tree.  
            You are, as always, free to choose whatever name you like.

            Also, I use ``$ py -m venv .venv --upgrade-deps`` so that the virtual environment is fully up to date when
            it is created.

        The new virtual is then activated with

        .. code:: console
                    
            PS C:\..\demo_root>.\.venv\Scripts\activate.bat

        Most terminals should now show something like

        .. code:: console
                    
            (.venv) PS C:\..\demo_root>

        The ``(.venv)`` indicating that your are now in a virtual environment called **.venv**
        which shows that you are using the python interpreter in your virtual environment.

Once the virtual environment is created we can install the modules needed to create the Sphinx documentation
with a look and feel of the Godot documentation.
