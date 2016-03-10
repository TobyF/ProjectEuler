x = 0
total = 0
file = open("p013_num.txt", "r")
for line in file:
    total += int(line)
file.close()
print(str(total)[:10])
