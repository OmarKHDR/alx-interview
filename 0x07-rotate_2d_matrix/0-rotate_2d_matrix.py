#!/usr/bin/python3
""" THose who can rotate
"""


def rotate_2d_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
