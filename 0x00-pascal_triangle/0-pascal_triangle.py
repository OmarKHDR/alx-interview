#!/usr/bin/python3
"""
pascal triangle
"""


def create_pascal(arr, begin, end):
    """
    create each level by recurssion
    """
    if begin == end:
        arr[end].append(1)
        return
    elif begin == 0:
        arr.append([])
        arr[end].append(1)
    elif end > 1:
        arr[end].append(arr[end-1][begin-1] + arr[end-1][begin])
    create_pascal(arr, begin + 1, end)


def pascal_triangle(n):
    """ a function looping through each level of pascal triangle
        return: the final triangle
    """
    triangle = [[],]
    if len(triangle) >= n:
        return triangle[:n]
    for i in range(n):
        create_pascal(triangle, 0, i)
    return triangle
