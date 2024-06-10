import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.integrate import quad
from scipy import integrate


T = np.pi/2

def l_1(t):
    return 5*(np.sin(t)**2)

def l_2(t):
    return 2*(np.cos(t)**3)

result_1, error = integrate.quad(l_1, 0, T)
result_2, error = integrate.quad(l_2, 0, T)

x = np.linspace(0,T,int(1e6))
f_1 = l_1(x)
f_2 = l_2(x)

k_1 = np.random.poisson(result_1)
k_2 = np.random.poisson(result_2)

def akceptacja(n,f,l):
    res = []
    k=0
    while k<n:
        x = np.random.uniform(0,T)
        y = np.random.uniform(0,np.max(f))
        if y<l(x):
            res.append(x)
            k+=1
    res = np.sort(res)
    return res

zdarzenia_1 = akceptacja(k_1,f_1,l_1)
zdarzenia_2 = akceptacja(k_2,f_2,l_2)
zdarznia = (zdarzenia_1,zdarzenia_2)

def combine(T, zdarzenia):
    t1, t2 = zdarzenia
    ts = np.concatenate((t1, t2))
    ts.sort()
    return ts

ts = combine(T, zdarznia)

plt.scatter([0], [0], color='black')
plt.scatter(ts, np.arange(len(ts)), edgecolor='black', facecolor='none')
plt.scatter(ts, np.arange(1, len(ts)+1), color='black')

for i in range(len(ts)-1):
    plt.plot([ts[i], ts[i+1]], [i+1, i+1], color='black')
    
plt.plot([0, ts[0]], [0, 0], color='black')
plt.plot([ts[-1], T], [len(ts)-1, len(ts)-1], color='black')

def cumulative_intensity_combined(t):
    result1, _ = quad(l_1, 0, t)
    result2, _ = quad(l_2, 0, t)
    return result1 + result2

t_values = np.arange(0, T+0.01, 0.01)
l_values = [cumulative_intensity_combined(t) for t in t_values]
plt.plot(t_values, l_values, linewidth=2)

plt.xlabel('t')
plt.ylabel('ilość zdarzeń')
plt.title('Łączone procesy Poissona')
plt.show()