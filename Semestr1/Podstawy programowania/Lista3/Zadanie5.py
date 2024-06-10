import math

Liczby = []
while True:
    inp = int(input("Wpisz liczbe calkowita wieksza od zera i nacisnij enter\n"))
    if inp == 0:
        break
    Liczby.append(inp)

Liczby.append(Liczby[-1])

for i in range(len(Liczby)-1):
    NWD = math.gcd(Liczby[i],Liczby[i+1])
    Liczby[i+1] = NWD

print("Najwiekszy wspolny dzielnik to ",NWD)

   
    