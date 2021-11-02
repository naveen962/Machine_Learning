'''Write a Python script to sort (ascending and descending) a dictionary by
   value. '''

import operator
def Ascending(d):
    return dict(sorted(d.items(), key = operator.itemgetter(1)))
def Descending(d, reverse = False):
    return dict(sorted(d.items(),  key = operator.itemgetter(1),reverse=True))
print("dictionary elements : ")
colors = {'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}
print(colors)
print("\nSorted in Ascending Order by Value :")
print(Ascending(colors))
print("\nSorted in Descending Order by Value :")
print(Descending(colors, True))
