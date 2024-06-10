
def iloczyn(m:int,n:int):
    if n > 0:
        return m + iloczyn(m,n-1)
    return 0 

print(iloczyn(9,2))

