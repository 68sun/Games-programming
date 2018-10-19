inventory=["sword", "shield", "leather armour"]
while True:
    action=input("what do you want to do?")
    if action.lower()=="inventory":
        print(inventory)
    elif action.lower()=="buy a potion":
        inventory.insert(len(inventory),"Potion")
    action="nothing"
