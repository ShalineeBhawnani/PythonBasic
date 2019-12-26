#**********************************************************************************************************************
# @purpose :Clinique Management System using JSON.
# @file  :Clinique.py
# @author :ShalineeBhawnani
#**********************************************************************************************************************
try:
    import json
except ImportError:
    print("import error")
class Search:
    # searching doctor & patients
    def search(self):
        #taking input from user
        select = input(" who's details u want? (d/p):")
        #taking d for doctor
        if (select == "d") or (select == "D"):
            try:
                #open json file
                f = open("Clinique_Management/json_file.json","r")
                data_key= json.load(f)

            except FileNotFoundError:
                print("file not found")
            #taking user Id from user
            specialization=input("please Type Doctor specialization:")  
            #check data in key
            for data in data_key["Doctors"]:
                if data["specialization"] == specialization:
                    #fetching doctor details based on given id
                    print("Doctor",data["name"],data["specialization"],"specialist", "Availability Time:",data["availability"])
                else:
                    f = open("Clinique_Management/new_doctor.json","a+")
                    def search(self):
                        contactNumber = input("Enter your Mobile Number: ")
                        availability = input("Enter the availability time: ")
                        cont = f.write(' [{'+'    "name" : "'+ name +'",\n' + '       "id" : "'+ id +'",\n' + '       "specialization"  : "'+str(specialization)+'",\n'+'       "contactNumber" : "'+str(contactNumber)+'",\n'+'       "availability" : "'+str(availability)+'"    }]\n')
                        #entring new doctor details based on requirment
                        print("The Data has been Stored Successfully in 'new_doctor.json' file. ")
        elif(select == "p") or (select == "P"):
            try:
                f = open("Clinique_Management/json_file.json","r")
                data_key= json.load(f)

            except FileNotFoundError:
                print("file not found")
        
            #taking patients name from user
            name=input("your good name:")  
            for data in data_key["Patients"]:
                if data["name"] == name:
                #fetching user name based on given id
                    #fetching patients name based on given name
                    print("Patient Name:",data["name"],"Patient Gender:",data["gender"], "Patient Age:",data["age"])
                else:
                    f = open("Clinique_Management/new_patients.json","a+")
                    def search(self):
                        weight = input("Enter yor weight: ")
                        height = input("Enter yor height: ")
                        cont = f.write(' [{'+'    "name" : "'+ name +'",\n' + '       "id" : "'+ id +'",\n' + '       "gender" : "'+str(gender)+'",\n'+'       "age" : "'+str(age)+'",\n'+'       "profession"  : "'+str(profession)+'",\n'+'       "weight" : "'+weight+'",\n'+'       "height" : "'+height+'"  }]\n' )
                    #adding new patients 
                        print("The Data has been Stored Successfully in 'new_patient.json' file. ")

find=Search()
find.search()