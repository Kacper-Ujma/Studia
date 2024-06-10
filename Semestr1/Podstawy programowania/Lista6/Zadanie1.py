import numpy as np
import random
import matplotlib.pyplot as plt
import math

fig, ax = plt.subplots() 

IloscKol = 100
positionx = []
positiony = []
Dyski = []
r=0.5
for i in range(IloscKol):
    x = random.uniform(-14.5,14.5)
    y = random.uniform(-14.5,14.5)
    positionx.append(x)
    positiony.append(y)
    Dyski.append([x,y])
    Kolo = plt.Circle((x,y), radius = r,edgecolor='b',linewidth=1,facecolor='r')
    ax.add_patch(Kolo)
  
plt.xlim(-15,15)
plt.ylim(-15,15)
plt.grid()
plt.show()
