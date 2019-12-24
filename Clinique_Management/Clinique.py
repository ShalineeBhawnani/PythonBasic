#******************************************************************************************************************
# @purpose :Clinique Management System using JSON.
# @file  :Clinique.py
# @author :ShalineeBhawnani
#*******************************************************************************************************************
try:
    import json
except ImportError:
    print("import error")
class Clinique:
    def FileOpen(self):
        try:
            with open('json_file.json') as file:
                data=json.load(file)
        except FileNotFoundError:
            print("file not found")
        for p in data['Doctors']:
            print('Name: ' + p['name'])
            print('Gender: ' + p['gender'])
            print('Type: ' + p['type'])
            print("Address:" +p['address'])
            print('ContactNumber ' +p['contactNumber'])
clinique=Clinique()
clinique.FileOpen()