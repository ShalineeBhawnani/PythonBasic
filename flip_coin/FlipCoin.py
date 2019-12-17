# ******************************************************************************************************************
# @purpose :Demonstrate FlipCoinToss.
# @file  :FlipCoin.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************

#import random function
import random

#creating method to toss coin
def flipcoin():

    #initialize head & tail 0
    headcount = 0
    tailcount = 0
    count = 0

    #checking count value
    while count <100:
        coin= random.randint(1,2)

        if coin == 1:
            print("head\n")
            headcount+=1
            count +=1
        elif coin ==2:
            print("tail\n")
            tailcount+=1
            count+=1

    # return head & tail count
    return headcount,tailcount
    
# calling flipcoin() & printing 
print(flipcoin())

