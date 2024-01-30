Why? – Yet another powerset package
====================================

There appear to be an abundance of power set packages,
along with many code samples for producing power sets in Python.
So it is fair to ask why I created this one.

Although I have not done a thorough review of packages turned up in a 
`search for powerset on PyPi <https://pypi.org/search/?q=powerset>`_,
but the few that I glanced at seemed deficient in one way or others.

Among the features that I wanted were,

* Returning a :py:class:`collections.abc.Generator`.

  Power sets grow expontentially with the size of their input.
  I wanted to accomodate larger sets without consuming hugh amounts
  of memory.

    .. testcode:: python

        import sys
        from powerset_generator import subsets

        m = subsets([n for n in range(32)])
        sys.getsizeof(m) < 500

    .. testoutput::

        True

    ``m`` does not consume many gigabytes of memory.

* Include the empty set and the full set of elements of the input among the output sets.

  Some packages appeared to not follow the mathematical definition that way.
  I do understand that in many use cases, the behavior following the mathematical definition is not what people want,
  but if we need to pick one behavior, it should be what follows from the conventional definition.

* Ignore duplicated elements in the input collection.

  Although we can't actually take a Python py:class:`set` as our input,
  we should still generatoe the powerset ignoring duplicate elements.

* Clearly document the decisions on the above.

  While users may not agree with the decisions I've made regarding such things as the empty set or the treatment of duplicates,
  I have clearly docummented them.
  You do not have to experiment or read the source to know how this power set package behaves.

* Be clear and as flexible as possible about types.

  Some code I'd seen produced tuples, others lists and often without documenting that.
  I have chosen :py:class:`set` to accentuate my attempt
  to follow set theoretic definitions.
  
  Because sets are generated, the minimum requirement on the elements of the input is tha they be :py:class:`collections.abc.Hashable`.
  And the most general type of the input is that it be a
  :py:class:`collections.abc.Collection`.

* I get to learn how to prepare my first Python package.

  Sure, this package may be over engineered,
  with an excessive amount of documentation and testing for what is
  just a few lines of simple code.
  But I've learned a great deal about Python packaging, decomentation,
  testing, and deployment in this process.
  This was my primary purpose.

None of this may be sufficient reason in *your view* for me to create yet another powerset package, but it was suffient for *me*.
