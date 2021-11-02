''' Write a Python program to reverse the order of the items in the array.'''


from array import *
arr = array('i',[1,3,5,7,9])  #array
for i in arr:
    print(i) 
arr.reverse() #reverse array elements
print("After Reversing array elements : ")
for i in arr:
    print(i) 
