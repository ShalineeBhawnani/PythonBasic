#******************************************************************************************************************
# @purpose :Demonstrate Anagram Logic.
# @file  :Anagram.py
# @author :ShalineeBhawnani
#*******************************************************************************************************************
s1 = input("Enter First String:")
s2 = input("Enter Second String:")
def anagram(s1,s2):
    count = 0
    if(len(s1)!=len(s2)):
        print("Strings are not anagram")
    else:
        s1=s1.lower()
        s2=s2.lower()
        for i in s1:
            for j in s2:
                if i==j:
                    count=count+1
        if count==len(s1):
            print("Anagram")
        else:
            print("Not Anagram")

anagram(s1,s2)
