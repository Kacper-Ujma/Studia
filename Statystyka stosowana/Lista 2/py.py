import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parametry rozkładu normalnego
mu = 0  # Średnia
sigma = 1  # Odchylenie standardowe
n = 100  # Liczba obserwacji w próbie
num_samples = 1000  # Liczba prób w Monte Carlo

def ECDF(data):
    dane = np.array(data)
    dane.sort()
    jumps = np.arange(1, len(dane)+1) / len(dane)
    return dane, jumps

# Generowanie prób i obliczanie statystyki U = max(X1, ..., Xn)
u_empirical = []
for i in range(num_samples):
    sample = np.random.normal(mu, sigma, n)
    u_empirical.append(np.max(sample))

# Obliczanie empirycznej dystrybuanty dla U
x_empirical, y_empirical = ECDF(u_empirical)

# Obliczanie teoretycznej dystrybuanty dla U
x_theoretical = np.linspace(mu - 3*sigma, mu + 4*sigma, 1000)
y_theoretical = [norm.cdf((u - mu) / sigma) ** n for u in x_theoretical]

# Rysowanie wykresu
plt.plot(x_empirical, y_empirical, label='Empiryczna dystrybuanta', linestyle='--')
plt.plot(x_theoretical, y_theoretical, label='Teoretyczna dystrybuanta', linestyle='-')
plt.xlabel('Wartość maksymalna U')
plt.ylabel('Dystrybuanta')
plt.title('Dystrybuanta statystyki U dla próby z rozkładu normalnego')
plt.legend()
plt.grid(True)
plt.show()
