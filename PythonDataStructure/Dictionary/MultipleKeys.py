
'''Write a Python program to check multiple keys exists in a dictionary.'''

student = {1: 'Alex',2: 'Varun', 3: 'Arjun'}
print(student.keys() >= {1,2})
print(student.keys() >= {2,1})
print(student.keys() >= {3,'Alex'})