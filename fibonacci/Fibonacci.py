#******************************************************************************************************************
# @purpose :Demonstrate Fibonacci.
# @file  :Fibonacci.py
# @author :ShalineeBhawnani
#*******************************************************************************************************************

#creating method to check Fibonacci number
def Fibonacci(n):
    if n<0 :
        print("Incorrect input")
    elif n==1 :
            return 0
    elif n==2 :
        return 1
    else :
        #retuning fibonacci number
        return Fibonacci(n-1)+Fibonacci(n-2)
    print(Fibonacci(9))

#printing Fibonacci number
print(Fibonacci(9))