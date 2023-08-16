#!/usr/bin/python3
"""
2D matrix rotation module.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates an m by n 2D matrix in place.
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    rows = len(matrix)
    cols = len(matrix[0])
    if not all(map(lambda x: len(x) == cols, matrix)):
        return
    cm, rw = 0, rows - 1
    for i in range(cols * rows):
        if i % rows == 0:
            matrix.append([])
        if rw == -1:
            rw = rows - 1
            cm += 1
        matrix[-1].append(matrix[rw][cm])
        if cm == cols - 1 and rw >= -1:
            matrix.pop(rw)
        rw -= 1