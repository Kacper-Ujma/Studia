import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Wygenerowanie 1000 próbek z rozkładu jednostajnego U(0,1)
u = np.random.uniform(0, 1, 1000)
lam = 2
alpha = 3

# Generowanie próbek z rozkładu Pareto
dane_pareto = lam * (np.power((1 - u), -1/alpha) - 1)

# Obliczanie KDE (empirycznej gęstości rozkładu Pareto)
kde = gaussian_kde(dane_pareto)
x_vals = np.linspace(min(dane_pareto), max(dane_pareto), 1000)
kde_vals = kde(x_vals)

# Rysowanie histogramu i empirycznej gęstości na jednym wykresie
plt.figure(figsize=(8, 6))
plt.hist(dane_pareto, bins=30, density=True, alpha=0.6, color='g', label='Histogram')
plt.plot(x_vals, kde_vals, color='r', label='Empiryczna gęstość (KDE)')
plt.title('Histogram i empiryczna gęstość rozkładu Pareto')
plt.xlabel('Wartość')
plt.ylabel('Gęstość')
plt.legend()
plt.show()
