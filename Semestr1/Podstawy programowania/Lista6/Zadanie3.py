import numpy as np
import random
import matplotlib.pyplot as plt
import math

fig, (ax1,ax2) = plt.subplots(1,2) 

IloscKol = 100
positionx = []
positiony = []
Dyski = []
Vector = [1,1]
r=0.5
for i in range(IloscKol):
    x = random.uniform(-14.5,14.5)
    y = random.uniform(-14.5,14.5)
    positionx.append(x)
    positiony.append(y)
    Dyski.append([x,y])
    Kolo = plt.Circle((x,y), radius = r,edgecolor='b',linewidth=1,facecolor='r')
    ax1.add_patch(Kolo)
print(Dyski)
ax1=plt.subplot(1,2,1)
ax1.set_xticks(np.arange(-15,16,3), np.arange(-15,16,3))
ax1.set_yticks(np.arange(-15,16,3), np.arange(-15,16,3))
ax1.grid()
ax1.set_title('Przed przesunieciem')
ax2=plt.subplot(1,2,2,sharey=ax1,sharex=ax1)
ax2.set_title('Po przesunieciu')
ax2.grid()

def Przsuniecie(Position,V):
    Position[0][0]=Position[0][0]+V[0]
    Position[0][1]=Position[0][1]+V[1]
    Kolo = plt.Circle((Position[0][0],Position[0][1]), radius = r,edgecolor='b',linewidth=1,facecolor='r')
    ax2.add_patch(Kolo)
    plt.show()


Przsuniecie(Dyski,Vector)
