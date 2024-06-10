import math
Wyznaczniki = []
for i in range(3):
    a = float(input("Wpisz wspolczynnik a przy kolejnych potegach zaczynajac od najwiekszej\n"))
    Wyznaczniki.append(a)

print("Twoj wielomina wyglada to:\n""(",Wyznaczniki[0],")x^2 + (",Wyznaczniki[1],")x +",Wyznaczniki[2])

 
if (Wyznaczniki[1]**2)-4*Wyznaczniki[0]*Wyznaczniki[2]>=0:
    delta = math.sqrt((Wyznaczniki[1]**2)-4*Wyznaczniki[0]*Wyznaczniki[2])
    if delta==0:
        print("Rownianie posiada jedno roziwawzanie podwojne =",((-Wyznaczniki[1])/(2*Wyznaczniki[0])))    
    else:
        x1 = ((-Wyznaczniki[1]+delta)/(2*Wyznaczniki[0]))
        x2 = ((-Wyznaczniki[1]-delta)/(2*Wyznaczniki[0]))
        print("Pierwiastki rowniania to odpowiednio =",x1,x2)
else:
    print("Delta ujmena, rownianie nie ma rzeczywistych rozwiazan rownaia")    