import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats

def ecdf(data:list):
    dane = data
    dane = np.sort(dane)
    n = len(dane)
    probabilities = np.zeros(n)
    for i in range(n):
        probabilities[i] = (i+1)/n
    return(probabilities)

# Parametry rozkładu normalnego
mu = 0
sigma = 1
n = 7  # liczba próbek

# Liczba symulacji
num_simulations = 1000

# Symulacja próbek
samples = np.random.normal(mu, sigma, size=(num_simulations, n))

# Obliczenie estymatorów
theta1 = np.mean(samples, axis=1)
theta2 = (2*samples[:,0] - samples[:,5] + samples[:,3]) / 2

# Teoretyczne wartości estymatorów
theta1_mean = mu
theta1_var = sigma**2 / n

theta2_mean = mu
theta2_var = 3*sigma**2 / 2

# Dystrybuanty empiryczne
x_values_1 = np.sort(theta1)
y_values_theta1_empirical = ecdf(x_values_1)
z = y_values_theta1_empirical
y_values_theta1_empirical = stats.ecdf(x_values_1)
y_values_theta1_empirical=y_values_theta1_empirical.cdf.probabilities
# y_values_theta1_empirical = np.arange(1, num_simulations + 1) / num_simulations

x_values_2 = np.sort(theta2)
y_values_theta2_empirical = stats.ecdf(x_values_2)
y_values_theta2_empirical=y_values_theta2_empirical.cdf.probabilities

# Porównanie dystrybuant
plt.figure(figsize=(10, 6))
plt.plot(x_values_1, y_values_theta1_empirical, label='Empiryczna Θ1', linestyle='-', color='b')
plt.plot(x_values_2, y_values_theta2_empirical, label='Empiryczna Θ2', linestyle='-', color='r')
plt.title('Porównanie dystrybuant empirycznych i teoretycznych')
plt.legend()
plt.grid(True)
plt.show()

