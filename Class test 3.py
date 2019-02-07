import random

potionColours = ["Red", "Green", "Blue"]

inventory = []

coinPoints = 0

potionPoints = 0

totalPoints = 0

level = 1

class Coins:
    
    def __init__ (self, count):
        self.count = count


class Potions:

    points = 0

    def __init__ (self, count, colour):
        self.count = count
        self.colour = colour



while True:

    choice = int(input("Enter a number between 1 and 6"))

    if choice <= 3:
        coinPouch = Coins (random.randint(1,20))

        inventory.append ("Coin pouch(%d)" % coinPouch.count)

        coinPoints += coinPouch.count
        totalPoints += coinPouch.count

        print ("Coins: %d" % coinPoints)
        print("Total Points: %d" % totalPoints)
        print (inventory)

    elif choice >3 and choice <= 6:
        newPotion = Potions(random.randint (1,3), random.choice(potionColours))
        
        inventory.append (newPotion.colour + " potion")

        if newPotion.colour == "Green":
            newPotion.points = -100

            if totalPoints < 0:
                totalPoints = 0

        else:
            newPotion.points = 100
            potionPoints += newPotion.points
            

        
        totalPoints += newPotion.points
        
        print ("Potions value: %d" % potionPoints)
        print ("Total Points: %d" % totalPoints)
        print (inventory)


    if potionPoints >= 300:
        potionPoints = 0

        level += 1

        print ("You leveled up!")
        print ("Level: %d" % level)
        print ("Potions value: %d" % potionPoints)

    elif coinPoints >= 300:
        coinPoints = 0

        level += 1

        print ("You leveled up!")
        print ("Level: %d" % level)
        print ("Coins: %d" % coinPoints)



    

    if totalPoints >= 600:
        print ("END")
        break

    

        
        
        
        







