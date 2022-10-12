Creating the Sample Godot Project
=================================

Creating the DesignPatterns Godot project is relatively simple and can be accomplished with one command.
Change into ``DesignPatternsProject``, the root folder of the project and enter:

If you are not using git then download the repository from `gds2rst_scripts <https://github.com/DouglasWebster/gds2rst_scripts.git>`_
using the green **Code** button 
        
.. image:: /images/get_scripts_zip.png

and extract the contents to a subfolder of ``DesignPatterns`` named ``DesignPatternsDoc``.

Else

.. tabs:: 

    .. tab:: Linux/macOS

        .. code:: console

            [DesignPatternsProject]$ git clone https://github.com/DouglasWebster/DesignPatterns.git


    .. tab:: Windows (cmd)

        .. code:: PowerShell

            [DesignPatternsProject]> git clone https://github.com/DouglasWebster/DesignPatterns.git

    .. tab:: Windows (ps)

        .. code:: PowerShell

            [DesignPatternsProject]ps git clone https://github.com/DouglasWebster/DesignPatterns.git


This should create ``DesignPatterns`` folder with the following structure:

.. code:: console

    DesignPatterns    
    ├── ECS
    │   ├── Components
    │   │   ├── PowerReceiver.gd
    │   │   └── PowerSource.gd
    │   ├── Entities
    │   │   ├── BatteryEntity.gd
    │   │   ├── BatteryEntity.tscn
    │   │   ├── GeneratorEntity.gd
    │   │   └── GeneratorEntity.tscn
    │   ├── Game.gd
    │   ├── Game.tscn
    │   ├── PowerSystem.gd
    │   └── Shared
    │       ├── battery_indicator.png
    │       ├── battery_indicator.png.import
    │       ├── tileset.svg
    │       ├── tileset.svg.import
    │       └── tileset.tres
    ├── Shared
    │   ├── background.png
    │   ├── background.png.import
    │   ├── monserrate_bold.tres
    │   ├── montserrat_extrabold.otf
    │   ├── player.png
    │   ├── player.png.import
    │   ├── tileset_platformer.png
    │   ├── tileset_platformer.png.import
    │   └── tileset_platformer.tres
    ├── icon.png
    ├── icon.png.import
    ├── project.godot
    └── default_env.tres

At this point, as with the documentation, I change into the ``DesignPatterns`` folder and start up a VSCode
window in that folder.  

Another advantage of having separate VSCode windows is that the DesignPatterns project does not benefit from
having a virtual python environment so there is no need to activate one.