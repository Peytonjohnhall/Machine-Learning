"""
(5 points) Program 3: Research NumPy tile Function
Research and use NumPy’s tile function to create a checkerboard pattern of dashes and
asterisks.
"""

import numpy as np

size = 7 # size of the 2x2 board

def create_checkerboard(size):
    # create 2x2 checkerboard pattern
    pattern = np.array([['-', '*'], ['*', '-']])

    # extend into larger grid
    checkerboard = np.tile(pattern, (size, size))

    return checkerboard

checkerboard = create_checkerboard(size)

print(checkerboard)