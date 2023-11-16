#!/usr/bin/python3
"""
Given an nxn 2D matrix, rotate it 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """Rotate 2D Matrix"""
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
