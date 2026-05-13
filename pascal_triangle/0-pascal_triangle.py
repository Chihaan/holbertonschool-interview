#!/usr/bin/python3
"""Triangle Pascal"""

def pascal_triangle(n):
    """Triangle Pascal"""
    triangle = []
    if n <= 0:
        return  triangle
    triangle = [[1]]
    for i in range(1, n):
        prev_line = triangle[-1]
        triangle.append([1])
        for j in range(len(prev_line) - 1):
            triangle[-1].append(prev_line[j] + prev_line[j + 1])
        triangle[-1].append(1)
    return triangle
