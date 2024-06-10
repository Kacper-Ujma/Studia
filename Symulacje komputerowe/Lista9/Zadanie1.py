import numpy as np
import matplotlib.pyplot as plt

# Funkcja do generowania losowej miary Poissonowskiej na zbiorze Ω
def generate_poisson_measure(omega, lam):
    # Krok 1: Wylosuj zmienną N(Ω) ∼ Poiss(λ|Ω|)
    N_omega = np.random.poisson(lam * len(omega))

    # Krok 2: Wylosuj N(Ω) niezależnych zmiennych losowych z rozkładu jednostajnego U(Ω)
    poisson_measure = np.random.choice(omega, size=N_omega, replace=True)
    
    return poisson_measure

# Zbiór Ω
# (a) Liczby {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
omega_a = np.arange(1, 11)

# (b) Sześcian
omega_b = [(x, y, z) for x in range(1, 4) for y in range(1, 4) for z in range(1, 4)]

# (c) Koło - przyjmujemy koło o promieniu 5 i środku w punkcie (0, 0)
radius = 5
center = (0, 0)
num_points = 1000
theta = np.random.uniform(0, 2 * np.pi, num_points)
r = radius * np.sqrt(np.random.uniform(0, 1, num_points))
omega_c = [(center[0] + r[i] * np.cos(theta[i]), center[1] + r[i] * np.sin(theta[i])) for i in range(num_points)]

# Parametr λ
lam = 3

# Generowanie losowej miary Poissonowskiej dla każdego zbioru Ω
poisson_measure_a = generate_poisson_measure(omega_a, lam)
poisson_measure_b = generate_poisson_measure(omega_b, lam)
poisson_measure_c = generate_poisson_measure(omega_c, lam)

# Wizualizacja wyników
plt.figure(figsize=(15, 5))

# (a) Liczby
plt.subplot(1, 3, 1)
plt.hist(poisson_measure_a, bins=np.arange(0.5, 11.5, 1), color='skyblue', edgecolor='black')
plt.title('Liczby')
plt.xlabel('Wartość')
plt.ylabel('Liczba punktów')

# (b) Sześcian
poisson_measure_b_arr = np.array(poisson_measure_b)
plt.subplot(1, 3, 2)
plt.scatter(poisson_measure_b_arr[:, 0], poisson_measure_b_arr[:, 1], color='green')
plt.title('Sześcian')
plt.xlabel('Współrzędna X')
plt.ylabel('Współrzędna Y')

# (c) Koło
poisson_measure_c_arr = np.array(omega_c)
plt.subplot(1, 3, 3)
plt.scatter(poisson_measure_c_arr[:, 0], poisson_measure_c_arr[:, 1], color='orange')
plt.title('Koło')
plt.xlabel('Współrzędna X')
plt.ylabel('Współrzędna Y')

plt.tight_layout()
plt.show()
