import numpy as np

# Generowanie próbki z rozkładu normalnego
mean = 2
variance = 2
sample_size = 200
sample = np.random.normal(mean, variance, sample_size)

# Obliczanie charakterystyk
median = np.median(sample)
quartiles = np.percentile(sample, [25, 50, 75])
interquartile_range = quartiles[2] - quartiles[0]
sample_range = np.max(sample) - np.min(sample)
variance_sample = np.var(sample, ddof=1)  # Używamy ddof=1, aby obliczyć estymator nieobciążony
standard_deviation_sample = np.std(sample, ddof=1)

# Wyświetlanie wyników
print("Mediana:", median)
print("Kwartyle:", quartiles)
print("Rozstęp międzykwartylowy:", interquartile_range)
print("Rozstęp z próby:", sample_range)
print("Wariancja z próby:", variance_sample)
print("Odchylenie standardowe:", standard_deviation_sample)
