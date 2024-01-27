.. Powerset generator documentation master file, created by
   sphinx-quickstart on Sun Jan 21 21:13:16 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

A Python Generator of power sets
==============================================

This is documentatation for version |version| of |project| package,
a simply python package for creating power sets of a collection.

Installation
------------

To use powerset generator, first install it with `pip`

.. code-block:: console

    $ pip install powerset-generator

.. note:: 
    That installation won't work until this powerset-generator package is actually published. It isn't yet.

Example
-------

The root (and so far only) module is |root|,
providing the only function, :func:`subsets`.

.. code-block:: python

   from powerset_generator import subsets
   for e in subsets( ["one", "two", "three", "three"])]:
      print(e)

should produce a result *similar to*

.. code-block:: python

   set()
   {'one'}
   {'three'}
   {'two'}
   {'one', 'three'}
   {'one', 'two'}
   {'three', 'two'}
   {'one', 'three', 'two'}

.. note::

   1. The empty set, ``set()``, is included in the output;

   2. The full set ``{'one', 'two', 'three'}`` is included in the output;

   3. The duplicated input element ``"three"`` is treated as if it appeared only once;
   
   4. The order in which the subsets are generated is not defined.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage
   yapp
   credits


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
