# creates list triData, containing a list for every row of pyramid
with open("p067_triangle.txt", "r") as triFile:
    print("Importing data...")
    triData = []
    for line in triFile:
        triData.append(line.split())
    print("Finished")
    print("Data imported to location: triData\n")

print("Converting triData's values to intergers...")
for row in range(len(triData)):
    for col in range(len(triData[row])):
        # print("row:",row,"col:",col)
        triData[row][col] = int(triData[row][col])
print("Finished\n")

print("Algorithm Starting...")
print(len(triData), "rows to compute")
for rowi in range(len(triData))[::-1][1:]:
    # print("rowi",rowi)
    if rowi % 10 == 0: print(str(100 - rowi) + "% complete")
    for coli in range(len(triData[rowi])):
        triData[rowi][coli] += max(triData[rowi + 1][coli:coli + 2])
        #print("row:",rowi,"col:",coli,"values below",triData[rowi+1][coli:coli+2],"max:", max(triData[rowi+1][coli:coli+2]),"new value:", triData[rowi][coli])

print("Finished\n")

print("Optimum route gives total:", triData[0][0])
    
