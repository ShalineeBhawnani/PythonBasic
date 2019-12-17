# ******************************************************************************************************************
# @purpose :Demonstrate Gambler.
# @file  :Gambler.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************

#import random function 
import random

#taking value of stake,goal & trails
def gambler(stake,goal,trails):

    # Run trialCount experiments that start with stake and terminate on
    # 0 or goal.
    bets=0
    win=0
    loss=0
    for i in range(0,51):
        cash=stake
        while(cash>0 and cash<goal):

            # Simulate one bet.
            bets+=1

            #storing random number
            num= random.randint(1,2)
            if num==1:
                cash+=1
            elif num==2:
                cash-=1

            if cash==goal:
                win+=1
            else:
                loss+=1
                
        #printing number of bets
        print("number of bet", bets)
        return win,loss

wins,loss=gambler(20,30,40)
print("number of win",wins)
print("number of loss",loss)
print(f"percentage of win {(wins/(wins+loss))*100}")
print(f"percentage of loss {(loss/(wins+loss))*100}")

