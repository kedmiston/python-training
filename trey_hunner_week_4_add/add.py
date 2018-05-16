
# most pythonic version, but also hard to read
# def add(matrix1, matrix2):
#     """Add corresponding numbers in given 2-D matrices."""
#     return [[n+m for n, m in zip(r1, r2)] for r1, r2 in zip(matrix1, matrix2)]


# more easy version to read...less comprehensions
# def add(matrix1, matrix2):
#     """Add corresponding numbers in given 2-D matrices."""
#     return [
#         [n + m for n, m in zip(row1, row2)]
#         for row1, row2 in zip(matrix1, matrix2)
#     ]

# bonus #1 solution
def add(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*matrices)
    ]