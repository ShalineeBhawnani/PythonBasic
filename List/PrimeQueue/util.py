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

