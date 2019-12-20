from __future__ import generators
import random
from enum import Enum, auto

class InventoryType(Enum):
    RICE  = auto() # Some Rice
    PULSES  = auto() # Some Pulses

class Inventory(object):
    pass

class Rice(Inventory):
    def name(self): 
        print("Rice.name")
    def price(self): 
        print("Rice.price")

class Pulses(Inventory):
    def name(self): 
        print("Pulses.name")
    def price(self): 
        print("Pulses.price")

class InventoryFactory(object):

    @staticmethod
    def create(type):
        #return eval(type + "()") # simple alternative
        if type in InventoryFactory.choice:
            return InventoryFactory.choice[type]()

        assert 0, "No data Found: " + type    

    choice = { InventoryType.RICE:  Rice,
               InventoryType.PULSES:  Pulses                
             }

# Test factory
# Generate shape name strings:
def shapeNameGen(n):

    types = list(InventoryType)

    for i in range(n):
        yield random.choice(types)

data = \
  [ InventoryFactory.create(i) for i in shapeNameGen(2)]

for shape in data:
    shape.name()
    shape.price()