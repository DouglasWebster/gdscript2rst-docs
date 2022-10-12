Next steps
==========

Now that we have created the initial build of the documentation we can refresh them at any time by
running **generate_reference** again.

If you look at the documentation for **GeneratorEntity** you will see that its title is
**GeneratorEntity.gd**.  This is because there is no *class_name* allocated to this class so it defaults
to the gdscript file name. Also, the file is not very well commented.  We can fix this easily in a few
simple steps.

Open up DesignPatterns in **Godot** and amend the GeneratorEntity.gd file as follows:

.. code:: gdscript

    # This is used iniate the animation and control the anination speed
    #
    # On startup it sets the Power Source efficiency to 1.0

    class_name GeneratorEntity

    extends Node2D

    # The link to the animation - set after the animation is ready.
    onready var animation_player := $AnimationPlayer


    func _ready() -> void:
        animation_player.play("Work")
        $PowerSource.efficiency = 1.0


    # Respond to power draw by setting the animation speed to a percentage of
    # the power taken vs amount of power it's able to output
    func _on_PowerSource_power_drawn(power: float, _delta: float) -> void:
        var proportion: float = power / $PowerSource.power_amount
        animation_player.playback_speed = proportion

We can now regenerate the documentation by running the same command that built the documentation initially.
However, unless we are changing the version number there is no need set the version number or
regenerate the index file.  Also, there is probably no need to view all the logging information as well so
the command becomes 

.. tabs:: 

    .. tab:: Linux/macOS

            .. code:: shell-session

                    (.venv) [DesignPatternsDoc]$ ./generate_reference ../DesignPatterns -o APIs 

    .. tab:: Windows (cmd)

        To follow

    .. tab:: Windows (ps)
            .. code:: PowerShell

                (.venv) [DesignPatternsDoc]ps .\generate_reference ..\DesignPatterns -o APIs

Further refinements
-------------------

The software is designed to aid in the creation of larger projects where the source tree is not flat.
You can select the starting folder and document only those items in that folder and it's children.

For example if you have a project structure like 

.. code:: console

    game
    ├── characters
    │   ├── elf.gd
    │   ├── human.gd
    │   ├── dwarf.gd
    │   ├── orc.gd
    │   └── troll.gd
    ├── weapons
    │   ├── sword.gd
    │   ├── axe.gd
    │   ├── spear.gd
    │   └── club.gd
    └── item
        ├── poison.gd
        ├── gold.gd
        ├── potion.gd
        └── amulet.gd

Running the three following commands:

.. tabs:: 

    .. tab:: Linux/macOS

            .. code:: shell-session

                    (.venv) [DesignPatternsDoc]$ ./generate_reference ../game/characters -o APIs/Characters
                    (.venv) [DesignPatternsDoc]$ ./generate_reference ../game/weapons -o APIs/Weapons
                    (.venv) [DesignPatternsDoc]$ ./generate_reference ../game/item -o APIs/Items 

    .. tab:: Windows (cmd)

        To follow

    .. tab:: Windows (ps)
            .. code:: PowerShell

                    (.venv) [DesignPatternsDoc]ps .\generate_reference ..\game\characters -o APIs\Characters
                    (.venv) [DesignPatternsDoc]$ .\generate_reference ..\game\weapons -o APIs\Weapons
                    (.venv) [DesignPatternsDoc]$ .\generate_reference ..\game\item -o APIs\Items


Which would give an output like

.. code:: console

    APIs
    ├── Characters
    │   ├── elf.rst
    │   ├── human.rst
    │   ├── dwarf.rst
    │   ├── orc.rst
    │   └── troll.rst
    ├── Weapons
    │   ├── sword.rst
    │   ├── axe.rst
    │   ├── spear.rst
    │   └── club.rst
    └── Items
        ├── poison.rst
        ├── gold.rst
        ├── potion.rst
        └── amulet.rst

Even finer grain selection of items and documentation folder composition can be achieved if you 
resort to the :doc:`manual method </api_creation/rst_manual_method>`  of generating the documentation.  

I leave it to the reader to explore this option as it probably will require extensive manual control 
of the resultant project documentation.
