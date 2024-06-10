import numpy as np
import matplotlib.pyplot as plt

# Parametry rozkładu Pareto
x0 = 1  # Parametr przesunięcia
alpha = 3  # Parametr kształtu
n = 1000  # Liczba próbek
N = np.arange(100,5001,100)
# Generowanie próbki z rozkładu Pareto
sample = (np.random.pareto(alpha, n) + 1) * x0

# Estymacja parametrów
x0_est = np.min(sample)
alpha_est = n / np.sum(np.log(sample / x0_est))

# Funkcja dystrybuanty empirycznej (ECDF)
def ecdf(data):
    sorted_data = np.sort(data)
    y = np.arange(1, len(data)+1) / len(data)
    return sorted_data, y

# Teoretyczna funkcja dystrybuanty rozkładu Pareto
def pareto_cdf(x, x0, alpha):
    return 1 - (x0 / x) ** alpha

# Empiryczna dystrybuanta
x_empirical, y_empirical = ecdf(sample)

# Teoretyczna dystrybuanta
x_theoretical = np.linspace(np.min(sample), np.max(sample), 1000)
y_theoretical = pareto_cdf(x_theoretical, x0_est, alpha_est)


distances= []
for s in N:
    distance = []
    for i in range(1000):
        sample = (np.random.pareto(alpha,s)+1)*x0
        x0_est = np.min(sample)
        alpha_est = n / np.sum(np.log(sample / x0_est))
        distance.append(np.abs(alpha_est-alpha))
    distances.append(np.mean(distance))

# Rysowanie wykresu
plt.figure(figsize=(10, 6))
plt.subplot(121)
plt.step(x_empirical, y_empirical, label='Empiryczna dystrybuanta', color='blue')
plt.plot(x_theoretical, y_theoretical, label='Teoretyczna dystrybuanta (MLE)', color='red', linestyle='--')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.title('Empiryczna i teoretyczna dystrybuanta rozkładu Pareto')
plt.subplot(122)
plt.plot(N,distances)
plt.title("Distance from theoretical alpha")
plt.legend()
plt.grid(True)
plt.show()
