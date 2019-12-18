#******************************************************************************************************************
# @purpose :Evaluate the Iventry object using JSON.
# @file  :json.py
# @author :ShalineeBhawnani
#*******************************************************************************************************************

#importing json file
import json

#Reading JSON from a File
with open('json_file.json') as f:

    #read string from JSON & storing in variable
    data= json.load(f)

for Rice in data['Rice']:
    print(Rice)
for Pulses in data['Pulses']:
    print(Pulses)
for Wheats in data['Wheats']:
    print(Wheats)

    #Storing data
    rice=data["Rice"]
    pulses=data["Pulses"]
    wheats=data["Wheats"]

total_price = 0
total_weight =0

#itrating total price & weight of the Rice
for item in rice:
    total_price += item["price"]
    total_weight +=item["weight"]
print("total price of rice :",total_price)
print("total weigth of rice :",total_weight)

#itrating total price & weight of the pulses
for item in pulses:
    total_price += item["price"]
    total_weight +=item["weight"]
print("total price of pulses :",total_price)
print("total weigth of pulses :",total_weight)

#itrating total price & weight of the wheats
for item in wheats:
    total_price += item["price"]
    total_weight +=item["weight"]
print("total price of wheats :",total_price)
print("total weigth of wheats :",total_weight)

#converting data in
json_string = json.dumps(data)
print(json_string)
 
 
