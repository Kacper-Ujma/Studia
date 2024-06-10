
n = int(input("wpisz ile pierwszych wyrazow ciagu fibonaciiego bedziemy sprawdzac\n"))
def CiagFibonnaciego (n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return CiagFibonnaciego (n-1) + CiagFibonnaciego(n-2)

for i in range (n):
    print (CiagFibonnaciego(i+1))
   