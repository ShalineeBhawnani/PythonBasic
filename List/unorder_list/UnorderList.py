# ******************************************************************************************************************
# @purpose :Demonstrate UnorderList.
# @file  :UnorderList.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************

#importing util from utility
from Utility.util import Node

#creating class
class linked_list:

    #default constuctor
    def __init__(self):
        self.head = None

    #creating method to push the data
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # remove the list item with the item
    def deleteNode(self, key):

        temp = self.head

        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if (temp == None):
            return

        prev.next = temp.next

        temp = None

    #print the list
    def printList(self):
        temp = self.head
        while (temp):
            print
            " %d" % (temp.data),
            temp = temp.next

    # search the linked list for the node that has this value
    def search(self, key):
        cur_node = self.head
        while cur_node.next is not None:
            if cur_node.data == key:
                self.deleteNode(key)
            cur_node = cur_node.next
        else:
            self.push(key)
            cur_node = cur_node.next

        return
    def display(self):
        list1 = []
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
def open_file():
    i = 1
    f = open("A.txt", "r+")
    line = f.read()
    li = linked_list()
    for word in line.split( ):
        li.push(word)
        i += 1
    li.display()
    key = input("enter a word to search: ")
    li.search(key)
    li.deleteNode(key)
    li.display()
    f.write(" "+str(key))
    f.close()


open_file()