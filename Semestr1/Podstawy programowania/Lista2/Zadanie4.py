
Lancuch = str(input("Podaj slowo ktore bedziemy sprawdzac\n"))
Litera = str(input("Wpisz litere ktorej ilosc bedziemy sprawdzac\n"))
IloscZnakow = 0
i = 0

while i < len(Lancuch):
    if Lancuch[i] == Litera:
        IloscZnakow = IloscZnakow+1
    i = i+1 

print("ilosc znakow '",Litera,"' wystepujacych w slowie",Lancuch,"=",IloscZnakow)
