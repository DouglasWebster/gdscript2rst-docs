##########################################
Automatic method of creating documentation
##########################################

Creating the reStructuredText files from :ref:`correctly commented <comment_godot_script_files>` Godot script files
can be done in one pass running either the ``generate_ref`` script file (linus/MacOS) or the ``generate_ref.bat`` file (windows).

The files ``Collector.gd`` and ``ReferenceCollectorCLI.gd`` have to be in the current working directory.  These are used to parse the
Godot project file and create a *\*.json* file.  The script/bat file will initially copy these files to the Godot project then, when
they have done their job will delete them.

.. attention:: 

    As far as possible I have tried to make both the *script file* and the *.bat* file identical.  Unfortunately I am not a user of
    Windows on a regular basis and the workings of windows *\*.bat* files is not something I have delved into deeply.
    
    The Linux/MacOSversion of the script file will allow you to cherry pick the directories within your Godot project. 
    The Windows version does not.

.. tabs::

    .. tab:: Linux/MacOS

        Creating the reStructuredText files is accomplished by running the ``generate_reference`` script file.

        This should be invoked as follows:
        
        ``$ generate_reference $project_directory [options]``

        ``&project_directory`` is the location of the Godot project.  This location can be either absolute
        or relative to the current working directory.  The Godot project directory should have a godot_project file
        in that directory or in one of its subdirectories.

        ``[options]`` can be any of the following:

        .. list-table::
            :widths: 20 60
            :header-rows: 1
            :class: tight-table

            * - Option
              - Result
            * - -h or -\-help 
              - Display then help message.
            * - -o or -\-output-directory
              - path to the directory for the *\*.rst* files.  Will be created if not already existing.  This can be either
                an absolute or relative path
            * - -d or -\-directory
              - Name of the directory within the Godot project to use as the starting point for generating
                the API documentation.  This is relative to the Godot *res:// folder*. It can be declared multiple
                times for a single disjointed scan.
            * - -i/
              - Create the index,rst file in the output directory. The index file will include the project name, the version number
                and a table of contents that includes all the files in the output directory. 
                Only one index file is created even if multiple directory sources are give.
            * - -v or -\-verbose
              - Set the verbosity level i.e the level of logging output to the display. For example -vv will set the level to 2 and
                give detailed logging whilst -v set the level to 1 and give less information.  The default level is 0 for minimum 
                logging output.
            * - -V or-\-version
              - Print the version number of the script and exit
            * - -\-doc-version
              - Set the document version number if there is no version found in the JSON file.  Defaults to 0.0.0
                At the time of writing there is no simple method that I'm aware of to set the project version from within Godot. 



        Usage example: 

            ``$ generate_reference ~/godot-projects/my-new-game/
            -o docs/source/api/addons -d addons -i -v --doc-version 0.1.5``

        This command

        * Looks in the users ``~/godot-projects/my-new-game`` directory for a Godot project 
        * Walks files in the *res://addons* directory (the ``-d addons`` option) of the godot_project.
        * Stores the resultant *\*.json* file in the  *docs/source/api/addons* directory (``-o docs/source/api/addons`` option) 
          relative to the current working directory. 
        * Creates an reST file for each class in the *\*.json* file storing them in the same output directory.
        * It will also create an index file (``-i`` option) in the output directory. 
        * There will be a reasonable amount of information logged to the display (``-v`` option)
        * API documentation will be set to 0.1.5 (``--doc-version 0.1.5`` option).

 
    .. tab:: Windows

        This is the windows version
    
        .. note:: 
            Cherry picking directories involves changing a *.gd* file on the fly which is something
            I don't know how to do in a *.bat* file and I don't have the time to learn how to do it.
            This project is open source so any Windows experts who can do that feel free!