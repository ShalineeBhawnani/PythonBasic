import math
arr=[]
with open('MyFirstFile.txt','r') as f:
    for line in f:
        for word in line.split():
            arr.append(word)
            print(arr)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert(root, item):
    temp = Node(item)

    if (root == None):
        root = temp
    else:
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp

    return root


def display(root):
    while (root != None):
        print(root.data, end=" ")
        root = root.next


def arrayToList(arr, n):
    root = None
    for i in range(0, n, 1):
        root = insert(root, arr[i])

    return root
word1 = input("search the word is present or not: ")
    if word1 in arr:
        arr.remove(word1)
    else:
        arr.append(word1)
    print(arr)


if __name__ == '__main__':
    arr =[]
    n = len(arr)
    root = arrayToList(arr, n)
    display(root)
