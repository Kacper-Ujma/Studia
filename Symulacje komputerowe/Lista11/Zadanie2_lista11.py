import numpy as np
import matplotlib.pyplot as plt

# Definicja funkcji symulacji ruchu Browna w 1D
def brownian_motion_1d(times, n_simulations):
    delta_t = np.diff(times)
    std_dev = np.sqrt(delta_t)
    increments = np.random.normal(0, std_dev, size=(n_simulations, len(delta_t)))
    return np.cumsum(np.hstack([np.zeros((n_simulations, 1)), increments]), axis=1)

# Funkcja do obliczenia czasu pierwszego wyjścia procesu Wienera poza granice a i b
def first_exit_time(bm, a, b):
    for i in range(len(bm)):
        if np.any(bm[i] < a) or np.any(bm[i] > b):
            return i
    return len(bm)

# Definicja punktów czasowych
times = np.arange(0, 3, 0.001)

# Symulacja ruchu Browna dla n_simulacji
n_simulations = 10000
bm_1d = brownian_motion_1d(times, n_simulations)

# Symulacja czasu pierwszego wyjścia procesu Wienera poza granice a i b
a, b = -3, 3
exit_times = []
for _ in range(100):
    exit_time = first_exit_time(bm_1d, a, b)
    exit_times.append(exit_time)

# Tworzenie wykresu średniej z próby czasów pierwszego wyjścia
plt.figure(figsize=(10, 6))
plt.hist(exit_times, bins=20, density=True, alpha=0.6, color='blue')
plt.xlabel('Czas pierwszego wyjścia poza granice [a, b]')
plt.ylabel('Częstość występowania')
plt.title('Rozkład czasów pierwszego wyjścia procesu Wienera poza granice [a, b]')
plt.grid(True)
plt.show()
