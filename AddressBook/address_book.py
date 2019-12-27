#**********************************************************************************************************************
# @purpose :Address Management System using JSON.
# @file  :AddressBook.py
# @author :ShalineeBhawnani
#**********************************************************************************************************************
try:
    import json
except ImportError:
    print("import error")

# address book class is created
class AddressBook():  

    # here file is initialised with file name
    def __init__(self, filename):  
        with open(filename) as f:
             # json file is loaded
            self.data = json.load(f) 
    # this function is used for added data to the json file
    def addRecord(self):  
        while True:
            try:
                cities = ["jammu", "chhatisgarh", "bhopal" ]
                states = ["j&k", "chhatisgarh", "bhopal"]

                first_name = input("enter your first name :")
                if first_name.isalpha() is False:
                    print("enter vaild name ")
                    continue

                last_name = input("enter your last name :")
                if last_name.isalpha() is False:
                    print("length of last name should be less than 26")
                    continue

                address = input("enter your 1st and 2nd line of address :")
                if len(address) >= 100:
                    print("length of address should be less than 100")
                    continue

                for i in cities:
                    print("cities", i, end=" ")
                city = input("\nenter the city name from above list :")
                while True:
                    flag = 0
                    try:
                        for i in cities:
                            if city == i:
                                print("done")
                                flag = 1
                                break
                            else:
                                return
                        if flag == 1:
                            break
                    except ValueError:
                        print("error")

                state = input("enter the state name :")

                zipcode = int(input("enter the zip code :"))
                if len(str(zipcode)) >= 7:
                    print("length of input should be less than 7")
                    continue

                phone_number = int(input("enter the full mobile number"))
                if phone_number <= 916000000000 or phone_number >= 920000000000:
                    print("enter vaild number starting from 91")
                    continue

                # dic is used for storing user input data
                dic = {"first_name": first_name,
                       "last_name": last_name,
                       "address": address,
                       "city": city,
                       "state": state,
                       "zipcode": zipcode,
                       "phone_number": phone_number}
                print("user data added successfully")

                data = self.data
                # user data is added to the file
                data.append(dic)
                # now data and input data is called in main file  
                print(dic)  
                break
            except ValueError:
                print("check user input")
    # this function is used for deleting data in the json file
    def delete(self):  

        # input is used for deleting data
        datadelete = input("\nname of the person you want to delete from the address book :")
        print(datadelete, "is deleted from address book ")

        name = []
        for i in range(len(self.data)):
            name.append(self.data[i]["first_name"])
        # index is used for keeping track of the index where we have to delete the data
        index = -1  
        # para is used for transversing through the data
        for para in self.data:  
            index += 1
            # if condition is used for checking user input
            if datadelete == para["first_name"]: 
                # here data is deleted if data  matches 
                del self.data[index] 
                # index is returned for future 
                return index  
        print(datadelete, " is deleted from address book ")
    # this function is used for printing data in mailing format
    def printData(self):  

        data = self.data
        # for loop is used transversing values through data
        for i in range(len(data)):  
            for j in data[i].values():
                print(j)
            print()

    def sort(self):  # sort function is used for sorting the data in json file

        array = []
        data = self.data  # data is stored in var

        for i in range(len(self.data)):  # first name is appended in array
            array.append((self.data[i]["first_name"]))
        name_sort = sorted(array)  # here only names are sorted

        sorteddata = []  # this empty array is used for storing sorted file

        for i in name_sort:  # nested loop is used for matching sorted names to file
            for j in range(len(data)):
                if i == data[j]["first_name"]:
                    sorteddata.append(data[j])  # if name matches then data is appended

        self.data = sorteddata  # now we have swapped data with sorted data
        return sorteddata  # here we have return sorted data

    def dumping(self, filename):  
        # this function is used for dumping edited data to the json file
        with open('/home/bridgelabz/Videos/DS/AddressBook/address_json.json', 'w') as f:
            json.dump(self.data, f, indent=2)

    def onlyNames(self):  # this function is used for printing only names from the file
        data = self.data
        for i in range(len(data)):

             print("**", (data[i]["first_name"]), end=" ")
