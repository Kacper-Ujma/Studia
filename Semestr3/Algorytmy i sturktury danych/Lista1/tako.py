import random
import time
import numpy as np
from scipy.optimize import curve_fit

a = [random.random()*100 for i in range(10**5)]
t_1 = []
for i in a:
    t_mnozenie = time.process_time()
    i*2
    t_mnozenie = time.process_time() - t_mnozenie
    t_1.append(t_mnozenie)

t = np.sum(t_1)

t_lista = time.process_time()
for i in range(len(a)):
    a[i]
t_lista = time.process_time() - t_lista

print("t mnozenie: {m}\nt lista: {n}".format(m=t,n=t_lista))

