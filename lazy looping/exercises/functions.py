"""Generator Function Exercises."""



#def unique(interable):
#    """Yield iterable elements in order, skipping duplicate values."""
#    ulist = list()
#    for i in interable:
#        if i not in ulist:
#            ulist.append(i)
#            yield i

def unique(iterable):
    """Yield iterable elements in order, skipping duplicate values."""
    uniques = set()
    for item in iterable:
        if item not in uniques:
            yield item
            uniques.add(item)

#Set is faster than List - set uses hashing and hence faster

#def unique(*args):
#    uniq =[]
#    for i in args:
#        for j in i:
#            if j not in uniq:
#                uniq.append(j)
#                yield j
#    """Yield iterable elements in order, skipping duplicate values."""


def float_range():
    """Return iterable of numbers from start to stop by step."""


def head():
    """Return first n items of a given iterable."""


def pairwise():
    """
    Yield a tuple containing each item and the item following it.

    The item after the last one is treated as ``None``.
    """


def around():
    """
    Yield a tuple of the previous, current, and next items.

    The previous item should start at ``None`` and the next item should
    be ``None`` for the last item in the iterable.
    """


def stop_on():
    """Yield from the iterable until the given value is reached."""


def deep_flatten():
    """Flatten an iterable of iterables."""


def get_primes_over():
    """Return given number of primes over 1,000,000."""
