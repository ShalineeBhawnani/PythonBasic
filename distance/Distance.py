# ******************************************************************************************************************
# @purpose :Demonstrate Distance.
# @file  :Distance.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************
#importing math function
import math

#creating method to calculate distance between two point
def calculateDistance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    #printing distance
    print(dist)
    return dist

