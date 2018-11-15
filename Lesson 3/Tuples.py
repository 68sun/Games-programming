tupleList = [ (), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d') ]
for i in tupleList:
    if i==():
        tupleList.remove(i  )
        continue
print(tupleList)
