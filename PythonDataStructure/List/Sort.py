''' Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.'''


new_list = [('john', 6), ('Micheal', 9), ('George', 2), ('steve', 19)]

new_list.sort(key=lambda y: y[1]) #sorting

print(new_list)