import numpy as np 
import matplotlib.pyplot as plt
import scipy.stats as sc

class Data():
    def __init__(self,dane:list):
        self.data = np.array(dane)
        self.q = np.percentile(dane,[25,50,75])
    
    def interquartile_range(self):
        return self.q[-1]-self.q[0]
    
    def sample_range(self):
        return max(self.data)-min(self.data)

    def variance(self):
        return np.var(self.data,ddof=1)
    
    def standard_deviation(self):
        return np.std(self.data,ddof=1)

    def kurtosis(self):
        return sc.kurtosis(self.data)
    
    def curviture(self):
        return sc.skew(self.data)

    def quantile_1st(self):
        return self.q[0]
    
    def quantile_2nd(self):
        return self.q[1]
    
    def quantile_3rd(self):
        return self.q[2]
    
    def get_quantile(self,p):
        return np.percentile(self.data,p)

    def median(self):
        return np.median(self.data)

    def mean_aritmetic(self):
        return np.mean(self.data)
    
    def mean_harmonic(self):
        c = self.data.copy()
        for i in range(len(self.data)):
            if not c[i] == 0:
                c[i] = c[i]**(-1)
        res = len(self.data) / np.sum(c)
        return res

    def mean_geometric(self):
        c = self.data.copy()
        for i in range(len(c)):
            c[i] = np.power(c[i],1/len(c))
        res = np.prod(c)
        return res

    def mean_cut(self,k):
        d = np.sort(self.data)
        d = d[k:-k]
        res = np.mean(d)
        return res

    def mean_winsor(self, k):
        d = np.sort(self.data)
        n = len(d)
        d[:k] = d[k]
        d[-k:] = d[-k-1]
        res = np.mean(d)
        return res
    
    def __len__(self):
        return len(self.data)
    
    def hist(self, bins: int, density: float):
        # Sort the data
        dane = np.sort(self.data)
        
        # Calculate the spread of the data
        spread = dane[-1] - dane[0]
        
        # Determine the bin width
        bin_width = spread / bins
        
        # Initialize an array to store the counts
        counts = np.zeros(bins)
        
        # Assign each data point to its corresponding bin index
        bin_indices = np.digitize(dane, np.linspace(dane[0], dane[-1], bins + 1)) - 1

        # Clip bin indices to ensure they fall within the valid range
        bin_indices = np.clip(bin_indices, 0, bins - 1)

        # Count the number of data points falling into each bin
        for bin_index in bin_indices:
            counts[bin_index] += 1
        
        # Normalize the counts if desired
        if density:
            counts /= (len(self.data) * bin_width)
        
        # Plot the histogram using bar plots
        bin_edges = np.linspace(dane[0], dane[-1], bins + 1)
        plt.bar(bin_edges[:-1], counts, width=bin_width, align='edge')
        plt.xlabel('Bins')
        plt.ylabel('Frequency' if not density else 'Probability Density')
        plt.title('Histogram')
        plt.show()

    def mode(self):
        return sc.mode(self.data)[0][0]
    
    def _show_plot(self,show):
        if show:
            plt.show()

class DiscreteData(Data):
    def __init__(self, dane: list):
        super().__init__(dane)

    def cdf(self,show:bool):

        def remove_duplicates(list1,list2):
            indexes = []
            i = 0
            while i < len(list1) - 1:
                if list1[i] == list1[i + 1]:
                    start_index = i
                    while i < len(list1) - 1 and list1[i] == list1[i + 1]:
                        i += 1
                    end_index = i
                    indexes.append([start_index, end_index])
                i += 1

            # Usuwamy elementy o podanych indeksach
            for start, end in reversed(indexes):
                del list1[start + 1:end + 1]
                del list2[start + 1:end + 1]

            return indexes
        
        dane = list(self.data)
        n = len(dane)
        dane.sort()
        probs = []
        xs = list(np.arange(np.min(dane)-1,np.max(dane)+2,1))
        for event in xs:
            probs.append(dane.count(event) / n)
        probs = list(np.cumsum(probs[:-1]))

        remove_duplicates(probs,xs)

        fig, ax = plt.subplots()
        ax.hlines(y=probs, xmin=xs[:-1], xmax=xs[1:],color='red', zorder=1)
        ax.vlines(x=xs[1:-1], ymin=probs[:-1], ymax=probs[1:], color='red',linestyle='dashed', zorder=1)
        ax.scatter(xs[1:-1], probs[1:], color='red', s=18, zorder=3)
        ax.scatter(xs[1:-1], probs[:-1], color='white', s=18, zorder=2,edgecolor='red')
        self._show_plot(show=show)

        return xs, probs
    
class ContinuousData(Data):
    def __init__(self, dane: list):
        super().__init__(dane)

    def _hist(self,density=1.0,show=False,bins=15):
        bins = bins
        counts,bitch,_ = plt.hist(self.data,bins=bins,density=density)
        if not show:
            plt.clf()
        return bitch

    def pdf_normal(self,mu,variance,show:bool,hist:bool,bins=15):
        dane = np.array(self._hist(show=hist,bins=bins))
        y = 1/(np.sqrt(2*np.pi)*variance)*np.exp(-0.5*((dane-mu)/variance)**2)
        plt.plot(dane,y,color='r')
        self._show_plot(show)

        return dane ,y

    def pdf_uniform(self,a,b,show:bool,hist:bool,bins=15):
        dane = np.array(self._hist(show=hist,bins=bins))
        y = [1/(b-a) for i in range(len(dane))]
        plt.plot(dane,y,color='r')
        self._show_plot(show)

        return dane,1/(b-a)
    
    def pdf_exponential(self,lam,show:bool,hist:bool,bins=15):
        dane = np.array(self._hist(show=hist,bins=bins))
        y = lam*np.exp(-lam*dane)
        plt.plot(dane,y,color='r')
        self._show_plot(show)

        return dane,y
    
    def pdf_gamma(self):
        return None
    
    def cdf(self,show:bool):
        dane = self.data
        dane.sort()
        jumps = np.linspace(0,1,len(dane))
        plt.plot(dane,jumps)
        plt.title('Dystrybuanta empiryczna')
        self._show_plot(show=show)


if __name__ == "__main__":
    T = 10
    dane = ContinuousData(np.random.exponential(10,100000))
    # dane.pdf_exponential(1,True,True,bins=100)
    dane.cdf(True)
