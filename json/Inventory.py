import json

with open('json_file.json') as f:
    data= json.load(f)
for Rice in data['Rice']:
    print(Rice)
for Pulses in data['Pulses']:
    print(Pulses)
for Wheats in data['Wheats']:
    print(Wheats)
