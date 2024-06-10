import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde, lognorm

mu = 1
sigma = 1
N = 1000
dane = np.random.lognormal(mean=mu, sigma=sigma, size=N)

x_theoretical = np.linspace(0, np.max(dane), 10000)
y_theoretical = lognorm.pdf(x_theoretical, s=sigma, scale=np.exp(mu))

kde = gaussian_kde(dane, bw_method='scott')
x_empirical = np.linspace(np.min(dane), np.max(dane), 1000)
y_empirical = kde(x_empirical)

plt.hist(dane, bins=50, density=True, alpha=0.3, label='Histogram', color='blue')
plt.plot(x_empirical, y_empirical, color='green', label='Empiryczna gęstość (KDE)')
plt.plot(x_theoretical, y_theoretical, color='red', label='Teoretyczna gęstość')

cdf_theoretical = lognorm.cdf(x_theoretical, s=sigma, scale=np.exp(mu))
sorted_data = np.sort(dane)
cdf_empirical = np.arange(1, N + 1) / N

plt.figure()
plt.plot(sorted_data, cdf_empirical, marker='.', linestyle='none', color='green', label='Empiryczna dystrybuanta')
plt.plot(x_theoretical, cdf_theoretical, color='red', label='Teoretyczna dystrybuanta')

plt.title("Dystrybuanty: Empiryczna vs. Teoretyczna")
plt.xlabel("Wartość")
plt.ylabel("Prawdopodobieństwo")
plt.legend()
plt.show()
