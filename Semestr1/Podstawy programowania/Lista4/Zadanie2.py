import math
import matplotlib.pyplot as plt
import numpy as np

def SumaCzesciowa(x):
    Suma=0 
    Lista = []
    for i in range (61):
        Suma += (x**i)/(math.factorial(i))
        #Suma -= math.exp(x)
        Lista.append(abs((Suma-math.exp(x)))/math.exp(x))
    return Lista

Indeks = np.arange(61)

plt.subplot(1,2,1)
plt.title("Blad bezwzglednhyh dla 2 i -2")
plt.plot(Indeks,SumaCzesciowa(2))
plt.plot(Indeks,SumaCzesciowa(-2))
plt.legend(['2','-2'])
plt.yscale('log')
plt.ylabel("Blad\n(skala logarytmiczna)")

plt.subplot(1,2,2)
plt.title("Blad bezwzglednhyh dla 10 i -10")
plt.plot(Indeks,SumaCzesciowa(10))
plt.plot(Indeks,SumaCzesciowa(-10))
plt.legend(['10','-10'])
plt.yscale('log')
plt.ylabel("Blad\n(skala logarytmiczna)")

plt.show()
