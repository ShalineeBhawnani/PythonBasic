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
            #storing key
            data = data1["Stock_report"]
        return data

#creating object of class
stock=Stock()
#storing method return value
a =stock.getStockDetails()