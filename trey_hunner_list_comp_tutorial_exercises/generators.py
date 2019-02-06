"""Generator Exercises."""

words = {
    'esta': 'is',
    'la': 'the',
    'en': 'in',
    'gato': 'cat',
    'casa': 'house',
    'el': 'the'
}


def is_prime(number):
    """Return True if candidate number is prime."""
    # for n in range(2, number):
    #     if number % n == 0:
    #         return False
    # return True

    # return not any(
    #     number % n == 0
    #     for n in range(2, number)
    # )

    return all(number % n != 0 for n in range(2, number))


def all_together(*iterables):
    """String together all items from the given iterables."""
    return (item for iterable in iterables for item in iterable)


def interleave(*inputs):
    """Return iterable of one item at a time from each list."""
    return (item for pair in zip(*inputs) for item in pair)


def translate(spanish):
    """Return a transliterated version of the given sentence."""
    # english = []
    # for s_word in spanish.split():
    #     english.append(words[s_word])
    #
    # return " ".join(english)

    return " ".join(
        words[s_word]
        for s_word in spanish.split()
    )

def parse_ranges():
    """Return a list of numbers corresponding to number ranges in a string"""


def first_prime_over(n):
    """Return the first prime number over a given number."""
    for x in range(n+1, n**2):
        if is_prime(x):
            return x

def is_anagram():
    """Return True if the given words are anagrams."""
