.. meta::
   :description: Rougail python library home page
   :keywords: python, Rougail, Tiramisu
   :http-equiv=Pragma: no-cache

.. title:: Rougail

Rougail
===========

.. image:: images/logo.png

- is a `delicious cooked dish <https://fr.wikipedia.org/wiki/Rougail>`_ from the Mauritius  and Reunion Islands,

- it is also a `Python3 <https://www.python.org/>`_ library  which enables us to conveniently load application :term:`variable`\ s in a simple `YAML <https://yaml.org/>`_ format in such a way that the end user consumer can handle them consistently (that is, against an user-defined consistency).

In other words, using Rougail in your application or your python libraries can tansform end user consumer defined consistency rules into highly consistent business objects.

We then have to say that the handling system used to ensure the variables integrity is another python library, called :term:`Tiramisu`. Rougail is currently strongly affiliated with Tiramisu.

.. note:: Rougail is currently intended to work in coordination with :term:`Tiramisu` and **is not** intended to be connected with any other consistency handling system.

Explained differently, Rougail allows you to easily implement an integration of the powerful tiramisu consistency handling system.

.. toctree::
   :titlesonly:
   :caption: Getting started

   gettingstarted
   tutorial

.. toctree::
   :titlesonly:
   :caption: The library
   
   library
   configuration

.. toctree::
   :titlesonly:
   :caption: The dictionaries

   dictionary
   dict_convention
   
.. toctree::
   :titlesonly:
   :caption: The variables

   variable
   family
   fill
   Value checks <check>
   condition
      
.. toctree::
   :titlesonly:
   :caption: Notes
   
   developer

.. rubric:: Index page

- :ref:`genindex`
