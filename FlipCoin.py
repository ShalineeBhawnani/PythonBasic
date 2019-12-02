import random
def flipcoin():
    headcount = 0
    tailcount = 0
    count = 0
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
    return headcount,tailcount
print(flipcoin())

