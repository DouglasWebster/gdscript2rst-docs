Creating Godot API hyperlinks
#############################

Whichever method is chosen to create the reStructuredText files a prerequisite is that a file called
``godot_api_call.json`` has to be available.
This file is a list of all the Godot APIs with its associated hyperlink to the relevant Godot help page.  This enables
the automatic creation of Godot help file links within the users final documentation.

The utility *godot_api_ref* will create this file for you.  The following shows the usage and the options available.

.. code:: text
      
   usage: python -m godot_api_ref [options]

   Given a godot-docs branch it scans the class folder and creates a JSON file
   linking the Godot class name with the API reference

   options:
      -h, --help        show this help message and exit
      --token TOKEN     optional github access token 
                        (default "" may only gives 60 reads/hour)
      --branch BRANCH   optional branch for the class files (default: stable)
      -v, --verbose     Set the verbosity level. For example -vv sets
                        verbosity to level 2. Default: 0.
      --check-branches  print out a list of the Godot document branches 
                        then exit without making the links

Running ``python -m godot_api_ref`` will create a *godot_api_calls.json* file with links to the **stable** versions 
documentation **at the time of creation**.  

For those with projects created by earlier versions of Godot the program can be invoked with the ``--branch`` option e.g.
``python -m godot_api_ref --branch 3.2`` will create the *godot_api_calls.json* file with links to the 
version 3.2 documentation.

Invoking with ``python -m godot_api_ref --check-branches`` will display a list of available document versions for
creating the *godot_api_calls.json* file.
