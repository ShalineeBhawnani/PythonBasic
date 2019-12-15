# ******************************************************************************************************************
# @purpose :Demonstrate Time.
# @file  :StioWatch.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************
import time
def stopwatch():
    startTimer=0
    stopTimer=0
    time1=input("Do u want to start?")
    time_start=time.time()
    time2= input("Do u want to stop?")
    time_stop=time.time()
    mid=time_stop-time_start
    print(mid)
    return mid

stopwatch()

