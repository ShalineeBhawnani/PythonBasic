#******************************************************************************************************************
# @purpose :Evaluate the Stock Report using JSON.
# @file  :Stock.py
# @author :ShalineeBhawnani
#*******************************************************************************************************************
import json

if __name__ == '__main__' :
    inp = input(" Are having an Existing Account? (y/n):")
    if (inp == "y") or (inp == "Y"):
        
        f = open("newUser.json","r")
        data_key= json.load(f)
        user=input("\nType:4 for buying shares")
        if user=='4':
            customerId=input("Enter the customer Id: ")   
            for data in data_key["User"]:
            
                if data["customerId"] == "1":
                    print("Welcome",data["Name"])
                    break
                elif data["customerId"] == "2":
                    print("Welcome",data["Name"])
                elif data["customerId"] == "3":
                    print("Welcome",data["Name"])
                    break
                elif data["customerId"] == "4":
                    print("Welcome",data["Name"])
                    break
                else: 
                    print("no customer")
                    break
                   
        #filename = input("Enter the File name: ")
    else:
        f = open("newUser.json","a+")
        customerId=input("Enter the customer Id: ")
        name = input("Enter the Name: ")
        Age = int(input("Enter the Age: "))
        phno = int(input("Enter your Mobile Number: "))
        amount = int(input("Enter the Amount for Shares: "))
        cont = f.write(' [{'+'    "customerId" : "'+ customerId +'",\n' + '       "Name" : "'+ name +'",\n' + '       "Age"  : "'+str(Age)+'",\n'+'       "Ph.No" : "'+str(phno)+'",\n'+'       "Share Amount" : "'+str(amount)+'"      }]\n')
        print("The Data has been Stored Successfully in 'newUser.json' file. ")

class StockAccount:
    #getting details from json file
    def getStockDetails(self):
        file=open("/home/bridgelabz/Videos/DS/Commercial_Data_Processing/company_shares.json","r")
        #loading data from json
        data_key= json.load(file)
        data1=data_key["Company"]
        data2=data_key["Shares"]
        data3=data_key["Products"]
        entry1=0

        #taking input from customer to buy shares
        type=int(input("\nType:0 for HCL share:Production\nType:1 for TCS share:Sales\nType 2 for CGI share: Marketing"))
        if type==0:
            for data in data_key["Shares"]:
                if data['share'] == "Production":
                    input_amount=int(input("enter amount"))  
                    data['amount'] -= input_amount
                    with open('company_shares.json', '+w') as json_file:
                        json.dump(data_key, json_file)
        if type==1:
            for data in data_key["Shares"]:
                print("hello")
                if data['share'] == "Sales": 
                    input_amount=int(input("enter amount"))
                    data['amount'] -= input_amount
                    with open('company_shares.json', '+w') as json_file:
                        json.dump(data_key, json_file)
        if type==2:
            for data in data_key["Shares"]:
                print("hello")
                if data['share'] == "Marketing":
                    input_amount=int(input("enter amount"))
                    data['amount'] -= input_amount
                    with open('company_shares.json', '+w') as json_file:
                        json.dump(data_key, json_file)

        else: ("bye")

#creating object
obj1=StockAccount()
obj2=obj1.getStockDetails()


   