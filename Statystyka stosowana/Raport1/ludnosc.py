import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
from Funkcje.dystrybuanta import data


# Przerabianie danych
df = pd.read_excel("Semestr4\\Statystyka stosowana\\Raport1\\Zbiory danych\\pl_lud_2023_00_04_k2.xlsx")
df_2002 = pd.read_excel('Semestr4/Statystyka stosowana/Raport1/Zbiory danych/pl_lud_2002_00_04.xls')

liczba = df['Ogółem'].values[1:]
liczba_przedzialy = []
liczba_kolejno = []

wiek = df['ROCZNIKI URODZENIA'].values[1:]
wiek_przedzialy = []
wiek_kolejno = []

for i in range(2, len(wiek)-1):
    if i % 6 == 0:
        a,b = wiek[i].split('-')
        wiek_przedzialy.append('{}-{}'.format(2023-int(b),2023-int(a)))
        liczba_przedzialy.append(liczba[i])
    else:
        liczba_kolejno.append(liczba[i])
        wiek_kolejno.append(2023 - int(wiek[i]))

wiek_kolejno.append(100)
liczba_kolejno.append(liczba[-1])
wiek_przedzialy[-1] = '100 i starsi'

wiek_przedzialy.reverse()
liczba_przedzialy.reverse()
wiek_kolejno.reverse()
liczba_kolejno.reverse()
dane_ludnosci = []
for i,licznosc in enumerate(liczba_kolejno):
    dane_ludnosci.extend([wiek_kolejno[i]]*licznosc)
dane_ludnosci.reverse()
print(dane_ludnosci[-1])

# Liczenie zmiennych opisowych
q = np.percentile(dane_ludnosci,[25,50,75])
m = np.mean(dane_ludnosci)
v = np.var(dane_ludnosci,ddof=1)
sigma = np.std(dane_ludnosci,ddof=1)
kurtoza = stats.kurtosis(dane_ludnosci)
print('kwantyle',q,'średnia',m,v,sigma,kurtoza)

empirical_cdf = np.arange(1, len(dane_ludnosci) + 1) / len(dane_ludnosci)


for i in range(len(wiek_kolejno)):
    wiek_kolejno[i] = str(wiek_kolejno[i])

# fig, axs = plt.subplots(1, 3)
# axs[0].bar(wiek_przedzialy, liczba_przedzialy, align='center', width=0.8)
# axs[0].set_xlabel('Wiek', fontsize=10)
# axs[0].set_ylabel('Liczba ludności', fontsize=10)
# axs[0].tick_params(axis='x', rotation=45, labelsize=8)
# axs[0].set_title('Histogram liczby ludności w przedziałach wiekowych', fontsize=12)

# axs[1].bar(wiek_kolejno, liczba_kolejno, align='center', width=0.8)
# axs[1].set_xlabel('Wiek', fontsize=10)
# axs[1].set_ylabel('Liczba ludności', fontsize=10)
# axs[1].tick_params(axis='x', rotation=90, labelsize=5)
# axs[1].set_title('Histogram liczby ludności w latach', fontsize=12)

# axs[2].step(dane_ludnosci, empirical_cdf)
# plt.tight_layout()
# plt.show()

