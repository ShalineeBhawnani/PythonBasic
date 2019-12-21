import json
class StockAccount:
      def getStockDetails(self):
        #Reading JSON from a File
        file=open("/home/bridgelabz/Videos/DS/Commercial_Data_Processing/company_shares.json","r")

        data_key= json.load(file)
        data1=data_key["Users"]
        data2=data_key["Shares"]
        data3=data_key["Products"]
        list1=[]
        list1.append(data1)
        list1.append(data2)
        list1.append(data3)
        print(list1)
     
#creating object of class
StAc=StockAccount()
#storing method return value
StAc.getStockDetails()

if __name__ == '__main__' :

    inp = input(" Are having an Existing Account? (y/n):")
    if (inp == "y") or (inp == "Y"):
        filename = input("Enter the File name: ")
        StAc.getStockDetails()
    else:
        f = open("newUser.json","a+")
        name = input("Enter the Name: ")
        Age = int(input("Enter the Age: "))
        phno = int(input("Enter your Mobile Number: "))
        amount = int(input("Enter the Amount for Shares: "))
        cont = f.write(' [{'+'     "Name" : "'+ name +'",\n' + '        "Age"  : "'+str(Age)+'",\n'+'       "Ph.No" : "'+str(phno)+'",\n'+'"Share Amount" : "'+str(amount)+'" }]\n'         )
        print("The Data has been Stored Successfully in 'newUser.json' file. ")