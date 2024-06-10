import numpy as np
import matplotlib.pyplot as plt

def empirical_density(data, bins=30):
    # Obliczanie histogramu
    hist, bin_edges, _ = plt.hist(data, bins=bins, density=True)
    
    # Obliczanie szerokości przedziałów
    bin_widths = bin_edges[1:] - bin_edges[:-1]
    
    # Normalizacja histogramu
    density = hist / np.sum(hist * bin_widths)
    
    return bin_edges[:-1], density

# Parametry rozkładu normalnego
mean = 0
variance = 1
N = 100000  # Liczba próbek

# Generowanie danych z rozkładu normalnego
data_normal = np.random.normal(mean, variance, N)

# Obliczanie empirycznej funkcji gęstości
bins, density = empirical_density(data_normal)

# Rysowanie wykresu empirycznej funkcji gęstości
plt.plot(bins, density, color='blue', label='Empiryczna gęstość')
plt.hist(data_normal,density=1,bins=50)

# Dodanie tytułu i etykiet osi
plt.title('Empiryczna gęstość danych z rozkładu normalnego')
plt.xlabel('Wartość')
plt.ylabel('Gęstość')

# Wyświetlenie wykresu
plt.legend()
plt.show()
