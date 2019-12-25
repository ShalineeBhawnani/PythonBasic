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
    try:
        with open("json_file.json") as f:
            data= json.load(f)
    except FileNotFoundError:
        print("file not found")
    
class Search:
     def search(self):
         if (inp == "d") or (inp == "D"):
            for doctor in data["Doctors"]:
                print(doctor)
         elif (inp=="p") or (inp=="P"):
            for patient in data["Patients"]:
                print(patient)
find=Search()
find.search()
         