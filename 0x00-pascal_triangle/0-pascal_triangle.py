#!/usr/bin/python3
"""
pascal triangle
"""
triangle = [[1],]


def create_pascal(arr, begin, end):
	"""
	create each level by recurssion
	"""
    if end == 0:
        return
    if begin == end:
        triangle[end].append(1)
        return
    elif begin == 0:
        triangle.append([])
        triangle[end].append(1)
    elif end > 1:
        triangle[end].append(arr[end-1][begin-1] + arr[end-1][begin])
    create_pascal(arr, begin + 1, end)


def pascal_triangle(n):
	""" a function looping through each level of pascal triangle
		return: the final triangle
	"""
    if len(triangle) >= n:
        return triangle[:n]
    for i in range(n):
        create_pascal(triangle, 0, i)
    return triangle
