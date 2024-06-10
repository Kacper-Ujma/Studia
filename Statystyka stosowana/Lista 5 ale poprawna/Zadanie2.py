import numpy as np


n = 1000
mu = 0 
sigma = 2

dane = np.random.lognormal(mu,sigma,n)



variance_hat = np.log(sigma/(np.mean(dane)**2)+1)
mean_hat = np.log(np.mean(dane))-variance_hat/2

print(mu,mean_hat)
print(sigma,variance_hat)
