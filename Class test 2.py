import random

names = ["Tatsumi", "Nick", "Yuri", "Dave", "Chuck", "Johan", "James", "Kirk"]

clans = ["Red Dragons", "Fuscia Playtypi", "Emerald Pythons"]

abilities = ["Dragons Breath", "Playtypus Drill", "Python Dash"]

class Enemies:

    weapons = ["shuriken", "katana", "onions"]

    def __init__ (self, name, clan, ability):
        self.name = name
        self.clan = clan
        self.ability = ability


    def desc(self):
        self.descript = "%s is a member of the %s, and can use the ability %s" % (self.name, self.clan, self.ability)

    def weapon(self):
        self.weapon = random.choice(self.weapons)




for i in range(5):
    enemy = Enemies (random.choice(names), random.choice(clans), random.choice(abilities))
    enemy.desc()
    enemy.weapon()
    print ("Name: " + enemy.name)
    print ("Clan: " + enemy.clan)
    print ("Special ability: " + enemy.ability)
    print ("Weapon of choice: " + enemy.weapon)
    
    print (enemy.descript)
    
        
##
##
##enemy1 = Enemies ("Tasumi", "Red Dragons", "Dragons breath")
##enemy1.desc()
##enemy1.weapon()
##print ("Name: " + enemy1.name)
##print("Clan: " + enemy1.clan)
##print ("Special ability: " + enemy1.ability)
##print ("Weapon of choice: " + enemy1.weapon[0])
##print (enemy1.descript)
##
##enemy2 = Enemies ("Dave", "Fuscia Platypi", "Platypus Drill")
##enemy2.desc()
##enemy2.weapon()
##print ("Name: " + enemy2.name)
##print("Clan: " + enemy2.clan)
##print ("Special ability: " + enemy2.ability)
##print ("Weapon of choice: " + enemy2.weapon[0])
##print (enemy2.descript)
##













    
