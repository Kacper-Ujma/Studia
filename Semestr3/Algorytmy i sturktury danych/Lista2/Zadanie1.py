

def Znajdywanie_Najwiekszego_Elementu(lista:list,acc):
    if len(lista) > 0:
        if acc < lista[0]:
            acc = lista[0]
        return Znajdywanie_Najwiekszego_Elementu(lista[1:],acc)
    else: return acc

    
if __name__ == "__main__":
    import time
    import random
    import matplotlib.pyplot as plt
    import psutil
    import numpy as np
    from scipy.optimize import curve_fit

    fig, (ax1,ax2,ax3) = plt.subplots(ncols=3,nrows=1)

    N = [2,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900]
    S = [random.randint(-1000,1000) for i in range(N[0])]
    n = 1000

    Data,Data_mean = [],[]
    Times = []
    Time_mean = 0
    Memory = []
    Memory_mean = 0

    def func(x,a,b):
        return a*x + b

    for size in N:
        for i in range(n):
            Data_single = [random.randint(-100,100) for j in range(size)]
            Data_mean.append(Data_single)
        Data.append(Data_mean)
        Data_mean = []

    for set in Data:
        for d in set:
            # print(d,d[0])
            process = psutil.Process()

            t = time.process_time()
            Znajdywanie_Najwiekszego_Elementu(d,d[0])
            t = time.process_time() - t

            m = process.memory_info().rss
            Znajdywanie_Najwiekszego_Elementu(d,d[0])
            m = process.memory_info().rss - m

            Time_mean += t 
            Memory_mean += m
        Times.append(Time_mean/n)
        Memory.append(Memory_mean/n)
        Time_mean = 0
        Memory_mean = 0
    print(Times,Memory)

    popt,pcov = curve_fit(func,N,Times)
    print("a = %s, b = %s"%(popt[0],popt[1]))
    curve_data = np.arange(N[0],N[-1],10)


    plt.style.use('ggplot')
    ax1.plot(N,Times,'ro',label="Pomiary czasu")
    ax1.plot(curve_data,func(curve_data,*popt),label="Dopoasowanie")
    ax1.set_xlabel("Rozmiar listy")
    ax1.set_ylabel("Czas wykonania")
    ax1.legend()
    ax1.set_title("Czas i dopasowanie")
    ax2.plot(N,Memory)
    ax2.set_xlabel("Rozmiar listy")
    ax2.set_ylabel("Zuzuta pamiec")
    ax2.set_title("Zuzycie pamieci")
    ax3.loglog(N,Times)
    ax3.set_xlabel("Rozmiar listy")
    ax3.set_ylabel("Czas wykonania")
    ax3.set_title("Wykres log log") 

    fig.savefig("Semestr3\Lista2\\Wykresy_Zadanie_1.png") 
    fig.tight_layout()
      
    plt.show()
    # print(Data)
