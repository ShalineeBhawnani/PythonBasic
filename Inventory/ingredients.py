#Import generators for  sequence of results 
from __future__ import generators
try:
    import random
    from enum import Enum, auto
except:
  print("An exception occurred")
#declearing Enum
class InventoryType(Enum):
    RICE  = auto() # Some Rice
    PULSES  = auto() # Some Pulses

#creating interface
class Inventory(object):
    pass
#implementing interface in rice class
class Rice(Inventory):
    def name(self): 
        print("Brown Rice")
        print("Rajbhoga")
        print("Kidney Beans")
    def price(self): 
        total_rice_price=0
        price=2000
        print("Brown Rice price",price)
        price1=3000
        print("Rajbhoga price",price)
        price2=4000
        print("Kidney Beans price",price)
        total_rice_price=0
        total_rice_price=price+price2+price2
        print(total_rice_price)
  
#implementing interface in pulses class      
class Pulses(Inventory):
    def name(self): 
        print("Green Gram")
        print("Black lentils")
        print("Kidney Beans")
    
    def price(self): 
        price=250
        print("Brown Rice price",price)
        price1=350
        print("Black lentils price",price1)
        price2=450
        print("Green Gram",price2)
        total_pulses_price=0
        total_pulses_price=price+price2+price2
        print(total_pulses_price)
                
#factory design
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
# Generate datas name strings:
def datasNameGen(n):

    types = list(InventoryType)

    for i in range(n):
        yield random.choice(types)

#taking random value for 5 times
data = [ InventoryFactory.create(i) for i in datasNameGen(5)]

for datas in data:
    datas.name()
    datas.price()
