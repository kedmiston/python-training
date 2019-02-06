"""List comprehension trey_hunner_list_comp_tutorial_exercises"""


def get_vowel_names(list):
    """Return a list containing all names given that start with a vowel."""
    vowels = ('a', 'e', 'i', 'o', 'u')
    return [n for n in list if n.lower().startswith(vowels)]


def power_list(list):
    """Return a list that contains each number raised to the i-th power."""
    return [p**i for i, p in enumerate(list)]

def flatten(matrix):
    """Return a flattened version of the given 2-D matrix (list-of-lists)."""
    return [n for l in matrix for n in l]

def reverse_difference():
    """Return list subtracted from the reverse of itself."""


def matrix_add():
    """Add corresponding numbers in given 2-D matrices."""


def transpose():
    """Return a transposed version of given list of lists."""


def get_factors():
    """Return a list of all factors of the given number."""


def triples():
    """Return list of Pythagorean triples less than input num."""
