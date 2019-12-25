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
                    print("Doctor",data["name"],data["specialization"],"specialist", "Availability Time",data["availability"])
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
         
find=Search()
find.search()