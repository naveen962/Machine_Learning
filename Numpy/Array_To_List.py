'''program to convert a NumPy array into Python list structure'''

import numpy as np
x= np.arange(6).reshape(3, 2)
print("Original array elements:")
print(x)
print("Array to list:")
print(x.tolist())