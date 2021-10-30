'''Write a program WindChill.java that takes two double command-line arguments t
and v and prints the wind chill. Use Math.pow(a, b) to compute ab. Given the
temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
National Weather Service defines the effective temperature (the wind chill) to be:

Note: the formula is not valid if t is larger than 50 in absolute value or if v is larger
than 120 or less than 3 (you may assume that the values you get are in that range).'''


import math
# functiondefinition
def WindChill(temp, speed):

    w=(35.74+0.6215*temp+(0.4275*temp-35.75)*math.pow((speed),0.16))
    print(w)

#taking inputs temperature and speed
temperature=int(input("Enter temperature  greater than 50 : "))
speed=int(input(("Enter the speed : ")))
#checking condition
if(temperature<50 and (speed<120 or speed>3)):
    WindChill(temperature,speed)
else:
    print("Please enter the valid temperature and speed ")