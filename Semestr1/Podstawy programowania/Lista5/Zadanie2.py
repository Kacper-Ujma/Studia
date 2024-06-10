
hex=input("wpisz kolor formatu HTML\n")

def ToDec(List):
    r = ''.join([str(elem) for elem in List[0:2]])
    g = ''.join([str(elem) for elem in List[2:4]])
    b = ''.join([str(elem) for elem in List[4:7]])
    r = (int(r,16))
    g = (int(g,16))
    b = (int(b,16))
    return ("Twoj tryplet RGB to","R =",r,"G =",g,"B =",b)
     
if len(hex)!=6:
    print("podales zla wartosc")
else: print(ToDec(hex))