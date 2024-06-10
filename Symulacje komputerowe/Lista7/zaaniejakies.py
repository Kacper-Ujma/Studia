from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

T = 1

def l(t):
    return (t-1)**2 + 1


def F(t):
    return 

result, error = integrate.quad(l, 0, T)

x = np.linspace(0,T,int(1e6))
f = l(x)

print(result)