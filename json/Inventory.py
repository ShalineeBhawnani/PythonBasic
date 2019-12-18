import json

with open('json_file.json') as f:
    data= json.load(f)
for Rice in data['Rice']:
    print(Rice)
for Pulses in data['Pulses']:
    print(Pulses)
for Wheats in data['Wheats']:
    print(Wheats)
    rice=data["Rice"]
    pulses=data["Pulses"]
    wheats=data["Wheats"]

total_price = 0
total_weight =0

for item in rice:
    total_price += item["price"]
    total_weight +=item["weight"]
print("total price of rice :",total_price)
print("total weigth of rice :",total_weight)

for item in pulses:
    total_price += item["price"]
    total_weight +=item["weight"]
print("total price of pulses :",total_price)
print("total weigth of pulses :",total_weight)

for item in wheats:
    total_price += item["price"]
    total_weight +=item["weight"]
print("total price of wheats :",total_price)
print("total weigth of wheats :",total_weight)
 
 
