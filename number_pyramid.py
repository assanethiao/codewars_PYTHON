"""
Number pyramid
Number pyramid is a recursive structure where each next row is constructed by
adding adjacent values of the current row.

For example:

Row 1     [1     2     3     4]
Row 2        [3     5     7]
Row 3           [8    12]
Row 4             [20]
Task
Given the first row of the number pyramid, find the value stored in its last row.
Performance tests
Number of tests: 10
List size: 10,000

"""


def reduce_pyramid(base):
    while len(base) > 1:
        base = [base[i] + base[i+1] for i in range(len(base) - 1)]
    return base[0]
