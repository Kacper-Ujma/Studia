a=int(input("wpisz wartosc r\n"))
b=int(input("wpisz wartosc g\n"))
c=int(input("wpisz wartosc b\n"))

            
def toHex(r,g,b):
    convertString = "0123456789ABCDEF"
    przeksztalcenie = ''
    przeksztalcenieR = ''
    przeksztalcenieG = ''
    przeksztalcenieB = ''
    def odwracanie(s):
        koniec =  s[::-1]
        return koniec
    if r>15:
        while r>0:
            rest=r%16
            przeksztalcenieR = przeksztalcenieR + convertString[rest]
            r=r//16
    else: przeksztalcenieR = przeksztalcenieR+convertString[r]+"0"
    if g>15:
        while g>0:
            rest=g%16
            przeksztalcenieG = przeksztalcenieG + convertString[rest]
            g=g//16
    else: przeksztalcenieG = przeksztalcenieG+convertString[g]+"0"
    if b>15:
        while b>0:
            rest=b%16
            przeksztalcenieB = przeksztalcenieB + convertString[rest]
            b=b//16
    else: przeksztalcenieB = przeksztalcenieB+convertString[b]+"0"
    przeksztalcenie=odwracanie(przeksztalcenieR)+odwracanie(przeksztalcenieG)+odwracanie(przeksztalcenieB)
    return "#"+przeksztalcenie

if a>=0 and a<256:
    if b>=0 and b<256:
        if c>=0 and c<256:
            print(toHex(a,b,c))
        else: print("wpisales zla wartosc b")
    else: print("wpisales zla wartosc g")
else: print("wpisales zla wartosc r")

