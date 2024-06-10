import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
from Funkcje.dystrybuanta import data

df1 = pd.read_excel('Semestr4\\Statystyka stosowana\\Raport1\\Zbiory danych\\Ludnosc_w_Polsce_1989-2022.xls')
df2 = pd.read_excel('Semestr4\\Statystyka stosowana\\Raport1\\Zbiory danych\\Ludnosc_w_Polsce_1989-2022.xls')

liczba_ludnosci_w_latach = df1.loc[5].values[1:] * 1000
liczba_ludnosci_w_latach = data(liczba_ludnosci_w_latach)
x = np.linspace(1989,2022,num=(2022-1989+1))
print(x)

plt.plot(x,liczba_ludnosci_w_latach.data)
plt.ylim(34e6,40e6)
plt.grid()
plt.show()

with open('Semestr4\Statystyka stosowana\Raport1\Zmienne statystyczne\plik.txt','w') as f:
    f.write('Zmienne statystyczne\n')
    f.write('2022 , 2002\n')
    f.write('Srednie arytmetyczne {}]\n'.format(1))