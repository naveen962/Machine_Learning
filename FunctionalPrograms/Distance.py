'''Write a program Distance.java that takes two integer command-line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function'''


import math

def Distance(x1,y1,x2,y2):                            #function definition
    distance=(math.pow((x2-x1),2))+(math.pow((y2-y1),2)) #calculating distance
    print(math.sqrt(distance))
 
x1=0  #origin
y1=0  #origin
x2=int(input("Enter the point X2 : ")) #taking points from user
y2=int(input("Enter the point y2 : "))
Distance(x1,y1,x2,y2)