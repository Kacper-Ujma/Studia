import numpy as np
import math

a,c= 1,1
Lista = np.linspace(10**7.4,10**8.5,100)
for b in Lista:
    x1 = 1/(2*a)*(-b-np.sign(b)*math.sqrt((b**2)-(4*a*c)))
    x2 = 1/(2*a)*(-b+np.sign(b)*math.sqrt((b**2)-(4*a*c)))
    x3 = x1
    x4 = c/(a*x3)
    print(x1,x2,x3,x4)

