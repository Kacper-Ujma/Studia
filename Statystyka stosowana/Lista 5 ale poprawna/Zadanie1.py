import numpy as np

# Definiujemy próbkę X1, ..., Xn z rozkładu Poissona
n = 1000  # wielkość próbki
lam = 3  # parametr rozkładu Poissona

# Generujemy próbkę z rozkładu Poissona
sample = np.random.poisson(lam, n)

# Obliczamy estymator momentu pierwszego (średniej)
lambda_hat_1 = np.mean(sample)

# Obliczamy estymator momentu drugiego
lambda_hat_2 = np.mean(sample ** 2)

# Obliczamy estymator parametru λ
lambda_estimator = np.sqrt(lambda_hat_2)

print("Estymator momentu pierwszego λ:", lambda_hat_1)
print("Estymator momentu drugiego λ^2:", lambda_hat_2)
print("Estymator parametru λ:", lambda_estimator)
