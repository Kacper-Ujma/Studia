import numpy as np
import matplotlib.pyplot as plt

# Parametry symulacji
T = 10000  # czas do którego symulujemy ruch Browna
dt = 0.1   # krok czasowy
n_steps = int(T / dt)  # liczba kroków czasowych

# Symulacja ruchu Browna
np.random.seed(42)  # dla powtarzalności wyników
increments = np.random.normal(0, np.sqrt(dt), n_steps)
brownian_motion = np.cumsum(increments)
times = np.arange(0, T, dt)

# Obliczenie granic prawa iterowanego logarytmu
lil_upper_bound = np.sqrt(2 * times * np.log(np.log(times + 2)))
lil_lower_bound = -lil_upper_bound

# Wizualizacja ruchu Browna oraz prawa iterowanego logarytmu
plt.figure(figsize=(12, 6))
plt.plot(times, brownian_motion, label='Ruch Browna', color='blue')
plt.plot(times, lil_upper_bound, label='Granica górna LIL', linestyle='--', color='red')
plt.plot(times, lil_lower_bound, label='Granica dolna LIL', linestyle='--', color='green')
plt.xlabel('Czas')
plt.ylabel('Pozycja')
plt.title('Ruch Browna oraz prawo iterowanego logarytmu')
plt.legend()
plt.grid(True)
plt.show()
