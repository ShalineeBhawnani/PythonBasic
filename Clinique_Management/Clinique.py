#**********************************************************************************************************************
# @purpose :Clinique Management System using JSON.
# @file  :Clinique.py
# @author :ShalineeBhawnani
#**********************************************************************************************************************  
import json
class Search:
    def search(self):
        inp = input(" whos details u want? (d/p):")
        if (inp == "d") or (inp == "D"):
            try:
                f = open("json_file.json","r")
                data_key= json.load(f)

            except FileNotFoundError:
                print("file not found")
        #taking user Id from user
            specialization=input("please Type Doctor specialization:")  
            for data in data_key["Doctors"]:
                if data["specialization"] == specialization:
                #fetching user name based on given id
                    print("Doctor",data["name"],data["specialization"],"specialist", "Availability Time:",data["availability"])
                else:
                    f = open("new_doctor.json","a+")
                    name = input("Enter the Name: ")
                    id=input("Enter the doctor Id: ")
                    specialization = input("Enter the specialization: ")
                    contactNumber = input("Enter your Mobile Number: ")
                    availability = input("Enter the availability time: ")
                    cont = f.write(' [{'+'    "name" : "'+ name +'",\n' + '       "id" : "'+ id +'",\n' + '       "specialization"  : "'+str(specialization)+'",\n'+'       "contactNumber" : "'+str(contactNumber)+'",\n'+'       "availability" : "'+str(availability)+'"    }]\n')
                    print("The Data has been Stored Successfully in 'new_doctor.json' file. ")

        elif(inp == "p") or (inp == "P"):
            try:
                f = open("json_file.json","r")
                data_key= json.load(f)

            except FileNotFoundError:
                print("file not found")
        #taking user Id from user
            name=input("your good name:")  
            for data in data_key["Patients"]:
                if data["name"] == name:
                #fetching user name based on given id
                    print("Patient Name:",data["name"],"Patient Gender:",data["gender"], "Patient Age:",data["age"])
                else:
                    f = open("new_patients.json","a+")
                    name = input("Enter your Name: ")
                    id=input("Enter the patient Id: ")
                    profession = input("Enter the profession: ")
                    gender = input("Enter your gender: ")
                    age = input("Enter yor age: ")
                    weight = input("Enter yor weight: ")
                    height = input("Enter yor height: ")
                    cont = f.write(' [{'+'    "name" : "'+ name +'",\n' + '       "id" : "'+ id +'",\n' + '       "gender" : "'+str(gender)+'",\n'+'       "age" : "'+str(age)+'",\n'+'       "profession"  : "'+str(profession)+'",\n'+'       "weight" : "'+weight+'",\n'+'       "height" : "'+height+'"  }]\n' )
                    print("The Data has been Stored Successfully in 'new_patient.json' file. ")

find=Search()
find.search()