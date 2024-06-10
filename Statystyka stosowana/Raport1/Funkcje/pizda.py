import numpy as np
import matplotlib.pyplot as plt
# Sample data
X = np.array([1, 2, 3, 4, 5])

# Min-Max scaling
X_norm = (X - X.min()) / (X.max() - X.min())

print(X_norm)
plt.hist(X_norm)
plt.show()

