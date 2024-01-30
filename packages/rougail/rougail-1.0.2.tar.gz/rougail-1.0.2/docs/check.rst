Verification function
==========================

Synopsis
-------------

A verification is a complementary validation to the type which allows the content of a variable to be validated more precisely.

A :term:`validator` is necessarily a Jinja type calculation.

Parameters
--------------

Depending on the types of calculation, the parameters will be different:

.. list-table:: 
   :widths: 15 25 20 15
   :header-rows: 1
   
   * - **Calculation type**
     - **Parameter**
     - **Comments**
     - **Sample**
     
   * - 
     - **type** 
     
       `string`
       
       `mandatory`
     - Type of calculation, the only possible value is: jinja    
     - jinja
   * - **jinja** 
     
       `string`
       
       `mandatory`
     - Jinja template
     - {% if rougail.variable == 'not_allowed' %}not allowed!{% endif %}
     - 
   * - **params**
       
       `list`
     - Additional parameters passed to the Jinja template
     - 
     - 

There are two types of parameter:

- the standard parameters (string, boolean, integer, null), in this case just do: "key: value"
- advanced settings:
  
  - parameter via a variable
  - parameter via an information
  - parameter via a suffix: in the case of a variable in a dynamic family
  - parameter via an index: in the case of a :term:`follower` variable
  
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
     - Parameter's name 
     - my_param
   * - 
     - **type** 
     
       `string`
       
       `mandatory`
     - Type of parameter, possible values are: variable, information, suffix or index
     - suffix 
   * - Variable
     - **variable** 
     
       `string`
       
       `mandatory`
     - variable's name
     - rougail.variable
   * - Variable (`mandatory`) information
     - **propertyerror**
     
       `boolean`
     - If access to the variable is not possible due to a property 
       (for example `disabled`) by default an error is returned. 
       If the attribute is `False`, the parameter is not passed to the Jinja template.
       
       **Default value**: `True`
     - True  
   * - Information
     - **information** 
     
       `string`
       
       `mandatory`
     - Name of the information whose value we want to retrieve.
     - doc

Samples
--------------

Strict verification of values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is a simple example of validating values:

.. code-block:: yaml

    ---
    version: '1.0'
    my_variable:
      validators:
        - type: jinja
          jinja: |
            {% if rougail.my_variable and not rougail.my_variable.islower() %}
            {{ rougail.my_variable }} is not lowercase string
            {% endif %}        
     

A verification function must take into account 2 important aspects:

- the value may not be entered (even if the variable is mandatory), the None value must be taken into account
- if the value is invalid, a sentence must be returned with an explicit message.

From now on only `None` and lowercase values will be allowed.       

Checking values with warning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the constraint, it is possible to specify the error level and put it as a warning:

.. code-block:: yaml

    ---
    version: '1.0'
    my_variable:
      validators:
        - type: jinja
          jinja: |+
            {% if rougail.my_variable and not rougail.my_variable.islower() %}
            {{ rougail.my_variable }} is not lowercase string
            {% endif %}        
          params:
            warnings_only: true

In this case a value with a capital letter will be accepted, but a warning message will appear.

Verification with parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    ---
    version: '1.0'
    my_hidden_variable:
      disabled: true
    my_variable:
      validators:
        - type: jinja
          jinja: |
            {% if param1 is defined and rougail.my_variable == param1 %}
            has same value as rougail.unknown_variable
            {% endif %}
            {% if param2 is defined and rougail.my_variable == param2 %}
            has same value as rougail.my_hidden_variable
            {% endif %}        
          params:
            param1:
              type: variable
              variable: rougail.unknown_variable
              optional: true
            param2:
              type: variable
              variable: rougail.my_hidden_variable
              propertyerror: false

An example with a suffix type parameter:

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
        validators:
          - type: jinja
            jinja: |
              {% if rougail.my_dyn_family_.my_dyn_var == param1 %}
              forbidden!
              {% endif %}          
            params:
              param1:
                type: suffix

In this example, we see a dynamic family. Two families will be created: `rougail.my_dyn_family_val1.my_dyn_var` and `rougail.my_dyn_family_val2.my_dyn_var`.

The value of the variable within this family cannot be equal to the value 
of the suffix (`val1` and `val2` respectively).

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
        type: number
        validators:
          - type: jinja
            jinja: |
              {% if rougail.family.follower1 == param1 %}
              forbidden!
              {% endif %}          
            params:
              param1:
                type: index

Redefinition
---------------

In a first dictionary, let's declare our variable and its verification function:

.. code-block:: yaml

    ---
    version: '1.0'
    my_variable:
      validators:
        - type: jinja
          jinja: |
            {% if rougail.my_variable and not rougail.my_variable.islower() %}
            {{ rougail.my_variable }} is not lowercase string
            {% endif %}        

In a second dictionary it is possible to redefine the calculation:

.. code-block:: yaml

    ---
    version: '1.0'
    my_variable:
      redefine: true
      validators:  
        - type: jinja
          jinja: |
            {% if rougail.my_variable and ' ' in rougail.my_variable %}
            {{ rougail.my_variable }} has a space
            {% endif %}        

In this case only this validator will be executed.

Here is a third dictionary in which we remove the validation:

.. code-block:: yaml

    ---
    version: '1.0'
    my_variable:
      redefine: true
      validators:
