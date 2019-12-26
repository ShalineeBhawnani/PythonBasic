#**********************************************************************************************************************
# @purpose :Address Management System using JSON.
# @file  :AddressBook.py
# @author :ShalineeBhawnani
#**********************************************************************************************************************
try:
    import json
except ImportError:
    print("import error")
class AddressBook:
    def print_address_details(self):
        #Reading JSON from a File
        with open('/home/bridgelabz/Videos/DS/Address_Book/address_json.json') as f:

            #read string from JSON & storing in variable
            data= json.load(f)
address=AddressBook()
address.print_address_details()