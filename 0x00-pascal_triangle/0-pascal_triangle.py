#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    people people people people
    people people people people
    """
    pascal_tri = []

    if m <= 0:
        return []

    for k in range(m):
        if (k == 0):
            pascal_tri.append([1])
        else:
            cur_row = []
            for j in range(k + 1):
                if (j == 0 or j == k):
                    cur_row.append(1)
                else:
                    cur_row.append(pascal_tri[k - 1][j - 1] +
                                   pascal_tri[k - 1][j])

            pascal_tri.append(cur_row)

    return (pascal_tri)
