# ******************************************************************************************************************
# @purpose :Demonstrate BankAccount.
# @file  :BankAccount.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def printQueue(self):
      return self.queue

class Customer:
    bankname="State Bank"
    def __init__(self, name, balance=0.00):
        self.name = name
        self._balance = balance


    def deposit(self, amount):
        self._balance += amount
        print("balance", self._balance)
        queue.enqueue(amount)
        queue.printQueue()

    def withdraw(self, amount):
        if amount > self._balance:
            print("insufficient balance")
        self._balance -= amount
        queue.dequeue()
        queue.printQueue()

        print("balance", self._balance)
        return self._balance

print("wel_come to",Customer.bankname)
num = int(input("enter how many people are in Queue: "))
queue=Queue()
for i in range(num):
    name=input("Enter person name:")
    queue.enqueue(name)
queue.printQueue()
c=Customer(name)
num12=int(input("view options: "))

while num12>0:

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

