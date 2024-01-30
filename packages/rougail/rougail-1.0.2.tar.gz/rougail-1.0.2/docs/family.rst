A family
============

Synopsis
---------

A family is a container of variables and subfamily.

.. attention:: A family without a subfamily or subvariable will be automatically deleted.

Name
-------------

It is with this name that we will be able to interact with the family.

It's best to follow the :ref:`convention on variable names`.

Parameters
---------------

.. FIXME: faire une page sur la "convention on variable names"

.. list-table:: 
   :widths: 15 45
   :header-rows: 1

   * - Parameter
     - Comments
       
   * - type, _type

       `string`
       
     - possile values:
     
       - `family` (**default value**)
       - `leadership`
       - `dynamic`
       
       .. note:: If a subfamily or a subvariable already has the name `"type"`, it is possible to use the `"_type"` attribute.

   * - description, _description

       `string`
     - Description of the family.
       
       User information to understand the usefulness of the family.

       ..note:: If a subfamily or subvariable already has the name "description" it is possible to use the "_description" attribute.

   * - help, _help

       `string`
     - Additional help associated with the family.

       .. note:: If a subfamily or a subvariable already has the name "help" it is possible to use the "_help" attribute.       

   * - mode, _mode

       `string`
     - Family mode.

       The default mode of a family is the smallest mode of the parent families, child variables, or child families that are contained in that family.
       
       This mode also allows you to define the default mode for variables or families included in this family.
       
       .. note:: If a subfamily or a subvariable already has the name "mode" it is possible to add the "_mode" attribute.

   * - hidden, _hidden

       `string`
     - Invisible family.
     
       Allows you to hide a family as well as the variables or families included in this family.

       This means that the family will no longer be visible in `read-write` mode, but only for calculations or in `read-only` mode.

       .. note:: If a subfamily or a subvariable already has the name "hidden" it is possible to add the "_hidden" attribute.  

   * - disabled, _disabled

       `string`

     - Disabled family.
     
       Allows you to deactivate a family as well as the variables or families included in this family.
     
       This means that the family will no longer be visible to the user but also to a :term:`calculation`.

       .. note:: If a subfamily or a subvariable already has the name "disabled" it is possible to use the "_disabled" attribute.

Dynamically created family
-----------------------------

To create a family dynamically, you must create a fictitious family linked to a variable. 
The family name and description will actually be the prefix of the new name / description. 
The suffix will come from the value of the bound variable. 
The name of the families and variables it contains will be preserved, however, the description will be the prefix of the real description.

Obviously if the content of the linked variable were to evolve, new dynamic families will appear or disappear.

To note that:

- the variable linked to the family must be a multiple variable
- it is not possible to put a simple family into a dynamic family
- it is possible to put a leading family into a dynamic family     

Leader or foller variable
-----------------------------

A leader family has a typical attribute of “leadership”. The type is required.

A leader family 
----------------

The leader and follower variables are placed in a leader family.

A leader family cannot contain other families.

The default mode of the leader family is the mode of the leader variable.

Leader variable
----------------

A leader variable is a variable that will guide the length of other variables (called follower variables).

A leader variable is a :doc:`variable` that must have the `multiple` type.

A leader variable may be mandatory.

The default mode corresponds to the smallest mode defined for the follower variables.

Follower variable
--------------------

A follower variable is a variable whose length is not determined by itself, but is identical to that of the leader variable on which it depends.

A follower variable is a variable placed just behind a leader variable or another follower variable.

The order in which the tracking variables are defined is important.

This variable can be of multiple type. In this case, for a determined index of the leading variable, it is possible to put several values to the same variable.

A follower variable may be required. This means that when a leader variable is entered, the follower variable must also be a value at the index considered. If no value is defined for the leader variable, no value is specified for the follower variable.

The default mode of a follower variable corresponds to the mode of the leader variable.

If a leader variable is hidden or disabled, the follower variables will be hidden or disabled as well.

Examples
----------

Simple family 

.. code-block:: yaml

    ---
    version: '1.0'
    my_family:
      type: family
      description: This is a great family
      help: This is the help of a great family
      mode: expert

Dynamically created family 
----------------------------

.. code-block:: yaml

    ---
    version: '1.0'
    varname:
      multi: true
      default:
        - val1
        - val2
    my_dyn_family_:
      type: dynamic
      variable: rougail.varname
      description: 'Describe '
      my_dyn_var:
        type: string
        description: 'Variable description for '

This will dynamically create two families:

- "rougail.my_dyn_family_val1" with the description "Describe val1"
- "rougail.my_dyn_family_val2" with the description "Describe val2"

In the dynamic family "rougail.my_dyn_family_val1" we will find a variable "my_dyn_var" with the description "Variable description for val1".

Leader or follower variable 
-------------------------------

Definition of leader and follower variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is an example of defining a leading variable and two following variables:

.. code-block:: yaml

    ---
    version: '1.0'
    family:
      type: leadership
      leader:
        multi: true
      follower1:
      follower2:
        multi: true

Adding a new follower variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add a new follower variable, in a new dictionary, simply define one or more new variables in the leader family:

.. code-block:: yaml

    ---
    version: '1.0'
    family:
      follower3:

