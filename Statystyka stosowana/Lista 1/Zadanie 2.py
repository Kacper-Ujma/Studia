import numpy as np
import matplotlib.pyplot as plt

# Parametry rozkładu Pareto
x_m = 1  # Wartość minimalna
alpha = 2  # Wykładnik cięcia

# Odwrotna dystrybuanta dla rozkładu Pareto
def pareto_inverse_cdf(u, x_m, alpha):
    return x_m / np.power(1 - u, 1 / alpha)

# Teoretyczna funkcja gęstości prawdopodobieństwa dla rozkładu Pareto
def pareto_pdf(x, x_m, alpha):
    return (alpha * x_m**alpha) / (x**(alpha + 1))

# Generowanie próbek z rozkładu jednostajnego
num_samples = 1000
uniform_samples = np.random.rand(num_samples)

# Generowanie próbek z rozkładu Pareto przy użyciu odwrotnej dystrybuanty
pareto_samples = pareto_inverse_cdf(uniform_samples, x_m, alpha)

# Empiryczna dystrybuanta
sorted_samples = np.sort(pareto_samples)
empirical_cdf = np.arange(1, len(sorted_samples) + 1) / len(sorted_samples)

# Teoretyczna gęstość prawdopodobieństwa rozkładu Pareto
x_values = np.linspace(1, 10, 1000)
pareto_pdf_values = pareto_pdf(x_values, x_m, alpha)

# Tworzenie subplotów
fig, axs = plt.subplots(1, 2, figsize=(8, 12))

# Histogram wygenerowanych próbek
axs[0].hist(pareto_samples, bins=300, density=True, alpha=0.6, color='g')
axs[0].plot(x_values, pareto_pdf_values, 'r-', lw=2, label='Teoretyczna gęstość prawdopodobieństwa')
axs[0].set_title('Porównanie gęstości empirycznej i teoretycznej')
axs[0].set_xlabel('Wartość')
axs[0].set_ylabel('Gęstość prawdopodobieństwa')
axs[0].legend()
axs[0].grid(True)

# Empiryczna dystrybuanta
axs[1].step(sorted_samples, empirical_cdf, color='b', label='Empiryczna dystrybuanta')
axs[1].set_title('Empiryczna dystrybuanta')
axs[1].set_xlabel('Wartość')
axs[1].set_ylabel('Prawdopodobieństwo')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()
