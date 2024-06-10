import numpy as np
import matplotlib.pyplot as plt

M = 1000
theta = 5
dane_jednorodne = np.random.uniform(0, 1, M)
dane_wykladnicz = np.random.exponential(1, M)

def zamiana(dane):
    return -np.log(dane)

def funkcja(dane, theta):
    dane.sort()
    res = []
    for i in range(len(dane)):
        res.append(np.exp(-(dane[i] - theta)))
    return res

dane = zamiana(dane_jednorodne)
dane_funckja = funkcja(dane_wykladnicz, theta)

# Normalizing histogram
# plt.hist(dane,15,density=True)

# Normalizing density function
dane_funckja = np.array(dane_funckja)
dane_funckja = dane_funckja / np.max(dane_funckja)

# plt.plot(dane_wykladnicz, dane_funckja, 'r')
# plt.show()
n = np.arange(1,10000,100)

estimators = []
for i in n:
    cos = []
    for j in range(500):
        dane_najwazniejsze = np.random.exponential(1,i)-5
        cos.append(np.min(dane_najwazniejsze))
    estimators.append(np.mean(cos))

plt.plot(n,estimators)
plt.show()