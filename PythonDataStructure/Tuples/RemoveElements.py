''' Write a Python program to remove an item from a tuple.'''
Tup=(10,20,30,40,50) 
print(type(Tup))
print(Tup)


List=list(Tup)  #convert Tuple to List because tuple is immutable
List.remove(30) # remove element 30

Tup=tuple(List) #convert List to Tuple
print(Tup)

