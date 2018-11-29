x = input("Enter something")
check = "code"
number = 0

for i in range(len(x)-1):
    if x[i-2] + x[i-1] + x[i+1] == "coe":
        number += 1
print(number)
