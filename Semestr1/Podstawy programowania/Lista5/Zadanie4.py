import time
n=int(input("wpisz ile pierwszych werazow ciagu fibonnaciego chcesz zobaczyc\n"))
'''
def CiagFibonanaciegoRec(n):
    memo = {0:0,1:1}
    for i  in range(n):
        def CiagFibonnaciego (i,m):
                if i in m :
                    return m[i]
                else:
                    m[i] =  CiagFibonnaciego (i-1,m) + CiagFibonnaciego(i-2,m)
                    return m[i]
        return (CiagFibonnaciego(i,memo))
'''
def CiagFibonanaciegoRec(n):
    for i  in range(n):
        def CiagFibonnaciego (i):
                if i <=1:
                    return i 
                else:
                    return CiagFibonnaciego(i-1) + CiagFibonnaciego(i-2)
        return (CiagFibonnaciego(i))

def CiagFibonnaciegoLoop(n):
        a0=1
        a1=1
        for i in range (0,n):
            print(a0)
            a0,a1=a1,a0+a1

print(CiagFibonnaciegoLoop(n),CiagFibonanaciegoRec(n))

CzasFibRecSTR = time.time()
time.sleep(0.001)
CiagFibonanaciegoRec(n)
CzasFibRecEND = time.time()

CzasFibLoopSTR = time.time()
time.sleep(0.001)
CiagFibonnaciegoLoop(n)
CzasFibLoopEND = time.time()

print(CzasFibRecEND-CzasFibRecSTR,CzasFibLoopEND-CzasFibLoopEND)
