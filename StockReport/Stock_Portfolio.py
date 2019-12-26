#******************************************************************************************************************
# @purpose :Evaluate the Stock Report using JSON.
# @file  :Stock_Protfolio.py
# @author :ShalineeBhawnani
#*******************************************************************************************************************

import json
from Stock import Stock

class Stock_Portfolio:
    def gettingAllData(self,data):
       
        total_number_of_share =0
        total_share_price =0
        total_stock_price =0

        #itrating total price & shares & stock price of the Stock_report
        for item in data:
            total_number_of_share = total_number_of_share+item["number_of_share"]
            total_share_price = total_share_price+item["share_price"]
            total_stock_price = total_stock_price+item["stock_price"]

        print("total number_of_share :",total_number_of_share)
        print("total share_price :",total_share_price)
        print("total stock_price :", total_stock_price)
       
    def eachdata(self,data):

        each_price=0

        #itrating each item_price & shares_price of the Stock_report
        for item in data:
            each_price=item["share_price"] * item["stock_price"]
            print("each_price :", each_price)
           
        #converting data in string
        json_string = json.dumps(data)
        print(json_string)

stock=Stock()
data = stock.getStockDetails()
obj=Stock_Portfolio()
obj.gettingAllData(data)
obj.eachdata(data)

