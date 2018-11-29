testList = [1,2,2,1,13]
afterThirteen = False
listSum = 0

for i in testList:
    if afterThirteen == True:
        afterThirteen = False
        continue
    if i == 13:
        afterThirteen = True
        continue
    listSum += i
print(listSum)
    
