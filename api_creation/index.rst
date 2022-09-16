#######################
API Creation
#######################

The following sections deals with creating the API documentation manually from a projects Godot script files.
It is assumed that Python is working correctly and that the gdscript2rest module is installed.

The creation of the the documentation from the Godot script files is a three stage process:

#. The script files have to be commented correctly so that the relevant data can be extracted.
#. A reference file is created from the commented script files.
#. The data in the reference file is converted to restructured documents, one for each class.

There is the short way to do it and the long way, both of which will be described.  Whichever way
you go the Godot script files have to be commented in a specific way in order for the data to be extracted.

After commenting the Godot script files correctly the reStructuredText files can be generated one of two ways:

* automatically using a script file (linux/macOS) or a bat file (windows)
* manually using the two python modules.

.. note:: 

   For most project documentation the automatic method should be perfectly adequate.  If very
   fine grained partitioning of the documentation is required then the manual method might be
   required.

.. toctree:: 
   :maxdepth: 1
   
   Comment Godot script files <comment_scripts>
   Linking user docs to Godot help files <create_godot_hyperlinks>
   Automatic method <rst_using_scripts>
   Manual method <rst_manual_method>


.. important:: 
   The code for this part of the project was adapted from the 
   `gdscript-doc-maker <https://github.com/GDQuest/gdscript-docs-maker>`_ 
   written by `GDQuest <gdquest.com>`_ and can be referenced if you require
   plain markdown and/or hugo format files. 

   I assume that if you are using Godot then `GDQuest <gdquest.com>`_ is familiar
   to you. If not then I strongly recommend checking out their site as there is
   plenty of excellent material for the Godot coder. 