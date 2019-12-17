# ******************************************************************************************************************
# @purpose :Demonstrate QuadraticEquestion.
# @file  :Quadratic.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************

#import math funtion
import math
a = 3
b = 19
c = 8

# creating method for getting delta
def quadratic(a,b,c):
    delta=b*b-4*a*c

    # deffinig root
    if delta>0:
        root1=(-b+math.sqrt(delta))/(2*a)
        root2=(-b-math.sqrt(delta))/(2*a)
    
    #returning root value
    return [root1,root2]

