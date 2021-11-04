'''Write a Python program to get a string from a given string where all occurrences of its
first char have been changed to '$', except the first char itself.'''

def change_char(str1):
  char = str[0]  #taking a copy of first character
  str1 = str.replace(char, '$') #replace character to dollar
  str1 = char + str[1:]

  return str

print(change_char('restart'))