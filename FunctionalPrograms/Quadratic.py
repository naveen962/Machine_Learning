'''Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
can be found using a formula (Note: Take a, b and c as input values)
delta = b*b - 4*a*c
Root 1 of x = (-b + sqrt(delta))/(2*a)
Root 2 of x = (-b - sqrt(delta))/(2*a)'''


import math

def Find_Roots(a,b,c):    #function definition
    
    #calculating the two roots 
    delta=b*b-4*a*c
    Root1=(-b+math.sqrt(delta))/(2*a)
    Root2=(-b+math.sqrt(delta))/(2*a)
    print("Root1 of x is : ",Root1)
    print("Root2 of x is : ",Root2)

#taking user inputs a,b,c
a=int(input("Enter the valuea of a"))
b=int(input("Enter the valuea of b"))
c=int(input("Enter the valuea of c"))
Find_Roots(a,b,c)  # calling a function