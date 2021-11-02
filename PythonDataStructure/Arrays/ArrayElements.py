'''Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes.'''


from array import *
arr = array('i',[1,3,5,7,9])  #array
for i in arr:
    print(i)   #display array elements
print(" first three Elements :")
print(arr[0]) #display 1st element
print(arr[1]) #display 2nd element
print(arr[2]) #display 3rd element