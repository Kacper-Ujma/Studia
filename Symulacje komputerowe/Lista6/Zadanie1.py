import numpy as np
import matplotlib.pyplot as plt


T = 10
l = 1
M = int(1e6)
def bell(l):
    return np.random.exponential(l)

def a(T,l):
    t=0
    N=0
    while t < T:
        t=t+bell(l)
        N += 1
    N -= 1
    return N

def poison(l,size):
    return np.random.poisson(l*T,size=size)


Ns = []
for i in range(M):
    Ns.append(a(T,l))

pois = poison(l,M)
xs = np.linspace(0,20,20)

# Tworzenie histogramu dla Ns
plt.hist(Ns,density=True,bins=15, alpha=0.5,align='mid')

# Tworzenie histogramu dla pois


# Obliczenie zliczeń i utworzenie wykresu plot dla Ns
unique_Ns, counts_Ns = np.unique(Ns, return_counts=True)
plt.plot(unique_Ns, counts_Ns / np.sum(counts_Ns), 'ro-')

# Obliczenie zliczeń i utworzenie wykresu plot dla pois
unique_pois, counts_pois = np.unique(pois, return_counts=True)
plt.plot(unique_pois, counts_pois / np.sum(counts_pois), 'bo-')

# Dodanie legendy
plt.legend()

plt.show()
