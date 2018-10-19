x = input("who are you?")
print ("Greetings", x)
y = input("Do you want to leave?")
if y == "yes" or y == "Yes":
    print("Well too bad %s, you can never leave" % x)
elif y == "no" or y == "No":
    print("Good, because you never will", x)
else:
    print("I need a yes or no answer", x)
