'''program to find the real and imaginary parts of an array of complex numbers'''

import numpy as np
x = np.sqrt([1+0j])
y = np.sqrt([0+1j])
print("Original array:x ",x)
print("Original array:y ",y)
print("Real part of the array:") #real part
print(x.real)
print(y.real)
print("Imaginary part of the array:") #imaginary part
print(x.imag)
print(y.imag)