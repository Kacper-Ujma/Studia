import numpy as np
import matplotlib.pyplot as plt
from data import Data, DiscreteData, ContinuousData

# Load data from file
with open("C:\\Users\\kacpu\\Downloads\\dane_lista1.txt") as f:
    dane_X = [float(line.strip()) for line in f]

dane_Y = np.exp(dane_X)
bars = 20
# c, d, e

dane_X=ContinuousData(dane_X)
dane_Y=ContinuousData(dane_Y)
pdf_X = dane_X.pdf_normal(0,1,False,False,bins=30)
pdf_Y = dane_Y.pdf_lognormal(0,1,False,False,bins=30)

plt.subplot(121)
plt.hist(dane_X.data,density=1,bins=bars,edgecolor='b')
plt.plot(pdf_X[0],pdf_X[1])
plt.subplot(122)
plt.hist(dane_Y.data,density=1,bins=bars,edgecolor='b')
plt.plot(pdf_Y[0],pdf_Y[1])
plt.show()
plt.clf()

