import numpy as np
import matplotlib.pyplot as plt


# Load data from file
with open("C:\\Users\\kacpu\\Downloads\\dane_lista1.txt") as f:
    dane_X = [float(line.strip()) for line in f]

# Generate dane_Y
dane_Y = np.exp(dane_X)

# Define PDF functions
def pdf_X(dane):
    return np.exp(-0.5 * dane**2) / np.sqrt(2 * np.pi)

def pdf_Y(dane):
    return np.exp(-0.5 * dane**2) / (np.sqrt(2 * np.pi) * dane)

# Generate theoretical data
teor_X = np.linspace(min(dane_X), max(dane_X), 1000)
teor_Y = np.linspace(min(dane_Y), max(dane_Y), 1000)

# Calculate PDF values for theoretical data
teor_X_pdf = pdf_X(teor_X)
teor_Y_pdf = pdf_Y(teor_Y)

# Plot histograms and theoretical distributions
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(dane_X, bins=15, density=True)
plt.plot(teor_X, teor_X_pdf, color='r')
plt.title('Histogram of dane_X')

plt.subplot(1, 2, 2)
plt.hist(dane_Y, bins=15, density=True)
plt.plot(teor_Y, teor_Y_pdf, color='r')
plt.title('Histogram of dane_Y')

plt.tight_layout()
plt.show()
