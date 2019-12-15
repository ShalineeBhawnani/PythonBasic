# ******************************************************************************************************************
# @purpose :Demonstrate Gambler.
# @file  :Gambler.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************
import random
def gambler(stake,goal,trails):
    bets=0
    win=0
    loss=0
    for i in range(0,51):
        cash=stake
        while(cash>0 and cash<goal):
            bets+=1

            num= random.randint(1,2)
            if num==1:
                cash+=1
            elif num==2:
                cash-=1

            if cash==goal:
                win+=1
            else:
                loss+=1
        print("number of bet", bets)
        return win,loss

wins,loss=gambler(20,30,40)
print("number of win",wins)
print("number of loss",loss)
print(f"percentage of win {(wins/(wins+loss))*100}")
print(f"percentage of loss {(loss/(wins+loss))*100}")

