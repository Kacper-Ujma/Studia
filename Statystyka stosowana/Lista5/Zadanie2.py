import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

# Funkcja do generowania losowej macierzy kowariancji 2x2
def generate_covariance_matrix_2x2():
    A = np.random.randint(2, 2)
    return np.dot(A, A.T)

# Funkcja do generowania losowej macierzy kowariancji 3x3
def generate_covariance_matrix_3x3():
    A = np.random.rand(3, 3)
    return np.dot(A, A.T)

# Funkcja do obliczania wektorów własnych i wartości własnych
def calculate_eigen(matrix):
    eigen_values, eigen_vectors = np.linalg.eig(matrix)
    return eigen_values, eigen_vectors

# Generowanie losowej macierzy kowariancji 2x2
covariance_matrix_2x2 = generate_covariance_matrix_2x2()
print("Macierz kowariancji 2x2:")
print(covariance_matrix_2x2)

# Obliczanie wektorów własnych dla macierzy 2x2
eigenvalues_2x2, eigenvectors_2x2 = calculate_eigen(covariance_matrix_2x2)
print("Wartości własne dla macierzy 2x2:")
print(eigenvalues_2x2)
print("Wektory własne dla macierzy 2x2:")
print(eigenvectors_2x2)

# Generowanie losowej macierzy kowariancji 3x3
covariance_matrix_3x3 = generate_covariance_matrix_3x3()
print("\nMacierz kowariancji 3x3:")
print(covariance_matrix_3x3)

# Obliczanie wektorów własnych dla macierzy 3x3
eigenvalues_3x3, eigenvectors_3x3 = calculate_eigen(covariance_matrix_3x3)
print("Wartości własne dla macierzy 3x3:")
print(eigenvalues_3x3)
print("Wektory własne dla macierzy 3x3:")
print(eigenvectors_3x3)

# Zwizualizuj rozkład wektorów normalnych dla macierzy 2x2
mean = [0, 0]  # średnia dla macierzy 2x2
x, y = np.mgrid[-3:3:.01, -3:3:.01]
pos = np.dstack((x, y))
rv = multivariate_normal(mean, covariance_matrix_2x2)
plt.figure(figsize=(10, 6))
plt.contourf(x, y, rv.pdf(pos), cmap='viridis')
plt.title('Rozkład wektorów normalnych dla macierzy 2x2')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar()
plt.show()

# Zwizualizuj rozkład wektorów normalnych dla macierzy 3x3
mean = [0, 0, 0]  # średnia dla macierzy 3x3
x, y, z = np.mgrid[-3:3:.01, -3:3:.01, -3:3:.01]
pos = np.dstack((x, y, z))
rv = multivariate_normal(mean, covariance_matrix_3x3)
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.contour3D(x, y, z, rv.pdf(pos), cmap='viridis')
ax.set_title('Rozkład wektorów normalnych dla macierzy 3x3')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
