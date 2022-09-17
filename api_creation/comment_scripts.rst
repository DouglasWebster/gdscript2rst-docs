.. _comment_godot_script_files:

Commenting Godot script files
#############################

The term Docstring is applied to the comments within the code that is meant to be extracted for
inclusion in documents detailing the use of that code.  In several languages the Docstring has a 
special format built in e.g python's ``"""this is a docstring"""`` uses a triple speech mark to delimit these comments.
Unfortunately, at the time of writing, Godot hasn't got a docstring format so the code has to be commented in a 
specific to enable extraction of these pseudo Docstrings.

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
final output.  If you want a line break then use an empty comment line to;
this will have the effect of starting an new paragraph.

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

The comment blocks must immediately precede the statement being commented and contain
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



Example reStructuredText file
-----------------------------

.. admonition:: Sample reStructuredText output
    
    .. _class_CharacterBaseClass:

    CharacterBaseClass
    ==================

    **Extends:** :godot_class:`KinematicBody2D <kinematicbody2d>`

    Description
    -----------

    The following class is the base class for all the characters in the game.

    .. warning:: Creating a character from this base class will   result in an unusable character as there are no movement   actions defined in the base.

    The class defines the minimum attributes that are common to all characters and all the other types of characters should be inherited from this base class. 

    Properties
    ----------

    +--+-----------------------------------------------------------------------------+------------------------------+-------+
    |  | :ref:`character_health<class_CharacterBaseClass_property_character_health>` | :godot_class:`float <float>` |       |
    +--+-----------------------------------------------------------------------------+------------------------------+-------+
    |  | :ref:`health<class_CharacterBaseClass_property_health>`                     | :godot_class:`float <float>` |       |
    +--+-----------------------------------------------------------------------------+------------------------------+-------+

    Methods
    -------

    +----------------------------------------------------------------------------------------------------------------------------------+----------------------------+
    | :ref:`ready<class_CharacterBaseClass_method_ready>` **(**  **)**                                                                 | var                        |
    +----------------------------------------------------------------------------------------------------------------------------------+----------------------------+
    | :ref:`am_i_stronger<class_CharacterBaseClass_method_am_i_stronger>` **(** opponents_strength: :godot_class:`float <float>` **)** | :godot_class:`bool <bool>` |
    +----------------------------------------------------------------------------------------------------------------------------------+----------------------------+
    | :ref:`do_nothing<class_CharacterBaseClass_method_do_nothing>` **(**  **)**                                                       | void                       |
    +----------------------------------------------------------------------------------------------------------------------------------+----------------------------+

    Signals
    -------

    .. _class_CharacterBaseClass_signal_state_changed:

    _ **state_changed** **(**  **)**

    Let anyone who is interested know when this character changes state 

    Enumerations
    ------------

    .. _enum_CharacterBaseClass_CHARACTER_STATE:

    .. _class_CharacterBaseClass_constant_ALIVE:

    .. _class_CharacterBaseClass_constant_DEAD:

    .. _class_CharacterBaseClass_constant_LIMBO:

    enum **CHARACTER_STATE** :

    - **ALIVE** = **0**
    - **DEAD** = **1**
    - **LIMBO** = **2**

    A character can be in one of three states - it is fantasy after all! 

    Constants
    ---------

    .. _class_CharacterBaseClass_constant_MAX_HEALTH:

    - **MAX_HEALTH** :float = **150** --- Normally health will not go above 100% but certain potions and spells could override this. The override is not allowed to go too high though 

    Property Descriptions
    ---------------------

    .. _class_CharacterBaseClass_property_character_health:

    - **character_health** : :godot_class:`float <float>`

    ----

    .. _class_CharacterBaseClass_property_health:

    - **health** : :godot_class:`float <float>`

    The characters actual health normally starts at 100% 

    Method Descriptions
    -------------------

    .. _class_CharacterBaseClass_method_ready:

    - METHOD **ready(**  **)** -> var

    but all non virtual functions are listed out. 

    ----

    .. _class_CharacterBaseClass_method_am_i_stronger:

    - METHOD **am_i_stronger(** opponents_strength: :godot_class:`float <float>` **)** -> :godot_class:`bool <bool>`

    The function documentation will list all parameters with their respective types if known. It will also list the return type as well if there is one. 

    ----

    .. _class_CharacterBaseClass_method_do_nothing:

    - METHOD **do_nothing(**  **)** -> void

    And this comment doesn't get reported either but the function will, just without an explanation! 
