import numpy as np
import matplotlib.pyplot as plt

N = np.arange(200, 10000 + 1, 200)
mu = 2
sigma = 1
mean_teor = np.exp(mu + (sigma ** 2) / 2)

mu1_hat = []
mu2_hat = []
var_1 = []
var_2 = []

for n in N:
    mu1_temp = []
    mu2_temp = []
    
    for i in range(1000):
        data = np.random.lognormal(mean=mu, sigma=sigma, size=n)
        
        mu1_est = 2 * np.log(np.mean(data)) - 0.5 * np.log(np.mean(data ** 2))
        mu1_temp.append(mu1_est)
        
        mu2_est = np.mean(np.log(data))
        mu2_temp.append(mu2_est)
    
    mu1_hat.append(np.mean(np.abs(np.array(mu1_temp) - mu)))
    mu2_hat.append(np.mean(np.abs(np.array(mu2_temp) - mu)))
    
    var_1.append(np.var(mu1_temp))
    var_2.append(np.var(mu2_temp))

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(N, mu1_hat, label='mu1', color='blue')
plt.plot(N, mu2_hat, label='mu2', color='red')
plt.title("Średnia odległość estymatora od wartości teoretycznej")
plt.xlabel('Wielkość próbki')
plt.ylabel('Średnia odległość')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(N, var_1, label='mu1', color='blue')
plt.plot(N, var_2, label='mu2', color='red')
plt.title("Wariancja estymatorów")
plt.xlabel('Wielkość próbki')
plt.ylabel('Wariancja')
plt.legend()

plt.tight_layout()
plt.show()
