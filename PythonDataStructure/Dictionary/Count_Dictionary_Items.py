'''Write a Python program to count number of items in a dictionary value
that is a list.'''

d =  {'Naveen': ['sub1', 'sub2', 'sub3'], 'Hemanth': ['sub1', 'sub2']}
ctr = sum(map(len, d.values()))
print(ctr)