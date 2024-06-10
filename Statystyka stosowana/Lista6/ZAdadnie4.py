import numpy as np
from scipy.stats import norm, t

# Parametry
mi = 2.1
sigma = 0.2
alpha = 0.02
n_values = [20, 50, 100]
M = 1000

# Funkcja do obliczania przedziału ufności przy znanym sigma
def confidence_interval_known_sigma(sample_mean, n, sigma, alpha):
    z = norm.ppf(1 - alpha/2)
    margin_of_error = z * sigma / np.sqrt(n)
    return (sample_mean - margin_of_error, sample_mean + margin_of_error)

# Funkcja do obliczania przedziału ufności przy nieznanym sigma
def confidence_interval_unknown_sigma(sample_mean, sample_std, n, alpha):
    t_critical = t.ppf(1 - alpha/2, df=n-1)
    margin_of_error = t_critical * sample_std / np.sqrt(n)
    return (sample_mean - margin_of_error, sample_mean + margin_of_error)

# Symulacje
results_known_sigma = {n: 0 for n in n_values}
results_unknown_sigma = {n: 0 for n in n_values}

np.random.seed(42)  # Dla powtarzalności wyników

for n in n_values:
    for _ in range(M):
        # Generowanie próby
        sample = np.random.normal(mi, sigma, n)
        sample_mean = np.mean(sample)
        sample_std = np.std(sample, ddof=1)
        
        # Przedział ufności dla znanego sigma
        ci_known_sigma = confidence_interval_known_sigma(sample_mean, n, sigma, alpha)
        if ci_known_sigma[0] <= mi <= ci_known_sigma[1]:
            results_known_sigma[n] += 1
        
        # Przedział ufności dla nieznanego sigma
        ci_unknown_sigma = confidence_interval_unknown_sigma(sample_mean, sample_std, n, alpha)
        if ci_unknown_sigma[0] <= mi <= ci_unknown_sigma[1]:
            results_unknown_sigma[n] += 1

# Wyniki
print("Wyniki dla znanego sigma:")
for n in n_values:
    print(f"n = {n}: {results_known_sigma[n] / M * 100:.2f}%")

print("\nWyniki dla nieznanego sigma:")
for n in n_values:
    print(f"n = {n}: {results_unknown_sigma[n] / M * 100:.2f}%")
