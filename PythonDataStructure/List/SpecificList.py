''' Write a Python program to print a specified list after removing the 0th, 4th and
5th elements.'''


l = ['Red', 'Yellow', 'White', 'Black', 'Pink', 'Green']
for x in l:
    if x=='Red' or x=='Pink' or x=='Yellow':
        l.remove(x)

print(l)

    