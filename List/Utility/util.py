class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def printQueue(self):
      return self.queue



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class PrimeQueue:
    def __init__(self):
        self.first =  None


    #insert at last
    def pqueue(self,value):
        newnode = Node(value)
        if (self.first == None):
            self.first = newnode
        else:
            temp = self.first
            while temp.next != None:
                temp = temp.next
            temp.next = newnode

