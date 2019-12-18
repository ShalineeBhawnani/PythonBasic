import os

# A structure to represent a queue  
class Queue:

    # default constructor to ininialize data
    def __init__(self):
        self.queue = []

    # method for add an item to the right side of the list
    def enqueue(self, item):
        self.queue.append(item)

    # method for removing data
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # count the number of items with a certain value
    def size(self):
        return len(self.queue)

    # print the queue
    def printQueue(self):
      return self.queue

# creating Class
class Node:

    # constructor to initiate this object
    def __init__(self,data):
        self.data = data
        self.next = None

# creating class
class PrimeQueue:

    # default constructor
    def __init__(self):
        self.first =  None


    #insert data at last 
    def pqueue(self,value):
        newnode = Node(value)
        if (self.first == None):
            self.first = newnode
        else:
            temp = self.first
            while temp.next != None:
                temp = temp.next
            temp.next = newnode

