# my attempt...all tests passed
# def tail(*args):
    # return list(list(args[0])[-args[1]:]) if args[1] > 0 else []


# one of Trey's solutions
# def tail(iterable, n):
#     """Return the last n items of given iterable."""
#     items = []
#     if n == 1:
#         for item in iterable:
#             items = [item]
#     elif n > 0:
#         for item in iterable:
#             items = [*items[-n+1:], item]
#     return items


# another Trey solution
# def tail(iterable, n):
#     """Return the last n items of given iterable."""
#     items = []
#     if n <= 0:
#         return []
#     elif n == 1:
#         index = slice(0, 0)
#     else:
#         index = slice(-(n-1), None)
#     for item in iterable:
#         items = [*items[index], item]
#     return items


# another Trey solution
# from collections import deque
#
#
# def tail(iterable, n):
#     """Return the last n items of given iterable."""
#     if n <= 0:
#         return []
#     items = deque(maxlen=n)
#     for item in iterable:
#         items.append(item)
#     return list(items)


# and the last Trey solution
from collections import deque


def tail(iterable, n):
    """Return the last n items of given iterable."""
    if n <= 0:
        return []
    return list(deque(iterable, maxlen=n))
