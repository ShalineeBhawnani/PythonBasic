# ******************************************************************************************************************
# @purpose :Demonstrate CouponNumber.
# @file  :CouponNumber.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************

# importing random function
import random

#initializing empty array
arr1=[]
arr2=[]

#creating method to check randomNumber
def randomNumber():

    #taking input from user
    n = int(input("choose n number:"))
    while n >0:
        num1 = random.randint(1, 9)

        #appending random number & storing in array
        arr1.append(num1)

        n -= 1
    #printing array
    print("number", arr1)
    for i in arr1:
        
        #checking element in array2
        if i not in arr2:
            #appending array in array2
           arr2.append(i)

    #printing array2
    print("number2",arr2)

#calling method
randomNumber()
