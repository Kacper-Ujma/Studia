import numpy as np
import matplotlib.pyplot as plt

T = 10  # czas końcowy
lambda_ = 1  # intensywność zdarzeń

k = np.random.poisson(lambda_*T)
events = [0] + sorted(np.random.uniform(0,T,k)) + [T]

print(k)
y = np.array(range(1,k+1))
yn = np.insert(y, 0, 0)
print(yn)
fig, ax = plt.subplots()
ax.set_facecolor('white')

ax.hlines(y=yn, xmin=events[:-1], xmax=events[1:],
          color='red', zorder=1)

ax.vlines(x=events[1:-1], ymin=yn[:-1], ymax=yn[1:], color='red',
          linestyle='dashed', zorder=1)

ax.scatter(events[1:-1], y, color='red', s=18, zorder=2)
ax.scatter(events[1:-1], yn[:-1], color='white', s=18, zorder=2,
           edgecolor='red')
ax.grid(False)


plt.show()