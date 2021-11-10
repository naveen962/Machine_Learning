''' program to compare two arrays'''

import numpy as np
a = np.array([1, 2])
b = np.array([4, 5])
print("Array a: ",a)
print("Array b: ",b)
print("a > b")
print(np.greater(a, b)) #greater than
print("a >= b")
print(np.greater_equal(a, b)) #greater than or equal
print("a < b")
print(np.less(a, b)) #less than
print("a <= b")
print(np.less_equal(a, b)) #less Than or equal