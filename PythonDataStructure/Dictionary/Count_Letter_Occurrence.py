'''Write a Python program to create a dictionary from a string.

Note: Track the count of the letters from the string.'''


str = 'Naveen' 
my_dict = {}
for letter in str:
    if letter in my_dict.keys(): #checking whether the letter is already existed in dictionary or not
        my_dict[letter]+=1
    else:
        my_dict[letter]=1
print(my_dict)