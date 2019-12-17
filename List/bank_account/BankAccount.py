# ******************************************************************************************************************
# @purpose :Demonstrate BankAccount.
# @file    :BankAccount.py
# @author  :ShalineeBhawnani
# *******************************************************************************************************************

# importing Queue from util class
from Utility.util import Queue

#Creating a Class For Customer Initialisation
class Customer:
    # naming of Bank
    bankname="State Bank"

    # parameterized constructor creation
    def __init__(self, name, balance=0.00):
        
        # body of the constructor
        self.name = name
        self._balance = balance

    # method to deposit amount
    def deposit(self, amount):
        self._balance += amount
        print("balance", self._balance)
        queue.enqueue(amount)
        queue.printQueue()

    # method to withdraw amount
    def withdraw(self, amount):
        if amount > self._balance:
            print("insufficient balance")
        self._balance -= amount
        queue.dequeue()
        queue.printQueue()

        # printing balance
        print("balance", self._balance)
        return self._balance

# printing welcome messege & program start from here
print("wel_come to",Customer.bankname)

# taking input from user
num = int(input("enter how many people are in Queue: "))
queue=Queue()
for i in range(num):
    name=input("Enter person name:")
    queue.enqueue(name)
queue.printQueue()
c=Customer(name)
num12=int(input("view options: "))

# run the loop until customer count will be zero
while num12>0:

    # Asking, which opration user want to do for
    print('d-Deposit\nw-Withdraw\ne-Exit')

    option=input("Choose ur option!!")
    if option=='d' or option=='D' :
        amount=float(input(("enter ur amount")))
        c.deposit(amount)

    elif option=='w' or option=='W' :
        amount = float(input(("enter ur amount")))
        result=c.withdraw(amount)
        while result < 1:
            print("bye bye bank empty")
            break
    elif option=='e' or option=='E' :
        print("Thanku")
    num12-=1

