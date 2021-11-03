'''Write a Python program to create a symmetric difference.'''
s1 = set(["green", "blue"])             #set created
s2 = set(["blue", "yellow"])
print("Original set elements:")
print(s1)
print(s2)
print("\nIntersection of two said sets:")
s3 = s1.symmetric_difference(s2)                         

s4=s2.symmetric_difference(s1)
print(s3)
print(s4)