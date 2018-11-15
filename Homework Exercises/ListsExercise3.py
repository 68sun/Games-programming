myList = ["axe", "dagger", "oranges"]
for i in range(len(myList)):
    if myList[i] != "*":
        myList.insert(i, "*")
print(myList)
