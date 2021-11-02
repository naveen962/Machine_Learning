'''Write a Python program to get the number of occurrences of a specified element in an
array.'''

from array import *
arr = array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: ",arr)
print("Number of occurrences of the number 3 in the said array: ",arr.count(3))