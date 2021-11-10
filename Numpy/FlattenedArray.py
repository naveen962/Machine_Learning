'''Python program to create a contiguous flattened array.'''
import numpy as np
x = np.array([[10, 20, 30], [20, 40, 50]])
print("Original array:")
print(x)
y = np.ravel(x) #ravel converts mutidimensional array into one dimensional array
print("New flattened array:")
print(y)