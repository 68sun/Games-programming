weapons = ["sword", "dagger"]
inventory = {"dagger" : 0, "bluePotion" : 0, "goldenFeather" : 0, "manuscript" : 0}
abilities = {"fly" : 0, "stealth" : 0}
fightMode = False
forest = False

while True:

        usr=input("Where to? ")

        if usr in ["n", "north"]:
                print("Oh this looks like trouble!")


                 
                usr = input("Will you fight?").lower()
                if usr in ["yes", "y", "hell yeah"]:
                        fightMode = True
                else:
                        continue
        

                while fightMode:
                        if fightMode:
                                usr = input("which weapon you want to use: ") 

                                usrp = usr.split(" ") #list
          
                                for word in usrp:
                                        if word in weapons:
                                                if word == "sword":
                                                        print("With this you do 5 damage. On we go!")
                                                        fightMode = False
                                                elif word == "dagger":
                                                        print("With this you do 3 damage. On we go!")
                                                        fightMode = False
                                                 
                                else:
                                        print("please choose a weapon you actually have")
                                        


        elif usr in ["e", "east","w", "west"]:
                print("nothing there")




        elif usr in ["s", "south"]:
                print("You find yourself in a forest. Looking around, you see Daggers, Blue potions, Golden Feathers and Manuscripts")
                forest = True
                while forest:
                        action = input("What do you want to do?")
                        if action == "take":
                                take = input("What do you want to take?")
                                if take.lower() == "dagger":
                                        inventory["dagger"] += 1
                                        print(inventory) 
                                elif take.lower() == "manuscript":
                                        inventory["manuscript"] += 1
                                        print(inventory)
                                elif take.lower() == "back":
                                        continue

                                elif take.lower() == "bluepotion":
                                        inventory["bluePotion"] += 1
                                        print(inventory)
                                        if abilities["stealth"] < 5:
                                                abilities["stealth"] += 1
                                                print(abilities)
                                        else:
                                                print("Stealth ability at max")




                                elif take.lower() == "goldenfeather":
                                        inventory["goldenFeather"] += 1
                                        print(inventory)
                                        if abilities["fly"] < 5:
                                                abilities["fly"] += 1
                                                print(abilities)
                                        else:
                                                print("Flight ability at max")


                                else:
                                        print("enter a valid command")

                                        
                        elif action == "leave":
                                break
                        else:
                                print("Enter a valid command")
                                        
                                
                        
                        
                
        else:
                print("This is not a valid direction")
                                         

                # Further code for the fight ...
 
                
         


                 
