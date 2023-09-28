#!/usr/bin/python3
""" pascal triangle quiz
"""


def pascal_triangle(n):
    """ solves the quiz
    """
    if n <= 0:
        return []

    triangle = []
    for row in range(n):
        current_row = [1]
        if row > 0:
            previous_row = triangle[row - 1]
            for col in range(1, row):
                current_row.append(previous_row[col - 1] + previous_row[col])
            current_row.append(1)
        triangle.append(current_row)

    return triangle
