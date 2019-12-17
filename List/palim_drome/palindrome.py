 # ******************************************************************************************************************
# @purpose :Demonstrate Palimdrome.
# @file  :Palimdrome.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************	 def is_palindrome(str):

# importing Node from util class
from Utility.util import Node

# definig method for checking palindrome
def is_palindrome(str):
    palindrome=Palindrome()

    for i in str:
        palindrome.insertfirst(i)
    result=palindrome.printpalindrome()
    count=0

    #loop for comparing length of string
    for i in range(len(str)):
        if result[i]==  str[i]:
            count+=1
    if count==len(str):
        print()
        print("String is palindrome")
    else:
        print()
        print("String is not palindrome")

class Palindrome:

    #default constructor
    def __init__(self):
        self.head=None

    #inserting data
    def insertfirst(self,val):
        if self.head==None:
            self.head=Node4(val)
        else:
            newnode=Node(val)
            newnode.next=self.head
            self.head=newnode

    #printing list
    def printpalindrome(self):
        if self.head==None:
            print("list is empty")
        else:
            temp = self.head
            list2=[]
            while temp != None:
                print(temp.data, end="->")
                x=temp.data
                list2.append(x)
                temp = temp.next
        return list2