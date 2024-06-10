def func(x,a,b):
    return a*x*np.log(x) + b

if __name__ == "__main__":
    import time
    import random
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.optimize import curve_fit

    fig, (ax1,ax2) = plt.subplots(ncols=2, nrows=1)
    figures = (ax1,ax2)

    data,times,dane_100 = [],[],[]
    n= []
    time_100 = []
    data_dic = {}

    for i in range(1,15,1):
        potega = 2**i
        for j in range(1000):
            dane_100 = [random.randint(-100,100) for k in range(potega)]
            data.append(tuple(dane_100))
        n.append(potega)
        data_dic[i] = data
        data = []
        print(i)

    for key,table in data_dic.items():
        for d in table:
            t = time.process_time()
            sorted(d)
            t = time.process_time() - t
            time_100.append(t)
        times.append(np.mean(time_100))
        time_100 = []

    popt,pcov = curve_fit(func,n,times)
    print("a = %s, b = %s"%(popt[0],popt[1]))
    dane_curve = np.arange(1,2**14,10)
    title = "Funkcja sorted"

    ax1.plot(n,times,'ro',label=title)
    ax1.plot(dane_curve,func(dane_curve,*popt))
    ax1.set_xlabel("Romziar listy")
    ax1.set_ylabel("Czas")
    ax1.set_title("Zaleznosc czasu od rozmiaru danych")
    ax2.loglog(n,times,'ro',label=title)
    ax2.set_xlabel("Romziar listy")
    ax2.set_ylabel("Czas")
    ax2.set_title("loglog")
    figure = fig
    figure.suptitle(title)
    plt.show()
    figure.savefig("Semestr3\\Lista1\\{s}.png".format(s=title))
