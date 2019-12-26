#******************************************************************************************************************
# @purpose :Match regex from string and replace with user details.
# @file  :regex.py
# @author :ShalineeBhawnani
#*******************************************************************************************************************

#importing regex module
try:
    import re
except ImportError:
    print("import error")

class Regex:
    #method to read and write file
    def check(self):
        with open ('file.txt', 'r') as f:
            text = f.read()
            print(text)
        try:
            #pattern matching
            result = re.sub(r"[<]{2}[a-zA-Z]{4}[>]{2}", "<<Shalu>>", text)
            result = re.sub(r"[<]{2}[a-zA-Z]{8}[>]{2}", "<<Shalu Bhawnani>>", result)
            result = re.sub(r"(x){10}", "4567586948", result)
            result = re.sub(r"X{2}/X{2}/X{4}", "01/01/2016", result)
            file1 = open("file.txt","w")
            file1.write(result) 
            print(result)
        except:
            #printing error
            print("An exception occurred")
 
#creating object
obj = Regex()
#calling method 
obj.check()
