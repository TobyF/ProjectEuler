# What is the total of all the name scores in the file?
with open("p022_names.txt", "r") as names:
    nameList = []
    for name in names.read().split(","):
        nameList.append(eval(name))

nameList.sort()
print("Names :", len(nameList))
total = 0
for i in range(len(nameList)):
    if i % 500 == 0: print("progress", i // 50, "%")
    letterSum = 0
    for letter in nameList[i]:
        #print("Name: ",nameList[i], "Letter: ",letter,"Score :",ord(letter)-6)
        letterSum += ord(letter) - 64
    #print("Total += ",i+1,"*",letterSum)
    total += (i + 1) * letterSum
print(total)
