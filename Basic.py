#num1=20
#num2=20
#sum=num1+num1
#print("some of {0} & {1} is {2}".format(num1, num2, sum))


#number1= float(input("First Number"))
#number2= float(input("second Number"))
#print(type(number2))
#print(number1+number2)


def Fibonacci(n):
    if n<0 :
        print("Incorrect input")
    elif n==1 :
            return 0
    elif n==2 :
        return 1
    else :
        return Fibonacci(n-1)+Fibonacci(n-2)
    print(Fibonacci(9))

print(Fibonacci(9))