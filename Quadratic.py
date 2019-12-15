# ******************************************************************************************************************
# @purpose :Demonstrate QuadraticEquestion.
# @file  :Quadratic.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************
import math
a = 3
b = 19
c = 8
def quadratic(a,b,c):
    delta=b*b-4*a*c

    if delta>0:
        root1=(-b+math.sqrt(delta))/(2*a)
        root2=(-b-math.sqrt(delta))/(2*a)
    return [root1,root2]

