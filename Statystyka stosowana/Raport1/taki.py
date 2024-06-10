import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
from Funkcje.dystrybuanta import data

df_2002 = pd.read_excel('Semestr4\\Statystyka stosowana\\Raport1\\Zbiory danych\\pl_lud_2002_00_04.xls')
df_2022 = pd.read_excel('Semestr4\\Statystyka stosowana\\Raport1\\Zbiory danych\\pl_lud_2022_00_04.xlsx')

# 2002
def wszystko_2002():
    roczniki_2002 = df_2002.iloc[10:,0].values[:]
    liczba_ludnosci_2002 = df_2002.iloc[8:,1].values[:]
    liczba_ludnosci_2002_calk = liczba_ludnosci_2002[0]
    liczba_ludnosci_2002 = liczba_ludnosci_2002[2:]

    wiek_przedzialy_2002 = []
    wiek_kolejno_2002 = []

    ilosc_ludzi_przedzialy_2002 = []
    ilosc_ludzi_kolejno_2002 = []

    for i in range(len(roczniki_2002)-1):
        if i % 6 == 0:
            a,b = roczniki_2002[i].split('-')
            wiek_przedzialy_2002.append('{}-{}'.format(2002-int(b),2002-int(a)))
            ilosc_ludzi_przedzialy_2002.append(liczba_ludnosci_2002[i])
        else:
            wiek_kolejno_2002.append('{}'.format(2002-int(roczniki_2002[i])))
            ilosc_ludzi_kolejno_2002.append(liczba_ludnosci_2002[i])

    wiek_przedzialy_2002.append('100 i starsi')
    wiek_kolejno_2002.append('100 i starsi')
    ilosc_ludzi_kolejno_2002.append(liczba_ludnosci_2002[-1])
    ilosc_ludzi_przedzialy_2002.append(liczba_ludnosci_2002[-1])

    wiek_kolejno_2002.reverse()
    wiek_przedzialy_2002.reverse()
    ilosc_ludzi_przedzialy_2002.reverse()
    ilosc_ludzi_kolejno_2002.reverse()

    liczba_ludnosci_2002_wiek = []
    liczba_ludnosci_2002_wiek.extend([100]*ilosc_ludzi_kolejno_2002[0])

    for i in range(1,len(ilosc_ludzi_kolejno_2002)):
        liczba_ludnosci_2002_wiek.extend([int(wiek_kolejno_2002[i])]*ilosc_ludzi_kolejno_2002[i])

    # plt.clf()
    # plt.subplots(figsize=(9, 6))
    # plt.bar(wiek_kolejno_2002,ilosc_ludzi_kolejno_2002,width=1,edgecolor='b')
    # plt.title('Histogram ludności 2002')
    # plt.xlabel('Wiek')
    # plt.ylabel('Liczba ludzi')
    # plt.tick_params(axis='x',rotation=90,labelsize=4)
    
    # plt.savefig('Semestr4\Statystyka stosowana\Raport1\Wykresy\\Histogram_2002.png')
    
    return data(liczba_ludnosci_2002_wiek)

# 2022
def wszystko_2022():
    roczniki_2022 = df_2022.iloc[9:,0].values[:]
    liczba_ludnosci_2022 = df_2022.iloc[6:,1].values[:]
    liczba_ludnosci_2022 = liczba_ludnosci_2022[2:]
    liczba_ludnosci_2022_calk = liczba_ludnosci_2022[0]
    liczba_ludnosci_2022 = liczba_ludnosci_2022[1:]

    wiek_przedzialy_2022 = []
    wiek_kolejno_2022 = []

    ilosc_ludzi_przedzialy_2022 = []
    ilosc_ludzi_kolejno_2022 = []

    for i in range(len(roczniki_2022)-1):
        if i % 6 == 0:
            a,b = roczniki_2022[i].split('-')
            wiek_przedzialy_2022.append('{}-{}'.format(2022-int(b),2022-int(a)))
            ilosc_ludzi_przedzialy_2022.append(liczba_ludnosci_2022[i])
        else:
            wiek_kolejno_2022.append('{}'.format(2022-int(roczniki_2022[i])))
            ilosc_ludzi_kolejno_2022.append(liczba_ludnosci_2022[i])

    wiek_przedzialy_2022.append('100 i starsi')
    wiek_kolejno_2022.append('100 i starsi')
    ilosc_ludzi_kolejno_2022.append(liczba_ludnosci_2022[-1])
    ilosc_ludzi_przedzialy_2022.append(liczba_ludnosci_2022[-1])

    wiek_kolejno_2022.reverse()
    wiek_przedzialy_2022.reverse()
    ilosc_ludzi_przedzialy_2022.reverse()
    ilosc_ludzi_kolejno_2022.reverse()

    liczba_ludnosci_2022_wiek = []
    liczba_ludnosci_2022_wiek.extend([100]*ilosc_ludzi_kolejno_2022[0])

    for i in range(1,len(ilosc_ludzi_kolejno_2022)):
        liczba_ludnosci_2022_wiek.extend([int(wiek_kolejno_2022[i])]*ilosc_ludzi_kolejno_2022[i])

    # plt.clf()
    # plt.subplots(figsize=(9, 6))
    # plt.bar(wiek_kolejno_2022,ilosc_ludzi_kolejno_2022,width=1,edgecolor='b')
    # plt.title('Histogram ludności 2022')
    # plt.tick_params(axis='x',rotation=90,labelsize=4)
    # plt.xlabel('Wiek')
    # plt.ylabel('Liczba ludzi')
    # plt.savefig('Semestr4\Statystyka stosowana\Raport1\Wykresy\\Histogram_2022.png')
    
    return data(liczba_ludnosci_2022_wiek)

def wczytywanie_danych(d1:data,d2:data):
    with open('Semestr4\Statystyka stosowana\Raport1\Zmienne statystyczne\plik.txt','w') as f:
        f.write('Zmienne statystyczne\n')
        f.write('2022 , 2002\n')
        f.write('Srednie arytmetyczne: {} {}\n'.format(d1.mean_aritmetic(),d2.mean_aritmetic()))
        f.write('Srednia harmoniczne {} {}\n'.format(d1.mean_harmonic(),d2.mean_harmonic()))
        f.write('Srednie geaometryczne {} {}\n'.format(d1.mean_geometric(),d2.mean_geometric()))
        f.write('Medaniany {} {}\n'.format(d1.median(),d2.median()))
        f.write('Wariancje {} {}\n'.format(d1.variance(),d2.variance()))
        f.write('Odchylenie standardowe {} {}\n'.format(d1.standard_deviation(),d2.standard_deviation()))
        f.write('Kurtoza {} {}\n'.format(d1.kurtosis(),d2.kurtosis()))
        f.write('Skosnionsc {} {}\n'.format(d1.curviture(),d2.curviture()))
        f.write('Pierwszy kwantyl {} {}\n'.format(d1.quantile_1st(),d2.quantile_1st()))
        f.write('Drugi kwantyl {} {}\n'.format(d1.quantile_2nd(),d2.quantile_2nd()))
        f.write('Trzeci kwantyl {} {}\n'.format(d1.quantile_3rd(),d2.quantile_3rd()))
        f.write('Rozstep kwantylowy {} {}\n'.format(d1.interquartile_range(),d2.interquartile_range()))

def distribution_discrete_visualize(d:data, name, year):
    data = d.data
    n = len(d)
    xs = list(np.arange(d.sample_range(), -1, -1))  # Zmiana kolejności na odwróconą
    probs = []
    for age in xs:
        probs.append(data.count(age) / n)
    probs = list(np.cumsum(probs))
    path = 'Semestr4\\Statystyka stosowana\\Raport1\\Wykresy\\' + name + '.png'
    return xs, probs, path

if __name__ == '__main__':
    dane_2022 = wszystko_2022()
    dane_2002 = wszystko_2002()
    # wczytywanie_danych(dane_2022,dane_2002)
    x_2022,y_2022,p_2022 = distribution_discrete_visualize(dane_2022,'Dystrybuanta_2022',2022)
    x_2002,y_2002,p_2002 = distribution_discrete_visualize(dane_2002,'Dystrybuanta_2002',2002)

    x_percentage = [i/100 for i in range(5,51,5)]
    mean_cut_2002 = []
    mean_cut_2022 = []

    # for i in range(len(x_percentage)):
    #     mean_cut_2002.append(dane_2002.mean_cut(int((len(dane_2002)*x_percentage[i])//2)))
    #     mean_cut_2022.append(dane_2022.mean_cut(int((len(dane_2022)*x_percentage[i])//2)))
    #     x_percentage[i] = '{}%'.format(x_percentage[i]*100)
    # print(mean_cut_2002,mean_cut_2022,x_percentage)
    plt.clf()
    plt.boxplot([list(dane_2002.data),list(dane_2022.data)])
    plt.xticks([1, 2], ['2002', '2022'])
    plt.savefig('Semestr4\Statystyka stosowana\Raport1\Wykresy\\Boxploty.png')
    plt.show()
    # plt.clf()
    # plt.subplots(figsize=(9, 6))
    # plt.title('Dystrybuanty empiryczne')
    # plt.step(x_2002, y_2002,color='b',label='2002')
    # plt.step(x_2022, y_2022,color='r',label='2022')
    # plt.xticks(np.arange(0, 100 + 1, 10))  # Dodanie etykiet na osi x co 10 lat
    # plt.gca().invert_xaxis()  # Odwrócenie osi x
    # plt.xlabel('Wiek')
    # plt.legend()
    # plt.savefig('Semestr4\\Statystyka stosowana\\Raport1\\Wykresy\\' + 'Dystrybuanty_empiryczne' + '.png')
    # plt.show()