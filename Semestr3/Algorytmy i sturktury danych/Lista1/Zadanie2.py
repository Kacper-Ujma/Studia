def example1(S):
    """Return the sum of the elements in sequence S."""
    n = len(S)
    total = 0
    for j in range(n):
        total += S[j]
    return total
# n 
def example2(S):
    """Return the sum of the elements with even index in sequence S."""
    n = len(S)
    total = 0
    for j in range(0, n, 2):
        total += S[j]
    return total
# n
def example3(S):
    """Return the sum of the prex sums of sequence S."""
    n = len(S)
    total = 0
    for j in range(n):
        for k in range(1+j):
            total += S[k]
    return total
# n**2
def create_plot(data:list,N:list,num:tuple,title,fig):
    n = N
    num[0].plot(n,data,label=title)
    num[0].set_xlabel("Romziar listy")
    num[0].set_ylabel("Czas")
    num[0].set_title("Zaleznosc czasu od rozmiaru danych")
    num[1].loglog(n,data,label=title)
    num[1].set_xlabel("Romziar listy")
    num[1].set_ylabel("Czas")
    num[1].set_title("loglog")
    figure = fig
    figure.suptitle(title)
    figure.savefig("Semestr3\Lista1\\{s}.png".format(s=title))

if __name__ == "__main__":
    import time
    import random
    import matplotlib.pyplot as plt
    import numpy as np

    fig1, (e1_plot,e1_log) = plt.subplots(ncols=2, nrows=1)
    fig2, (e2_plot,e2_log) = plt.subplots(ncols=2, nrows=1)
    fig3, (e3_plot,e3_log) = plt.subplots(ncols=2, nrows=1)
    num1 =(e1_plot,e1_log)
    num2 =(e2_plot,e2_log)
    num3 =(e3_plot,e3_log)

    data_sets = {}
    data_100 = []
    n = []
    times1,times2,times3 = [],[],[]
    time_sets1, time_sets2, time_sets3, time_sets4 = [],[],[],[]
    A,B,N = [],[],[1,10,50,100,250,500,750,1000,1500,2000,5000]

    for j in range(len(N)):
        # potega = 2**j
        for i in range(1000):
            data = [random.randint(-1000,1000) for i in range(N[j])]
            data_100.append(data)
        data_sets[j] = data_100
        data_100 = []
        # n.append(potega)
        print(j)

    for key,table in data_sets.items():
        for i in table:
            t = time.perf_counter()
            example1(i)
            t = time.perf_counter() - t
            times1.append(t)

            t = time.perf_counter()
            example2(i)
            t = time.perf_counter() - t
            times2.append(t)
            if len(i) <= 1000:
                t = time.perf_counter()
                example3(i)
                t = time.perf_counter() - t
                times3.append(t)

        time_sets1.append(np.mean(times1))
        time_sets2.append(np.mean(times2))
        if len(i) <= 1000:
            time_sets3.append(np.mean(times3))

        times1,times2,times3 = [],[],[]

    print('time set 1: {i}\ntime sets 2: {j}\ntime sets 3: {k}'.format(i=time_sets1,j=time_sets2,k=time_sets3))
            
    create_plot(time_sets1,N,num1,"Examaple 1",fig1)
    create_plot(time_sets2,N,num2,"Example 2",fig2)
    create_plot(time_sets3,N[0:8],num3,"Example 3",fig3)

