# def multimax(input):
#     """ a derivation of my original attempt """
#     # if not input:
#     #     return []
#     maxvar = max(input, default=None)
#     return [item for item in input if item == maxvar]


# def multimax(input):
#     """ starting to use some of Trey's solutions now...this one gets the 2nd bonus to work """
#     maximums = []
#     for item in input:
#         if not maximums or maximums[0] == item:
#             maximums.append(item)
#         elif item > maximums[0]:
#             maximums = [item]
#     return maximums

def multimax(input):
    """ this tweak to the first solution above will also get the 2nd bonus to work, but memory inefficient """
    iterable = list(input)
    maxvar = max(iterable, default=None)
    return [item for item in iterable if item == maxvar]