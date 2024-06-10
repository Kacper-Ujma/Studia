
Slowo = str(input("wpisz slowo do sprawdzenia czy jest palindormem\n"))
Palindrom = list(Slowo)
if Palindrom==list(reversed(Palindrom)):
    print(Slowo,"jest palindromem")
else:
    print(Slowo,"nie jest palindromem")