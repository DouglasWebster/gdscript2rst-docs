#######################################
Manual method of creating documentation
#######################################

Creating the reStructuredText files from the **correctly** commented script files is a two
stage process:

* Generate a *\*.json* file containing the details required.
* Convert the information in the *\*.json* file into reStructuredText files - 
  one .rst file for each class.

Create the reference.json file
##############################

The creation of the ``reference.json`` files depend on certain files being installed in the Godot project directory

* Collector.gd - This is the workhorse of the suite of files. It scans the directories of your project, 
  parses the GDscript files and extracts the code dictionaries getting the code reference data. 
* ReferenceCollector.gd  - This is one of the drivers for the Collector.gd script.  This is for use within Godot to
  generate the *\*.json* file .
* ReferenceCollectorCLI.gd - This is similar to ReferenceCollector.gd but is designed for use with ``generate_reference`` 

.. note:: 
  ``reference.json`` is the default name for the output file from the above scripts.  The following documentation
  will continue using this name.  
  The programs output file name is freely configurable however so it can be
  changed to a more descriptive name to suit your needs if so desired.

The manual creation of the ``reference.json`` file can be accomplished in one of two ways;

1. From within the Godot editor
-------------------------------

In this case copies of the files ``Collector.gd`` and ``ReferenceCollector.gd`` should be placed in the Godot project directory.
From within the editor if you open ``ReferenceCollector.gd`` you will see the following at the top of the file:

.. code:: gdscript

  # Finds and generates a code reference from gdscript files.
  #
  # To use this tool:
  #
  # - Place this script and Collector.gd in your Godot project folder.
  # - Open the script in the script editor.
  # - Modify the properties below to control the tool's behaviour.
  # - Go to File -> Run to run the script in the editor.


  var Collector: SceneTree = load("Collector.gd").new()
  # A list of directories to collect files from.
  var directories := ["res://src"]
  # If true, explore each directory recursively
  var is_recursive: = true
  # A list of patterns to filter files.
  var patterns := ["*.gd"]
  # Output path to save the class reference.
  var save_path := "res://reference.json"


As the brief instructions states you can alter the following variables to tailor the creation of ``reference.json`` file.

.. list-table:: ReferenceCollector configurable properties
    :widths: 1 1 10
    :header-rows: 1
    :class: tight-table

    * - Property
      - Type 
      - Function
    * - directories
      - array
      - An array of strings listing the directories to be scanned. Defaults to the **["res://src"]** 
        directory. 
    * - is_recursive
      - boolean
      - Whether to include all the subdirectories of the directories list. 
    * - patterns
      - array
      - a list of file patterns to be scanned - wild cards are allowed. Defaults to **["*.gd"]**
    * - save_path
      - string
      - the directory and name in which to save the output file. Defaults to **"res://reference.json"** 

Once the properties have been configured to your requirements then use the editors **File -> Run** command to generate
the output documentation.

2. From the command line
------------------------

In this case the files ``Collector.gd`` and ``ReferenceCollectorCLI.gd`` should be in the godot project directory.

Using a terminal or cmd window change to the project directory then enter:

``godot --editor --quit --script --no-window ReferenceCollectorCLI.gd``

This will start the godot editor, run the ``ReferenceCollectorCLI`` script, then quit.

The default script will create documentation for all the files in the project that has ``class_name`` defined.  It is possible
to configure the ``ReferenceCollectorCLI.gd`` script so that it is selective in the items chosen.

The script file contains the following lines:

.. code:: gdscript
  
  .
  .
  .
  # A list of directories to collect files from.
  var directories := ["res://"]
  # If true, explore each directory recursively
  var is_recursive: = true
  # A list of patterns to filter files.
  var patterns := ["*.gd"]
  .
  .
  .

Each of the variables can be changed to reflect the desired outcome.  
 
 * The **directories** variable is a comma separated string of paths
 * The **is_recursive** variable is a boolean.
 * The **patterns** variable is a comma separated string of file extensions to scan.

The output of this is a **reference.json** file stored in the 
`*res://* <https://docs.godotengine.org/en/stable/tutorials/io/data_paths.html>`_ folder of the Godot project .


Generate the API reStructuredText files
#######################################

This is accomplished by running the python module gdscript2rest. This module scans the *.json* file created by the above procedure.
It will create a separate *.rst* file for each class found in the *.json* file.

The program is invoked with:

``gdscript2rest [-h] [-p PATH] [-i] [-v] [--dry-run] [-V] files [files ...]``

It expects at least 1 ``files`` path to find the JSON data but can have multiple ``files`` paths if required.

The other options are:

.. list-table:: gdscript2rest configurable properties
    :widths: 3 10
    :header-rows: 1
    :class: tight-table

    * - Property
      - Function
    * - -h or -\-help
      - show the help message and exit. 
    * - -p PATH or -\-path PATH
      - The path to the output directory for the reStructuredText files.  Can be either an absolute or relative path.
    * - i
      - Create the index,rst file in the output directory. The index file will include the project name, the version number
        and a table of contents that includes all the files in the output directory. 
        Only one index file is created even if multiple directory sources are give.  
    * - -v or -\-verbose
      - Set the verbosity level. For example -vv sets verbosity to level 2. (Default: 0.)
    * - -\-dry-run 
      - Run the script at max verbosity without creating files. (For debugging purposes.)
    * - -V or -\-version 
      - Print the version number of the module and exit,
    * - -\-doc-version DOC_VERSION
      - Set the document version number if there is no version set in the JSON file.  Defaults to 0.0.0
      

