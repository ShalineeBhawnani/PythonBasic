import json
import InventoryFactory

class Inventory:
    def iventoryCal(self):
        #Reading JSON from a File
        with open('inventory_json.json') as f:

            #read string from JSON & storing in variable
            data= json.load(f)
            print(data)

obj=Inventory()
obj.iventoryCal()