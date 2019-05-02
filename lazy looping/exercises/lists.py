"""List comprehension exercises"""

#list comprehensions not to be used for print functions
#generators are one-time use, disposable - they exhaust
#length, indexing won't work
#can only interate - that too once
#yield is return but continue - results in generator function
#yield will put function on pause
#generator is both iterator and iterable
#iterator are single use, one direction
#using iter() to convert to iterator
#files are iterables but can be reset using seek()


def get_vowel_names(names):
    return [x for x in names if any(x.lower()[0] == i for i in ['a','e','i','o','u'])]
    """Return a list containing all names given that start with a vowel."""


def flatten(my_list):
    return [x for i in my_list for x in i]
    """Return a flattened version of the given 2-D matrix (list-of-lists)."""


def matrix_from_string(s):
    return [int(x) for x in s.split()]
    """Convert rows of numbers to list of lists."""


def power_list():
    """Return a list that contains each number raised to the i-th power."""


def matrix_add():
    """Add corresponding numbers in given 2-D matrices."""


def identity():
    """Return an identity matrix of size x size."""


def triples():
    """Return list of Pythagorean triples less than input num."""
