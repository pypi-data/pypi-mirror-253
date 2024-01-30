Customizing Rougail's configuration
=======================================

The `Rougail`\ 's configuration is located in the `RougailConfig` object:

.. code-block:: python 

    from rougail import RougailConfig

It's just a python dictionary with different keys.

To modify it, just do like with any python dictionary:

.. code-block:: python 

    RougailConfig[key] = value

Configuring the dictionnaries loading
-----------------------------------------

Setting the dictionnaries folders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two types of dictionary directories:

- the main dictionaries with the `dictionaries_dir` key. The default setting is `['/srv/rougail/dictionaries']`. This setting shall list the directories folders containing dictionaries files.

- the extra dictionaries with the `extra_dictionaries` key. The value is a dictionary with all namespaces. The key being the namespace and the value being a directory listing.

For example, to add the extra example you must do:

.. code-block:: python 

    RougailConfig['extra_dictionaries']['example'] = ['/dir1', '/dir2']

Dictionaries are loaded in the same order as the main dictionaries.

The functions file
~~~~~~~~~~~~~~~~~~~~~~~

The file which contains the custom functions is managed in the `functions_file` key and has the default value `/srv/rougail/functions.py`. This key can contain a list if there are several files.

.. important:: Functions must return a value, even if the variable being calculated is a :term:`multiple` variable. If the function can return a multiple value (a list), you must put the name of the function in the `multi_functions` key.

The `auto_freeze` variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `auto_freeze` property is only applied until a specific variable becomes `True`. By default the variable name is `instantiated_module`, but it is possible to change the name of this variable via the `auto_freeze_variable` key.

Modes
~~~~~~~~

.. glossary::

   mode
   
       modes are views on variables. 
   
       Modes are customizable in Rougail. By default the modes are `basic`, `standard` and `advanced`. It is possible to change this list via the `modes_level` key.

If you change these values, consider changing the default modes of families and variables in your dictionaries. 

Default mode for a family 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default mode for a family is `basic`. It is possible to change the default mode of a family via the `default_family_mode` key.

Default mode for a variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default mode for a variable is `standard`. It is possible to change the default mode of a variable via the `default_variable_mode` key.

Internal functions names 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is possible to add internal functions via the `internal_functions` key.
