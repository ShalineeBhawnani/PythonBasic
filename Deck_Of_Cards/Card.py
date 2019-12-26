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
    # object is created for card game
    cards = CardGame()  
    # distribute function is called from card game and results will be printed in 2d array
    data = cards.distribute()  

    # print(data) & distributed card will be printed out
    # for loop is used for adding each players cards to the linked list
    for hand in range(len(data)): 
        data[hand].sort()
        # hands are updated to the queue via linked list
        queue.enqueue(data[hand])  
    print()
    print()
    # same distributed cards are printed out in linked list format in queue
    print(queue.get_queue())  

"""
main function is called
"""
if __name__ == '__main__':
    playingCard()