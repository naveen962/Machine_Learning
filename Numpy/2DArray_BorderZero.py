'''Write a Python program to add a border (filled with 0's) around an existing array.'''

import numpy as np
x = np.zeros((5,5))
print("Original array:")
print(x)
print("1 on the border and 0 inside in the array")
x[1:-1,1:-1] = 1
print(x)