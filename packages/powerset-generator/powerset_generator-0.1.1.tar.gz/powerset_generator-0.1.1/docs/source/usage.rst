How? – How to use this package
==============================

The package provides a single function, :py:func:`subsets`, which returns a :py:class:`collections.abc.Generator` for the subsets of of ``collection``.

.. autofunction:: powerset_generator.subsets

Additional notes
----------------

The number of subsets of a collection with *N* unique elements
is :math:`2^N`.
You can compute that with

.. testcode:: python

    import collections 

    N = 20
    collection = list(range(N))
    2 ** len(collections.Counter(collection))

.. testoutput::

    1048576

You can work around the limitation that the members of the :py:class:`collections.abc.Collection`
must be :py:class:`collections.abc.Hashable` by using dictionary keys.
For example, if your collection is a dictionary,
you can just generate the powerset of the keys of your dictionary.










