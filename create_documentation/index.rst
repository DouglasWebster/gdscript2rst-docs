Creating the project documentation
==================================

In this section of the tutorial I shall base my instructions on the the 
Component-Entity design pattern which is a partial 
fork of the `GDQuest Design Patterns <https://github.com/GDQuest/godot-design-patterns>`_ project.
This is available `here <https://github.com/DouglasWebster/DesignPatterns>`_ 

The following assumes that you have *git* installed on your system.  If not then where the instructions are
to clone a repository you will have to download the zip file of the repository and unpack it to the relevant
directory.  The :doc:`/getting_started/installation/scripts` chapter has information on using
zip for extracting github repositories onto your system.  

Create a folder to hold the complete code for this tutorial - I called mine ``DesignPatternsProject``.  

After creating the root directory we can proceed with setting up the folders to hold both the example Godot
project and the documentation project.

.. note:: 
    The Godot project folder and the documentation folder do not have to be from a common root - I am only
    setting it up like this to make the instructions and diagrams easier.  The programs do not care where 
    the Godot project is as long as you can supply the path.

    P.S. I try to avoid names with spaces - they play havoc with parsing paths for lots of programs unless 
    you pass in the name correctly.

.. toctree:: 
    :maxdepth: 1

    doc_folder_setup
    godot_folder_setup
    first_build
    second_stage