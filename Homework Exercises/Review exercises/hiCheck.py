x = input("Enter")
number = 0

for i in range(len(x)-1):
    if x[i] + x[i+1] == "hi":
        number += 1
print("Hi appears %x times" % number)
