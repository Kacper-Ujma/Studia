import numpy as np
import random
import matplotlib.pyplot as plt
import math

fig, ax = plt.subplots() 

IloscKol = 10
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

def Kolizja (Dysk,Promien,n):
    for i in range(n):
        j=0
        while i-j>1:
            j +=1
            d = math.sqrt(((Dysk[i][0]-Dysk[j][0])**2)+((Dysk[i][1]-Dysk[j][1])**2))
            if d<Promien*2:
                return d<Promien*2
            else: continue
            
print(Kolizja(Dyski,r,IloscKol))    
    


plt.xlim(-15,15)
plt.ylim(-15,15)
plt.grid()
plt.show()
