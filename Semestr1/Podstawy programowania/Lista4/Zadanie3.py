import math
import sys
x=9.8**201
y=10.2**199

#Wynik1 = math.sqrt(x**2 + y**2)
Wynik2 = y*math.sqrt((x/y)**2 + 1)

print(Wynik2)

print(sys.float_info)