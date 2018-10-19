x=input("Give me a word")
if x[-3:]=="ing":
    print("%sly" % (x))

elif len(x)>=3:
    print("%sing" % (x))
else:
    print(x)
