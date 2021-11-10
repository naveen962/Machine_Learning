'''Python program to create an array which looks like below array.
Expected Output:
[[ 0. 0. 0.]
[ 1. 0. 0.]
[ 1. 1. 0.]
[ 1. 1. 1.]]'''



import numpy as np
x = np.tri(4, 3, -1) #tri is a function to create 1's at below diagonal and 0's at above diagonal
print(x)
