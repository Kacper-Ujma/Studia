import numpy as np
import matplotlib.pyplot as plt

# Parametry rozkładu normalnego
mu = 0  # Średnia
sigma = 1  # Odchylenie standardowe
m = 1000 # Liczba obserwacji w próbie

def ECDF(data):
    dane = np.array(data)
    dane.sort()
    jumps = np.linspace(0,1,len(dane))
    return dane,jumps

# Generowanie próby z rozkładu normalnego
u = []
for i in range(m):
    sample = np.random.normal(mu, sigma, 1000)
    u.append(np.max(sample))

# Wyznaczanie dystrybuanty empirycznej dla próby
x, y = ECDF(data=u)

# Wyznaczanie teoretycznej dystrybuanty dla rozkładu normalnego
theoretical_x = np.linspace(mu, mu + 5 * sigma, 1000)
theoretical_y = np.array([np.mean(u <= val) for val in theoretical_x])

# Rysowanie wykresu
plt.plot(x, y, label='Empiryczna')
plt.plot(theoretical_x, theoretical_y, label='Teoretyczna')
plt.xlabel('Wartość maksymalna')
plt.ylabel('Dystrybuanta empiryczna')
plt.title('Empiryczna dystrybuanta dla próby z rozkładu normalnego')
plt.legend()
plt.grid(True)
plt.show()
