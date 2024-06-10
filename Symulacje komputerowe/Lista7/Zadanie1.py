from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

T = 2*np.pi

def l(t):
    return 5*(np.sin(t)**2)

result, error = integrate.quad(l, 0, T)

x = np.linspace(0,T,int(1e6))
f = l(x)

k = np.random.poisson(result)


def akceptacja(n):
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

lam = akceptacja(k)

events = list(lam)
events.insert(0,0)
events += [T]

print(k)
y = np.array(range(1,k+1))
yn = np.insert(y, 0, 0)

fig, ax = plt.subplots(1,2)
print(events)

ax[0].hlines(y=yn, xmin=events[:-1], xmax=events[1:],
          color='red', zorder=1)

ax[0].vlines(x=events[1:-1], ymin=yn[:-1], ymax=yn[1:], color='red',
          linestyle='dashed', zorder=1)

ax[0].scatter(events[1:-1], y, color='red', s=18, zorder=2)
ax[0].scatter(events[1:-1], yn[:-1], color='white', s=18, zorder=2,
           edgecolor='red')
ax[0].grid(False)

ax[1].plot(x,f)


plt.show()