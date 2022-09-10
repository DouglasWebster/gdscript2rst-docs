
Commenting Godot script files
#############################

The term Docstring is applied to the comments within the code that is meant to be extracted for
inclusion in documents detailing the use of that code.  In several languages the Docstring has a 
special format built in e.g python uses a triple speech mark to delimit these comments - 
``"""this is a docstring"""``.  Unfortunately, at the time of writing Godot does not have this
built in so the code has to be commented in a specific to enable extraction of these Docstrings.

The following guidelines detail how to comment your script files.

Enabling a script file for Commenting
-------------------------------------

In order for a script file to be documented it must have the ``class_name`` defined.  If the
``class_name`` is defined then any comment appearing at the beginning of the script file will be used
as the general description of the class.

For example:

.. code-block:: gdscript

    # The following class is the base class for all the characters in the game.
    #
    # The class defines the minimum attributes that are common to all
    # characters and all the other types of characters should be
    # inherited from this base class.

    class_name CharacterBaseClass
    extends KinematicBody2D
    .
    .
    . 

.. note:: The first contiguous block of comments at the start of the script file will be used
    as the general description and does not have to immediately precede the ``class_name`` statement.

Format of comments
------------------

The comments can span multiple lines but they **must not** include an empty line.
Commented lines will be concatenated together in the
final output.  If you want a line break then separate the comment with and empty line.
This will have the effect of starting an new paragraph.

This can be used to advantage as restructuredText directives can be incorporated into the comment.

.. code-block:: gdscript

    # The following class is the base class for all the characters in the game.
    #
    #.. warning:: Creating a character from this base class will
    #   result in an unusable character as there are no movement
    #   actions defined in the base.
    #
    # The class defines the minimum attributes that are common to all 
    # characters and all the other types of characters should be 
    # inherited from this base class.

    class_name CharacterBaseClass
    extends KinematicBody2D
    .
    .

The section

.. code-block:: gdscript

    #
    #.. warning:: Creating a character from this base class will
    #   result in an unusable character as there are no movement
    #   actions defined in the base.
    #

will result in the the warning highlighting appearing in the final Sphinx document like this:

.. warning:: Creating a character from this base class will
    result in an unusable character as there are no movement
    actions defined in the base.

What can be documented?
-----------------------

* classes
* properties i.e, enums, constants, signals and variables
* functions

The comment blocks must immediately precedes the statement being commented and contain
no uncommented lines.

What isn't documented
---------------------

* All virtual callback functions.
* Comments inside of functions are ignored - function internals should be private!

Example Script file
-------------------

.. code:: gdscript

    # The following class is the base class for all the characters in the game.
    #
    #.. warning:: Creating a character from this base class will
    #   result in an unusable character as there are no movement
    #   actions defined in the base.
    #
    # The class defines the minimum attributes that are common to all 
    # characters and all the other types of characters should be 
    # inherited from this base class.

    class_name CharacterBaseClass
    extends KinematicBody2D

    # A character can be in one of three states - it is fantasy after all!
    enum CHARACTER-STATE {
        ALIVE,
        DEAD,
        LIMBO
    }

    # Normally health will not go above 100% but certain potions and spells
    # could override this.
    # The override is not allowed to go too high though
    const MAX_HEALTH := 150.0

    # The characters actual health normally starts at 100%
    var health := 100.0

    # Let anyone who is interested know when this character changes state
    signal state_changed


    # This comment is purely internal as the gdscript2rest ignores all inbuilt
    # virtual callback functions.
    func _ready():
        return ready():


    # but all non virtual functions are listed out.
    func ready():
        return "All set, let's begin."


    # The function documentation will list all parameters with their respective
    # types if known. It will also list the return type as well if there is one.
    func am_i_stronger(opponents_strength: float) -> bool:

        # An internal comment is not documented - function internals SHOULD 
        # remain private!  Later on I might change how I determine if the 
        # character is stronger or not and I don't want to have to redo
        # all the API

        return opponents_strength < my_strength


    # And this comment doesn't get reported either
    # but the function will, just without an explanation!

    func do_nothing() -> void:
        pass

