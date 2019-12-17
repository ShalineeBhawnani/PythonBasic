#******************************************************************************************************************
# @purpose :Demonstrate Searching.
# @file  :BinarySearch.py
# @author :ShalineeBhawnani
#*******************************************************************************************************************

# taking input from user
#arr = [ 2, 3, 4, 10, 40 ]
arr = ['aa','bb','cc','dd','ee','ff','gg','hh']
#n=int(input("enter number from given index:"))
n=input("enter string for search:")

# creating method to check binary number
def binary(arr,f,l,n):
    if f<=l:
        mid=(l+f)//2
        if arr[mid]==n:
            return mid
        elif arr[mid]>n:
            l=mid-1
            return l
        else:
            f = mid + 1
            return f
    return -1

# storing result 
result=binary(arr,0,len(arr)-1,n)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
