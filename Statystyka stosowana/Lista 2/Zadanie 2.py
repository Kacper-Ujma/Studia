import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.stats

mean = 0
variance = 1
N = 5000

def get_data(mean, variance, n):
    data = np.random.normal(mean, variance, n)
    return data

def Y(data):
    return abs(data - np.mean(data))

def theoretical_expected_value_Y(sigma):
    return 2 * sigma / np.sqrt(2 * np.pi)

def insert_list(data, value, numpy_array=False):
    data = list(data)
    for v in data:
        if v > value:
            index = np.where(data == v)[0][0]
            break
    data.insert(index, value)
    if numpy_array:
        return data
    else:
        return np.array(data)

def pdf_normal(data, mean, variance):
    data = np.sort(data)
    return 1 / (np.sqrt(2 * np.pi) * variance) * np.exp(-(data - mean)**2 / (2 * variance**2))

def pdf_Y(data, variance):
    data = np.sort(data)
    return 2 / (np.sqrt(2 * np.pi) * variance) * np.exp(-data**2 / (2 * variance**2))


def EPDF(data,bin,smoothing=1):
    heights, bins = np.histogram(data,bins=bin,density=1)
    new_bins = []
    for i in range(len(bins)-1):
        new_bins.append(np.mean([bins[i],bins[i+1]]))
    return new_bins[::smoothing] , heights[::smoothing]

def ECDF(data):
    dane = np.array(data)
    dane.sort()
    jumps = np.linspace(0,1,len(dane))
    return dane,jumps

data_normal = get_data(mean, variance, N)
data_Y = Y(data_normal)

normal_pdf = pdf_normal(data_normal, mean, variance)
Y_pdf = pdf_Y(data_Y, variance)

x_pdf_Y = np.linspace(np.min(data_Y),np.max(data_Y),N)
y_pdf_Y = pdf_Y(x_pdf_Y,variance)
x_pdf_normal = np.linspace(np.min(data_normal),np.max(data_normal),N)
y_pdf_normal = pdf_normal(x_pdf_normal,mean,variance)

expected_Y = theoretical_expected_value_Y(variance)


def ADFM(start=100,end=5000,step=100):
    przecietne_odchylenia_od_sredniej = []
    srednie = []
    N = np.arange(start=start,stop=end+1,step=step)
    for n in N:
        distances = []
        ms = []    
        for i in range(500):
            sample = get_data(mean,variance,n)
            sample = Y(sample)
            distances.append(np.abs(np.mean(sample)-expected_Y))
            ms.append(np.mean(sample))
        przecietne_odchylenia_od_sredniej.append(np.mean(distances))
        srednie.append(np.mean(ms))
    return N, przecietne_odchylenia_od_sredniej ,srednie
# Y
plt.subplot(2, 3, 1)

plt.plot(x_pdf_Y, y_pdf_Y, color='red', label='PDF')

heights_Y, bins_Y, _ = plt.hist(data_Y, density=1, bins=30, color='g', alpha=0.6)

x_Y,y_Y = EPDF(data_Y,30,3)
plt.plot(x_Y,y_Y, color='purple', label='EPDF')

plt.vlines(expected_Y, 0, np.max(heights_Y), colors='y', linestyles='dashed', label='Średnia')

xticks_Y = np.arange(np.floor(data_Y.min()), np.ceil(data_Y.max()) + 1)
xticks_Y = insert_list(xticks_Y, expected_Y)
plt.xticks(xticks_Y, rotation=90)
plt.title("Hist Y")

# Normal
plt.subplot(2, 3, 2)
plt.plot(x_pdf_normal, y_pdf_normal, color='red', label='PDF')

heights_normal, bins_normal, _ = plt.hist(data_normal, density=1, bins=31, color='g', alpha=0.6)

x_normal ,y_normal = EPDF(data_normal,31,2)
plt.plot(x_normal,y_normal,color='purple', label='EPDF')

plt.vlines(mean, 0, np.max(heights_normal), colors='y', linestyles='dashed', label='Średnia')

xticks_normal = np.arange(np.floor(data_normal.min()), np.ceil(data_normal.max()) + 1)
xticks_normal = insert_list(xticks_normal, mean)
plt.xticks(xticks_normal, rotation=90)
plt.title("Hist Normal")

plt.subplot(2,3,3)
x_ecdf_Y, y_ecdf_Y = ECDF(data_Y)
x_ecdf_normal, y_ecdf_normal = ECDF(data_normal)
plt.plot(x_ecdf_Y,y_ecdf_Y,label="ECDF-Y")
plt.plot(x_ecdf_normal,y_ecdf_normal,label="ECDF-Normal")
plt.title("Dystrybuanty")

plt.subplot(2,3,4)
x_means,y_means, calc_means = ADFM(end=10000,step=200)
plt.plot(x_means,y_means)
plt.title("ADFM")

plt.subplot(2,3,5)
plt.plot(x_means,calc_means,label='Wyliczone średnie')
plt.hlines(expected_Y,x_means[0],x_means[-1],color='r',label='Średnia teoretyczna')
plt.title("Srednie")

plt.legend()
plt.tight_layout()
plt.show()
