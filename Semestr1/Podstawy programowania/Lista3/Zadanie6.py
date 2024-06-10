import math
LiczbaRzedow = int(input("wpisz liczbe rzedow do pokazania\n"))
n=0

def ZnakNewtona(N):
    k=0
    Tablica = []
    while k <= N:
        ZnakNewtona1 = int((math.factorial(N))/(math.factorial(N-k)*math.factorial(k)))
        Tablica.append(ZnakNewtona1)
        k=k+1
    Rzad = ""
    for i in Tablica:
        Rzad += str(i)
        Rzad += " "
    return Rzad


while n < LiczbaRzedow:
    k=LiczbaRzedow-n
    print(" "*(k),ZnakNewtona(n))
    n=n+1



