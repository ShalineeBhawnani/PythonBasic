#**********************************************************************************************************************
# @purpose :Clinique Management System using JSON.
# @file  :Clinique.py
# @author :ShalineeBhawnani
#**********************************************************************************************************************
try:
    import json
except ImportError:
    print("import error")
    
#Executing as main program
if __name__ == '__main__' :
    inp = input(" Searching for doctor or Patients(d/p):")
    if (inp == "d") or (inp == "D"):
        try:
            f = open("json_file.json","r")
            data= json.load(f)
        except FileNotFoundError:
            print("file not found")
        for doctor in data["Doctors"]:
            print(doctor)
    elif (inp=="p") or (inp=="P"):
        try:
            f=open("json_file.json","r")
            data=json.load(f)
        except FileNotFoundError:
            print("file not found")
        for patient in data["Patients"]:
            print(patient)
# class Clinique:
#     def FileOpen(self):
#         try:
#             with open('json_file.json') as file:
#                 data=json.load(file)
#                 print(data)
#         except FileNotFoundError:
#             print("file not found")
        

# clinique=Clinique()
# clinique.FileOpen()
