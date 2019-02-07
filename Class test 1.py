class Shark:

    kind = "mammal"

    def __init__ (self, start_x, start_y):

        self.x = start_x

        self.y = start_y

    def move(self):

        self.x += 1

        self.kind = "orc"


##Sharky
sharky = Shark(20, 30)

print (sharky.x)

sharky.move()

print (sharky.x)

print (sharky.kind)

print (Shark.kind)



