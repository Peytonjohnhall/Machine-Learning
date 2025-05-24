"""
(10 points) Program 1: Array Slicing
Create an array containing the values 1–15, reshape it into a 3-by-5 array, then use indexing
and slicing techniques to perform each of the following operations:
a) Select row 2.
b) Select the column 4.
c) Select rows 0 and 1.
d) Select columns 2–4.
e) Select the element that is in row1 and column4.
f) Select all elements from rows 1 and 2 that are in columns 0, 2 and 4.
"""

import numpy as np

# Create an array containing the values 1–15 and reshape it into a 3x5 array
array = np.arange(1, 16).reshape(3, 5)

# select row 2
row2 = array[2]

# select column 4
column4 = array[:, 4]

# select rows 0 and 1
rows01 = array[:2]

# select columns 2–4
columns2to4 = array[:, 2:5]

# select the element that is in row 1 and column 4
element_row1_col4 = array[1, 4]

# select all elements from rows 1 and 2 that are in columns 0, 2, and 4
elements_rows1_2_cols024 = array[1:3, [0, 2, 4]]

print("a) Row 2:", row2)
print("b) Column 4:", column4)
print("c) Rows 0 and 1:", rows01)
print("d) Columns 2 to 4:", columns2to4)
print("e) Element at row 1, column 4:", element_row1_col4)
print("f) Elements from rows 1 and 2 in columns 0, 2, and 4:", 
	  elements_rows1_2_cols024)
