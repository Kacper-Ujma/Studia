import time

Lancuch = str(input("Podaj slowo ktore bedziemy sprawdzac\n"))
Litera = str(input("Wpisz litere ktorej ilosc bedziemy sprawdzac\n"))
IloscZnakow = 0
i = 0

CzasPetliST = time.time()
time.sleep(0.001)
while i < len(Lancuch):
    if Lancuch[i] == Litera:
        IloscZnakow = IloscZnakow+1
    i = i+1 
CzasPetliEND = time.time()

CzasCountST = time.time()
time.sleep(0.001)
Liczenie = Lancuch.count(Litera)
CzasCountEND = time.time()

print("roznica czasow wynosi",((CzasPetliEND-CzasPetliST)-(CzasCountEND-CzasCountST))*1000,"milisekund")