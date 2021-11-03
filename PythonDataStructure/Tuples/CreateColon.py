'''Write a Python program to create the colon of a tuple.'''
from copy import deepcopy
tup = ("HELLO", 5, [], True) 
print(tup)
#make a copy of a tuple using deepcopy() function
tup_colon = deepcopy(tup)
print(tup_colon)
