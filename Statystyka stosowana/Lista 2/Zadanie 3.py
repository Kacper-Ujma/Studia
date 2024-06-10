import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Wczytaj plik CSV
df = pd.read_csv("C:\\Users\\kacpu\\Downloads\\CreditCard.csv")
print(df)
# Wyświetl zawartość pliku CSV
ages = df['age'].values[:]

def harmonic(data):
    res = len(data) / np.sum(data**(-1))
    return res

def geometric(data):
    res = np.prod(np.power(data, 1/len(data)))
    return res

def cut(data, k):
    data = np.sort(data)
    data = data[k:-k]
    res = np.mean(data)
    return res

def winsor(data, k):
    data = np.sort(data)
    n = len(data)
    data[:k] = data[k]
    data[-k:] = data[-k-1]
    res = np.mean(data)
    return res

mean = np.mean(ages)
mean_harmonic = harmonic(ages)
mean_geometric = geometric(ages)
s = np.std(ages)

print('Średnia:', mean)
print('Średnia harmoniczna:', mean_harmonic)
print('Średnia geometryczna:', mean_geometric)
print(s)

mean_cut = []
mean_winsor = []
k_values = range(1, 100)

for k in k_values:
    mean_cut.append(cut(ages, k))
    mean_winsor.append(winsor(ages, k))

plt.plot(k_values, mean_winsor, label='Średnia winsorowana')
plt.plot(k_values, mean_cut, label='Średnia ucinana')
plt.xlabel('Wartość parametru k')
plt.ylabel('Średnia wartość')
plt.title('Porównanie średniej ucinanej i winsorowanej w zależności od parametru k')
plt.legend()
plt.show()

# Wykres pudełkowy
plt.boxplot(ages)
plt.xlabel('Wiek')
plt.ylabel('Wartość')
plt.title('Wykres pudełkowy wieku')
plt.show()
