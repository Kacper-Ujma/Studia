import numpy as np
import matplotlib.pyplot as plt

def simulate_shifted_exponential(theta, size):
    X = np.random.exponential(scale=1, size=size)
    Y = X + theta
    return Y

# Parametry symulacji
theta_true = 5  # Prawdziwa wartość theta
sample_sizes = np.arange(10, 1001, 50)  # Rozmiary próbek do analizy
num_simulations = 1000  # Liczba symulacji dla każdego rozmiaru próbki

# Przechowywanie wyników
mean_estimates = []
biases = []

for n in sample_sizes:
    theta_estimates = []
    for _ in range(num_simulations):
        sample = simulate_shifted_exponential(theta_true, n)
        theta_estimate = np.min(sample)
        theta_estimates.append(theta_estimate)
    
    mean_theta_estimate = np.mean(theta_estimates)
    bias = mean_theta_estimate - theta_true
    mean_estimates.append(mean_theta_estimate)
    biases.append(bias)

# Rysowanie wyników
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(sample_sizes, mean_estimates, label='Średnia estymacja theta', marker='o', linestyle='--')
plt.axhline(y=theta_true, color='red', linestyle='-', linewidth=2, label='Prawdziwa wartość theta')
plt.xlabel('Rozmiar próbki (n)')
plt.ylabel('Estymacja theta')
plt.title('Średnia estymacja theta w zależności od rozmiaru próbki')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(sample_sizes, biases, label='Bias estymatora theta', marker='o', linestyle='--')
plt.axhline(y=0, color='red', linestyle='-', linewidth=2, label='Brak biasu')
plt.xlabel('Rozmiar próbki (n)')
plt.ylabel('Bias estymatora')
plt.title('Bias estymatora theta w zależności od rozmiaru próbki')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
