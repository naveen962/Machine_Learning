'''User Input and Replace String Template “Hello <<UserName>>, How are you?”
a. I/P -> Take User Name as Input. Ensure UserName has min 3 char
b. Logic -> Replace <<UserName>> with the proper name
c. O/P -> Print the String with User Name'''


string="Hello <<UserName>>,How are you?"
UserName=input("Enter the UserName : ")  #taking userinput
print(string.replace("<<UserName>>",UserName)) #Replace string
