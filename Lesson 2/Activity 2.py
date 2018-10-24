x = ['mix', 'xyz', 'apple', 'xanadu', 'rovio']
y = []
z = []
for i in x:
    if i[0] == "x":
        y.append(i)
    else:
        z.append(i)
    if i == x[-1]:
        y.extend(z)
    else:
        continue
    print(y)
