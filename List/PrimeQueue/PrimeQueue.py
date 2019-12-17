# ******************************************************************************************************************
# @purpose :Demonstrate PrimeQueue.
# @file  :PrimeQueue.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************
from util import *
def is_primeQueue(Range):
    lst=[]
    for i in range(2,Range+1):
        count=0
        for j in range(1,i+1):
            if (i%j)==0:
                count+=1
        if count==2:
            lst.append(i)
    print(lst)
    is_anagramQueue(lst)

#anagram logic
def is_anagramQueue(lst):
    lst1=[]
    lst2=[]
    for i in lst:
        lst1.append(str(i))
    print("lst1 string=",lst1)
    for i in lst1:
        if i=='2' or i=='3' or i=='5' or i=='7':
            lst2.append(int(i))
            print("lst2=",lst2)
        else:
            for j in lst1:
                #print(type(i),"->",type(j),end=" ")
                if len(i)==len(j):
                    #print(i)
                    x=sorted(i)
                    y=sorted(j)
                    count=0
                    for k in range(0,len(i)):
                        if x[k]==y[k]:
                            count+=1
                    if count==len(i):
                        lst2.append(int(i))

    print(lst2)
    primequeue=PrimeQueue()
    for i in lst:
        primequeue.pqueue(i)
    primequeue.Printqueue()




    def Printqueue(self):
        if self.first==None:
            print("queue is Empty")
        temp = self.first
        while temp != None:
            print(temp.data, end="->")
            temp = temp.next