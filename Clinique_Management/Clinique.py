#******************************************************************************************************************
# @purpose :Clinique Management System using JSON.
# @file  :Clinique.py
# @author :ShalineeBhawnani
#*******************************************************************************************************************
import json
class Clinique:
    def FileOpen(self):
        with open('json_file.json') as file:
            data=json.load(file)
            for p in data['Doctors']:
                print('Name: ' + p['name'])
                print('Gender: ' + p['gender'])
                print('Type: ' + p['type'])
                print("Address:" +p['address'])
                print('ContactNumber ' +p['contactNumber'])
clinique=Clinique()
clinique.FileOpen()