'''Flip Coin and print percentage of Heads and Tails
a. I/P -> The number of times to Flip Coin. Ensure it is positive integer.
b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or
heads
c. O/P -> Percentage of Head vs Tails'''


import random
#taking user input
n=int(input("enter the no of flips : "))
Tailcount=0

for i in range(1,n):

      value=random.random()  #random number generated
      
      #checking condition
      if value<0.5:
            print("TAILS")
            Tailcount=Tailcount+1
      else:
            print("HEADS")
      
TailPercentage=(Tailcount/n)*100
HeadPercentage=100-TailPercentage
print("HeadPercentage = ",HeadPercentage)
print("TailPercentage = ",TailPercentage)