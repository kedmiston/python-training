
import re


def count_words(phrase):
    if not isinstance(phrase, str) or phrase is None:
        return {}

    stripped_str = re.sub("[^A-Za-z']+", " ", phrase)  # leaving this separate means it gets set only once...efficient

    word_dict = {}
    for word in stripped_str.lower().strip().split(" "):
        word_dict[word] = word_dict[word] + 1 if word in word_dict else 1
    return word_dict
