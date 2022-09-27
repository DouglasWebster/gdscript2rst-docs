Add gdscript2rst scripts
========================

AT this stage you should have a folder structure something like this:

.. code:: console

    .
    ├── _build
    ├── _static
    │   └── css
    │       └── custom.css
    ├── _templates
    ├── conf.py
    ├── index.rst
    ├── make.bat
    └── Makefile

We now need to add the gdscipt files that will extract the information from the Godot project and the files
that will convert this information to ``.rst`` files.

Follow the instructions for installing these found at :doc:`/getting_started/installation/scripts`

Once the script files are installed you have a folder structure like:

.. code:: console
    
    .
    ├── _build
    ├── godot-scripts
    │   ├── Collector.gd
    │   ├── ReferenceCollectorCLI.gd
    │   └── ReferenceCollector.gd
    ├── _static
    │   └── css
    │       └── custom.css
    ├── _templates
    ├── conf.py
    ├── generate_reference
    ├── generate_reference.bat
    ├── index.rst
    ├── make.bat
    └── Makefile
