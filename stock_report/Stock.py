#******************************************************************************************************************
# @purpose :Evaluate the Stock Report using JSON.
# @file  :Stock.py
# @author :ShalineeBhawnani
#*******************************************************************************************************************

#importing json file
import json

class Stock:
    def getStockDetails(self):
        #Reading JSON from a File
        with open('stock_json.json') as f:

            #read string from JSON & storing in variable
            data1= json.load(f)
            data=data1["Stock_report"]
        return data

stock=Stock()
a =stock.getStockDetails()