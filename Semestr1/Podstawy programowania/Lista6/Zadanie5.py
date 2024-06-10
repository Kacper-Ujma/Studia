import numpy as np
import random
import matplotlib.pyplot as plt
import math

fig, (ax1,ax2) = plt.subplots(1,2) 

IloscKol =100
PolozenieKol = []
r=0.5

for i in range(IloscKol):
    x = float(random.uniform(-14.5,14.5))
    y = float(random.uniform(-14.5,14.5))
    PolozenieKol.append([x,y])
    Kolo = plt.Circle((x,y), radius = r,edgecolor='b',linewidth=1,facecolor='r')
    ax1.add_patch(Kolo)

print(len(PolozenieKol))

ax1=plt.subplot(1,2,1)
ax1.set_xticks(np.arange(-15,16,3))
ax1.set_yticks(np.arange(-15,16,3))
ax1.grid()
ax1.set_title('Przed przesunieciem')

ax2=plt.subplot(1,2,2)
ax2.set_xticks(np.arange(-15,16,3))
ax2.set_yticks(np.arange(-15,16,3))
ax2.set_title('Po przesunieciu')
ax2.grid()

def Przsuniecie(PozycjaKola,Promien,Kolo1,Kolo2):
    '''
    Progam przsuwa koło o losowy wektor oraz sprawdza czy dalej istnieje kolizja miedzy kolami ktore sprawdzil
    jesli isntnieje to wywołuje sie iteracyjnie do momentu kiedy nie kola nie stykaja sie 
    '''  
    V=[random.uniform(((-2)*Promien),(2*Promien)),random.uniform(((-2)*Promien),(2*Promien))]
    PozycjaKola[Kolo1][0]=PozycjaKola[Kolo1][0]+V[0]
    PozycjaKola[Kolo1][1]=PozycjaKola[Kolo1][1]+V[1]
    while Kolizja(PozycjaKola,Promien,Kolo2,Kolo1)==True:
        Przsuniecie(PozycjaKola,Promien,Kolo1,Kolo2)
    if PozycjaKola[Kolo1][0]>14.5 or PozycjaKola[Kolo1][0]<-14.5 or PozycjaKola[Kolo1][1]>14.5 or PozycjaKola[Kolo1][1]<-14.5:
        Przsuniecie(PozycjaKola,Promien,Kolo1,Kolo2)

def Kolizja (Kola,Promien,Kolo1,Kolo2):
    '''
    funkcja wykorzystujac wzor matematyczney bolicza odleglosc miedzy dwoma punktami na plaszczyznie
    jelsi wynosi ona mniej niz dwa promienie kola wykrywa kolizje
    '''
    d = math.sqrt(((Kola[Kolo1][0]-Kola[Kolo2][0])**2)+((Kola[Kolo1][1]-Kola[Kolo2][1])**2))
    return d<Promien*2 
    
def Poprawka(PozycjeKol,Promien,n):             
    for a in range(n):
        for b in range(n):
            if a!=b: 
                #print("sprawdzam",a,b,Kolizja(PozycjeKol,Promien,a,b))
                if Kolizja(PozycjeKol,Promien,a,b)==True:
                    #print('przesuwam',b,'pozycja przed',PolozenieKol[b])
                    Przsuniecie(PozycjeKol,Promien,b,a)
                    #print('przesuwam',b,'pozycja po',PolozenieKol[b])
                else:
                    Kolo = plt.Circle((PozycjeKol[a][0],PozycjeKol[a][1]), radius = Promien,edgecolor='b',linewidth=1,facecolor='r')
                    #print("dodaje kolo",a,PolozenieKol[a])
                    ax2.add_patch(Kolo)
                ax2.add_patch(Kolo)

print(len(PolozenieKol),PolozenieKol)        
Poprawka(PolozenieKol,r,IloscKol)
plt.show()