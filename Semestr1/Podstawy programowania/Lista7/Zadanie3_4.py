import random 
import math
import matplotlib.pyplot as plt
import numpy as np

Rakiety = []
n = 5
Kolorki = {0:'r',1:'g',2:'b',3:'orange',4:'purple'}


class Rocket:
    
    def __init__(self,x,y):
        '''
        Funkcja__init__ inicjuje położenie rakiety, oraz ustawia lowsowo wybrane vectory z przedzialu (-10,10) oraz paliwo na poczatkowa wartos 100
        Input:
        x - wposlrzedna x rakiety (float)
        y - wpolrzedna y rakiety (float)
        '''
        self.PositionX = x
        self.PositionY = y
        self.Paliwo = 100

    def move(self):
        '''
        Funckja przesuwa rakiete o dwa wektory wzgledem osi x i y dodajac do pozycji losowe vektory
        '''
        self.VectorX = random.uniform(-10,10)
        self.VectorY = random.uniform(-10,10)
        self.PositionX += self.VectorX
        self.PositionY += self.VectorY

    def get_position(self):
        '''
        Funkcja zwraca pozycje rakiety
        Output:
        self.PosistionX(float)
        self.PositionY(float)
        '''
        return self.PositionX, self.PositionY
    
    def get_distnace(self,x2,y2):
        '''
        Funkcja sprawdza odleglosc miedzy soba a podana rakieta
        Input:
        x2 = Pozycja x drugiej rakiety(float)
        y2 = Pozycja y drugiej rakiety(float)
        Output:
        Odleglosc miedzy dwoma rakietami (float)
        '''
        return math.sqrt(((self.PositionX-x2)**2)+((self.PositionY-y2)**2))

    def fuel(self):
        '''
        Funkcja oblicza ilosc paliwa w rakiecie odejmujac od 
        poczatkowej wartosci paliwa paliwo zurzyte na podroz przez dwa vectory korzystajac ze wzoru na odleglosc 
        Output:
        Ilosc oakiwa pozostala w rakiecie 
        self.Paliwo(float)
        '''
        self.Paliwo = self.Paliwo - math.sqrt(((abs(self.VectorX)**2)+(abs(self.VectorY)**2)))*4
        return self.Paliwo

    def get_fuel(self):
        '''
        Funckcja sprawdza ilosc paliwa
        Output:
        jesli ilosc paliwa jest wieksza od 0 zwraca self.Paliwo(float)
        jesli ilosc paliwa jest mniejsza badz rowna zwraca 0
        '''
        if self.Paliwo>0:
            return self.Paliwo
        else: 
            self.Paliwo = 0 
            return self.Paliwo
            
    def wykres(self,colour):
        '''
        Funkcja dodaje do wykresu rakiete o aktualnym polozeniu
        Input:
        colour(string) - kolor rakiety
        Output:
        Rakieta w postaci kola dodana do wykresu plt.cicrle
        '''
        Kolo = plt.Circle((self.PositionX,self.PositionY),facecolor=colour,radius=10)
        ax.add_patch(Kolo)

for a in range(n):
    x = random.uniform(-60,60)
    y = random.uniform(-60,60)
    r = Rocket(x,y)
    Rakiety.append(r)
    print("Poczatkowa pozycja rakiety",a+1,Rakiety[a].get_position())

for j in range(5):
    print("------------------------- Tura",j+1,"-------------------------")
    for i in range (n):
        if Rakiety[i].get_fuel()>0:
            Rakiety[i].move()
            Rakiety[i].fuel()
            print("Nowa pozycja Rakiety",i+1,":",Rakiety[i].get_position(),"a jej stan paliwa to:",Rakiety[i].get_fuel())
        else:
            print("W rakiecie",i+1,"braklo paliwa zostala na pozycji",Rakiety[i].get_position())
    for i in range (n):
        k=0
        while k<5:
            if k>i:
                while Rakiety[i].get_distnace(Rakiety[k].PositionX,Rakiety[k].PositionY)<20:
                    print("rakiety",i+1,k+1,"w kolizji!!! inicjalizuje przesuniecie")
                    Rakiety[i].move()
                    Rakiety[i].fuel()
                print(" Odleglosc miedzy rakietami",i+1,"i",k+1,"wynosi",Rakiety[i].get_distnace(Rakiety[k].PositionX,Rakiety[k].PositionY))
            k = k+1
    print("---------------Przestawienie nr",j+1,"zakonczone--------------")



fig, ax = plt.subplots() 
ax.set_xticks(np.arange(-100,109,10))
ax.set_yticks(np.arange(-100,109,10))
for c in range(n):
    Rakiety[c].wykres(Kolorki[c])

plt.show()