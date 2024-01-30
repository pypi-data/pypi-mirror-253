Calculated properties
==========================

Synopsis
------------

Calculated properties allow you to add or remove properties to a :term:`variable`
or a :term:`family` depending on the context.

Here is the list of editable properties:

.. list-table:: 
   :widths: 15 15 25
   :header-rows: 1
   
   * - **Attribute applicable on**
     - **Property's name**
     - Comment
     
   * - Variable
   
       Family 
     - hidden
     - Hides a variable or a family, in this case it is not accessible in `read-write` mode, 
       but remains accessible in a calculation or in `read-only` mode
   * - Variable
   
       Family 
     - disabled
     - Deactivates a variable or family, in this case it is never accessible
   * - Variable
     - mandatory
     - The variable expects a value other than `None` or `[]` for multiple variables

A property can be calculated. In this case we have two possibilities:

- calculation via Jinja
- calculation via a variable          

Parameters
---------------

.. list-table:: 
   :widths: 15 25 20 15
   :header-rows: 1
   
   * - **Calculation type**
     - **Parameter**
     - **Comment**
     - **Sample**
   * - 
     - **type**
     
       `string`
       
       `mandatory`
     - Calculation type, possible values are: jinja, variable, information, suffix or index  
     - jinja
   * - Jinja 
     - **jinja**
     
       `string`
       
       `mandatory`
     - Jinja template . For a multiple variable, each line represents a value.
     - {% if rougail.variable %}

       {{ rougail.variable }}

       {% endif %}
   * - Jinja
     - **params**
     
       `list`
     - Additional parameters passed to the Jinja template
     - 
   * - Variable
     - **variable**
     
       `string`
       
       `mandatory`
     - Name of the associated variable.
     
       .. attention:: The variable must be of `boolean` type.
     - rougail.variable 
   * - Variable
     - **propertyerror**
     
       `boolean` 
     - If access to the variable is not possible due to a property 
       (for example `disabled`) by default an error is returned. 
       If the attribute is `False`, the calculated value is False.

       **Default value**: `True`
     - False

In the case of a Jinja type calculation, it is possible to have parameters.

There are two types of parameter:

- the standard parameters (string, boolean, integer, null), in this case just do: "key: value"

- advanced settings:

   - parameter via a variable
   - parameter via information
   - parameter via a suffix: in the case of a variable in a dynamic family
   - parameter via an index: in the case of a follower variable       
   
.. list-table:: 
   :widths: 15 25 20 15
   :header-rows: 1
   
   * - **Parameter's type**
     - **Parameter**
     - **Comments**
     - **Sample**
   * - 
     - **name**
     
       `string`
       
       `mandatory`
     - parameter's name 
     - my_param
   * - 
     - **type**
     
       `string`
       
       `mandatory`
     - Parameter's type, possible values are: variable, information, suffix or index
     - suffix
   * - Variable 
     - **variable**
     
       `string`
       
       `mandatory`
     - variable's name 
     - rougail.variable
   * - Variable (`mandatory`) Information   
     - **propertyerror**
     
       `boolean`
     - If access to the variable is not possible due to a property (for example `disabled`) by default an error is returned. If the attribute is False, the parameter is not passed to the Jinja template.

       **Default value**: `True`
     - False
   * - Variable
     - **optional**
     
       `boolean`
     - The variable may not exist depending on YAML file imports. If the optional parameter is True, the parameter will simply be deleted if the variable does not exist.
       **Default value**: `False`
     - True
     
   * - information
     - **information**
     
       `string`
       
       `mandatory`
     - Name of the information whose value we want to retrieve.
     - doc

Samples
------------

A Jinja-type calculated property
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is possible to write the condition in Jinja:


.. code-block:: yaml

    ---
    version: '1.0'
    condition:
      default: 'do not hide!'
    my_variable:
      hidden:
        type: jinja
        jinja: |
          {% if rougail.condition and rougail.condition == "hide!" %}
          this rougail.condition value is 'hide!'
          {% endif %}      
          
           
In this case the variable is hidden if the value of the variable "rougail.condition" is `hide!` and it did not hide for any other value. Be careful, always take into consideration that "rougail.condition" can be equal to `None`.

The message returned by the function is visible in the error message in the event of an access problem:                  

.. code-block:: python

    >>> from rougail import Rougail, RougailConfig
    >>> RougailConfig['dictionaries_dir'] = ['dict']
    >>> rougail = Rougail()
    >>> config = rougail.get_config()
    >>> config.property.read_write()
    [..]
    tiramisu.error.PropertiesOptionError: cannot access to option "my_variable" because has property "hidden" (this rougail.condition value is 'hide!')

It is possible to use parameters when calculating properties as for calculating the `default` attribute.

A calculated property of variable type 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A variable can therefore be calculated via the result of another variable. Please note, this other variable must be of `boolean` type:

.. code-block:: yaml

    ---
    version: '1.0'
    condition:
      type: boolean
    my_variable:
      hidden:
        type: variable
        variable: rougail.condition

If the value of the variable "rougail.condition" is `True` then the variable "rougail.my_variable" is hidden.

Redefintion
~~~~~~~~~~~~~~~~~

It may be that in a dictionary we decide to define a condition.

To delete the calculation from a variable, simply do in a new dictionary:

.. code-block:: yaml

    ---
    version: '1.0'
    my_variable:
      redefine: true
      hidden:

