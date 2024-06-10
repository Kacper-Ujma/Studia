import numpy as np
import matplotlib.pyplot as plt

N = np.arange(100, 10001, 100)

srednia = 0
sigma = 1
mean_theoretical = np.exp(srednia + (sigma ** 2) / 2)
var_theoretical = (np.exp(sigma ** 2) - 1) * np.exp(2 * srednia + sigma ** 2)

means = []
vars = []
d_means = []
d_vars = []
for n in N:
    mean_diffs = []
    var_diffs = []
    for i in range(1000):
        sample = np.random.lognormal(srednia, sigma, n)
        mean_sample = np.mean(sample)
        var_sample = np.var(sample)
        mean_diffs.append(np.abs(mean_sample - mean_theoretical))
        var_diffs.append(np.abs(var_sample - var_theoretical))
    means.append(np.mean(mean_sample))
    vars.append(np.mean(var_sample))
    d_means.append(np.mean(mean_diffs))
    d_vars.append(np.mean(var_diffs))

plt.subplot(221)
plt.plot(N, means, color='b', label='Średnie różnice')
plt.hlines(mean_theoretical, N[0], N[-1], colors='r', label='Średnia różnica')
plt.title("Średnie różnice")
plt.legend()

plt.subplot(222)
plt.plot(N, vars, color='b', label='Różnice wariancji')
plt.hlines(var_theoretical, N[0], N[-1], colors='r', label='Średnia różnica')
plt.title("Różnice wariancji")
plt.legend()

plt.subplot(223)
plt.plot(N, d_means)
plt.title('Średnie różnice')

plt.subplot(224)
plt.plot(N, d_vars)
plt.title('Różnice wariancji')

plt.tight_layout()
plt.show()
