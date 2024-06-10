
def example4(A, B): # assume that A and B have equal length
    """Return the number of elements in B equal to the sum of prexsums in A."""
    n = len(A)
    count = 0
    for i in range(n):
        total = 0
        for j in range(n):
            for k in range(1+j):
                total += A[k]
        if B[i] == total:
            count += 1
    return count


if __name__ == "__main__":
    import time
    import random
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit
    import numpy as np

    N = np.arange(1,501,50)

    A_sets,A_100 ={},[]
    B_sets,B_100 ={},[]
    t_sets,t_100 =[],[]

    for i in range(len(N)):
        for j in range(100):
            dane = [random.randint(-100,100) for k in range(N[i])]
            A_100.append(dane)
            dane = [random.randint(-100,100) for k in range(N[i])]
            B_100.append(dane)
        A_sets[i] = A_100
        B_sets[i] = B_100
        A_100,B_100 = [],[]

    for i in A_sets:
        print(i)
        for j in range(len(A_sets[i])):
            t = time.perf_counter()
            example4(A_sets[i][j],B_sets[i][j])
            t = time.perf_counter() - t
            t_100.append(t)
        t_sets.append(np.mean(t_100))
        t_100 = []

    fig, (ax1,ax2)  = plt.subplots(ncols=2,nrows=1)
    ax1.plot(N,t_sets)
    ax1.set_xlabel("Romziar listy")
    ax1.set_ylabel("Czas")
    ax1.set_title("Zaleznosc czasu od rozmiaru danych")
    ax2.loglog(N,t_sets)
    ax2.set_xlabel("Romziar listy")
    ax2.set_ylabel("Czas")
    ax2.set_title("loglog")
    figure = fig
    fig.show()
    figure.savefig("Semestr3\Lista1\\{s}.png".format(s="Exmaple 4"))
