import numpy
import random

def max_min(seq:list,max,min):
    if len(seq) > 0:
        if seq[0]>max:
            max = seq[0]
        elif seq[0]<min:
            min = seq[0]
        return max_min(seq[1:],max,min)
    return (max,min)

S = [random.randint(-1000,1000) for i in range(10)]

print(S,max_min(S,S[0],S[0]))

        