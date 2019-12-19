#******************************************************************************************************************
# @purpose :Evaluate the Stock Report using JSON.
# @file  :inventory.py
# @author :ShalineeBhawnani
#*******************************************************************************************************************

#importing json file
import json

class Stock:
    def getStockDetails(self):
        #Reading JSON from a File
        with open('stock_json.json') as f:

            #read string from JSON & storing in variable
            data= json.load(f)
            print(data)

stock=Stock()
stock.getStockDetails()
