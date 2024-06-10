import numpy as np
import matplotlib.pyplot as plt

mi = 0
variance = 1
N = 1000
proba = np.random.normal(mi,variance,N)
n = np.arange(5,406,10)


res_mean=[]
res_median=[]
for num in n:
    container_mean = []
    container_median = []
    for i in range(1000):
        dane = np.random.normal(mi,variance,num)
        container_mean.append(np.mean(dane))
        container_median.append(np.median(dane))
    res_mean.append(np.mean(container_mean)**2)
    res_median.append(np.mean(container_median)**2)

plt.plot(n,res_mean,label='Srednia',color='b')
plt.plot(n,res_median,label='Mediana',color='r')
plt.legend()
plt.show()