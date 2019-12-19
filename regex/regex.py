import re
with open ('file.txt', 'r') as f:
    text = f.read()
    print(text)
result = re.sub(r"[<]{2}[a-zA-Z]{4}[>]{2}", "<<Shalu>>", text)
result = re.sub(r"[<]{2}[a-zA-Z]{8}[>]{2}", "<<Shalu Bhawnani>>", result)
result = re.sub(r"(x){10}", "4567586948", result)
result = re.sub(r"XX/XX/XXXX", "01/01/2016", result)
file1 = open("file.txt","w")
file1.write(result) 
print(result)