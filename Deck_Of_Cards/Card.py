#******************************************************************************************************************
# @purpose :Evaluate the DeckOfCards.
# @file  :Card.py
# @author :ShalineeBhawnani
#*******************************************************************************************************************
# @import statement
try:
    from DS.PythonBasic import Deck
    from random import random,shuffle
except ImportError:
    print("import error")

#creating play method
def playingCard():
    cards = CardGame()  # object is created for card game

    data = cards.distribute()  # distribute function is called from card game and results will be printed in 2d array

    # print(data)   # distributed card will be printed out

    for hand in range(len(data)):  # for loop is used for adding each players cards to the linked list
        data[hand].sort()
        queue.enqueue(data[hand])  # hands are updated to the queue via linked list
    print()
    print()
    print(queue.get_queue())  # same distributed cards are printed out in linked list format in queue


"""
main function is called
"""
if __name__ == '__main__':
    playingCard()