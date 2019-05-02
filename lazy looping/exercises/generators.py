"""Generator Expression Exercises."""


def sum_all(my_list):
    return sum(x for i in my_list for x in i)
    #no need of double round brackets - python3 allows use of generators without round bracket if there is an outer round bracket
    """Return the sum of all numbers in the given list-of-lists."""


def all_together(args):

    #for i in args:

    """String together all items from the given iterables."""


def interleave():
    """Return iterable of one item at a time from each list."""


def deep_add():
    """Return sum of values in given iterable, iterating deeply."""


def parse_ranges():
    """Return a list of numbers corresponding to number ranges in a string"""


def is_prime():
    """Return True if candidate number is prime."""
