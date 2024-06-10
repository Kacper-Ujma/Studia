import random 
import math

class Rocket:
    def __init__(self):
        self.PositionX = 0
        self.PositionY = 0

    def move(self):
        Vector = random.uniform(-10,10)
        self.PositionX += Vector
        Vector = random.uniform(-10,10)
        self.PositionY += Vector

    def get_position(self):
        return self.PositionX, self.PositionY
    
    def get_distnace(self,x2,y2):
        return math.sqrt(((self.PositionX-x2)**2)+((self.PositionY-y2)**2))

r1 = Rocket()
r2 = Rocket()
r1.move()
r2.move()
print(r1.get_position(),r2.get_position())
print(r1.get_distnace(r2.PositionX,r2.PositionY),r2.get_distnace(r1.PositionX,r1.PositionY))