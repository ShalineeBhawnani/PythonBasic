# ******************************************************************************************************************
# @purpose :Demonstrate Parentheses.
# @file  :Parentheses.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************str = input("enter the string")

#importing util from utility
from Utility.util import Node

#creating method to check parantheses
def check(str):

    #initializing empty stack(list)
    stack = []
    for i in str:
        if i =='(' or i=='{' or i== '[':
            stack.append(i)
        elif i ==')' or i=='}' or i== ']':
            stack.pop()
    if len(stack)==0:
        print(True)
    else:
        print(False)

# calling check method
check(str)