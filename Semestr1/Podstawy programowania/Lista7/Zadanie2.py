import random 
import math

class Rocket:
    def __init__(self):
        self.PositionX = 0
        self.PositionY = 0

    def move(self):
        self.VectorX = random.uniform(-10,10)
        self.VectorY = random.uniform(-10,10)    
        self.PositionX += self.VectorX
        self.PositionY += self.VectorY

    def get_position(self):
        return self.PositionX, self.PositionY
    
    def get_distnace(self,x2,y2):
        return math.sqrt(((self.PositionX-x2)**2)+((self.PositionY-y2)**2))

r = Rocket()

for i in range (10):
    print("---------- Tura",i+1,"---------")
    print("Aktualna pozycja :",r.get_position())
    r.move()
    print("Przesuniecie o wektor:",r.VectorX,r.VectorY)
    print("Nowa pozycja :")
    print(r.get_position())