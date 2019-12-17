# ******************************************************************************************************************
# @purpose :Demonstrate Sorting.
# @file  :BubbleSort.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************

#creating method for sorting array
def bubbleSort(arr):

    #checking each & every element 
    for i in range(len(arr)):

        #comparing elements
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[12,33,56,87,123,90,33,55,12]

#calling sorting method
bubbleSort(arr)

#printing array
print(arr)
