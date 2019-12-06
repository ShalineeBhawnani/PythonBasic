list1 = []
with open('MyFirstFile.txt','r') as f:
    for line in f:
        for word in line.split():
            list1.append(word)
    print(list1)
    word1 = input("search the word is present or not: ")
    if word1 in list1:
        list1.remove(word1)
    else:
        list1.append(word1)
    print(list1)
