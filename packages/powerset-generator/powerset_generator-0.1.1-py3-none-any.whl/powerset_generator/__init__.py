from itertools import combinations
from collections import Counter
from collections.abc import Collection, Generator, Hashable
from typing import TypeVar

from . import __about__  # noqa

T = TypeVar("T", bound=Hashable)


def subsets(
    collection: Collection[T],
) -> Generator[set[T], None, None]:
    """Generates all the subsets of the powerset of collection.

    :param collection: The collection you want the subsets of

    Power sets
    ------------

    The power set of a collections is the set of all subsets of
    the collection.

    * The power set includes the empty set.

    * The power set includes a set of all members of the collections.
      That is, it is not limited to the proper subsets of the collection.

    * If the collection has *N* unique elements,
      the power set will have 2^N` elements.

    Usage notes
    -------------

    This this fuction generates sets irrespective of the type of its input.
    That is, given a list, it will yield sets.

    In the current version there is no enforcement of the type hinting
    that members of the input collection all be of the same type. But
    do not rely on this lax behavior.

    Example::

        from powerset_generator import subsets

        a_list: list[str] = ["one", "two", "three"]
        for element in subsets(s):
            print(element)

    produces::

        set()
        {'one'}
        {'three'}
        {'two'}
        {'one', 'three'}
        {'one', 'two'}
        {'three', 'two'}
        {'one', 'three', 'two'}

    Exceptions
    ----------

    powerset does not explicitly raise any exceptions on its own,
    but if its argument is not Collection[Hashable] some of the
    functions it calls internally are likely to raise a TypeError.
    """

    # We don't want duplicats, so
    s: set[T] = set(Counter(collection))

    # explicitly start at 0 to not forget that the empty set
    # is in the powerset
    for r in range(0, len(s) + 1):
        for result in combinations(s, r):
            # itertools.combinations spits out tuples
            yield set(result)
