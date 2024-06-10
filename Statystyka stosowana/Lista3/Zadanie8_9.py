import numpy as np 

dyrektor = [41,27,35,33,25,47,38,53,43,35,36]
wizytator = [38,24,34,29,27,47,43,52,39,31,29]
X = [5,4,6,2,1,3]
Y = [6,2,3,5,1,4]

def rang(data:list):
    res = {}
    posortowane = sorted(data.copy(),reverse=True)
    for i in range(len(data)):
        res[data[i]] = posortowane.index(data[i]) + 1 + (posortowane.count(data[i])-1)/2
    return res

rank_d=rang(dyrektor)
rank_w=rang(wizytator)

print(rank_d)
d = []
d9 = []
for i in range(len(dyrektor)):
    d.append((rank_d[dyrektor[i]]-rank_w[wizytator[i]])**2)

for i in range(len(X)):
    d9.append((X[i]-Y[i])**2)

print(d9)
n = len(X)
rs = 1 - 6*np.sum(d9)/n/(n**2-1)
rs = round(rs,2)
print(rs)

"""
Raport znaleźć dwa zrbiory danych wyciagnąć informacje na ich temat porównania wykresy 
coś żeby mozna było powiedzieć pierwsze co to czym sa i co o nich powiedzeic, źódła
wyciagniecie informacji na temat znanych zmiennych opisowych średnie mediany itp. 
wsyzstko opisywac nawet rysunki mówic co na nich jest i co to znaczy. 
dwa zbiry danych, na kocnu podsumowanie co zostało zrobione i jakie mamy wnioski np. dwa box-ploty
wystarczy 5 stron ale w punkt, nie trzeba wpisywac wzorów. Najważniejssze spojrzec na dane. Wrzucic pdf na goolge czy coś.
Dane wielkościowo min. 500. Bez kodu xd, korzystam z czego chce.  
"""