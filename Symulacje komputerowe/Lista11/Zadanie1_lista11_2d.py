import numpy as np
import matplotlib.pyplot as plt

def brownian_motion_nd(times, n_simulations, dimensions):
    delta_t = np.diff(times)
    std_dev = np.sqrt(delta_t)
    increments = np.random.normal(0, std_dev[:, None, None], size=(len(delta_t), n_simulations, dimensions))
    increments = np.vstack([np.zeros((1, n_simulations, dimensions)), increments])
    return np.cumsum(increments, axis=0)

times = np.arange(0,3,0.001)
dimensions = 2
n_simulations = 6
bm_2d = brownian_motion_nd(times, n_simulations, dimensions)

plt.figure(figsize=(10, 6))
for i in range(n_simulations):
    plt.plot(bm_2d[:, i, 0], bm_2d[:, i, 1], label=f'Symulacja {i+1}')
    plt.scatter(bm_2d[0, i, 0], bm_2d[0, i, 1], c='red', marker='x')  # Punkt początkowy
plt.xlabel('Pozycja x')
plt.ylabel('Pozycja y')
plt.title('Symulacja ruchu Browna w 2D z punktami początkowymi')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()



