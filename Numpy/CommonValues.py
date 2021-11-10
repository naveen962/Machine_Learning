'''Python program to find common values between two arrays.'''
import numpy as np
array1 = np.array([0, 10, 20, 40, 60]) #1st array
print("Array1: ",array1)
array2 = [10, 30, 40]  #2nd Array
print("Array2: ",array2)
print("Common values between two arrays:")
print(np.intersect1d(array1, array2)) #intersecting 2 arrays to get common values
