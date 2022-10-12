Build Initial Documentation
===========================

With the document folder and the Godot project folder in place we can now do the first build of the
documentation.

The sample **DesignPatterns**  project has the file ``.../ECS/Entities/BatteryEntity.gd``  already
commented as per the :doc:`/api_creation/comment_scripts` instructions.

If not already there change into the directory.  If you have an IDE configured for DesignPatternsDoc 
start that up.

To generate the API reStructuredText files and place them in a folder named APIs along with 
an index file run:

.. tabs:: 

    .. tab:: Linux/macOS

            .. code:: shell-session

                    (.venv) [DesignPatternsDoc]$ ./generate_reference ../DesignPatterns -o APIs -i -v --doc-version 0.1.0

    .. tab:: Windows (cmd)

        To follow

    .. tab:: Windows (ps)
            .. code:: PowerShell

                (.venv) [DesignPatternsDoc]ps .\generate_reference ..\DesignPatterns -o APIs -i -v --doc-version 0.1.0

If you make your documentation at this point the result will not be as expected as the ``conf.py`` file 
still has the default configuration.

Amend the conf.py file to match the one in :doc:`/appendix/conf_py`.

The ``conf.py`` file makes reference to the ``custom.css`` file which we still have to create.  

Create the folder ``css`` in the ``_static folder`` and then create a file ``custom.css`` in that folder.

.. tabs:: 

    .. tab:: Linux/macOS

        .. code:: shell-session

            (.venv) [DesignPatternsDoc]$ mkdir ./_static/css
            (.venv) [DesignPatternsDoc]$ touch _static/css/custom.css

    .. tab:: Windows (cmd)

        .. code:: PowerShell

            (.venv) [DesignPatternsDoc]> mkdir .\_static\css
            (.venv) [DesignPatternsDoc]> type nul > _static\css\custom.css

    .. tab:: Windows (ps)

        .. code:: PowerShell

            (.venv) [DesignPatternsDoc]ps mkdir .\_static\css
            (.venv) [DesignPatternsDoc]ps New-Item _static\css\custom.css


Then copy and paste the contents of either :doc:`/appendix/custom_css` or `Godot cusom.css 
<https://github.com/godotengine/godot-docs/blob/stable/_static/css/custom.css>`_ into the file.

Now we can build the documents to check that all is correct.  This is simply just one command:

.. code:: shell-session

     (.venv) [DesignPatternsDoc]$ make html

Sphinx will build the documentation in html format and place resultant output in ``_build/html``. 
Using a browser open the file ``DesignPatternsProject/DesignPatternsDoc/_build/html/index.html``

You should get something like:

.. image:: /images/initil_build.png

Not there yet!  There are no links to the documents we have created, only links to pages that do nothing.
This is because Sphinx starts the documentation in the ``index.rst`` file of the root directory and at
the moment it looks very spartan.

.. code:: reStructuredText

    .. Design Patterns documentation master file, created by
    sphinx-quickstart on Thu Sep 29 17:54:27 2022.
    You can adapt this file completely to your liking, but it should at least
    contain the root `toctree` directive.

    Welcome to Design Patterns's documentation!
    ===========================================

    .. toctree::
       :maxdepth: 2
       :caption: Contents:





    Indices and tables
    ==================

    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`


The Indices and tables section can be onerous to set up so let's just delete it!  The section ``toctree``
is the bit we are interested in. Add a line ``APIs/index`` under the ``:caption:``.  Layout is **very**
important in reStructuredText documents - there should be one blank line between ``:caption:`` and
``APIs/index``  and the **A** of API's should line up with the first **:** of :caption:.

Your ``index.rst`` should now look like:

.. code:: reStructuredText

    .. Design Patterns documentation master file, created by
    sphinx-quickstart on Thu Sep 29 17:54:27 2022.
    You can adapt this file completely to your liking, but it should at least
    contain the root `toctree` directive.

    Welcome to Design Patterns's documentation!
    ===========================================

    .. toctree::
       :maxdepth: 2
       :caption: Contents:

       APIs/index

If you now rebuild the documentation by again running ``make html`` and look the index page on your
browser you should be able to see:

.. image:: /images/first_step_build.png



