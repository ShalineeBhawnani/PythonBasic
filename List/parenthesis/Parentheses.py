# ******************************************************************************************************************
# @purpose :Demonstrate Parentheses.
# @file  :Parentheses.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************str = input("enter the string")

from Utility.util import Node
def check(str):
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

check(str)