
s = int(input("Wprowadz szerokosc chhoinki \n"))
h = int(input("wprowadz wysokosc choinki \n"))
i = 0
j = 0
l = 0
while i<(h):
    while j<=(s):
        k=s-j
        print((" "*k),"*"*(j*2+1))
        j=j+1
    j=0
    while l<(s-1):
        m=s-l
        print ((" "*(l+1)),"*"*(m*2-1))
        l=l+1
    l=0
    i=i+1
else:
    print((s)*" ","*")
    print((s)*" ","*")
# Wiem ze kod jest nieczytelny i brakuje opisow zmiennych, nastepnym razem przy wiekszym projekcie zadbam o czytelnosc.