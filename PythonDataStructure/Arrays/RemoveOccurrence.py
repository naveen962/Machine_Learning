'''Write a Python program to remove the first occurrence of a specified element from an
array.'''

from array import *
arr = array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: ",arr)
print("Number of occurrences of the number 3 in the said array: ",arr.count(3))
arr.remove(3) #removing first occurrence
print(arr) 