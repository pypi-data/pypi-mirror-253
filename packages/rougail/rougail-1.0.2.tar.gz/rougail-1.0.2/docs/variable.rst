The variables
===================

Synopsis
------------

.. glossary::

   variable
   variables

        A variable is an abstract black box (container) paired with an associated symbolic name, which contains some defined or undefined quantity of data referred to as a `value`.
        
.. discussion:: This definition, makes a heavy use of data typing.
                Indeed, depending on the type system definition of the constistency handling system used, variables may only be able to store a specified data type.
                OK, variables are the containers for storing the values. It has something to do with typing. 
                But this is not just about typing.

Name
-------------
       
Variable's associated symbolic name.
       
It's best to follow the :ref:`convention on variable names`.

Parameters
-------------

.. list-table:: 
   :widths: 15 45
   :header-rows: 1
   
   * - Parameter
     - Comments
   
   * - **help**

       `string` 
     - Additional help associated with the variable.
     
   * - **default** 
     - Default value(s) of the variable.
       
       This value is typed, you must correctly fill out the YAML file to avoid defining a value with an incorrect type. For example, a `number` must be a digit type, a multiple variable must be a `list` type, ...
       
       For a non :term:`leading` multiple variable, the first value defined in the list will also be the default value proposed if a new value is added to this variable.

   * - **validators**

       `list`
     - Value validators.
     
       Jinja template list. The value of the variable will be considered invalid if the template has a return value.    
   * - **auto_save**

       `boolean` 
     - Variable with automatically modified value.
       
       A variable with automatically modified value is a variable whose value will be considered as *modified* (that is, it is no longer the variable's default value).

       For example, if the value of this variable comes from a calculation, the value will no longer be recalculated.

       These variables are usually :term:`required` variables. In fact, these variables are only automatically modified if they have a value.
       
       A :term:`leader` or :term:`follower` variable cannot have the `auto_save` property.

       **Default value**: `false`
   * - **mode**

       `string`
     - Variable's mode.
     
       **Default value**: The `default` mode of a variable is the mode of the parent family.

       Special cases :
       
       - a variable with an automatically modified value or an automatic read-only variable is by default in `basic` mode
       - if the variable is not in a family, the variable will have a `standard` mode by default
       - a :term:`mandatory` variable without default value (calculate or not) will have a `basic` mode
   * - **multi**

       `boolean`
     - The value of the variable is a list.

       **Default value**: `false`
   * - **unique**

       `boolean`
     - The :term:`multiple` type variable accepts the same value several times. If unique is set to `false`, a :term:`multiple` variable only accepts the same value once in the list.

       **Default value**: `false`
   * - **hidden**

       `boolean` or :term:`calculation` 
     - Invisible variable.
        
       Enables us to *hide* a variable.

       This means that the variable will no longer be visible in `read-write` mode, but only for calculations or in `read-only` mode.
        
       When a variable is made invisible, the user will not be able to modify its value; if he has already succeeded in modifying it, this value will not be taken into account.

       **Default value**: `false`
   * - **disabled**

       `boolean` or :term:`calculation` 
     - Disabled variable.

       Allows us to deactivate a variable.

       This means that the variable will no longer be visible to the user but also to a :term:`calculation`.

       **Default value**: `false`.
   * - **mandatory**

       `boolean` or :term:`calculation` 
     - Mandatory variable.

       Variable whose value is `required`.

       For a multiple variable, this means that the list shall not be empty.

       **Default value**: `true`
   * - **redefine**

       `boolean`
     - It is possible to define a variable in one :term:`dictionary` and change its behavior in a second :term:`dictionary`. In this case you must explicitly redefine the variable.

       **Default value**: `false`
   * - **exists**

       `boolean`
     - This attribute does two things:

         - creates a variable if it does not exist in another :term:`dictionary` (otherwise do nothing), in this case the value of the attribute must be `true`
         - in conjunction with the `redefine` attribute set to `true`, only modifies the behavior if it is pre-existing, in which case the attribute's value must be `false`.
         
       **Default value**: `null`
   * - **test**

       `list`
     - The `test` attribute is a special attribute that allows :term:`dictionary` designers to influence a test robot by specifying useful values to test.
     
       Concretely, the content of this attribute is recorded in the `information` attribute of the corresponding `Tiramisu` option object.

Variables types
----------------
         
A variable **has a type**.

This type enables the variable to define the values that are accepted by this variable.

.. list-table:: 
   :widths: 15 25 20 15
   :header-rows: 1
   
   * - Value
     - Comments
     - Parameters
     - Samples
     
   * - string
     - character string (default type)
     - 
     - test
       
       "1"

       "true"
   * - number
     - a number 
     - `min_number`: minimum number allowed
     
       `max_number`: maximum number allowed
     - 1
   * - float
     - a floating number
     - 
     - 1.2
   * - boolean
     - A boolean, if no value is defined the default value of this variable will be `true`, the variable will also be :term:`mandatory` by default
     - 
     - `true`
     
       `false`
   * - secret
     - a secret (like a password, a private key, etc.)
     - 
     - `hO_'hi`
   * - mail 
     - a mail address 
     - 
     - test@rougail.example
   * - unix_filename
     - a file name in the Unix meaning
     - 
     - :file:`/etc/passwd`
   * - date 
     - a date in the format `%Y-%m-%d`
     - 
     - `2021-01-30`
   * - unix_user
     - a user in the Unix meaning 
     - 
     - test
   * - ip
     - any kind of IPv4 address
     - `private_only`: only private IPs (`false` by default)

       `allow_reserved`: allows reserved IPs (`true` by default)
     - `1.2.3.4`
   * - cidr
     - any IPv4 address in the CIDR format
     - `private_only`: only private IPs (`false` by default)
     
       `allow_reserved`: allows reserved IPs (`false` by default) 
     - `1.2.3.4/24`
   * - netmask
     - mask of an IPv4 address
     - 
     - `255.255.255.0`
   * - network
     - network address
     - 
     - `192.168.1.0`
   * - network_cidr
     - network address in CIDR format
     - 
     - `192.168.1.0/24`
   * - broadcast
     - broadcast address
     - 
     - `255.255.255.255`
   * - netbios
     - netbios name 
     - 
     - machine
   * - domainname
     - domain name 
     - `allow_ip`: allows an IP rather than a domain name (`false` by default)
       
       `allow_cidr_network`: allows a CIDR type network address (`false` by default)
       
       `allow_without_dot`: allows names without a dot (`false` by default)
       
       `allow_startswith_dot`: allows starting with a point (`false` by default)
     - `rougail.example`
   * - hostname 
     - host name 
     - `allow_ip`: allows an IP rather than a domain name (`false` by default)
     - machine
   * - web_address
     - web address
     - `allow_ip`: allows an IP rather than a domain name (`false` by default)
     
       `allow_without_dot`: allows names without a dot (`true` by default)
     - http://rougail.example
   * - port 
     - port 
     - `allow_range`: allows a port range, for example 80:85 (`false` by default)

       `allow_zero`: allows port 0 (false by default)

       `allow_wellknown`: allows ports from 1 to 1023 (`true` by default)
       
       `allow_registred`: allows ports from 1024 to 49151 (`true` by default)
       
       `allow_private`: allows ports greater than 49152 (`true` by default)
       
        `allow_protocol`: allows the addition of the protocol, for example tcp:80 (`false` by default)
        
     - 8080
   * - mac
     - MAC address
     - 
     - 11:11:11:11:11:11
   * - unix_permissions
     - access rights to the file, directory, etc.
     - 
     - 644
   * - choice 
     - choice variable 
     - 
     - 
