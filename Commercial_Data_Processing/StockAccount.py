import json
class StockAccount:
    def getStockDetails(self):
        #Reading JSON from a File
        file=open("/home/bridgelabz/Videos/DS/Commercial_Data_Processing/company_shares.json","r")

        data_key= json.load(file)
        print(data_key)
        data1=data_key["Company"]
        data2=data_key["Shares"]
        data3=data_key["Products"]
        entry1=0
        type=input("Type:0 for HCL share:Production\nType:1 for TCS share:Sales\nType 2 for CGI share: Marketing")
        if type==0:
            entry1 = data2[0]
            entry1=entry["amount"]
            print(entry1)
            return entry1
       
        elif type==1:
           entry1 = data2[1]
           entry1=entry["amount"]
           return entry1
       
        elif type==2:
            entry1 = data2[2]
            entry1=entry["amount"]
            return entry1
        #count = 0
        # for name in entry:
        #     print(name["amount"])
        #     count+=1
        # print(count)
            
        else: 
            print ("wrong chooise") 
        return entry1
        
    

    # def updateJson(self,data2):
    #     result=[sub["amount"] for sub in data2 ]
    #     input_amount=int(input("enter amount"))
    #     for i in result:
    #         list1=i- input_amount
    #         print(list1)
    #         return list1
    def updateJson(self,entry1):
        input_amount=int(input("enter amount"))
        sub = entry1 - input_amount
        print(sub)
        return sub

obj1=StockAccount()
obj2=obj1.getStockDetails()
obj3=obj1.updateJson(obj2)

if __name__ == '__main__' :

    inp = input(" Are having an Existing Account? (y/n):")
    if (inp == "y") or (inp == "Y"):
        filename = input("Enter the File name: ")
        obj1.getStockDetails()
        with open('person.json', 'w') as json_file:
            json.dump(obj3, json_file)
    else:
        f = open("newUser.json","a+")
        name = input("Enter the Name: ")
        Age = int(input("Enter the Age: "))
        phno = int(input("Enter your Mobile Number: "))
        amount = int(input("Enter the Amount for Shares: "))
        cont = f.write(' [{'+'     "Name" : "'+ name +'",\n' + '        "Age"  : "'+str(Age)+'",\n'+'       "Ph.No" : "'+str(phno)+'",\n'+'"Share Amount" : "'+str(amount)+'" }]\n'+''         )
        print("The Data has been Stored Successfully in 'newUser.json' file. ")