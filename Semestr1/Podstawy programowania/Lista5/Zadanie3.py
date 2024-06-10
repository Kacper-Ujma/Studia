n=int(input("wpisz ile pierwszych werazow ciagu fibonnaciego chcesz zobaczyc\n"))
def CiagFibonanaciegoOut(n):
    for i  in range(n):
        def CiagFibonnaciego (i):
                if i <= 0:
                    return 0
                elif i == 1:
                    return 1
                else:
                    return CiagFibonnaciego (i-1) + CiagFibonnaciego(i-2)
        print (CiagFibonnaciego(i))
    
print(CiagFibonanaciegoOut(n))