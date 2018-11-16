weapons = ["sword", "dagger"]
fightMode = False

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
                                        


        elif usr in ["s", "south", "e", "east","w", "west"]:
                print("nothing there")
        else:
                print("This is not a valid direction")
                                         

                # Further code for the fight ...
 
                
         


                 
