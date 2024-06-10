
Slowo1  = str(input("wpisz pierwsze slowo do poprownania\n"))
Slowo2  = str(input("wpisz drugie slowo do poprownania\n"))
Slowo1=Slowo1.replace(" ","")
Slowo2=Slowo2.replace(" ","")
Slowo1T = list(Slowo1) 
Slowo2T = list(Slowo2)

if len(Slowo1)==len(Slowo2):
    Slowo1T.sort()
    Slowo2T.sort()
    for i in range(len(Slowo1T)):
        if Slowo1T[i]==Slowo2T[i]:

            continue
        else:
            print("Slowa nie sa anagramami")
            break
    if i == len(Slowo1)-1:
        print("slowa sa anagramami")
else:
    print("Slowa nie sa anagramami poniewaz maja rozna dlugosc")