import numpy as np
import matplotlib.pyplot as plt

mean = 0  # Średnia log-normalnego rozkładu (parametr logarytmiczny)
sigma = 1  # Odchylenie standardowe log-normalnego rozkładu (parametr logarytmiczny)

M = 5000  # Liczba prób do symulacji

# Liczba próbek w każdej próbie
spaces = np.arange(5000, 10001, 500)

s1_means = []
s2_means = []

# Teoretyczna wariancja rozkładu lognormalnego
var_theoretical = (np.exp(sigma**2) - 1) * np.exp(2 * mean + sigma**2)

for n in spaces:
    s1_diffs = []
    s2_diffs = []
    for i in range(M):
        # Generowanie próbki z rozkładu lognormalnego
        data = np.random.lognormal(mean, sigma, n)
        data_2 = np.random.lognormal(mean, sigma, n)
        sample_mean = np.mean(data)
        
        # Obliczanie estymatorów wariancji
        s1 = np.sum((data - sample_mean) ** 2) / n
        s2 = np.sum((data_2 - sample_mean) ** 2) / (n - 1)
        
        # Obliczanie różnic bezwzględnych w odniesieniu do teoretycznej wariancji
        s1_diffs.append(np.abs(var_theoretical - s1))
        s2_diffs.append(np.abs(var_theoretical - s2))

    # Średnie różnice dla estymatorów
    s1_means.append(np.mean(s1_diffs))
    s2_means.append(np.mean(s2_diffs))

# pzida = np.abs(s1_means-s2_means)
print(s1_means,s2_means)
# Wykres porównania estymatorów
plt.plot(spaces, s1_means, label='S1 (biased)', color='blue')
plt.plot(spaces, s2_means, label='S2 (unbiased)', color='red')
# plt.plot(spaces, pzida)
plt.xlabel('Liczba próbek (n)')
plt.ylabel('Średnia różnica od teoretycznej wariancji')
plt.title('Porównanie estymatorów wariancji dla rozkładu lognormalnego')
plt.legend()
plt.grid(True)
plt.show()
