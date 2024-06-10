
PierwszeSlowo = str(input("Wpisz pierwsze slowo do porownania\n"))
DrugieSlowo = str(input("Wpisz drugie slowo do porownania\n"))

if len(PierwszeSlowo) <= len(DrugieSlowo):
    index = len(PierwszeSlowo)
else:
    index = len(DrugieSlowo)

for  i in range (index):
    if PierwszeSlowo[i] == DrugieSlowo[i]:
        print("Elemnt",i+1,"jest taki sam")
    else:
        print("Elemnt",i+1,"jest rozny")
if len(PierwszeSlowo) != len(DrugieSlowo):
    print("Dalszej czesi wyrazow nie mozna porownac poniewaz ronia sie od siebie dlugoscia")
