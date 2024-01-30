The dictionaries
=====================

What do you mean by :term:`dictionary`?
-------------------------------------------

A :term:`dictionary` is a YAML file whose structure is described in this documentation page.

A dictionary contains a set of variables loaded into :term:`Tiramisu`, usable at any time, especially in a :term:`templates`.

:term:`Families` and :term:`variables` can be defined in several dictionaries. These dictionaries are then aggregated.

Dictionaries are loaded in the directory order defined by the `dictionaries_dir` configuration parameter. 
Each directory is loaded one after the other. 
Inside these directories the YAML files will be classified in alphabetical order.

There is no alphabetical ordering of all YAML files in all directories.

It is also possible to :term:`redefine` elements to change the behavior of a family or a variable. 

The default namespace
-------------------------

The families and variables contained in these dictionaries are ordered, by default, in the `rougail` namespace. It is possible to change the name of this namespace :doc:`with the `variable_namespace` parameter of the configuration <configuration>`.

This namespace is a bit special, it can access variables in another namespace.

The extra dictionaries
---------------------------

An extra is a different namespace. The idea is to be able to classify the variables by theme.

Extra namespaces must be declared :doc:`when configuring Rougail <configuration>`.

In this namespace we cannot access variables from another `extra` namespace. 
On the other hand, it is possible to access the variable of the default namespace.
