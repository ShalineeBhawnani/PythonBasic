# ******************************************************************************************************************
# @purpose :Demonstrate Time.
# @file  :StioWatch.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************
#importing time
import time

# creating method to check time difference
def stopwatch():
    startTimer=0
    stopTimer=0

    #taking starting time
    time1=input("Do u want to start?")
    time_start=time.time()

    #taking stop time 
    time2= input("Do u want to stop?")
    time_stop=time.time()

    #finding difference between start & ending time
    mid=time_stop-time_start

    #printing difference
    print(mid)
    return mid

#calling method for execution
stopwatch()

