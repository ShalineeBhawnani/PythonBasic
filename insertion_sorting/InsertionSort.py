# ******************************************************************************************************************
# @purpose :Demonstrate Sorting.
# @file  :InsertionSort.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************
# storing array element
arr = [122, 131, 153, 25, 64]

#creating metod to take array
def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1

        #swaping element
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
#calling method
insertionsort(arr)

#print sorted array
print (arr)