"""
(10 points) Program 2: Horizontal and Vertical Stacking
Create the two-dimensional arrays array1 = np.array([[0, 1], [2, 3]])
array2 = np.array([[4, 5], [6, 7]])
a) Use vertical stacking to create the 4-by-2 array named array3 with array1 stacked on top
of array2.
b) Use horizontal stacking to create the 2-by-4 array named array4 with array2 to the right
of array1.
c) Use vertical stacking with two copies of array4 to create a 4-by-4 array5.
d) Use horizontal stacking with two copies of array3 to create a 4-by-4 array6.
"""

import numpy as np

# Create the two-dimensional arrays
array1 = np.array([[0, 1], [2, 3]])
array2 = np.array([[4, 5], [6, 7]])

# part a)
array3 = np.vstack((array1, array2))

# part b)
array4 = np.hstack((array1, array2))

# part c)
array5 = np.vstack((array4, array4))

# part d)
array6 = np.hstack((array3, array3))

print("Array 3 (Vertical stacking of array1 and array2):")
print(array3)
print("\nArray 4 (Horizontal stacking of array1 and array2):")
print(array4)
print("\nArray 5 (Vertical stacking of two copies of array4):")
print(array5)
print("\nArray 6 (Horizontal stacking of two copies of array3):")
print(array6)
