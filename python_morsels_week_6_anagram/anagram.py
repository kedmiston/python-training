from collections import deque, Counter
import unicodedata

# my first solution
# -----
# def is_anagram(string1, string2):
#     if len(string1) != len(string2):
#         return False
#
#     for letter in string1.lower():
#         if letter in string2.lower():
#             continue
#         else:
#             return False
#
#     return True


# my second solution
#   with bonus #1
# -----
# def is_anagram(string1, string2):
#
#     string1_clean = ''
#     for i in string1:
#         if i == ' ':
#             continue
#         else:
#             string1_clean += i
#     string2_clean = ''
#     for i in string2:
#         if i == ' ':
#             continue
#         else:
#             string2_clean += i
#
#     list1 = list(string1_clean.lower())
#     list2 = list(string2_clean.lower())
#
#     if len(list1) != len(list2):
#         return False
#
#     for item in list1:
#         if item not in list2:
#             return False
#
#     return True


# my third solution
#   with bonuses, except the third
# -----
# def is_anagram(string1, string2):
#     import re
#     pattern = r"(\W+)"
#     reg = re.compile(pattern, re.ASCII)
#
#     list1 = list(reg.sub('', string1).lower())
#     list2 = list(reg.sub('', string2).lower())
#
#     if len(list1) != len(list2):
#         return False
#
#     for item in list1:
#         if item not in list2:
#             return False
#
#     return True


# one of Trey's solutions --> Counter() (he likes this a wee bit better than sorted() below)
#  -- does not handle punctuation, spaces or unicode tho
# def is_anagram(string1, string2):
#     return Counter(string1.lower()) == Counter(string2.lower())

# another of Trey's solutions --> sorted()
#  -- does not handle punctuation, spaces or unicode tho
# def is_anagram(string1, string2):
#     return sorted(string1.lower()) == sorted(string2.lower())


# Bonus 1 of Trey's solutions --> string replace()
#  -- does not handle punctuation, spaces or unicode tho
# def is_anagram(string1, string2):
#     string1, string2 = string1.lower(), string2.lower()
#     return Counter(string1.replace(' ', '')) == Counter(string2.replace(' ', ''))


# Bonus 1/2 of Trey's solutions --> generator
# def is_anagram(string1, string2):
#     string1, string2 = string1.lower(), string2.lower()
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     letters1 = sorted(c for c in string1 if c in alphabet)
#     letters2 = sorted(c for c in string2 if c in alphabet)
#     return letters1 == letters2


# Bonus 1/2 of Trey's solutions --> isalpha()
# def is_anagram(string1, string2):
#     string1, string2 = string1.lower(), string2.lower()
#     letters1 = sorted(c for c in string1 if c.isalpha())
#     letters2 = sorted(c for c in string2 if c.isalpha())
#     return letters1 == letters2


# Bonus 1/2 of Trey's solutions --> isalpha() in separated function
# def letters_in(string):
#     """ returns letters of a string in sorted order """
#     return sorted(c for c in string if c.isalpha())
#
#
# def is_anagram(string1, string2):
#     string1, string2 = string1.lower(), string2.lower()
#     return letters_in(string1) == letters_in(string2)


# Bonus 1/2 of Trey's solutions --> Count() if isalpha(), in separated function
# def count_letters(string):
#     """ returns count of letters of a string """
#     return Counter(c for c in string if c.isalpha())
#
#
# def is_anagram(string1, string2):
#     string1, string2 = string1.lower(), string2.lower()
#     return count_letters(string1) == count_letters(string2)


# Bonus 3 of Trey's solutions --> NFKD normalization, in separated functions
def normalize_string(string):
    return unicodedata.normalize('NFKD', string)


def count_letters(string):
    """ returns count of letters of a string """
    clean_string = normalize_string(string.lower())
    return Counter(c for c in clean_string if c.isalpha())


def is_anagram(string1, string2):
    return count_letters(string1) == count_letters(string2)

