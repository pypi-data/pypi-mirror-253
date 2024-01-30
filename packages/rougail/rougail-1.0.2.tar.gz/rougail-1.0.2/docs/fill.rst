Calculated default values
==============================

Synopsis
-----------

A value can be calculated. In this case we have four possibilities:

- calculation via Jinja
- calculation via a variable
- calculation via information
- calculation via a suffix: in the case of a variable in a dynamic family
- calculation via an index: in the case of a follower variable

If the user modifies the value of the variable, the default value is no longer used, so the calculation is no longer carried out. This is also the case if the variable has the `auto_save` attribute.

On the other hand, if the variable is hidden (with the `hidden` parameter), it is the default value that is used and not the value customized by the user.

.. note:: A follower variable cannot be calculated automatically.

Parameters
--------------

Depending on the types of calculation, the parameters will be different:

.. list-table:: 
   :widths: 15 25 20 15
   :header-rows: 1
   
   * - Calculation type 
     - Parameter
     - Comments
     - Sample

   * - 
     - **type** 
     
       `string`
       
       `mandatory`
       
     - Type of calculation, possible values are: jinja, variable, information, suffix or index
     - jinja
   * - Jinja 
     - **jinja**
     
       `string`
       
       `mandatory`
     - Template Jinja. For a multiple variable, each line represents a value.
     - `{% if rougail.variable %}

       {{ rougail.variable }}

       {% endif %}`
   * - Jinja 
     - **params** 
     
       `list` 
     - Additional parameters passed to the Jinja template
     -  
   * - Variable (`mandatory`)

       Information
     - **variable** 

       `string`
     - Name of associated variable
     - rougail.variable 
   * - Variable
     - **propertyerror** 
     
       `boolean`
     - If access to the variable is not possible due to a property (for example `disabled`) by default an error is returned. If the attribute is `false`, the calculated value is empty.

       **Default value:** `true`
     - false 
     
   * - Information
     - **information**
            
       `string`
       
       `mandatory`
     - Name of the information whose value we want to retrieve.
     - doc

In the case of a Jinja type calculation, it is possible to have parameters.

There are two types of parameter:

-  the standard parameters (string, boolean, integer, null), in this case just do: "key: value"

-  the advanced settings:

    - parameter via a variable
    - parameter via an information
    - parameter via a suffix: in the case of a variable in a dynamic family
    - parameter via an index: in the case of a follower variable

.. list-table:: 
   :widths: 15 25 20 15
   :header-rows: 1
   
   * - Parameter type 
     - Parameter
     - Comments
     - Sample

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
     - parameter's type, possible values are: variable, information, suffix or index
     - suffix
   * - Variable
     - **variable**
     
       `string`
       
       `mandatory`
 
     - Variable's name 
     - rougail.variable
   * - Variable (`mandatory`) information
     - **propertyerror** 
     
       `boolean`
     - If access to the variable is not possible due to a property (for example `disabled`) by default an error is returned. If the attribute is `False`, the parameter is not passed to the Jinja template.
     - **Default value**: `True`
   * - Variable 
     - **optional**
             
       `boolean`
     - The variable may not exist depending on YAML file imports. 
       If the optional parameter is `True`, the parameter will simply be deleted if the variable does not exist.

       Default value : `False`  
     - True
   * - Information
     - **information**
     
       `string`
       
       `mandatory`
     - Name of the information whose value we want to retrieve.
     - doc
     
Examples
-----------

Calculation via a Jinja template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's start with an example from a simple Jinja template:

.. code-block:: yaml

    ---
    version: '1.0'
    my_calculated_variable:
      default:
        type: jinja
        jinja: 'no'

Here is a second example with a boolean variable:        

.. code-block:: yaml

    ---
    version: '1.0'
    my_calculated_variable:
      type: boolean
      default:
        type: jinja
        jinja: 'false'

And a multiple value of the number type:

.. code-block:: yaml

    ---
    version: '1.0'
    my_calculated_variable:
      type: number
      multi: true
      default:
        type: jinja
        jinja: |
          1
          2
          3      

Let's create a variable whose value is returned by a python function:

.. code-block:: yaml

    ---
    version: '1.0'
    my_calculated_variable:
      default:
        type: jinja
        jinja: '{{ return_no() }}'

Then let's create the `return_no` function:

.. code-block:: python 

    def return_no():
        return 'no'

An example with parameters:

.. code-block:: yaml

    ---
    version: '1.0'
    my_calculated_variable:
      description: my description
      default:
        type: jinja
        jinja: |
                {{ param1 }}{% if param2 is defined %}_{{ param2 }}{% endif %}_{{ param3 }}
        params:
          param1: value
          param2:
            type: variable
            variable: rougail.unknown_variable
            optional: true
          param3:
            type: information
            information: doc
            variable: rougail.my_calculated_variable

An example with a `suffix` type parameter:

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
        default:
          type: jinja
          jinja: 'the suffix is: {{ param1 }}'
          params:
            param1:
              type: suffix

In this example, we see a dynamic family. Two families will be created: `rougail.my_dyn_family_val1.my_dyn_var` and `rougail.my_dyn_family_val2.my_dyn_var`.

The value of the variable inside this family 'this suffix is: ' + the value of the suffix (`val1` and `val2` respectively).

An example with an index type parameter:

.. code-block:: yaml

    ---
    version: '1.0'
    family:
      type: leadership
      leader:
        multi: true
        default:
          - val1
          - val2
      follower1:
        default:
          type: jinja
          jinja: 'the index is: {{ param1 }}'
          params:
            param1:
              type: index

Calculation via a variable
-----------------------------

Copy a variable in another: 

.. code-block:: yaml

    ---
    version: '1.0'
    my_variable:
      multi: true
      default:
        - val1
        - val2
    my_calculated_variable:
      multi: true
      default:
        type: variable
        variable: rougail.my_variable

Copy one variable to another if the source has no `property` problem:

.. code-block:: yaml

    ---
    version: '1.0'
    my_variable:
      default: val1
      disabled: true
    my_calculated_variable:
      multi: true
      default:
        type: variable
        variable: rougail.my_variable
        propertyerror: false

Copy two non-multiple variables into a multiple variable:

.. code-block:: yaml

    ---
    version: '1.0'
    my_variable_1:
      default: val1
    my_variable_2:
      default: val2
    my_calculated_variable:
      multi: true
      default:
        - type: variable
          variable: rougail.my_variable_1
        - type: variable
          variable: rougail.my_variable_2

A variable in a dynamic family can also be used in a calculation.

For example using the variable for a particular suffix:

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
      my_dyn_var_:
        type: string
        default:
          type: suffix
    all_dyn_var:
      default:
        type: variable
        variable: rougail.my_dyn_family_val1.my_dyn_var_val1

In this case, we recover the value `val1`.

Second example using the variable for all suffixes:

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
      my_dyn_var_:
        type: string
        default:
          type: suffix
    all_dyn_var:
      multi: true
      default:
        type: variable
        variable: rougail.my_dyn_family_.my_dyn_var_

In this case, we recover the `val1` and `val2` list.

Calculation via a suffix
---------------------------

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
      my_dyn_var_:
        type: string
        default:
          type: suffix

Calculation via an index
--------------------------

.. code-block:: yaml

    ---
    version: '1.0'
    family:
      type: leadership
      leader:
        multi: true
        default:
          - val1
          - val2
      follower1:
        type: number
        default:
          type: index

Redefinition
----------------

In a first dictionary, let's declare our variable and our calculation:

.. code-block:: yaml

    ---
    version: '1.0'
    my_calculated_variable:
      default:
        type: jinja
        jinja: 'the value is calculated'

In a second dictionary, it is possible to redefine the calculation:

.. code-block:: yaml

    ---
    version: '1.0'
    my_calculated_variable:
      redefine: true
      default:
        type: jinja
        jinja: 'the value is redefined'

In a third dictionary, we even can delete the calculation if needed:

.. code-block:: yaml

    ---
    version: '1.0'
    my_calculated_variable:
      redefine: true
      default: null

