inventory={"Potion" : 1, "Sword" : 1, "Mana potion" : 1}
values={"Health" : 80, "Mana" : 0}
while True:
    action = input("What do you want to do?")
    if action == "buy a potion":
        inventory["Potion"] = inventory["Potion"] + 1
        print("you bought a potion!")
        print(inventory)
    elif action == "drink a potion" and inventory["Potion"] >= 1:
        inventory["Potion"] = inventory["Potion"] - 1
        values["Health"] = values["Health"] + 10
        print("you drank a potion!")
        print(inventory)
        print(values)
