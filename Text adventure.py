#Variables
window=0
wait=0
name=input("Who are you?")
scene=0
while True:
    #First room
    if scene==0:
        scene=1+int(input("Hello %s. You awaken in a small room. The walls and roof around you are made of dark brown wooden planks. One wall has a large glass-paned window, beyond which you see a large cave. There is a small wooden door in the wall directly opposite the window. What do you want to do? 1: Open the door 2: go to the window 3: sit and wait" % name))
    if scene==1 and window==0:
        scene=1+int(input("The walls and roof around you are made of dark brown wooden planks. One wall has a large glass-paned window, beyond which you see a large cave. There is a small wooden door in the wall directly opposite the window. What do you want to do? 1: Open the door 2: go to the window 3: sit and wait"))
    elif scene==1 and window==1:
        scene=1+int(input("The walls and roof around you are made of dark brown wooden planks. One wall has a large smashed window, beyond which you see a large cave. There is a small wooden door in the wall directly opposite the window. What do you want to do? 1: Open the door 2: go to the window 3: sit and wait"))
    #Sit and wait
    if scene==4 and wait==3:
        scene=-1
    elif scene==4:
        wait=wait+1
        print("you sit and wait")
        scene=1
    if scene==-1:
        print("As you sit and wait for hours, eventually you see the door open. A man dressed in an all-white suit steps into the room and says 'Hello %s, he is ready to see you now'. As he says this, you feel yourself compelled forward through the door and are soon enveloped by a bright light. THE END" % name)
        break
    #Through the door
    if scene==2:
        scene=4+int(input("You open the door. Upon doing so, you see a long stone hallway lit by torches. What do you do? 1:Walk down the hallway 2:Close the door and go back"))
    if scene==5:
        print("as you walk through the door, everything goes black. suddenly you wake up again within the room you were in before")
        scene=1
    elif scene==6:
        scene=1
    #through the window
    if scene==3 and window==0:
        scene=6+int(input("you glance out the window into the cave, but cant make anything out. What do you do? 1: smash the window 2: return to the center of the room"))
    elif scene==3 and window==1:
        scene=6+int(input("you glance out the smashed window into the cave, but cant make anything out. What do you do? 1: go through the window 2: return to the center of the room"))
    if scene==7:
        print("You smash the window and jump through, avoiding the broken glass. You continue blindly into the dark cave for a few minutes, but suddenly you find yourself back in the room from before")
        scene=1
    elif scene==8:
        scene=1
    #error fixing
    if scene>8 or scene<-1:
        print("NOT A VALID VALUE. RESETTING GAME>>>")
        scene=0
    
