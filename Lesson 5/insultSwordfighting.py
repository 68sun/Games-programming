##imports
import random



##lists and variables
pirateHealth = 3
playerHealth = 3
insults = ["You fight like a dairy farmer!", "This is the END for you, you gutter crawling cur!"]
comebacks = ["How appropriate! You fight like a cow!", "And I've got a little TIP for you, get the POINT?"]
playerInsults = [1]



##functions

def pirate():
    print("You begin fighting a pirate")

    global pirateInsult
    pirateInsult = insults.index(random.choice(insults))
    print("The pirate shouts: " + insults[pirateInsult])

def player():
    for i in playerInsults:
        print("%x: " % i + comebacks[i-1])

    playerChoice = int(input("Which insult will you use?"))

    print("You shout: " + comebacks[playerChoice-1])
    
    if playerChoice - 1 == pirateInsult:
        pirateHealth -= 1
        print("The pirate is visibly shaken and you get a strike in! Hits left: %x" % pirateHealth)
    else:
        playerHealth -= 1
        print("The pirate is unaffected and you get hit! Hits until you lose: %x" % playerHealth)
    




while True:

    pirate()

    player()





    
    
