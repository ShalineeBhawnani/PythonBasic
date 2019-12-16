 # ******************************************************************************************************************
# @purpose :Demonstrate Palimdrome.
# @file  :Palimdrome.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************	 def is_palindrome(str):
    palindrome=Palindrome()
    for i in str:
        palindrome.insertfirst(i)
    result=palindrome.printpalindrome()
    count=0
    for i in range(len(str)):
        if result[i]==  str[i]:
            count+=1
    if count==len(str):
        print()
        print("String is palindrome")
    else:
        print()
        print("String is not palindrome")

class Node4:
    def __init__(self,data):
        self.data=data
        self.next=None

class Palindrome:
    def __init__(self):
        self.head=None

    def insertfirst(self,val):
        if self.head==None:
            self.head=Node4(val)
        else:
            newnode=Node4(val)
            newnode.next=self.head
            self.head=newnode

    def printpalindrome(self):
        if self.head==None:
            print("list is empty")
        else:
            temp = self.head
            y=[]
            while temp != None:
                print(temp.data, end="->")
                x=temp.data
                y.append(x)
                temp = temp.next
        return y