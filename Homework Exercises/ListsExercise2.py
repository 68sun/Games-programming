numbers = input("Enter a list of numbers")
numbers = numbers.split(" ")
while True:
    if "" in numbers:
        numbers.remove("")
    else:
        break
for i in numbers:
    if int(i) % 2 == 0 or int(i) == 0:
        continue
    numbers.remove(i)
print(numbers)
