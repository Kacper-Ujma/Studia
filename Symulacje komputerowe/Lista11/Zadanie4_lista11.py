import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import levy_stable

# Definicja czasów
times = np.arange(0.01, 5, 0.001)

# Symulacja procesu Gamma
gamma_samples = np.random.gamma(shape=2, scale=1, size=len(times))

# Symulacja procesu Variance Gamma
vg_samples = np.random.gamma(shape=2, scale=0.1, size=len(times))
vg_samples *= np.random.normal(0.1, 0.2, len(times))

# Symulacja procesu Symetrycznego Stabilnego
alpha = 1.5
beta = 0
gamma = 1
delta = 0
ss_samples = levy_stable.rvs(alpha, beta, loc=delta, scale=gamma, size=len(times))

gamma_proces = np.cumsum(gamma_samples)
vg_proces = np.cumsum(vg_samples)
ss_proces = np.cumsum(vg_samples)

# Wykresy procesów
plt.figure(figsize=(12, 6))

plt.subplot(2, 3, 1)
plt.plot(times, gamma_samples, color='blue')
plt.title('Proces Gamma')
plt.xlabel('Czas')
plt.ylabel('Wartość')

plt.subplot(2, 3, 2)
plt.plot(times, vg_samples, color='red')
plt.title('Proces Variance Gamma')
plt.xlabel('Czas')
plt.ylabel('Wartość')

plt.subplot(2, 3, 3)
plt.plot(times, ss_samples, color='green')
plt.title('Proces Symetrycznego Stabilnego')
plt.xlabel('Czas')
plt.ylabel('Wartość')

plt.subplot(2,3,5)
# plt.plot(times,gamma_proces,label='gamma')
plt.plot(times,vg_proces,label='Variance gamma')
plt.plot(times,ss_proces,label='ss')
plt.legend()


plt.tight_layout()
plt.show()
