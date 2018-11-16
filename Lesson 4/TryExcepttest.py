
while True:
    try:
        x = int(input("Give me a number!"))
    except ValueError:
        print("This is not a number!")
