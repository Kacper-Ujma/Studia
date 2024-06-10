
Lancuch = str(input("Podaj slowo ktore bedziemy sprawdzac\n"))
Litera = str(input("Wpisz litere ktorej pozycje bedziemy sprawdzac\n"))
index = int(input("od ktorej pozycji bedziemy przeszukiwac slowo\n"))-1
IloscZnakow = 0

while index < len(Lancuch):
    if Lancuch[index] == Litera:
        print("Pozycja",Lancuch[index],"w słowie",Lancuch,index+1)
    index = index+1
    