testList = [1,0,0,0,2,8,11]
newList = []

for i in testList:
    if i in newList:
        continue
    newList.append(i)
print(newList)
