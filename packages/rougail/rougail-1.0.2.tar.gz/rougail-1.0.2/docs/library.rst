`Rougail`'s library description
=================================

Rougail is a configuration management library that allows you to load variables in a simple and convenient way.

In the following examples, we will use a specific configuration of Rougail. You will find all the options to :doc:`customize the directories structure used <configuration>`.

To load the configuration you must import the `RougailConfig` class and set the `dictionaries_dir` values:

.. code-block:: python

    from rougail import RougailConfig

    RougailConfig['dictionaries_dir'] = ['dict']

Let's convert a dictionary
-----------------------------

As a reminder, a :term:`dictionary` is a set of instructions that will allow us to create :term:`families` and :term:`variables`.

Let's start by creating a simple dictionary.

Here is a first :file:`dict/00-base.yml` dictionary:

.. code-block:: yaml

    ---
    version: '1.0'
    my_variable:
      default: my_value

Then, let's create the :term:`Tiramisu` objects via the following script:

.. code-block:: python 
    :caption: the `script.py` file content
   
    from rougail import Rougail, RougailConfig

    RougailConfig['dictionaries_dir'] = ['dict']
    rougail = Rougail()
    config = rougail.get_config()
    print(config.value.get())
 
Let's execute `script.py`:

.. code-block:: bash

    $ python3 script.py
    {'rougail.my_variable': 'my_value'}

Let's convert an extra dictionary
-------------------------------------

.. index:: extras

The default namespace for variables and families is `rougail`. It is possible to define other namespaces. These additional namespaces are called `extras`.

.. FIXME: faire une page pour les extras

Additional namespaces are defined during configuration.

For example, here's how to add an `example` namespace:

.. code-block:: python

    RougailConfig['extra_dictionaries']['example'] = ['extras/']

Then let's create an extra :term:`dictionary` :file:`extras/00-base.yml`:

.. code-block:: yaml
   :caption: the :file:`extras/00-base.yml` file content
    ---
    version: '1.0'
    my_variable_extra:
      default: my_value_extra

Then, let's create the :term:`Tiramisu` objects via the following :file:`script.py` script:

.. code-block:: python 
    :caption: the :file:`script.py` file content 
    
    from rougail import Rougail, RougailConfig

    RougailConfig['dictionaries_dir'] = ['dict']
    RougailConfig['extra_dictionaries']['example'] = ['extras/']
    rougail = Rougail()
    config = rougail.get_config()
    print(config.value.dict())

Let's execute `script.py`:

.. code-block:: bash

    $ python3 script.py
    {'rougail.my_variable': 'my_value', 'example.my_variable_extra': 'my_value_extra'}

Let's create a custom function
----------------------------------

We create the complementary :term:`dictionary` named :file:`dict/01-function.yml` so that the  `my_variable_jinja` variable is :term:`calculated`:

.. code-block:: yaml

    ---
    version: '1.0'
    my_variable_jinja:
      type: "string"
      default:    
        type: jinja
        jinja: "{{ return_no() }}"

Then let's define the :func:`return_no` function in :file:`functions.py`:

.. code-block:: python 
   :caption: the :file:`functions.py` content
   
   def return_no():
       return 'no'

Then, let's create the :term:`Tiramisu` objects via the following script:

.. code-block:: python 
    :caption: the `script.py` file content

    from rougail import Rougail, RougailConfig

    RougailConfig['dictionaries_dir'] = ['dict']
    RougailConfig['extra_dictionaries']['example'] = ['extras/']
    RougailConfig['functions_file'] = 'functions.py'
    rougail = Rougail()
    config = rougail.get_config()
    print(config.value.dict())

Let's execute `script.py`:

.. code-block:: bash

    $ python3 script.py
    {'rougail.my_variable': 'my_value', 'rougail.my_variable_jinja': 'no', 'example.my_variable_extra': 'my_value_extra'}

The value of the `my_variable_extra` variable is calculated, and it's value comes from the :func:`return_no` function.
