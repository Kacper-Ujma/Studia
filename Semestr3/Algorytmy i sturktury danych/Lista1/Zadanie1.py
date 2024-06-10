

# Zad. 1. Algorytm klasy O(n^2)
def Liczenie_Wielomianu(a,point):
    value = 0
    potega = 1
    for i,factor in enumerate(a):
        for j in range(i):
         potega *= point
        value += potega*factor
        potega = 1
    return value

# Zad. 1. Algorytm klasy O(nlogn)
def Liczenie_Potegi(base,exp):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
            base *= base
            exp = exp//2
        elif exp % 2 == 0:
            base *= base
            exp = exp//2
    return result

def Liczenie_wielomianu2(a,point):
    value = 0
    for i,a in enumerate(a):
        value += a*Liczenie_Potegi(point,i)
    return value

# Zad. 1. Schemat Hornera
def Liczenie_Wielomianu3(a:list,point):
    result = a.pop()
    a.reverse()
    a_rev = a
    for i in a_rev:
        result = result*point + i
    return result
    # Najwiecej czasu zajmuje mnożenie elementów, wykonywane jest n-1 razy, gdzie n to dlugosc listy



if __name__ == "__main__":
    import time
    import numpy as np
    import random

    p = [random.random()*1000 for i in range(30)]
    x = 2

    dane = (1,10,100,1000,5000,10000,100000,1000000)
    czasy = []

    print(Liczenie_Wielomianu(p,x),'   ',Liczenie_wielomianu2(p,x),'   ',Liczenie_Wielomianu3(p,x))
