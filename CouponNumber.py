# ******************************************************************************************************************
# @purpose :Demonstrate CouponNumber.
# @file  :CouponNumber.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************
import random
arr1=[]
arr2=[]
def randomNumber():
    n = int(input("choose n number:"))
    while n >0:
        num1 = random.randint(1, 9)
        arr1.append(num1)

        n -= 1
    print("number", arr1)
    for i in arr1:
        if i not in arr2:
           arr2.append(i)
    print("number2",arr2)




randomNumber()
