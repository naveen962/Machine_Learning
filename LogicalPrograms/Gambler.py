'''Gambler
a. Desc -> Simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
times he/she wins and the number of bets he/she makes. Run the experiment N
times, averages the results, and prints them out.
b. I/P -> $Stake, $Goal and Number of times
c. Logic -> Play till the gambler is broke or has won
d. O/P -> Print Number of Wins and Percentage of Win and Loss.'''


import random
def gambler(stake, goal, n): #function definition
    
    bet = 1
    win = loss = temp = 0
    for i in range(1,n+1):
        if ( random.random() >= 0.5):  # if generated random is gt 0.5 gamer wins then stake incremnts by 1  and bets again
            win = win + 1                  
            stake = stake + bet
            if (stake == goal):
                break
        else:
            loss = loss + 1
            stake= stake - bet
            if (stake == 0):
                print("The game was completed")
                break
           
        temp = i

    if (temp <= n) and (stake == goal):
        print("The goal has reached")
    elif (temp == n) and (stake != goal):
        print(" Goal not reached")
    else:
        print("No more stake")

    print("No.of Wins:", win)
    WinPercentage= 100*(win/n)  # prints winning percentage
    print("WinPercentage : ",WinPercentage)
    print("No.of Loss:", loss)
    LossPercentage= 100-WinPercentage  # prints loss percentage
    print("LossPercentage : ",LossPercentage)

stake = int(input("Enter the amount: "))                      #enter amount 
goal = int(input("Enter the amount he want to gain: "))
n = int(input("How many times you want to repeat experiment:"))
gambler(stake, goal, n) #function calling